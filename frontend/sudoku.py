from sudoku_UI import *
from PyQt5.QtWidgets import QApplication, QMessageBox, QDialog, QLabel, QHBoxLayout
from authentication import *
import sys
from communication import *
from board import isLegal, isDone, verify
import json

MATCH_REQUEST = 0
MATCH_FOUND = 1
CHECK_SOLUTION = 2
VALID_SOLUTION = 3
DONE = 4
MOVE = 5
CHANGE_VALUE = 6
ERROR = 7


class MessageBox(QMessageBox):

    def __init__(self, title, text, pos):
        super(QMessageBox, self).__init__()
        self.title = title
        self.text = text
        self.pos = pos

    def showMessage(self):
            self.move(self.pos)
            self.setIcon(QMessageBox.Information)
            self.setText(self.text)
            self.setWindowTitle(self.title)
            self.exec_()

class WorkerSignals(QtCore.QObject):
    result = QtCore.pyqtSignal(tuple)
    error = QtCore.pyqtSignal()
    
class Worker(QtCore.QRunnable):
    def __init__(self, fn, conn):
        super(Worker, self).__init__()
        self.fn = fn
        self.conn = conn
        self.signals = WorkerSignals()  

    def run(self):
        while(True):
            try:   
                result = self.fn(self.conn)
                if result[0] == 0:
                    self.conn.shutdown(socket.SHUT_RDWR)
                    self.conn.close()
                    print("connection closed")
                    #self.signals.error.emit()
                    break
                self.signals.result.emit(result) 
            except socket.error:
                print("connection closed")
                break
class sudokuController:
    #view
    #token
    #box_grid_row
    #box_grid_col
    #item_row
    #item_col
    #board
    def __init__(self, view):
        self.view = view
        self.connectSignals()
        self.threadpool = QtCore.QThreadPool()

    #connects signals of buttons to slots
    def connectSignals(self):
        self.view.signInButton.clicked.connect(lambda : self.onSignInButton())
        self.view.signUpButton.clicked.connect(lambda : self.onSignUpButton())
        self.view.registrationButton.clicked.connect(lambda : self.onRegistrationButton())
        self.view.challengeButton.pressed.connect(lambda mode = "0" : self.setMode(mode))
        self.view.collaborativeButton.pressed.connect(lambda mode = "1" : self.setMode(mode))
        self.view.easyButton.pressed.connect(lambda difficulty = "easy" : self.setDifficulty(difficulty))
        self.view.mediumButton.pressed.connect(lambda difficulty = "medium" : self.setDifficulty(difficulty))
        self.view.hardButton.pressed.connect(lambda difficulty = "hard" : self.setDifficulty(difficulty))
        for r in range(0,9):
            for c in range(0,9):
                box_grid = self.view.gridLayout.itemAtPosition(r//3,(c//3)+1)
                item = box_grid.itemAtPosition(r%3,c%3)        
                tool_button = item.widget()
                tool_button.pressed.connect(lambda pos = (r, c): self.onItem(pos[0], pos[1]))

        
    def onSignInButton(self):
        username = self.view.usernameLine.text()
        password = self.view.passwordLine.text()
        res = login(username,password)
        response = res.read().decode()
        data = json.loads(response)
        if res.status == 200:
            self.token = data["token"]
            self.view.stackedWidget.setCurrentIndex(2)
        else:
            msg = MessageBox("Bad credentials",data["message"],self.view.geometry().center())
            msg.showMessage()
        
    def onSignUpButton(self):
        self.view.stackedWidget.setCurrentIndex(1)

    def onRegistrationButton(self):
        username = self.view.usernameLineRegistration.text()
        password = self.view.passwordLineRegistration.text()
        repeated_password = self.view.repeatPasswordLine.text()
        if password == repeated_password:
            res = registration(username,password)
            response = res.read().decode()
            data = json.loads(response)
            if res.status == 201:
                self.view.stackedWidget.setCurrentIndex(0)
                self.token = data["token"]
            else:
                msg = MessageBox("Bad credetials", data["message"], self.view.geometry().center())
                msg.showMessage()
        else:
            msg = MessageBox("Bad credetials", "Insert the same password", self.view.geometry().center())
            msg.showMessage()

    def setMode(self, mode):
        self.mode = mode
        self.view.stackedWidget.setCurrentIndex(3)

    def setDifficulty(self, difficulty):
        self.view.setWindowIcon(QtGui.QIcon("media/icon.png"))
        movie = QtGui.QMovie("media/loading1.gif")
        self.view.loadLabel.setMovie(movie)
        movie.start()  
        self.view.stackedWidget.setCurrentIndex(4)
        self.difficulty = difficulty
        self.sendMatchRequest()

    def sendMatchRequest(self):
        match_request = {"token" : self.token, "mode" : int(self.mode), "difficulty" : self.difficulty}
        try:
            self.conn = createConnection()
        except socket.error:
            message = "There is a connection error, retry"
            MessageBox("Connetion Error", message, self.view.geometry().center())
            msg.showMessage()
            self.view.stackedWidget.setCurrentIndex(2)
            print("connetion error")
        else:
            sendPacket(self.conn, MATCH_REQUEST, json.dumps(match_request))
            worker = Worker(receivePacket,self.conn)
            worker.signals.result.connect(self.packed_received)
            worker.signals.error.connect(self.error_received)
            self.threadpool.start(worker)


    def packed_received(self, res):
        packet_type = res[0]
        payload = res[1]
        payload = json.loads(payload)
        '''if packet_type == MATCH_REQUEST_ACK:
            if payload["status"] is not 0:
                MessageBox("Connetion Error", message, self.view.geometry().center())
                msg.showMessage()
                self.view.stackedWidget.setCurrentIndex(2)'''
        if packet_type == MATCH_FOUND:
            self.opponent = payload["opponentUsername"]
            self.fillBoard(payload["board"])
            self.view.stackedWidget.setCurrentIndex(5)
        elif packet_type == VALID_SOLUTION:
            if payload["valid"] is True:
                msg = MessageBox("Match finished","Congratulations, you won", self.view.geometry().center())
                msg.buttonClicked.connect(lambda: self.onMsgButton())
                msg.showMessage()
        elif packet_type == DONE: 
            #to do, check if done is true  
            if self.mode == "0":
                self.timer.stop()
                msg = MessageBox("Match finished","Game over,you lost", self.view.geometry().center())
                msg.buttonClicked.connect(lambda: self.onMsgButton())
                msg.showMessage()
            else:
                self.timer.stop()
                msg = MessageBox("Match finished","Sudoku completed", self.view.geometry().center())
                msg.buttonClicked.connect(lambda: self.onMsgButton())
                msg.showMessage()
        elif packet_type == CHANGE_VALUE:
            self.updateBoard(payload["row"],payload["col"],payload["value"])
        elif packet_type == ERROR:
            msg = MessageBox("Error","Internal server error", self.view.geometry().center())
            msg.buttonClicked.connect(lambda: self.onMsgButton())
            msg.showMessage()
  
    def fillBoard(self, board):
        self.board = board  
        self.count = 0
        self.mask = [[True for j in range(9)] for i in range(9)]

        for r in range(0,9):
            for c in range(0,9):
                box_grid = self.view.gridLayout.itemAtPosition(r//3,(c//3)+1)
                item = box_grid.itemAtPosition(r%3,c%3)        
                tool_button = item.widget()
                if board[r][c] != 0:
                    tool_button.setText(str(board[r][c]))
                    style = tool_button.styleSheet().replace("background-color: white;", "background-color: #f5f5f5;")
                    tool_button.setStyleSheet(style)
                    tool_button.setEnabled(False)
                else:
                    self.count += 1
        self.setupTimer()


    def setupTimer(self):
        self.view.opponentLabel.setText(self.opponent)
        self.view.timeEdit.setTime(QtCore.QTime(0, 0, 0))
        self.view.timeEdit.setDisplayFormat('hh:mm:ss')
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateTimer)
        self.timer.start(1000)

    def updateTimer(self):
        self.view.timeEdit.setTime(self.view.timeEdit.time().addSecs(1))
                    
    def onItem(self, row, col):
        self.row = row
        self.col = col
        self.box_grid_row = row // 3
        self.box_grid_col = (col // 3) + 1
        self.item_row = row % 3
        self.item_col = col % 3
        numeric_keypad = QDialog()
        grid_layout = QtWidgets.QGridLayout()
        v = 1
        for r in range(3):
            for c in range(3):
                button = QtWidgets.QToolButton()
                button.setText(str(v))
                button.pressed.connect(lambda value = (str(v),numeric_keypad) : self.onKeyPad(value[0], value[1]))
                grid_layout.addWidget(button,r,c,1,1)
                v += 1
        numeric_keypad.setLayout(grid_layout)
        numeric_keypad.resize(100,100)
        box_grid = self.view.gridLayout.itemAtPosition(self.box_grid_row,self.box_grid_col)
        item = box_grid.itemAtPosition(self.item_row, self.item_col).widget()
        offset_x = self.view.pos().x()
        offset_y = self.view.pos().y()
        x = item.pos().x() + offset_x - 10
        y = item.pos().y() + offset_y + 100
        numeric_keypad.move(x,y)
        numeric_keypad.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Popup)
        numeric_keypad.exec_()


    def onKeyPad(self, value, keypad):
        box_grid = self.view.gridLayout.itemAtPosition(self.box_grid_row,self.box_grid_col)
        item = box_grid.itemAtPosition(self.item_row, self.item_col)        
        tool_button = item.widget()

        if self.board[self.row][self.col] == 0:
            self.count -= 1

        tool_button.setText(value)
         
        self.board[self.row][self.col] = int(value)
        
        
        verify(self.board, self.row, self.col, self.mask)
                
        for i in range(9):
            for j in range(9):
                box_grid = self.view.gridLayout.itemAtPosition(i//3, (j//3) + 1)
                item = box_grid.itemAtPosition(i%3, j%3)        
                tool_button = item.widget()
                if self.mask[i][j] == True:
                    if "color:red;" in tool_button.styleSheet():
                        style = tool_button.styleSheet().replace("color:red;", "color:black;")
                        tool_button.setStyleSheet(style)
                else:
                    if "color:black;" in tool_button.styleSheet():
                        style = tool_button.styleSheet().replace("color:black;", "color:red;")
                        tool_button.setStyleSheet(style)
        #challenge mode
        if self.mode == "0":
            if self.count == 0:
                for i in range(9):
                    for j in range(9):
                        if self.mask[i][j] == False:
                            keypad.close() 
                            return
                self.timer.stop()
                payload = {"board" : self.board}
                sendPacket(self.conn, CHECK_SOLUTION, json.dumps(payload).replace(" ", "", -1))
        #collaborative mode
        else:
            payload = {"row":self.row,"col":self.col,"value":int(value)}
            #move
            sendPacket(self.conn, MOVE, json.dumps(payload).replace(" ", "", -1))
        
        keypad.close()
           

    def error_received(self):
        title = "Connection Error"
        text = "There is a connection error, retry"
        msg = MessageBox(title, text, self.view.geometry().center())
        msg.showMessage()
        self.view.stackedWidget.setCurrentIndex(2)
        

    def flushBoard(self):
        for r in range(9):
            for c in range(9):
                box_grid = self.view.gridLayout.itemAtPosition(r//3, (c//3) + 1)
                item = box_grid.itemAtPosition(r%3, c%3)        
                tool_button = item.widget()
                tool_button.setText("")
                tool_button.setEnabled(True)

    
    def onMsgButton(self):
        self.flushBoard()
        self.view.stackedWidget.setCurrentIndex(2)
        
    def updateBoard(self, row, col, value):

        box_grid = self.view.gridLayout.itemAtPosition(row//3, (col//3) + 1)
        item = box_grid.itemAtPosition(row%3, col%3)        
        tool_button = item.widget()
        tool_button.setText(str(value))

        self.board[row][col] = int(value)
        verify(self.board, row, col, self.mask)
                
        for i in range(9):
            for j in range(9):
                box_grid = self.view.gridLayout.itemAtPosition(i//3, (j//3) + 1)
                item = box_grid.itemAtPosition(i%3, j%3)        
                tool_button = item.widget()
                if self.mask[i][j] == True:
                    if "color:red;" in tool_button.styleSheet():
                        style = tool_button.styleSheet().replace("color:red;", "color:black;")
                        tool_button.setStyleSheet(style)
                else:
                    if "color:black;" in tool_button.styleSheet():
                        style = tool_button.styleSheet().replace("color:black;", "color:red;")
                        tool_button.setStyleSheet(style)

        '''if done is True:
            msg = QMessageBox()
            msg.move(self.view.pos().x() + 100,self.view.pos().y() + 100)
            msg.setIcon(QMessageBox.Information)
            msg.setText("sudoku completed")
            msg.setWindowTitle("Match finished")
            msg.buttonClicked.connect(lambda: self.onMsgButton())
            msg.exec_()'''





class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = MainWindow()
    sudokuController(view=view)
    view.show()
    sys.exit(app.exec_())
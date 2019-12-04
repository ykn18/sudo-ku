from sudoku_UI import *
from PyQt5.QtWidgets import QApplication, QMessageBox, QDialog, QLabel, QHBoxLayout
from authentication import *
import sys
from communication import *
from board import isLegal, isDone, verify
import json


class WorkerSignals(QtCore.QObject):
    result = QtCore.pyqtSignal(tuple)
    
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
        status_txt = QLabel(self.view.page_6)
        status_txt.setAlignment(QtCore.Qt.AlignCenter)
        movie = QtGui.QMovie("loading1.gif")
        status_txt.setMovie(movie)
        movie.start()
        layout = QHBoxLayout()
        layout.addWidget(status_txt)
        self.view.page_6.setLayout(layout)
        self.connectSignals()
        self.threadpool = QtCore.QThreadPool()

    #connects signals of buttons to slots
    def connectSignals(self):
        self.view.signInButton.clicked.connect(lambda : self.onSignInButton())
        self.view.signUpButton.clicked.connect(lambda : self.onSignUpButton())
        self.view.registrationButton.clicked.connect(lambda : self.onRegistrationButton())
        self.view.challengeButton.pressed.connect(lambda mode = "0" : self.setMode(mode))
        self.view.collaborativeButton.pressed.connect(lambda mode = "1" : self.setMode(mode))
        self.view.easyButton.pressed.connect(lambda mode = "easy" : self.setDifficulty(mode))
        self.view.mediumButton.pressed.connect(lambda mode = "medium" : self.setDifficulty(mode))
        self.view.hardButton.pressed.connect(lambda mode = "hard" : self.setDifficulty(mode))
        
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
            msg = QMessageBox()
            msg.move(self.view.pos().x() + 100,self.view.pos().y() + 100)
            msg.setIcon(QMessageBox.Information)
            msg.setText(data["message"])
            msg.setWindowTitle("Bad credentials")
            msg.exec_()
        
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
                msg = QMessageBox()
                msg.move(self.view.pos().x() + 100,self.view.pos().y() + 100)
                msg.setIcon(QMessageBox.Information)
                msg.setText(data["message"])
                msg.setWindowTitle("Bad credentials")
                msg.exec_()
        else:
            msg = QMessageBox()
            msg.move(self.view.pos().x() + 100,self.view.pos().y() + 100)
            msg.setIcon(QMessageBox.Information)
            msg.setText("Insert the same password")
            msg.setWindowTitle("Bad credentials")
            msg.exec_()
    
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
                else:
                    self.count += 1
                    tool_button.pressed.connect(lambda pos = (r, c): self.onItem(pos[0], pos[1]))
    
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


        if self.count == 0:
            for i in range(9):
                for j in range(9):
                    if self.mask[i][j] == False:
                        keypad.close() 
                        return
            payload = {"board" : self.board}
            sendPacket(self.conn, 7, json.dumps(payload).replace(" ", "", -1))
        keypad.close()     


    def setMode(self, mode):
        self.mode = mode
        self.view.stackedWidget.setCurrentIndex(3)

    def setDifficulty(self, difficulty):  
        self.view.stackedWidget.setCurrentIndex(4)
        self.difficulty = difficulty
        self.sendMatchRequest()

    def sendMatchRequest(self):
        match_request = {"token" : self.token, "mode" : self.mode, "difficulty" : self.difficulty}
        try:
            self.conn = createConnection()
        except socket.error:
            msg = QMessageBox()
            msg.move(self.view.pos().x() + 100,self.view.pos().y() + 100)
            msg.setIcon(QMessageBox.Information)
            msg.setText("There is a connection error, retry")
            msg.setWindowTitle("Connection Error")
            msg.exec_()
            self.view.stackedWidget.setCurrentIndex(2)
            print("connetion error")
        else:
            sendPacket(self.conn, 0, json.dumps(match_request))
            worker = Worker(receivePacket,self.conn)
            worker.signals.result.connect(self.packed_received)
            self.threadpool.start(worker)

    def flushBoard(self):
        for r in range(9):
            for c in range(9):
                box_grid = self.view.gridLayout.itemAtPosition(r//3, (c//3) + 1)
                item = box_grid.itemAtPosition(r%3, c%3)        
                tool_button = item.widget()
                tool_button.setText("")


    
    def onMsgButton(self):
        self.conn.shutdown(socket.SHUT_RDWR)
        self.conn.close()
        self.flushBoard()
        self.view.stackedWidget.setCurrentIndex(2)

    def packed_received(self, res):
        packet_type = res[0]
        payload = res[1]
        payload = json.loads(payload)
        if packet_type == 1:
            if payload["status"] is not 0:
                msg = QMessageBox()
                msg.move(self.view.pos().x() + 100,self.view.pos().y() + 100)
                msg.setIcon(QMessageBox.Information)
                msg.setText("Error in the match request")
                msg.setWindowTitle("Error")
                msg.exec_()
                self.view.stackedWidget.setCurrentIndex(2)
        elif packet_type == 2:
            self.fillBoard(payload["board"])
            self.view.stackedWidget.setCurrentIndex(5)
        elif packet_type == 8:
            if payload["valid"]:
                msg = QMessageBox()
                msg.move(self.view.pos().x() + 100,self.view.pos().y() + 100)
                msg.setIcon(QMessageBox.Information)
                msg.setText("Congratulations, you won")
                msg.setWindowTitle("Match finished")
                msg.buttonClicked.connect(lambda: self.onMsgButton())
                msg.exec_()
        elif packet_type == 5:
                msg = QMessageBox()
                msg.move(self.view.pos().x() + 100,self.view.pos().y() + 100)
                msg.setIcon(QMessageBox.Information)
                msg.setText("Game over,you lost")
                msg.setWindowTitle("Match finished")
                msg.buttonClicked.connect(lambda: self.onMsgButton())
                msg.exec_()

        


        


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
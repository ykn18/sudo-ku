from sudoku_UI import *
from PyQt5.QtWidgets import QMessageBox, QDialog
from authentication import *
import sys
from communication import *
from board import verify
import json

import time
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.patheffects as path_effects

MATCH_REQUEST = 1
MATCH_FOUND = 2
CHECK_SOLUTION = 3
VALID_SOLUTION = 4
DONE = 5
MOVE = 6
CHANGE_VALUE = 7
PING = 8
PING_ACK = 9
ERROR = 10 

waiting = False
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
        global waiting
        playing = False
        while(True):
            try:   
                result = self.fn(self.conn)
                if result[0] == DONE or result[0] == VALID_SOLUTION:
                    playing = False
                    self.signals.result.emit(result)
                    return
                if result[0] == ERROR:
                    self.signals.result.emit(result)
                    self.conn.shutdown(socket.SHUT_RDWR)
                    self.conn.close()
                    print("connection closed")
                    return
                if result[0] == MATCH_FOUND:
                    playing = True
                    waiting = False
                if result[0] == 0 and (playing or waiting):
                    playing = False
                    waiting = False
                    self.conn.shutdown(socket.SHUT_RDWR)
                    self.conn.close()
                    print("connection closed")
                    self.signals.error.emit()
                    return
                self.signals.result.emit(result) 
            except socket.error:
                print("connection closed")
                return
            
class sudokuController:
    def __init__(self, view):
        self.view = view
        self.view.setWindowTitle("SUDO-KU")
        self.connectSignals()
        self.threadpool = QtCore.QThreadPool()
        self.view.setWindowIcon(QtGui.QIcon("media/icon.png"))

        #Init canvas to draw stats
        self.view.canvasWidget = FigureCanvas(Figure())
        self.view.verticalLayout_6.addWidget(self.view.canvasWidget)
        self.view.canvasWidget.setSizePolicy(QtWidgets.QSizePolicy.Expanding, 
                                  QtWidgets.QSizePolicy.Expanding)
        self.view.canvasWidget.updateGeometry()
        self.ax = self.view.canvasWidget.figure.subplots()

        
    def updateCanvas(self):
        self.ax.clear()
        self.ax.set_facecolor('#828282')
        self.ax.set_ylabel("Numbers inserted", family='sans-serif', size="13", weight="bold")
        self.ax.set_xlabel("Time", family='sans-serif', size="13", weight="bold")
        self.ax.set_title("Match stats", family='sans-serif', size="15", weight="bold")
        self.ax.step(list(map(lambda x: x[0], self.moves)), list(map(lambda x: x[1], self.moves)), color="white", linewidth=5.0, 
        path_effects=[path_effects.SimpleLineShadow(shadow_color="white"),
        path_effects.Normal()])
        self.ax.figure.canvas.draw()


    #connects signals of buttons to slots
    def connectSignals(self):
        self.view.homeButton.clicked.connect(lambda : self.onHomeButton())
        self.view.playButton.clicked.connect(lambda : self.onPlayButton())
        self.view.statsButton.clicked.connect(lambda : self.onStatsButton())
        self.view.signInButton.clicked.connect(lambda : self.onSignInButton())
        self.view.signUpButton.clicked.connect(lambda : self.onSignUpButton())
        self.view.registrationButton.clicked.connect(lambda : self.onRegistrationButton())
        self.view.challengeButton.pressed.connect(lambda mode = 0 : self.setMode(mode))
        self.view.collaborativeButton.pressed.connect(lambda mode = 1 : self.setMode(mode))
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
            self.view.stackedWidget.setCurrentIndex(7)
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

    def onPlayButton(self):
        self.view.stackedWidget.setCurrentIndex(2)
    
    def onHomeButton(self):
        self.view.stackedWidget.setCurrentIndex(7)
    
    def onStatsButton(self):
        pass
        #TO DO: ADD LEADERBOARD

    def setMode(self, mode):
        self.mode = mode
        self.view.stackedWidget.setCurrentIndex(3)

    def setDifficulty(self, difficulty):
        self.view.easyButton.setEnabled(False)
        self.view.mediumButton.setEnabled(False)
        self.view.hardButton.setEnabled(False)
        movie = QtGui.QMovie("media/loading1.gif")
        self.view.loadLabel.setMovie(movie)
        movie.start()  
        self.view.stackedWidget.setCurrentIndex(4)
        self.difficulty = difficulty
        self.sendMatchRequest()
        print("call send match request  ")

    def sendMatchRequest(self):
        global waiting
        match_request = {"token" : self.token, "mode" : self.mode, "difficulty" : self.difficulty}
        try:
            self.conn = createConnection()
        except socket.error:
            message = "There is a connection error, retry"
            msg = MessageBox("Connetion Error", message, self.view.geometry().center())
            msg.buttonClicked.connect(lambda: self.onMsgButton("ERROR"))
            msg.showMessage()
            self.view.stackedWidget.setCurrentIndex(2)
            print("connetion error")
        else:
            print("send match request")
            sendPacket(self.conn, MATCH_REQUEST, json.dumps(match_request))
            worker = Worker(receivePacket,self.conn)
            worker.signals.result.connect(self.packed_received)
            worker.signals.error.connect(self.error_received)
            self.threadpool.start(worker)
            waiting = True


    def packed_received(self, res):
        packet_type = res[0]
        payload_legth = res[1]
        if payload_legth != 0:
            payload = res[2]
            payload = json.loads(payload)
        if packet_type == MATCH_FOUND:
            self.opponent = payload["opponentUsername"]
            self.fillBoard(payload["board"])
            self.view.stackedWidget.setCurrentIndex(5)
        elif packet_type == VALID_SOLUTION:
            if payload["valid"] == True:
                msg = MessageBox("Match finished","Congratulations, you won", self.view.geometry().center())
                self.updateCanvas()
                msg.buttonClicked.connect(lambda: self.onMsgButton("MATCH_FINISHED"))
                msg.showMessage()
            else:
                msg = MessageBox("Irregular board","There are illegal changes", self.view.geometry().center())
                msg.buttonClicked.connect(lambda: self.onMsgButton("ERROR"))
                msg.showMessage()
        elif packet_type == DONE: 
            if payload["done"] == True:
                if self.mode == 0:
                    self.timer.stop()
                    msg = MessageBox("Match finished","Game over,you lost", self.view.geometry().center())
                    self.updateCanvas()
                    msg.buttonClicked.connect(lambda: self.onMsgButton("MATCH_FINISHED"))
                    msg.showMessage()
                else:
                    self.timer.stop()
                    msg = MessageBox("Match finished","Sudoku completed", self.view.geometry().center())
                    self.updateCanvas()
                    msg.buttonClicked.connect(lambda: self.onMsgButton("MATCH_FINISHED"))
                    msg.showMessage()
            else:
                msg = MessageBox("Irregular board","There are illegal changes", self.view.geometry().center())
                msg.buttonClicked.connect(lambda: self.onMsgButton("ERROR"))
                msg.showMessage()
        elif packet_type == CHANGE_VALUE:
            self.updateBoard(payload["row"],payload["col"],payload["value"])
        elif packet_type == PING:
            sendPacket(self.conn, PING_ACK, "")
        elif packet_type == ERROR:
            msg = MessageBox("Error",payload["msg"], self.view.geometry().center())
            msg.buttonClicked.connect(lambda: self.onMsgButton("ERROR"))
            msg.showMessage()

  
    def onMsgButton(self, msg):
        self.enableDifficultyButton()
        self.flushBoard()
        if msg == "ERROR":
            self.view.stackedWidget.setCurrentIndex(7)
        elif msg == "MATCH_FINISHED":
            self.view.stackedWidget.setCurrentIndex(6)

    def fillBoard(self, board):
        self.board = board  
        self.count = 0
        self.mask = [[True for j in range(9)] for i in range(9)]

        self.moves = []
        for r in range(0,9):
            for c in range(0,9):
                box_grid = self.view.gridLayout.itemAtPosition(r//3,(c//3)+1)
                item = box_grid.itemAtPosition(r%3,c%3)        
                tool_button = item.widget()
                if board[r][c] != 0:
                    tool_button.setText(str(board[r][c]))
                    style = tool_button.styleSheet().replace("background-color: white;", "background-color: #dddddd;")
                    tool_button.setStyleSheet(style)
                    tool_button.setEnabled(False)
                else:
                    self.count += 1
        self.start_time = time.time()
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
        button = QtWidgets.QToolButton()
        button.setText('C')
        button.pressed.connect(lambda value = (str(0),numeric_keypad) : self.onKeyPad(value[0], value[1]))
        grid_layout.addWidget(button,3,1,1,1)

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
        old_value = tool_button.text()
        old_value = int(old_value) if old_value != "" else 0 
        if self.board[self.row][self.col] == 0 and value != "0":
            self.count -= 1
        elif self.board[self.row][self.col] != 0 and value == "0":
            self.count += 1

        self.moves.append((time.time()-self.start_time, 81-self.count))
        tool_button.setText(value if value != "0" else "")
        self.board[self.row][self.col] = int(value)
        verify(self.board, self.row, self.col, old_value, int(value), self.mask)
        self.cellsColor()
        #challenge mode
        if self.mode == 0:
            if self.count == 0:
                for i in range(9):
                    for j in range(9):
                        if self.mask[i][j] == False:
                            print(i)
                            print(j)
                            print(self.mask[i][j])
                            print(self.board[i][j])
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


    def cellsColor(self):
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
         

    def error_received(self):
        title = "Connection Error"
        text = "There is a connection error, retry"
        msg = MessageBox(title, text, self.view.geometry().center())
        msg.buttonClicked.connect(lambda: self.onMsgButton("ERROR"))
        msg.showMessage()
        self.view.stackedWidget.setCurrentIndex(2)
        
    def enableDifficultyButton(self):
        self.view.easyButton.setEnabled(True)
        self.view.mediumButton.setEnabled(True)
        self.view.hardButton.setEnabled(True)

    def flushBoard(self):
        for r in range(9):
            for c in range(9):
                box_grid = self.view.gridLayout.itemAtPosition(r//3, (c//3) + 1)
                item = box_grid.itemAtPosition(r%3, c%3)        
                tool_button = item.widget()
                style = tool_button.styleSheet().replace("background-color: #dddddd;", "background-color: white;")
                style = tool_button.styleSheet().replace("color:red;", "color:black;")
                tool_button.setStyleSheet(style)
                tool_button.setText("")
                tool_button.setEnabled(True)

        
    def updateBoard(self, row, col, value):
        box_grid = self.view.gridLayout.itemAtPosition(row//3, (col//3) + 1)
        item = box_grid.itemAtPosition(row%3, col%3)        
        tool_button = item.widget()
        old_value = tool_button.text()
        old_value = int(old_value) if old_value != "" else 0 
        tool_button.setText(str(value))
        self.board[row][col] = int(value)
        verify(self.board, row, col, old_value, int(value), self.mask)       
        self.cellsColor()


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    view = MainWindow()
    sudokuController(view=view)
    view.show()
    sys.exit(app.exec_())
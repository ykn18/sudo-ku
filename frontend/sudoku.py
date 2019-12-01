from sudoku_UI import *
from PyQt5.QtWidgets import QApplication, QMessageBox, QDialog, QLabel, QHBoxLayout
from authentication import *
import sys
import ast
from communication import *
import json

class sudokuController:
    #view
    #token
    #box_grid_row
    #box_grid_col
    #item_row
    #item_col
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
                msg.setIcon(QMessageBox.Information)
                msg.setText(data["message"])
                msg.setWindowTitle("Bad credentials")
                msg.exec_()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Insert the same password")
            msg.setWindowTitle("Bad credentials")
            msg.exec_()
    
    def fillBoard(self, board):
        #board = "[[0 0 0 1 2 0 4 0 0] [2 7 0 0 6 0 5 3 0] [0 5 4 0 0 0 0 0 0] [0 0 2 6 9 1 0 0 0] [0 1 8 3 0 0 0 0 4] [0 0 0 4 8 7 0 2 3] [9 0 0 0 0 8 0 0 0] [6 0 5 0 0 9 0 4 0] [0 0 1 0 3 0 0 8 0]]"
        #board = board.replace(" ", ", ")
        #oard = ast.literal_eval(board)
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
                    tool_button.pressed.connect(lambda pos = (r, c): self.onItem(pos[0], pos[1]))
    
    def onItem(self, row, col):
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
        tool_button.setText(value)
        style = tool_button.styleSheet().replace("background-color: white;", "background-color: #f5f5f5;")
        tool_button.setStyleSheet(style)
        keypad.close()

    def setMode(self, mode):
        self.mode = mode
        self.view.stackedWidget.setCurrentIndex(3)

    def setDifficulty(self, difficulty):  
        self.view.stackedWidget.setCurrentIndex(4)
        self.difficulty = difficulty
        self.sendMatchRequest()
        

    def sendMatchRequest(self):
        print("send match request") 
        match_request = {"token" : self.token, "mode" : self.mode, "difficulty" : self.difficulty}
        conn = createConnection()
        sendPacket(conn, 0, json.dumps(match_request))
        packet_type, payload = receivePacket(conn)
        print(packet_type)
        print(payload)
        payload = json.loads(payload)
        if (packet_type is not 1) and (payload["status"] is not 0):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Error in the match request")
            msg.setWindowTitle("Error")
            msg.exec_()
            self.view.stackedWidget.setCurrentIndex(2)
        else:
            self.waitMatchFound(conn)
    
    def waitMatchFound(self, conn):
        print("wait match found")
        packet_type, payload = receivePacket(conn)
        if packet_type == 2:
            payload = json.loads(payload)
            self.fillBoard(payload["board"])
            self.view.stackedWidget.setCurrentIndex(5)


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
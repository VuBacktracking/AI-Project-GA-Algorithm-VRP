import sys
import time
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QFileDialog, QMessageBox, QLineEdit
from PyQt6.QtGui import QIntValidator, QKeySequence, QPainter, QColor, QFont, QPen
from Chromosome import TourManager, Tour
from Population import Population
from Genetic import Genetic
from Map import drawMap, HCMMapWindow

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.tourmanager = TourManager()
        self.best_path = None

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(938, 754)
        MainWindow.setStyleSheet("background-color: rgb(171, 222, 255);")

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Dòng chữ ở giữa
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(510, 0, 411, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")

        # Input box
        self.Input = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.Input.setGeometry(QtCore.QRect(510, 60, 420, 360))
        self.Input.setObjectName("Input")

        # Label City Data (Input)
        self.label_City_data = QtWidgets.QLabel(parent=self.Input)
        self.label_City_data.setGeometry(QtCore.QRect(10, 30, 111, 31))
        self.label_City_data.setObjectName("label_City_data")

        # File Line Edit (Input)
        self.File_lineEdit = QtWidgets.QLineEdit(parent=self.Input)
        self.File_lineEdit.setGeometry(QtCore.QRect(140, 30, 181, 31))
        self.File_lineEdit.setObjectName("File_lineEdit")

        # Browse City Button (Input)
        self.Browse_city_Button = QtWidgets.QPushButton(parent=self.Input)
        self.Browse_city_Button.setGeometry(QtCore.QRect(330, 30, 80, 31))
        self.Browse_city_Button.setObjectName("Browse_city_Button")
        self.Browse_city_Button.clicked.connect(self.browsefile_button)

        # Data Type Label (Input)
        self.Datatype_label = QtWidgets.QLabel(parent=self.Input)
        self.Datatype_label.setGeometry(QtCore.QRect(10, 80, 111, 31))
        self.Datatype_label.setObjectName("Datatype_label")

        # Data Type Combo Box (Input)
        self.Datatype_comboBox = QtWidgets.QComboBox(parent=self.Input)
        self.Datatype_comboBox.setGeometry(QtCore.QRect(140, 80, 181, 31))
        self.Datatype_comboBox.setObjectName("Datatype_comboBox")
        self.Datatype_comboBox.setCurrentText("Ma trận trọng số")
        self.Datatype_comboBox.addItem("Ma trận trọng số")
        self.Datatype_comboBox.addItem("Danh sách tọa độ")
        self.Datatype_comboBox.currentTextChanged.connect(self.on_datatype_combobox_changed)

        # Cost Label (Input)
        self.Cost_label = QtWidgets.QLabel(parent=self.Input)
        self.Cost_label.setGeometry(QtCore.QRect(10, 130, 111, 31))
        self.Cost_label.setObjectName("label_Cost")

        # Cost Line Edit (Input)
        self.Cost_lineEdit = QtWidgets.QLineEdit(parent=self.Input)
        self.Cost_lineEdit.setGeometry(QtCore.QRect(140, 130, 181, 31))
        self.Cost_lineEdit.setObjectName("Cost_lineEdit")

        # Browse Cost Button (Input)
        self.Browse_Cost_Button = QtWidgets.QPushButton(parent=self.Input)
        self.Browse_Cost_Button.setGeometry(QtCore.QRect(330, 130, 80, 31))
        self.Browse_Cost_Button.setObjectName("Browse_Cost_Button")
        self.Browse_Cost_Button.clicked.connect(self.browsecost_button)

        # NumGen Label (Input)
        self.NumGen_label = QtWidgets.QLabel(parent=self.Input)
        self.NumGen_label.setGeometry(QtCore.QRect(10, 180, 121, 31))
        self.NumGen_label.setObjectName("label_NumGen")

        # NumGen Line Edit (Input)
        self.NumGen_lineEdit = QtWidgets.QLineEdit(parent=self.Input)
        self.NumGen_lineEdit.setGeometry(QtCore.QRect(140, 180, 181, 31))
        self.NumGen_lineEdit.setObjectName("NumGen_lineEdit")
        self.validator = QIntValidator()
        self.validator.setRange(0, 25000)
        self.NumGen_lineEdit.setValidator(self.validator)

        # Pop Size Label (Input)
        self.PopSize_label = QtWidgets.QLabel(parent=self.Input)
        self.PopSize_label.setGeometry(QtCore.QRect(10, 230, 131, 31))
        self.PopSize_label.setObjectName("label_PopSize")

        # Pop Size Line Edit (Input)
        self.PopSize_lineEdit = QtWidgets.QLineEdit(parent=self.Input)
        self.PopSize_lineEdit.setGeometry(QtCore.QRect(140, 230, 181, 31))
        self.PopSize_lineEdit.setObjectName("PopSize_lineEdit")
        self.validator1 = QIntValidator()
        self.validator1.setRange(0, 25000)
        self.PopSize_lineEdit.setValidator(self.validator1)

        # Cost Check Box
        self.CostcheckBox = QtWidgets.QCheckBox(parent=self.Input)
        self.CostcheckBox.setGeometry(QtCore.QRect(70, 270, 111, 31))
        self.CostcheckBox.setObjectName("CostcheckBox")

        #Distance Check Box
        self.DistancecheckBox = QtWidgets.QCheckBox(parent=self.Input)
        self.DistancecheckBox.setGeometry(QtCore.QRect(250, 270, 141, 31))
        self.DistancecheckBox.setObjectName("DistancecheckBox")

        # Calculation Button
        self.Calc_Button = QtWidgets.QPushButton(parent=self.Input)
        self.Calc_Button.setGeometry(QtCore.QRect(170, 310, 81, 31))
        self.Calc_Button.setObjectName("Calc_Button")
        self.Calc_Button.clicked.connect(self.findfittest)

        # Map Button
        self.Map_Button = QtWidgets.QPushButton(parent=self.Input)
        self.Map_Button.setGeometry(QtCore.QRect(40, 310, 80, 31))
        self.Map_Button.setObjectName("Map_Button")
        self.Map_Button.clicked.connect(self.drawMap)

        # Clear Button
        self.Clear_Button = QtWidgets.QPushButton(parent=self.Input)
        self.Clear_Button.setGeometry(QtCore.QRect(300, 310, 80, 31))
        self.Clear_Button.setObjectName("Clear_Button")
        self.Clear_Button.clicked.connect(self.clearbutton)

        # Answer Group Box
        self.Answer_groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.Answer_groupBox.setGeometry(QtCore.QRect(510, 430, 421, 131))
        self.Answer_groupBox.setObjectName("TimegroupBox")

        # Time Label (AGB)
        self.Time_label = QtWidgets.QLabel(parent=self.Answer_groupBox)
        self.Time_label.setGeometry(QtCore.QRect(20, 30, 131, 31))
        self.Time_label.setObjectName("Timelabel")

        # Time Line Edit (AGB)
        self.Time_lineEdit = QtWidgets.QLineEdit(parent=self.Answer_groupBox)
        self.Time_lineEdit.setGeometry(QtCore.QRect(160, 30, 231, 31))
        self.Time_lineEdit.setObjectName("Time_lineEdit")

        # Fittest Label (AGB)
        self.Fittest_label = QtWidgets.QLabel(parent=self.Answer_groupBox)
        self.Fittest_label.setGeometry(QtCore.QRect(20, 80, 131, 31))
        self.Fittest_label.setObjectName("Timelabel")

        # Fittest Line Edit (AGB)
        self.Fittest_lineEdit = QtWidgets.QLineEdit(parent=self.Answer_groupBox)
        self.Fittest_lineEdit.setGeometry(QtCore.QRect(160, 80, 231, 31))
        self.Fittest_lineEdit.setObjectName("Time_lineEdit")

        # Output box
        self.Output = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.Output.setGeometry(QtCore.QRect(20, 570, 911, 151))
        self.Output.setObjectName("Output")

        # Output Text Edit (Ouput)
        self.Output_textEdit = QtWidgets.QTextEdit(parent=self.Output)
        self.Output_textEdit.setGeometry(QtCore.QRect(20, 20, 871, 120))
        self.Output_textEdit.setObjectName("Output_textEdit")
        self.Output_textEdit.setReadOnly(True)

        # Image Label
        self.Image_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.Image_label.setGeometry(QtCore.QRect(10, 10, 491, 551))
        self.Image_label.setText("")
        self.Image_label.setPixmap(QtGui.QPixmap("ban-do-dien-tich-cac-quan-tphcm-full-hd.png"))
        self.Image_label.setScaledContents(True)
        self.Image_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Image_label.setObjectName("Image_label")

        # menubar
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 938, 26))
        self.menubar.setObjectName("menubar")

        # menuFile
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.menuFile.setFont(font)
        self.menuFile.setObjectName("menuFile")

        # action
        MainWindow.setMenuBar(self.menubar)
        self.actionOpen = QtGui.QAction(parent=MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpen.triggered.connect(self.browsefile_button)
        self.actionOpen.setShortcut("Ctrl+O")
        seq = QKeySequence('Ctrl+O')
        self.actionOpen.setShortcut(seq)

        self.actionClear = QtGui.QAction(parent=MainWindow)
        self.actionClear.setObjectName("actionClear")
        self.actionClear.triggered.connect(self.clearbutton)
        self.actionClear.setShortcut("Ctrl+D")
        seq2 = QKeySequence('Ctrl+D')
        self.actionClear.setShortcut(seq2)

        self.actionClose = QtGui.QAction(parent=MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionClose.triggered.connect(self.fileclose)

        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionClear)
        self.menuFile.addAction(self.actionClose)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def findfittest(self):
        if (self.PopSize_lineEdit.text() == ''):
            self.Message()
        elif (self.NumGen_lineEdit.text() == ''):
            self.Message()
        elif (self.File_lineEdit.text() == ''):
            self.Message()
        elif self.tourmanager is None:
            self.Message()
        else:
            if self.Datatype_comboBox.currentText() == "Danh sách tọa độ":
                temp = TourManager()
                temp.read_file_coor_tour(self.File_lineEdit.text())
                self.tourmanager = temp
                start_time = time.time()
                gen_size = self.NumGen_lineEdit.text()
                POPULATION_SIZE = self.PopSize_lineEdit.text()
                pop = Population(self.tourmanager, int(POPULATION_SIZE), True)
                ga = Genetic(self.tourmanager, int(gen_size))
                best_gene = ga.evolveCoorDistancePopulation(pop)
                end_time = time.time()
                self.best_path = best_gene.getFittestCoorDistance()
                total_Distance = str(best_gene.getFittestCoorDistance().getCoorDistance())
                self.Time_lineEdit.setText(f'{(end_time - start_time)} s')
                self.Fittest_lineEdit.setText(total_Distance)
                self.Output_textEdit.setText("Chi tiết chu trình: " + str(self.best_path.get_answer_for_coord()))
            if self.Datatype_comboBox.currentText() == "Ma trận trọng số":
                if self.Cost_lineEdit.text() == "":
                    self.Message()
                elif self.CostcheckBox.isChecked()==False and self.DistancecheckBox.isChecked()==False:
                    self.Message()
                else:
                    self.tourmanager.reset_tour()
                    temp = TourManager()
                    temp.read_file_tour(self.File_lineEdit.text())
                    temp.read_file_matrix(self.Cost_lineEdit.text())
                    self.tourmanager = temp
                    start_time = time.time()
                    gen_size = self.NumGen_lineEdit.text()
                    POPULATION_SIZE = self.PopSize_lineEdit.text()
                    pop = Population(self.tourmanager, int(POPULATION_SIZE), True)
                    ga = Genetic(self.tourmanager, int(gen_size))
                    best_gene = ga.evolveCostPopulation(pop)
                    end_time = time.time()
                    self.best_path = best_gene.getFittestCost()
                    total_cost = best_gene.getFittestCost().getCost()
                    self.Time_lineEdit.setText(f'{(end_time - start_time)} s')    
                    if self.CostcheckBox.isChecked():
                        self.Fittest_lineEdit.setText(str(round(total_cost, 2)) +" đồng")
                        self.Output_textEdit.setText("Chi tiết chu trình: " + str(self.best_path.get_answer_for_apply()))
                    elif self.DistancecheckBox.isChecked():
                        self.Fittest_lineEdit.setText(str(round(total_cost / 1000, 2)) +" km")
                        self.Output_textEdit.setText("Chi tiết chu trình: " + str(self.best_path.get_answer_for_apply()))

    def drawMap(self):
        if self.Datatype_comboBox.currentText() == "Danh sách tọa độ":
            drawMap(self.tourmanager, self.best_path)
        else:
            self.second_window = HCMMapWindow()
            self.second_window.draw(self.best_path)
            self.second_window.show()

    def on_datatype_combobox_changed(self, current_text):
        if current_text == "Ma trận trọng số":
            self.Cost_label.setVisible(True)
            self.Cost_lineEdit.setVisible(True)
            self.Browse_Cost_Button.setVisible(True)

            self.CostcheckBox.setVisible(True)
            self.DistancecheckBox.setVisible(True)

        if current_text == "Danh sách tọa độ":
            self.Cost_label.setVisible(False)
            self.Cost_lineEdit.setVisible(False)
            self.Browse_Cost_Button.setVisible(False)

            self.CostcheckBox.setVisible(False)
            self.DistancecheckBox.setVisible(False)

    def browsefile_button(self):
        self.tourmanager.reset_tour()
        self.fileName = QFileDialog.getOpenFileName(None, 'Open file', '', '(*.txt)')
        self.File_lineEdit.setText(self.fileName[0])

    def browsecost_button(self):
        self.tourmanager.reset_tour()
        self.fileName = QFileDialog.getOpenFileName(None, 'Open file', '', '(*.txt)')
        self.Cost_lineEdit.setText(self.fileName[0])

    def clearbutton(self):
        self.NumGen_lineEdit.clear()
        self.PopSize_lineEdit.clear()
        self.Time_lineEdit.clear()
        self.Output_textEdit.clear()
        self.CostcheckBox.setChecked(False)
        self.DistancecheckBox.setChecked(False)
        self.tourmanager.reset_tour()

    def fileclose(self):
        exit()

    def Message(self):
        self.msg = QMessageBox(MainWindow)
        self.msg.setText("Vui lòng nhập đầy đủ thông tin Input")
        self.msg.setWindowTitle("WARNING!")
        self.msg.setIcon(QMessageBox.Icon.Warning)
        self.msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        self.msg.exec()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hệ thống tối ưu hóa hành trình vận chuyển đơn hàng"))
        self.Input.setTitle(_translate("MainWindow", "INPUT"))
        self.Browse_city_Button.setText(_translate("MainWindow", "Browse"))
        self.label_City_data.setText(_translate("MainWindow", "Dữ liệu thành phố"))
        self.Cost_label.setText(_translate("MainWindow", "Dữ liệu trọng số"))
        self.Browse_Cost_Button.setText(_translate("MainWindow", "Browse"))
        self.NumGen_label.setText(_translate("MainWindow", "Số thế hệ tối đa"))
        self.PopSize_label.setText(_translate("MainWindow", "Kích thước quần thể"))
        self.Calc_Button.setText(_translate("MainWindow", "Calculation"))
        self.Map_Button.setText(_translate("MainWindow", "Map"))
        self.CostcheckBox.setText(_translate("MainWindow", "Tối ưu chi phí"))
        self.DistancecheckBox.setText(_translate("MainWindow", "Tối ưu quãng đường"))
        self.Clear_Button.setText(_translate("MainWindow", "Clear"))
        self.Datatype_label.setText(_translate("MainWindow", "Loại dữ liệu"))
        self.Output.setTitle(_translate("MainWindow", "OUTPUT"))
        self.Answer_groupBox.setTitle(_translate("MainWindow", "TIME"))
        self.Time_label.setText(_translate("MainWindow", "Thời gian thực hiện"))
        self.Fittest_label.setText(_translate("MainWindow", "Kết quả tối ưu"))
        self.label.setText(_translate("MainWindow", "HỆ THỐNG TỐI ƯU HÓA HÀNH TRÌNH VẬN CHUYỂN ĐƠN HÀNG"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionClear.setText(_translate("MainWindow", "Clear"))
        self.actionClear.setShortcut(_translate("MainWindow", "Ctrl+D"))
        self.actionClose.setText(_translate("MainWindow", "Close"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(355, 450)
        MainWindow.setStyleSheet("QToolTip\n"
"{\n"
"     border: 1px solid black;\n"
"     background-color: #ffa02f;\n"
"     padding: 1px;\n"
"     border-radius: 3px;\n"
"     opacity: 100;\n"
"}\n"
"\n"
"QWidget\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QTreeView, QListView\n"
"{\n"
"    background-color: silver;\n"
"    margin-left: 5px;\n"
"}\n"
"\n"
"QWidget:item:hover\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #ca0619);\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:item:selected\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    background: transparent;\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    background: #444;\n"
"    border: 1px solid #000;\n"
"    background-color: QLinearGradient(\n"
"        x1:0, y1:0,\n"
"        x2:0, y2:1,\n"
"        stop:1 #212121,\n"
"        stop:0.4 #343434/*,\n"
"        stop:0.2 #343434,\n"
"        stop:0.1 #ffaa00*/\n"
"    );\n"
"    margin-bottom:-1px;\n"
"    padding-bottom:1px;\n"
"}\n"
"\n"
"QMenu\n"
"{\n"
"    border: 1px solid #000;\n"
"}\n"
"\n"
"QMenu::item\n"
"{\n"
"    padding: 2px 20px 2px 20px;\n"
"}\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:disabled\n"
"{\n"
"    color: #808080;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QAbstractItemView\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0.1 #646464, stop: 1 #5d5d5d);\n"
"}\n"
"\n"
"QWidget:focus\n"
"{\n"
"    /*border: 1px solid darkgray;*/\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-width: 1px;\n"
"    border-color: #333;\n"
"    border-style: solid;\n"
"    border-radius: 25;\n"
"    padding: 3px;\n"
"    font-size: 12px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    min-width: 40px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #ffaa00;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QComboBox:hover,QPushButton:hover\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f25, stop: 1 #f25);\n"
"}\n"
"\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"    selection-background-color: #ffaa00;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    border: 2px solid darkgray;\n"
"    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 15px;\n"
"\n"
"     border-left-width: 0px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"     border-bottom-right-radius: 3px;\n"
" }\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"     image: url(:/dark_orange/img/down_arrow.png);\n"
"}\n"
"\n"
"QGroupBox\n"
"{\n"
"    border: 1px solid darkgray;\n"
"    margin-top: 10px;\n"
"}\n"
"\n"
"QGroupBox:focus\n"
"{\n"
"    border: 1px solid darkgray;\n"
"}\n"
"\n"
"QTextEdit:focus\n"
"{\n"
"    border: 1px solid darkgray;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"     border: 1px solid #222222;\n"
"     background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"     height: 7px;\n"
"     margin: 0px 16px 0 16px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"      subcontrol-position: right;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal, QScrollBar::left-arrow:horizontal\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"      width: 7px;\n"
"      margin: 16px 0 16px 0;\n"
"      border: 1px solid #222222;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      height: 14px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #d7801a, stop: 1 #ffa02f);\n"
"      height: 14px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QPlainTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161, stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QCheckBox:disabled\n"
"{\n"
"color: #414141;\n"
"}\n"
"\n"
"QDockWidget::title\n"
"{\n"
"    text-align: center;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button, QDockWidget::float-button\n"
"{\n"
"    text-align: center;\n"
"    spacing: 1px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button:hover, QDockWidget::float-button:hover\n"
"{\n"
"    background: #242424;\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed, QDockWidget::float-button:pressed\n"
"{\n"
"    padding: 1px -1px -1px 1px;\n"
"}\n"
"\n"
"QMainWindow::separator\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #4c4c4c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QMainWindow::separator:hover\n"
"{\n"
"\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #d7801a, stop:0.5 #b56c17 stop:1 #ffa02f);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QToolBar::handle\n"
"{\n"
"     spacing: 3px; /* spacing between items in the tool bar */\n"
"     background: url(:/dark_orange/img/handle.png);\n"
"}\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 2px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"QProgressBar\n"
"{\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: #d7801a;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #444;\n"
"    border-bottom-style: none;\n"
"    background-color: #323232;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-top: 3px;\n"
"    padding-bottom: 2px;\n"
"    margin-right: -1px;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #444;\n"
"    top: 1px;\n"
"}\n"
"\n"
"QTabBar::tab:last\n"
"{\n"
"    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
"    border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:first:!selected\n"
"{\n"
" margin-left: 0px; /* the last selected tab has nothing to overlap with on the right */\n"
"\n"
"\n"
"    border-top-left-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    border-bottom-style: solid;\n"
"    margin-top: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:.4 #343434);\n"
"}\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    margin-bottom: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover\n"
"{\n"
"    /*border-top: 2px solid #ffaa00;\n"
"    padding-bottom: 3px;*/\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:0.4 #343434, stop:0.2 #343434, stop:0.1 #ffaa00);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked, QRadioButton::indicator:unchecked{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked\n"
"{\n"
"    background-color: qradialgradient(\n"
"        cx: 0.5, cy: 0.5,\n"
"        fx: 0.5, fy: 0.5,\n"
"        radius: 1.0,\n"
"        stop: 0.25 #ffaa00,\n"
"        stop: 0.3 #323232\n"
"    );\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    width: 9px;\n"
"    height: 9px;\n"
"}\n"
"\n"
"QRadioButton::indicator\n"
"{\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover, QCheckBox::indicator:hover\n"
"{\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    image:url(:/dark_orange/img/checkbox.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:disabled, QRadioButton::indicator:disabled\n"
"{\n"
"    border: 1px solid #444;\n"
"}\n"
"\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border: 1px solid #3A3939;\n"
"    height: 8px;\n"
"    background: #201F1F;\n"
"    margin: 2px 0;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1,\n"
"      stop: 0.0 silver, stop: 0.2 #a8a8a8, stop: 1 #727272);\n"
"    border: 1px solid #3A3939;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    margin: -4px 0;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid #3A3939;\n"
"    width: 8px;\n"
"    background: #201F1F;\n"
"    margin: 0 0px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 silver,\n"
"      stop: 0.2 #a8a8a8, stop: 1 #727272);\n"
"    border: 1px solid #3A3939;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    margin: 0 -4px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QAbstractSpinBox {\n"
"    padding-top: 2px;\n"
"    padding-bottom: 2px;\n"
"    border: 1px solid darkgray;\n"
"\n"
"    border-radius: 2px;\n"
"    min-width: 50px;\n"
"}\n"
"")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.lcdNumber.setFont(font)
        self.lcdNumber.setStyleSheet("")
        self.lcdNumber.setDigitCount(10)
        self.lcdNumber.setObjectName("lcdNumber")
        self.verticalLayout.addWidget(self.lcdNumber)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_n4 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_n4.setMinimumSize(QtCore.QSize(52, 50))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_n4.setFont(font)
        self.pushButton_n4.setStyleSheet("QPushButton {\n"
"color: #1976D;\n"
"}")
        self.pushButton_n4.setObjectName("pushButton_n4")
        self.gridLayout.addWidget(self.pushButton_n4, 3, 0, 1, 1)
        self.pushButton_n1 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_n1.setMinimumSize(QtCore.QSize(52, 50))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_n1.setFont(font)
        self.pushButton_n1.setStyleSheet("QPushButton {\n"
"color: #1976D;\n"
"}")
        self.pushButton_n1.setObjectName("pushButton_n1")
        self.gridLayout.addWidget(self.pushButton_n1, 4, 0, 1, 1)
        self.pushButton_n8 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_n8.setMinimumSize(QtCore.QSize(52, 50))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_n8.setFont(font)
        self.pushButton_n8.setStyleSheet("QPushButton {\n"
"color: #1976D;\n"
"}")
        self.pushButton_n8.setObjectName("pushButton_n8")
        self.gridLayout.addWidget(self.pushButton_n8, 2, 1, 1, 1)
        self.pushButton_mul = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_mul.setMinimumSize(QtCore.QSize(52, 50))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_mul.setFont(font)
        self.pushButton_mul.setObjectName("pushButton_mul")
        self.gridLayout.addWidget(self.pushButton_mul, 2, 3, 1, 1)
        self.pushButton_n7 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_n7.setMinimumSize(QtCore.QSize(52, 50))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_n7.setFont(font)
        self.pushButton_n7.setStyleSheet("QPushButton {\n"
"color: #1976D;\n"
"}")
        self.pushButton_n7.setObjectName("pushButton_n7")
        self.gridLayout.addWidget(self.pushButton_n7, 2, 0, 1, 1)
        self.pushButton_n6 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_n6.setMinimumSize(QtCore.QSize(52, 50))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_n6.setFont(font)
        self.pushButton_n6.setStyleSheet("QPushButton {\n"
"color: #1976D;\n"
"}")
        self.pushButton_n6.setObjectName("pushButton_n6")
        self.gridLayout.addWidget(self.pushButton_n6, 3, 2, 1, 1)
        self.pushButton_n5 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_n5.setMinimumSize(QtCore.QSize(52, 50))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_n5.setFont(font)
        self.pushButton_n5.setStyleSheet("QPushButton {\n"
"color: #1976D;\n"
"}")
        self.pushButton_n5.setObjectName("pushButton_n5")
        self.gridLayout.addWidget(self.pushButton_n5, 3, 1, 1, 1)
        self.pushButton_n0 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_n0.setMinimumSize(QtCore.QSize(52, 50))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_n0.setFont(font)
        self.pushButton_n0.setStyleSheet("QPushButton {\n"
"color: #1976D;\n"
"}")
        self.pushButton_n0.setObjectName("pushButton_n0")
        self.gridLayout.addWidget(self.pushButton_n0, 5, 0, 1, 1)
        self.pushButton_n2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_n2.setMinimumSize(QtCore.QSize(52, 50))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_n2.setFont(font)
        self.pushButton_n2.setStyleSheet("QPushButton {\n"
"color: #1976D;\n"
"}")
        self.pushButton_n2.setObjectName("pushButton_n2")
        self.gridLayout.addWidget(self.pushButton_n2, 4, 1, 1, 1)
        self.pushButton_n9 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_n9.setMinimumSize(QtCore.QSize(52, 50))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_n9.setFont(font)
        self.pushButton_n9.setStyleSheet("QPushButton {\n"
"color: #1976D;\n"
"}")
        self.pushButton_n9.setObjectName("pushButton_n9")
        self.gridLayout.addWidget(self.pushButton_n9, 2, 2, 1, 1)
        self.pushButton_n3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_n3.setMinimumSize(QtCore.QSize(52, 50))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_n3.setFont(font)
        self.pushButton_n3.setStyleSheet("QPushButton {\n"
"color: #1976D;\n"
"}")
        self.pushButton_n3.setObjectName("pushButton_n3")
        self.gridLayout.addWidget(self.pushButton_n3, 4, 2, 1, 1)
        self.pushButton_div = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_div.setMinimumSize(QtCore.QSize(52, 50))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_div.setFont(font)
        self.pushButton_div.setObjectName("pushButton_div")
        self.gridLayout.addWidget(self.pushButton_div, 1, 3, 1, 1)
        self.pushButton_sub = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_sub.setMinimumSize(QtCore.QSize(52, 50))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_sub.setFont(font)
        self.pushButton_sub.setObjectName("pushButton_sub")
        self.gridLayout.addWidget(self.pushButton_sub, 3, 3, 1, 1)
        self.pushButton_add = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_add.setMinimumSize(QtCore.QSize(52, 50))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_add.setFont(font)
        self.pushButton_add.setObjectName("pushButton_add")
        self.gridLayout.addWidget(self.pushButton_add, 4, 3, 1, 1)
        self.pushButton_ac = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_ac.setMinimumSize(QtCore.QSize(52, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_ac.setFont(font)
        self.pushButton_ac.setStyleSheet("QPushButton {\n"
"    color: #f4433;\n"
"}")
        self.pushButton_ac.setObjectName("pushButton_ac")
        self.gridLayout.addWidget(self.pushButton_ac, 1, 0, 1, 1)
        self.pushButton_mr = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_mr.setMinimumSize(QtCore.QSize(52, 50))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_mr.setFont(font)
        self.pushButton_mr.setStyleSheet("QPushButton {\n"
"   color: #FFC10;\n"
"}")
        self.pushButton_mr.setObjectName("pushButton_mr")
        self.gridLayout.addWidget(self.pushButton_mr, 1, 2, 1, 1)
        self.pushButton_m = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_m.setMinimumSize(QtCore.QSize(52, 50))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_m.setFont(font)
        self.pushButton_m.setStyleSheet("QPushButton {\n"
"   color: #FFC10;\n"
"}")
        self.pushButton_m.setObjectName("pushButton_m")
        self.gridLayout.addWidget(self.pushButton_m, 1, 1, 1, 1)
        self.pushButton_pc = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_pc.setMinimumSize(QtCore.QSize(52, 50))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_pc.setFont(font)
        self.pushButton_pc.setObjectName("pushButton_pc")
        self.gridLayout.addWidget(self.pushButton_pc, 5, 1, 1, 1)
        self.pushButton_eq = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_eq.setMinimumSize(QtCore.QSize(52, 50))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_eq.setFont(font)
        self.pushButton_eq.setStyleSheet("QPushButton {\n"
"color: #4CAF5;\n"
"}")
        self.pushButton_eq.setObjectName("pushButton_eq")
        self.gridLayout.addWidget(self.pushButton_eq, 5, 2, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionReset = QtWidgets.QAction(MainWindow)
        self.actionReset.setObjectName("actionReset")
        self.actionAbout_Calculator = QtWidgets.QAction(MainWindow)
        self.actionAbout_Calculator.setObjectName("actionAbout_Calculator")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator - By : Anis Harkat"))
        MainWindow.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>QToolTip</p><p>{</p><p>     border: 1px solid black;</p><p>     background-color: #ffa02f;</p><p>     padding: 1px;</p><p>     border-radius: 3px;</p><p>     opacity: 100;</p><p>}</p><p><br/></p><p>QWidget</p><p>{</p><p>    color: #b1b1b1;</p><p>    background-color: #323232;</p><p>}</p><p><br/></p><p>QTreeView, QListView</p><p>{</p><p>    background-color: silver;</p><p>    margin-left: 5px;</p><p>}</p><p><br/></p><p>QWidget:item:hover</p><p>{</p><p>    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #ca0619);</p><p>    color: #000000;</p><p>}</p><p><br/></p><p>QWidget:item:selected</p><p>{</p><p>    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);</p><p>}</p><p><br/></p><p>QMenuBar::item</p><p>{</p><p>    background: transparent;</p><p>}</p><p><br/></p><p>QMenuBar::item:selected</p><p>{</p><p>    background: transparent;</p><p>    border: 1px solid #ffaa00;</p><p>}</p><p><br/></p><p>QMenuBar::item:pressed</p><p>{</p><p>    background: #444;</p><p>    border: 1px solid #000;</p><p>    background-color: QLinearGradient(</p><p>        x1:0, y1:0,</p><p>        x2:0, y2:1,</p><p>        stop:1 #212121,</p><p>        stop:0.4 #343434/*,</p><p>        stop:0.2 #343434,</p><p>        stop:0.1 #ffaa00*/</p><p>    );</p><p>    margin-bottom:-1px;</p><p>    padding-bottom:1px;</p><p>}</p><p><br/></p><p>QMenu</p><p>{</p><p>    border: 1px solid #000;</p><p>}</p><p><br/></p><p>QMenu::item</p><p>{</p><p>    padding: 2px 20px 2px 20px;</p><p>}</p><p><br/></p><p>QMenu::item:selected</p><p>{</p><p>    color: #000000;</p><p>}</p><p><br/></p><p>QWidget:disabled</p><p>{</p><p>    color: #808080;</p><p>    background-color: #323232;</p><p>}</p><p><br/></p><p>QAbstractItemView</p><p>{</p><p>    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0.1 #646464, stop: 1 #5d5d5d);</p><p>}</p><p><br/></p><p>QWidget:focus</p><p>{</p><p>    /*border: 1px solid darkgray;*/</p><p>}</p><p><br/></p><p>QLineEdit</p><p>{</p><p>    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);</p><p>    padding: 1px;</p><p>    border-style: solid;</p><p>    border: 1px solid #1e1e1e;</p><p>    border-radius: 5;</p><p>}</p><p><br/></p><p>QPushButton</p><p>{</p><p>    color: #b1b1b1;</p><p>    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);</p><p>    border-width: 1px;</p><p>    border-color: #1e1e1e;</p><p>    border-style: solid;</p><p>    border-radius: 6;</p><p>    padding: 3px;</p><p>    font-size: 12px;</p><p>    padding-left: 5px;</p><p>    padding-right: 5px;</p><p>    min-width: 40px;</p><p>}</p><p><br/></p><p>QPushButton:pressed</p><p>{</p><p>    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);</p><p>}</p><p><br/></p><p>QComboBox</p><p>{</p><p>    selection-background-color: #ffaa00;</p><p>    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);</p><p>    border-style: solid;</p><p>    border: 1px solid #1e1e1e;</p><p>    border-radius: 5;</p><p>}</p><p><br/></p><p>QComboBox:hover,QPushButton:hover</p><p>{</p><p>    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);</p><p>}</p><p><br/></p><p><br/></p><p>QComboBox:on</p><p>{</p><p>    padding-top: 3px;</p><p>    padding-left: 4px;</p><p>    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);</p><p>    selection-background-color: #ffaa00;</p><p>}</p><p><br/></p><p>QComboBox QAbstractItemView</p><p>{</p><p>    border: 2px solid darkgray;</p><p>    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);</p><p>}</p><p><br/></p><p>QComboBox::drop-down</p><p>{</p><p>     subcontrol-origin: padding;</p><p>     subcontrol-position: top right;</p><p>     width: 15px;</p><p><br/></p><p>     border-left-width: 0px;</p><p>     border-left-color: darkgray;</p><p>     border-left-style: solid; /* just a single line */</p><p>     border-top-right-radius: 3px; /* same radius as the QComboBox */</p><p>     border-bottom-right-radius: 3px;</p><p> }</p><p><br/></p><p>QComboBox::down-arrow</p><p>{</p><p>     image: url(:/dark_orange/img/down_arrow.png);</p><p>}</p><p><br/></p><p>QGroupBox</p><p>{</p><p>    border: 1px solid darkgray;</p><p>    margin-top: 10px;</p><p>}</p><p><br/></p><p>QGroupBox:focus</p><p>{</p><p>    border: 1px solid darkgray;</p><p>}</p><p><br/></p><p>QTextEdit:focus</p><p>{</p><p>    border: 1px solid darkgray;</p><p>}</p><p><br/></p><p>QScrollBar:horizontal {</p><p>     border: 1px solid #222222;</p><p>     background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);</p><p>     height: 7px;</p><p>     margin: 0px 16px 0 16px;</p><p>}</p><p><br/></p><p>QScrollBar::handle:horizontal</p><p>{</p><p>      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);</p><p>      min-height: 20px;</p><p>      border-radius: 2px;</p><p>}</p><p><br/></p><p>QScrollBar::add-line:horizontal {</p><p>      border: 1px solid #1b1b19;</p><p>      border-radius: 2px;</p><p>      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);</p><p>      width: 14px;</p><p>      subcontrol-position: right;</p><p>      subcontrol-origin: margin;</p><p>}</p><p><br/></p><p>QScrollBar::sub-line:horizontal {</p><p>      border: 1px solid #1b1b19;</p><p>      border-radius: 2px;</p><p>      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);</p><p>      width: 14px;</p><p>     subcontrol-position: left;</p><p>     subcontrol-origin: margin;</p><p>}</p><p><br/></p><p>QScrollBar::right-arrow:horizontal, QScrollBar::left-arrow:horizontal</p><p>{</p><p>      border: 1px solid black;</p><p>      width: 1px;</p><p>      height: 1px;</p><p>      background: white;</p><p>}</p><p><br/></p><p>QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal</p><p>{</p><p>      background: none;</p><p>}</p><p><br/></p><p>QScrollBar:vertical</p><p>{</p><p>      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);</p><p>      width: 7px;</p><p>      margin: 16px 0 16px 0;</p><p>      border: 1px solid #222222;</p><p>}</p><p><br/></p><p>QScrollBar::handle:vertical</p><p>{</p><p>      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);</p><p>      min-height: 20px;</p><p>      border-radius: 2px;</p><p>}</p><p><br/></p><p>QScrollBar::add-line:vertical</p><p>{</p><p>      border: 1px solid #1b1b19;</p><p>      border-radius: 2px;</p><p>      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);</p><p>      height: 14px;</p><p>      subcontrol-position: bottom;</p><p>      subcontrol-origin: margin;</p><p>}</p><p><br/></p><p>QScrollBar::sub-line:vertical</p><p>{</p><p>      border: 1px solid #1b1b19;</p><p>      border-radius: 2px;</p><p>      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #d7801a, stop: 1 #ffa02f);</p><p>      height: 14px;</p><p>      subcontrol-position: top;</p><p>      subcontrol-origin: margin;</p><p>}</p><p><br/></p><p>QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical</p><p>{</p><p>      border: 1px solid black;</p><p>      width: 1px;</p><p>      height: 1px;</p><p>      background: white;</p><p>}</p><p><br/></p><p><br/></p><p>QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical</p><p>{</p><p>      background: none;</p><p>}</p><p><br/></p><p>QTextEdit</p><p>{</p><p>    background-color: #242424;</p><p>}</p><p><br/></p><p>QPlainTextEdit</p><p>{</p><p>    background-color: #242424;</p><p>}</p><p><br/></p><p>QHeaderView::section</p><p>{</p><p>    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161, stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);</p><p>    color: white;</p><p>    padding-left: 4px;</p><p>    border: 1px solid #6c6c6c;</p><p>}</p><p><br/></p><p>QCheckBox:disabled</p><p>{</p><p>color: #414141;</p><p>}</p><p><br/></p><p>QDockWidget::title</p><p>{</p><p>    text-align: center;</p><p>    spacing: 3px; /* spacing between items in the tool bar */</p><p>    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);</p><p>}</p><p><br/></p><p>QDockWidget::close-button, QDockWidget::float-button</p><p>{</p><p>    text-align: center;</p><p>    spacing: 1px; /* spacing between items in the tool bar */</p><p>    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);</p><p>}</p><p><br/></p><p>QDockWidget::close-button:hover, QDockWidget::float-button:hover</p><p>{</p><p>    background: #242424;</p><p>}</p><p><br/></p><p>QDockWidget::close-button:pressed, QDockWidget::float-button:pressed</p><p>{</p><p>    padding: 1px -1px -1px 1px;</p><p>}</p><p><br/></p><p>QMainWindow::separator</p><p>{</p><p>    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);</p><p>    color: white;</p><p>    padding-left: 4px;</p><p>    border: 1px solid #4c4c4c;</p><p>    spacing: 3px; /* spacing between items in the tool bar */</p><p>}</p><p><br/></p><p>QMainWindow::separator:hover</p><p>{</p><p><br/></p><p>    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #d7801a, stop:0.5 #b56c17 stop:1 #ffa02f);</p><p>    color: white;</p><p>    padding-left: 4px;</p><p>    border: 1px solid #6c6c6c;</p><p>    spacing: 3px; /* spacing between items in the tool bar */</p><p>}</p><p><br/></p><p>QToolBar::handle</p><p>{</p><p>     spacing: 3px; /* spacing between items in the tool bar */</p><p>     background: url(:/dark_orange/img/handle.png);</p><p>}</p><p><br/></p><p>QMenu::separator</p><p>{</p><p>    height: 2px;</p><p>    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);</p><p>    color: white;</p><p>    padding-left: 4px;</p><p>    margin-left: 10px;</p><p>    margin-right: 5px;</p><p>}</p><p><br/></p><p>QProgressBar</p><p>{</p><p>    border: 2px solid grey;</p><p>    border-radius: 5px;</p><p>    text-align: center;</p><p>}</p><p><br/></p><p>QProgressBar::chunk</p><p>{</p><p>    background-color: #d7801a;</p><p>    width: 2.15px;</p><p>    margin: 0.5px;</p><p>}</p><p><br/></p><p>QTabBar::tab {</p><p>    color: #b1b1b1;</p><p>    border: 1px solid #444;</p><p>    border-bottom-style: none;</p><p>    background-color: #323232;</p><p>    padding-left: 10px;</p><p>    padding-right: 10px;</p><p>    padding-top: 3px;</p><p>    padding-bottom: 2px;</p><p>    margin-right: -1px;</p><p>}</p><p><br/></p><p>QTabWidget::pane {</p><p>    border: 1px solid #444;</p><p>    top: 1px;</p><p>}</p><p><br/></p><p>QTabBar::tab:last</p><p>{</p><p>    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */</p><p>    border-top-right-radius: 3px;</p><p>}</p><p><br/></p><p>QTabBar::tab:first:!selected</p><p>{</p><p> margin-left: 0px; /* the last selected tab has nothing to overlap with on the right */</p><p><br/></p><p><br/></p><p>    border-top-left-radius: 3px;</p><p>}</p><p><br/></p><p>QTabBar::tab:!selected</p><p>{</p><p>    color: #b1b1b1;</p><p>    border-bottom-style: solid;</p><p>    margin-top: 3px;</p><p>    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:.4 #343434);</p><p>}</p><p><br/></p><p>QTabBar::tab:selected</p><p>{</p><p>    border-top-left-radius: 3px;</p><p>    border-top-right-radius: 3px;</p><p>    margin-bottom: 0px;</p><p>}</p><p><br/></p><p>QTabBar::tab:!selected:hover</p><p>{</p><p>    /*border-top: 2px solid #ffaa00;</p><p>    padding-bottom: 3px;*/</p><p>    border-top-left-radius: 3px;</p><p>    border-top-right-radius: 3px;</p><p>    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:0.4 #343434, stop:0.2 #343434, stop:0.1 #ffaa00);</p><p>}</p><p><br/></p><p>QRadioButton::indicator:checked, QRadioButton::indicator:unchecked{</p><p>    color: #b1b1b1;</p><p>    background-color: #323232;</p><p>    border: 1px solid #b1b1b1;</p><p>    border-radius: 6px;</p><p>}</p><p><br/></p><p>QRadioButton::indicator:checked</p><p>{</p><p>    background-color: qradialgradient(</p><p>        cx: 0.5, cy: 0.5,</p><p>        fx: 0.5, fy: 0.5,</p><p>        radius: 1.0,</p><p>        stop: 0.25 #ffaa00,</p><p>        stop: 0.3 #323232</p><p>    );</p><p>}</p><p><br/></p><p>QCheckBox::indicator{</p><p>    color: #b1b1b1;</p><p>    background-color: #323232;</p><p>    border: 1px solid #b1b1b1;</p><p>    width: 9px;</p><p>    height: 9px;</p><p>}</p><p><br/></p><p>QRadioButton::indicator</p><p>{</p><p>    border-radius: 6px;</p><p>}</p><p><br/></p><p>QRadioButton::indicator:hover, QCheckBox::indicator:hover</p><p>{</p><p>    border: 1px solid #ffaa00;</p><p>}</p><p><br/></p><p>QCheckBox::indicator:checked</p><p>{</p><p>    image:url(:/dark_orange/img/checkbox.png);</p><p>}</p><p><br/></p><p>QCheckBox::indicator:disabled, QRadioButton::indicator:disabled</p><p>{</p><p>    border: 1px solid #444;</p><p>}</p><p><br/></p><p><br/></p><p>QSlider::groove:horizontal {</p><p>    border: 1px solid #3A3939;</p><p>    height: 8px;</p><p>    background: #201F1F;</p><p>    margin: 2px 0;</p><p>    border-radius: 2px;</p><p>}</p><p><br/></p><p>QSlider::handle:horizontal {</p><p>    background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1,</p><p>      stop: 0.0 silver, stop: 0.2 #a8a8a8, stop: 1 #727272);</p><p>    border: 1px solid #3A3939;</p><p>    width: 14px;</p><p>    height: 14px;</p><p>    margin: -4px 0;</p><p>    border-radius: 2px;</p><p>}</p><p><br/></p><p>QSlider::groove:vertical {</p><p>    border: 1px solid #3A3939;</p><p>    width: 8px;</p><p>    background: #201F1F;</p><p>    margin: 0 0px;</p><p>    border-radius: 2px;</p><p>}</p><p><br/></p><p>QSlider::handle:vertical {</p><p>    background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 silver,</p><p>      stop: 0.2 #a8a8a8, stop: 1 #727272);</p><p>    border: 1px solid #3A3939;</p><p>    width: 14px;</p><p>    height: 14px;</p><p>    margin: 0 -4px;</p><p>    border-radius: 2px;</p><p>}</p><p><br/></p><p>QAbstractSpinBox {</p><p>    padding-top: 2px;</p><p>    padding-bottom: 2px;</p><p>    border: 1px solid darkgray;</p><p><br/></p><p>    border-radius: 2px;</p><p>    min-width: 50px;</p><p>}</p><p><br/></p><p><br/></p><p><br/></p></body></html>"))
        self.pushButton_n4.setText(_translate("MainWindow", "4"))
        self.pushButton_n4.setShortcut(_translate("MainWindow", "4"))
        self.pushButton_n1.setText(_translate("MainWindow", "1"))
        self.pushButton_n1.setShortcut(_translate("MainWindow", "1"))
        self.pushButton_n8.setText(_translate("MainWindow", "8"))
        self.pushButton_n8.setShortcut(_translate("MainWindow", "8"))
        self.pushButton_mul.setText(_translate("MainWindow", "x"))
        self.pushButton_mul.setShortcut(_translate("MainWindow", "*"))
        self.pushButton_n7.setText(_translate("MainWindow", "7"))
        self.pushButton_n7.setShortcut(_translate("MainWindow", "7"))
        self.pushButton_n6.setText(_translate("MainWindow", "6"))
        self.pushButton_n6.setShortcut(_translate("MainWindow", "6"))
        self.pushButton_n5.setText(_translate("MainWindow", "5"))
        self.pushButton_n5.setShortcut(_translate("MainWindow", "5"))
        self.pushButton_n0.setText(_translate("MainWindow", "0"))
        self.pushButton_n0.setShortcut(_translate("MainWindow", "0"))
        self.pushButton_n2.setText(_translate("MainWindow", "2"))
        self.pushButton_n2.setShortcut(_translate("MainWindow", "2"))
        self.pushButton_n9.setText(_translate("MainWindow", "9"))
        self.pushButton_n9.setShortcut(_translate("MainWindow", "9"))
        self.pushButton_n3.setText(_translate("MainWindow", "3"))
        self.pushButton_n3.setShortcut(_translate("MainWindow", "3"))
        self.pushButton_div.setText(_translate("MainWindow", "÷"))
        self.pushButton_div.setShortcut(_translate("MainWindow", "/"))
        self.pushButton_sub.setText(_translate("MainWindow", "-"))
        self.pushButton_sub.setShortcut(_translate("MainWindow", "-"))
        self.pushButton_add.setText(_translate("MainWindow", "+"))
        self.pushButton_add.setShortcut(_translate("MainWindow", "+"))
        self.pushButton_ac.setText(_translate("MainWindow", "AC"))
        self.pushButton_ac.setShortcut(_translate("MainWindow", "Esc"))
        self.pushButton_mr.setText(_translate("MainWindow", "MR"))
        self.pushButton_mr.setShortcut(_translate("MainWindow", "R"))
        self.pushButton_m.setText(_translate("MainWindow", "M"))
        self.pushButton_m.setShortcut(_translate("MainWindow", "M"))
        self.pushButton_pc.setText(_translate("MainWindow", "%"))
        self.pushButton_pc.setShortcut(_translate("MainWindow", "%"))
        self.pushButton_eq.setText(_translate("MainWindow", "="))
        self.pushButton_eq.setShortcut(_translate("MainWindow", "Return"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionReset.setText(_translate("MainWindow", "Reset"))
        self.actionReset.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.actionAbout_Calculator.setText(_translate("MainWindow", "About Calculator"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

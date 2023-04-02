from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QButtonGroup,
    QFileDialog,
    QFrame,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QRadioButton,
    QSpinBox,
    QTextBrowser,
    QVBoxLayout,
    QWidget
)
import codewordgenerator


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Codeword Generator")

        # create layouts
        layout = QVBoxLayout()
        interaction_layout = QVBoxLayout()
        settings_layout = QHBoxLayout()
        style_layout = QVBoxLayout()
        customization_layout = QVBoxLayout()
        files_layout = QVBoxLayout()
        exec_layout = QVBoxLayout()
        results_layout = QVBoxLayout()

        # create & add widgets
        # style_layout
        self.cwStyle = -1
        style_layout.addWidget(QLabel("Style"))
        self.nnRadio = QRadioButton("Noun-Noun")
        self.anRadio = QRadioButton("Adjective-Noun")
        self.vnRadio = QRadioButton("Verb-Noun")
        self.radioGroup = QButtonGroup()
        self.radioGroup.addButton(self.nnRadio, 1)
        self.radioGroup.addButton(self.anRadio, 2)
        self.radioGroup.addButton(self.vnRadio, 3)

        self.radioGroup.buttonClicked.connect(self.setStyle)

        style_layout.addWidget(self.nnRadio)
        style_layout.addWidget(self.anRadio)
        style_layout.addWidget(self.vnRadio)
        style_layout.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        # customization_layout
        customization_layout.addWidget(QLabel("Number"))
        self.numBox = QSpinBox()
        self.numBox.setMinimum(1)
        customization_layout.addWidget(self.numBox)

        self.numBox.valueChanged.connect(self.setNum)

        customization_layout.addWidget(QLabel("Delimiter"))
        self.delBox = QLineEdit()
        self.delBox.setMaxLength(1)

        self.delBox.textChanged.connect(self.setDel)

        # delBox = QComboBox()
        # delBox.addItems(["", " ", "-", "_"])
        # delBox.setPlaceholderText("Delim")
        customization_layout.addWidget(self.delBox)
        customization_layout.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        # files_layout
        self.files = {"nFile":None,"aFile":None,"vFile":None}
        # files_layout.addWidget(QLabel("Noun List"))
        self.nFileBtn = QPushButton("Nouns File")
        self.nFilePath = QLabel(None)

        self.nFileBtn.clicked.connect(self.nFileBtnClicked)

        files_layout.addWidget(self.nFileBtn)
        files_layout.addWidget(self.nFilePath)
        # nFileBox = QFileDialog()
        # files_layout.addWidget(nFileBox)
        # files_layout.addWidget(QLabel("Adjective List"))
        self.aFileBtn = QPushButton("Adjectives File")
        self.aFilePath = QLabel(None)

        self.aFileBtn.clicked.connect(self.aFileBtnClicked)

        files_layout.addWidget(self.aFileBtn)
        files_layout.addWidget(self.aFilePath)
        # files_layout.addWidget(QLabel("Verb List"))
        self.vFileBtn = QPushButton("Verbs File")
        self.vFilePath = QLabel(None)

        self.vFileBtn.clicked.connect(self.vFileBtnClicked)

        files_layout.addWidget(self.vFileBtn)
        files_layout.addWidget(self.vFilePath)
        files_layout.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        # exec_layout
        # exec_layout.addWidget(QLabel("Generate Codeword"))
        # TODO: Add button widget
        self.runBtn = QPushButton("Execute")

        self.runBtn.clicked.connect(self.runBtnClicked)

        exec_layout.addWidget(self.runBtn)
        # TODO: Grey out button until all settings done
        # self.runBtn.setDisabled(True)

        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        exec_layout.addWidget(line)

        # results_layout
        results_layout.addWidget(QLabel("Codewords"))
        self.outBox = QTextBrowser()
        # self.outBox.setHidden(True)
        results_layout.addWidget(self.outBox)

        # nest layouts
        layout.addLayout(interaction_layout)
        layout.addLayout(results_layout)
        interaction_layout.addLayout(settings_layout)
        interaction_layout.addLayout(exec_layout)
        settings_layout.addLayout(style_layout)
        settings_layout.addLayout(customization_layout)
        settings_layout.addLayout(files_layout)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

    def setStyle(self, s):
        print("Style Radio clicked %s" % self.radioGroup.id(s))
        self.cwStyle = self.radioGroup.id(s)

    def setNum(self, s):
        print("Num set to %s" % self.numBox.value())

    def setDel(self, s):
        print("Del set to \'%s\'" % self.delBox.text())

    def nFileBtnClicked(self):
        print("nFileBtn was clicked")
        fname = QFileDialog.getOpenFileName(self, 'Open file', './', "Text files (*.txt)")
        self.nFilePath.setText(fname[0])
        self.files["nFile"] = fname[0]
        print("File selected %s" % fname[0])

    def aFileBtnClicked(self):
        print("aFileBtn was clicked")
        fname = QFileDialog.getOpenFileName(self, 'Open file', './', "Text files (*.txt)")
        self.aFilePath.setText(fname[0])
        self.files["aFile"] = fname[0]
        print("File selected %s" % fname[0])

    def vFileBtnClicked(self):
        print("vFileBtn was clicked")
        fname = QFileDialog.getOpenFileName(self, 'Open file', './', "Text files (*.txt)")
        self.vFilePath.setText(fname[0])
        self.files["vFile"] = fname[0]
        print("File selected %s" % fname[0])

    def runBtnClicked(self):
        print("runBtn was clicked")
        if None in self.files.values():
            print("ERROR NOT ALL FILES SET")
        else:
            print("RUNNING!")
            codes = []
            if self.cwStyle == 1:
                style = 'nn'
            elif self.cwStyle == 2:
                style = 'an'
            elif self.cwStyle == 3:
                style = 'vn'
            for i in range(self.numBox.value()):
                codes.append(codewordgenerator.gen_code(self.files["nFile"], self.files["aFile"], self.files["vFile"], self.delBox.text(), style))
            self.outBox.setText('\n'.join(codes))
            print(codes)
            print("DONE")


app = QApplication([])
window = MainWindow()
window.show()

app.exec()

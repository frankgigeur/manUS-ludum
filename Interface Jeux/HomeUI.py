from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import qtawesome as qta
import utils

class HomeUI(QWidget):
    nextBtnPressed = pyqtSignal(int)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__policy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        self.__initLayout()
        self.__initWidgets()
        self.__addWidgetsToLayouts()
        self.__layoutsNesting()

        # Init widgets in HomeUI

    def __initWidgets(self):
        # Label participant ID
        self.lbCode = QLabel("Participant ID ")
        self.lbCode.setSizePolicy(self.__policy)

        # Information icon
        self.info_button = QPushButton()
        info_icon = qta.icon('fa.info-circle')
        self.info_button.setIcon(info_icon)
        self.info_button.setFlat(True)

        self.completer = QCompleter(utils.completeIdIter())
        self.completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)

        # Line edit participant and verified if it's accurate 
        self.textCode = QLineEdit()
        self.textCode.setSizePolicy(self.__policy)
        self.textCode.setMinimumWidth(200)
        self.textCode.setPlaceholderText("E.g. H123/D123/P123")
        expr = QRegExp("^(?:[d,h,p,D,H,P][0-9][0-9][0-9])$")
        v = QRegExpValidator(expr)
        self.textCode.setValidator(v)
        self.textCode.setCompleter(self.completer)

        # Label comments
        self.lbComment = QLabel("Comments")
        self.lbComment.setSizePolicy(self.__policy)

        # Text area for comments
        self.textComment = QTextEdit()
        utils.setScrollArea(self.textComment)

        # Label List of tasks
        self.lbTask = QLabel("List of tasks")

        # Tasks list
        self.scrollTaskList = QListWidget()
        self.scrollTaskList.setSelectionMode(QListWidget.SelectionMode.MultiSelection)
        utils.setScrollArea(self.scrollTaskList)

        self.btnNew = QPushButton()
        self.btnNew.setSizePolicy(self.__policy)
        self.btnNew.setIcon(qta.icon('fa5s.file'))
        self.btnNew.setIconSize(QSize(20,20))

        # Buttons at the bottom
        self.btnOpen = QPushButton()
        self.btnOpen.setSizePolicy(self.__policy)
        self.btnOpen.setIcon(qta.icon('fa5s.folder-open'))
        self.btnOpen.setIconSize(QSize(20,20))

        # # Icon button next
        self.btnNext = QPushButton(qta.icon("mdi.arrow-right-bold-box-outline"), "")
        self.btnNext.setFlat(True)
        self.btnNext.setIconSize(QSize(36, 36))
        self.btnNext.setSizePolicy(self.__policy)




    # Init layout in HomeUI
    def __initLayout(self):
        self.__outterLayout = QVBoxLayout(self)
        self.__blockLayout = QHBoxLayout()
        self.__idBlockLayout = QVBoxLayout()
        self.__idLabelAndInfoLayout = QHBoxLayout()
        self.__idLineAndButtonLayout = QHBoxLayout()
        self.__taskBlockLayout = QVBoxLayout()
        self.__taskLabelLayout = QHBoxLayout()
        self.__scrollTaskWidget = QWidget()
        self.scrollTaskLayout = QVBoxLayout()
        self.__scrollTaskWidget.setLayout(self.scrollTaskLayout)
        self.__btnBlockLayout = QHBoxLayout()
        self.__leftBtnLayout = QHBoxLayout()
        self.__rightBtnLayout = QHBoxLayout()

    # Add widgets to layouts
    def __addWidgetsToLayouts(self):
        self.__idBlockLayout.addLayout(self.__idLabelAndInfoLayout)
        self.__idLabelAndInfoLayout.addWidget(self.lbCode)
        self.__idLabelAndInfoLayout.addWidget(self.info_button)
        self.__idLabelAndInfoLayout.addStretch()
        self.__idBlockLayout.addLayout(self.__idLineAndButtonLayout)
        self.__idLineAndButtonLayout.addWidget(self.textCode)
        self.__idLineAndButtonLayout.addWidget(self.btnNew)
        self.__idLineAndButtonLayout.addWidget(self.btnOpen)
        self.__idLineAndButtonLayout.addStretch()
        self.__idBlockLayout.addWidget(self.lbComment)
        self.__idBlockLayout.addWidget(self.textComment)
        self.__taskBlockLayout.addLayout(self.__taskLabelLayout)
        self.__taskLabelLayout.addWidget(self.lbTask)
        self.__taskLabelLayout.addStretch()
        # self.__taskLabelLayout.addWidget(self.btnMinus)
        # self.__taskLabelLayout.addWidget(self.btnPlus)
        self.__taskBlockLayout.addWidget(self.scrollTaskList)
        self.__leftBtnLayout.addStretch()
        # self.__leftBtnLayout.addWidget(self.btnOpen)
        self.__leftBtnLayout.addStretch()
        self.__rightBtnLayout.addWidget(self.btnNext)

    # Create the layout nesting
    def __layoutsNesting(self):
        self.__outterLayout.addLayout(self.__blockLayout)
        self.__blockLayout.addLayout(self.__idBlockLayout)
        self.__blockLayout.addLayout(self.__taskBlockLayout)
        self.__outterLayout.addLayout(self.__btnBlockLayout)
        self.__btnBlockLayout.addLayout(self.__leftBtnLayout)
        self.__btnBlockLayout.addLayout(self.__rightBtnLayout)



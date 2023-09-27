from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import QToolBar


class TopToolbar(QToolBar):
    def __init__(self):
        super(QToolBar, self).__init__()

        self.setIconSize(QSize(16, 16))
        self.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        button_action = QAction(QIcon("data/images/icon.png"), "&Your button", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)

        self.addAction(button_action)
        self.addSeparator()

        button_action2 = QAction(QIcon("data/images/icon.png"), "&Your button", self)
        button_action2.setStatusTip("This is your button")
        button_action2.triggered.connect(self.onMyToolBarButtonClick)
        button_action2.setCheckable(True)

        self.addAction(button_action2)

    def onMyToolBarButtonClick(self, s):
        print("click", s)

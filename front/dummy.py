from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class Widget(QWidget):

    def __init__(self, parent= None):
        super(Widget, self).__init__()

        btn_new = QPushButton("Append new label")
        btn_new.clicked.connect(self.add_new_label)

        #Container Widget       
        self.widget = QWidget()
        #Layout of Container Widget
        layout = QVBoxLayout(self)
        for _ in range(20):
            label = QLabel("test")
            layout.addWidget(label)
        self.widget.setLayout(layout)

        #Scroll Area Properties
        scroll = QScrollArea()
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setWidgetResizable(True)
        scroll.setWidget(self.widget)

        #Scroll Area Layer add
        vLayout = QVBoxLayout(self)
        vLayout.addWidget(btn_new)
        vLayout.addWidget(scroll)
        self.setLayout(vLayout)

    def add_new_label(self):
        label = QLabel("new")
        layout = self.widget.layout()
        layout.insertWidget(layout.count() - 1, label)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    dialog = Widget()
    dialog.show()

    app.exec_()
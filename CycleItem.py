from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QRadioButton, QLineEdit, QSizePolicy

from ListWidget import ListWidget


class CycleItem(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.list_item_layout = QVBoxLayout()

        layout = QHBoxLayout()

        self.delete_button = QPushButton()
        self.edit_button = QPushButton()

        layout.addWidget(QWidget(), stretch=8)
        layout.addWidget(self.edit_button, stretch=1)
        layout.addWidget(self.delete_button, stretch=1)

        self.list_item_layout.addLayout(layout)

        layout = QHBoxLayout()

        self.always_button = QRadioButton()
        self.count_button = QRadioButton()
        self.count_edit = QLineEdit()

        layout.addWidget(self.always_button, stretch=5)
        layout.addWidget(self.count_button, stretch=2)
        layout.addWidget(self.count_edit, stretch=3)

        self.list_item_layout.addLayout(layout)
        self.list_item_layout.addWidget(ListWidget())

        self.setLayout(self.list_item_layout)

        self.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)




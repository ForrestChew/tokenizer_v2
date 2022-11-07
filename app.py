import sys
from PyQt5 import QtWidgets as qtw
from ui import ui_main_components


class Tokenizer(qtw.QWidget, ui_main_components.UiComponents):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        left_gb = self.create_left_window_area()
        right_gb = self.create_right_window_area()
        window_layout = qtw.QHBoxLayout()
        window_layout.addWidget(left_gb, 2)
        window_layout.addWidget(right_gb, 2)
        self.setLayout(window_layout)
        self.setGeometry(10, 10, 1024, 576)
        self.center()
        self.setWindowTitle("Tokenizer")
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = qtw.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    # def closeEvent(self, event):
    #     reply = qtw.QMessageBox.question(
    #         self,
    #         "Message",
    #         "Are you sure you want to quit?",
    #         qtw.QMessageBox.Yes | qtw.QMessageBox.No,
    #     )
    #     if reply == qtw.QMessageBox.Yes:
    #         event.accept()
    #     else:
    #         event.ignore()


def main():
    app = qtw.QApplication(sys.argv)
    app.setStyle("Fusion")
    ex = Tokenizer()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

from PyQt5 import QtWidgets as qtw


def notification_popup(message: str, window_title: str) -> None:
    msg = qtw.QMessageBox()
    msg.setWindowTitle(window_title)
    msg.setText(message)
    msg.setStandardButtons(qtw.QMessageBox.Ok)
    msg.exec()
    if msg == qtw.QMessageBox.Ok:
        msg.close()

from PyQt5.QtWidgets import QApplication, QMessageBox, QPushButton

def on_button_clicked():
    alert = QMessageBox()
    alert.setText('You clicked the button!')
    alert.exec()


app = QApplication([])
app.setStyleSheet("QPushButton { margin: 10ex; }")
button = QPushButton('OK')


button.clicked.connect(on_button_clicked)
button.show()
app.exec_()

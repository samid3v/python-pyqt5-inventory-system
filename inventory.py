from PyQt5 import QtWidgets, uic
import os.path

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('inventory.ui', self) # Load the .ui file



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = Ui()
    window.show()

    sys.exit(app.exec_())

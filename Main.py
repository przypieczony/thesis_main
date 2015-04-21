from GUIv0_8 import *

class Test(Ui_MainWindow):
    def __init__(self):
        Ui_MainWindow.__init__(self)
        self.sourceAddress = Ui_MainWindow.sourceAddressField.text()
        print self.sourceAddress

if __name__ == "__main__":
	Test()
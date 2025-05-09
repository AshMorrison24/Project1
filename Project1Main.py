from Project1GUI import *


def main():
   """This function creates the window."""
   application = QApplication([])
   window = MainWindow()
   window.setGeometry(100,100,300,300)
   window.show()
   application.exec()


if __name__ == '__main__':
   main()

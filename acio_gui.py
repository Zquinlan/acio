## AC.IO GUI

#import dependencies
import sys, os

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMainWindow, QStatusBar, QToolBar, QAction
from PyQt5.QtWidgets import QFileDialog, QLineEdit, QMessageBox, QErrorMessage, QHBoxLayout, QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtCore import pyqtSlot, QDir

class mainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Ac.Io'
        self.left = 10
        self.top = 10
        self.geometry = app.desktop().availableGeometry()
        self.height = self.geometry.height()
        self.width = self.geometry.height()


        if sys.platform == "linux" or sys.platform == "linux2":
            self.key = "Ctrl"
        elif sys.platform == "darwin":
            self.key = "Cmnd"
        elif sys.platform == "win32" or sys.platform == "win64":
            self.key = "Ctrl"

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        #Making the Menu Bar
        mainMenu = self.menuBar()
        mainMenu.setNativeMenuBar(False)

        fileMenu = mainMenu.addMenu('File')
        editMenu = mainMenu.addMenu('Edit')
        viewMenu = mainMenu.addMenu('View')
        helpMenu = mainMenu.addMenu('Help')

        quitButton = QAction('Exit', self)
        quitButton.setShortcut(self.key + '+Q')
        quitButton.setStatusTip('Quit Application')
        quitButton.triggered.connect(self.close)
        fileMenu.addAction(quitButton)

        #Search Directory bar and button
        self.searchDirectory = QLineEdit(self)
        self.searchDirectory.setText("Your Github Repository")
        self.searchDirectory.move(10,40)
        self.searchDirectory.resize(200,20)

        self.findDirectory = QPushButton("Set Directory", self)
        self.findDirectory.move(210, 35)
        self.findDirectory.resize(150, 30)
        self.findDirectory.clicked.connect(self.dirclick)

        # Make Framework button
        self.mkFramework = QPushButton("Acio Website", self)
        self.mkFramework.move(10, 65)
        self.mkFramework.resize(120,30)
        self.mkFramework.clicked.connect(self.makeclick)


    @pyqtSlot()
    def dirclick(self):
        currentDirectory = self.searchDirectory.text()
        fname = QFileDialog.getExistingDirectory(self, 'Select a directory', currentDirectory)

        if fname:
            # Returns pathName with the '/' separators converted to separators that are appropriate for the underlying operating system.
            # On Windows, toNativeSeparators("c:/winnt/system32") returns
            # "c:\winnt\system32".
            fname = QDir.toNativeSeparators(fname)

        if os.path.isdir(fname):
            self.searchDirectory.setText(fname)
    
    def makeclick(self):
        currentDirectory = self.searchDirectory.text()
        if currentDirectory == "Your Github Repository":
            message = QMessageBox.question(self, "Error", "No Directory selected", QMessageBox.Cancel, QMessageBox.Cancel)

        else: 
            for root, dirs, files in os.walk(currentDirectory):
                files = [f for f in files if not f[0] == '.']
                dirs[:] = [d for d in dirs if not d[0] == '.']
                level = root.replace(currentDirectory, '').count(os.sep)
                indent = ' ' * 4 * (level)
                print('{}{}/'.format(indent, os.path.basename(root)) + '\n')
                subindent = ' ' * 4 * (level + 1)
                for f in files:
                    print('{}{}'.format(subindent, f) + '\n')

            message = QMessageBox.question(self, "Success!", "Framework Created!!", QMessageBox.Ok, QMessageBox.Ok)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = mainWindow()
    win.show()
    sys.exit(app.exec_())


# Run this to generate the bundled app: pyinstaller --onefile --windowed myscript.p
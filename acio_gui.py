import sys, os

import qdarkstyle
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtSlot, QDir, Qt, QSize

class themeScroll(QScrollArea):
    def __init__ (self):
        super().__init__()
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setWidgetResizable(True)

        #Defining scroll area
        radioButtonContent = QWidget()
        radioButtonLayout = QGridLayout(radioButtonContent)
        radioButtonLayout.setSpacing(20)
        radioButtonLayout.setContentsMargins(0,0,0,20)

        themes = ["Minimal", "Gridster", "Millennial", "Alembic", "Bulma"]
        col = 0


        for theme in themes:
            self.themeSelect = QRadioButton(theme)
            self.themeSelect.theme = theme
            self.themeSelect.toggled.connect(self.onClicked)

            self.themeImage = QLabel(theme)
            img = QPixmap("./theme_images/%s.png" % theme) # This needs to change so that it will work on mac or windows
            img = img.scaled(200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.themeImage.setPixmap(img)

            radioButtonLayout.addWidget(self.themeImage, 0, col)
            radioButtonLayout.addWidget(self.themeSelect, 1, col)

            col += 1

        self.setWidget(radioButtonContent)
        self.setWidgetResizable(True)

    @pyqtSlot()
    def onClicked(self):
        themeSelected = self.sender()

        if themeSelected.isChecked():
            print("Theme is %s" % (themeSelected.theme)) # This needs to change





class dirSearch(QWidget):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0,0,0,0)
        self.searchDirectory = QLineEdit(self)
        self.searchDirectory.setFixedWidth(300)
        self.searchDirectory.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        self.findButton = QPushButton("Select Directory", self)
        self.findButton.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.findButton.clicked.connect(self.dirClick)

        layout.addWidget(self.searchDirectory, 0)
        layout.addWidget(self.findButton, 2)
        layout.setAlignment(Qt.AlignLeft)

    @pyqtSlot()
    def dirClick(self):
        currentDirectory = self.searchDirectory.text()
        fname = QFileDialog.getExistingDirectory(self, 'Select a Directory', currentDirectory)

        if fname:
            # Returns pathName with the '/' separators converted to separators that are appropriate for the underlying operating system.
            # On Windows, toNativeSeparators("c:/winnt/system32") returns
            # "c:\winnt\system32".
            fname = QDir.toNativeSeparators(fname)

        if os.path.isdir(fname):
            self.searchDirectory.setText(fname)





class fileSearch(QWidget):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0,0,0,0)
        self.searchDirectory = QLineEdit(self)
        self.searchDirectory.setFixedWidth(300)
        self.searchDirectory.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        self.findButton = QPushButton("Select File", self)
        self.findButton.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.findButton.clicked.connect(self.dirClick)

        layout.addWidget(self.searchDirectory, 0)
        layout.addWidget(self.findButton, 2)
        layout.setAlignment(Qt.AlignLeft)

    @pyqtSlot()
    def dirClick(self):
        # currentDirectory = self.searchDirectory.text()
        fname = QFileDialog.getOpenFileName(self, 'Select a File', '','All files (*.*)')[0] # Needs to select a file and not a folder

        if fname:
            # Returns pathName with the '/' separators converted to separators that are appropriate for the underlying operating system.
            # On Windows, toNativeSeparators("c:/winnt/system32") returns
            # "c:\winnt\system32".
            fname = QDir.toNativeSeparators(fname)

        if os.path.isfile(fname):
            self.searchDirectory.setText(fname)




class gPhotosPop(QDialog): # Maybe this should be optional between a file or google photos
    def __init__(self, parent = None): # Need to get current album responses. Import from mainWindow (make parent?)
        super().__init__(parent)

        self.initUI()

    def initUI(self):

        self.layout = QVBoxLayout()
        self.layout.setSpacing(20)

        #All google photos
        #Label for logo link
        self.gLogoLabel = QLabel(self)
        self.gLogoLabel.setText("Logo from Google Photos Sharing link:")
        self.gLogoLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        
        #Logo link line edit
        self.gLogoLine = QLineEdit()
        self.gLogoLine.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        
        #Label for google album
        self.gPhotoLabel = QLabel(self)
        self.gPhotoLabel.setText("Google Photos Album Sharing link:")
        self.gPhotoLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        #Album link line edit
        self.gPhotoLine = QLineEdit()
        self.gPhotoLine.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        #All local photos
        #Label for logo
        self.localLogoLabel = QLabel(self)
        self.localLogoLabel.setText("Logo from local file:")
        self.localLogoLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        #Logo link line edit
        self.localLogoLine = fileSearch()
        self.localLogoLine.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        

        #Label for google album
        self.localPhotoLabel = QLabel(self)
        self.localPhotoLabel.setText("Local Photo Album:")
        self.localPhotoLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        #Album link line edit
        self.localPhotoLine = dirSearch()
        self.localPhotoLine.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)


        # Error label
        self.noPhotos = QLabel(self)
        self.noPhotos.setText("Please check an option for photo source")

        # Save Button
        self.save = QPushButton("Save", self)
        self.save.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.save.clicked.connect(self.closeClick)

        # Add Widgets
        self.layout.addWidget(self.localLogoLabel)
        self.layout.addWidget(self.localLogoLine)
        self.layout.addWidget(self.localPhotoLabel)
        self.layout.addWidget(self.localPhotoLine)
        self.layout.addWidget(self.gLogoLabel)
        self.layout.addWidget(self.gLogoLine)
        self.layout.addWidget(self.gPhotoLabel)
        self.layout.addWidget(self.gPhotoLine)
        self.layout.addWidget(self.noPhotos)
        self.layout.addWidget(self.save)

        self.setLayout(self.layout)
        self.setGeometry(0, 0, 500, 400)


    @pyqtSlot()
    def closeClick(self):
        self.close()


class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Ac.Io'
        self.left = 0
        self.top = 0
        self.geometry = app.desktop().availableGeometry()
        self.height = self.geometry.height()
        self.width = self.geometry.height()

        if sys.platform == "linux" or sys.platform == "linux2":
            self.key = "Ctrl"
        elif sys.platform == "darwin":
            self.key = "Cmnd"
        elif sys.platform == "win32" or sys.platform == "win64":
            self.key = "Ctrl"

        self.createMenuBar()
        self.initUI()

    def createMenuBar(self):
        # Making the Menu bar
        mainMenu = self.menuBar()
        mainMenu.setNativeMenuBar(False)

        fileMenu = mainMenu.addMenu('File')
        editMenu = mainMenu.addMenu('Edit')
        viewMenu = mainMenu.addMenu('View')
        helpMenu = mainMenu.addMenu('Help')

        # File Actions
        self.closeButton = QAction('&Close Window', self)
        self.quitButton = QAction('&Quit Application', self)
        
        # Edit Actions
        self.copyButton = QAction('&Copy', self)
        self.cutButton = QAction('&Cut', self)
        self.pasteButton = QAction('&Paste', self)

        # Shortcuts and actions
        self.closeButton.setShortcut(self.key + '+W')
        # self.closeButton.triggered.connect(self.close)

        self.quitButton.setShortcut(self.key + '+Q')
        self.quitButton.triggered.connect(self.quit)

        self.copyButton.setShortcut(self.key + '+C')
        # self.copyButton.triggered.connect(self.copy)

        self.cutButton.setShortcut(self.key + '+X')
        # self.cutButton.triggered.connect(self.cut)

        self.pasteButton.setShortcut(self.key + '+V')
        # self.pasteButton.triggered.connect(self.paste)


        # Add actions to menuBar
        fileMenu.addAction(self.closeButton)
        fileMenu.addAction(self.quitButton)

        editMenu.addAction(self.copyButton)
        editMenu.addAction(self.cutButton)
        editMenu.addAction(self.pasteButton)


    def initUI(self):
        # Setting Window Geometry
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        #Defining scroll area
        scroll = QScrollArea()
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setAlignment(Qt.AlignTop)

        # Adding Widgets
        # Directory Selection
        self.dir = dirSearch()
        self.dir.searchDirectory.setText("Your Github Repository")
        layout.addWidget(self.dir)

        # Theme selection
        self.themeSelect = themeScroll()
        self.themeSelect.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        layout.addWidget(self.themeSelect)

        # Add README button
        self.readMe = QCheckBox(self)
        self.readMe.setText("Use README as main page?")
        layout.addWidget(self.readMe)

        #Photos layout
        self.photos = QWidget()
        photosLayout = QHBoxLayout(self.photos)
        photosLayout.setContentsMargins(0,0,0,0)

        #Photo Radio Buttons
        self.localPhotos = QCheckBox(self)
        self.localPhotos.setText("Upload photos")
        photosLayout.addWidget(self.localPhotos)

        self.googlePhotos = QCheckBox(self)
        self.googlePhotos.setText("Google photos")
        photosLayout.addWidget(self.googlePhotos)

        # Google Photos pop out
        self.gPhotosButton = QPushButton("Google Photos (Optional)", self)
        self.gPhotosButton.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.gPhotosButton.clicked.connect(self.photosClick)

        self.gLogoLink = "Copy + Paste Link Here"
        self.gAlbumLink = "Copy + Paste Link Here"
        self.localLogoLink = 'Find Picture'
        self.localAlbumLink = 'Find Album Folder'

        photosLayout.setAlignment(Qt.AlignLeft)
        photosLayout.addWidget(self.gPhotosButton)

        #Add photos layout to page
        layout.addWidget(self.photos)

        # Make website button
        self.mkFramework = QPushButton("Acio Website", self)
        self.mkFramework.clicked.connect(self.makeClick)
        self.mkFramework.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        layout.addWidget(self.mkFramework)

        #Setting scroll area as central widget
        scroll.setWidget(widget)
        scroll.setWidgetResizable(True)
        self.setCentralWidget(scroll)

    @pyqtSlot()
    def quit(self):
        sys.exit()

    def photosClick(self):
        self.popout = gPhotosPop()

        if self.localPhotos.isChecked() and not self.googlePhotos.isChecked():
            self.popout.localLogoLine.searchDirectory.setText(self.localLogoLink)
            self.popout.localPhotoLine.searchDirectory.setText(self.localAlbumLink)

            self.popout.gLogoLabel.hide()
            self.popout.gLogoLine.hide()
            self.popout.gPhotoLabel.hide()
            self.popout.gPhotoLine.hide()
            self.popout.noPhotos.hide()


        if self.googlePhotos.isChecked() and not self.localPhotos.isChecked():
            self.popout.gLogoLine.setText(self.gLogoLink)
            self.popout.gPhotoLine.setText(self.gAlbumLink)


            self.popout.localLogoLabel.hide()
            self.popout.localLogoLine.hide()
            self.popout.localPhotoLabel.hide()
            self.popout.localPhotoLine.hide()
            self.popout.noPhotos.hide()

        if self.googlePhotos.isChecked() and self.localPhotos.isChecked():
            self.popout.localLogoLine.searchDirectory.setText(self.localLogoLink)
            self.popout.localPhotoLine.searchDirectory.setText(self.localAlbumLink)
            self.popout.gLogoLine.setText(self.gLogoLink)
            self.popout.gPhotoLine.setText(self.gAlbumLink)

            self.popout.noPhotos.hide()

        if not self.localPhotos.isChecked() and not self.googlePhotos.isChecked():
            self.popout.gLogoLabel.hide()
            self.popout.gLogoLine.hide()
            self.popout.gPhotoLabel.hide()
            self.popout.gPhotoLine.hide()
            self.popout.localLogoLabel.hide()
            self.popout.localLogoLine.hide()
            self.popout.localPhotoLabel.hide()
            self.popout.localPhotoLine.hide()


        # Retrieve line text when closed
        self.popout.exec_()
        self.gLogoLink = self.popout.gLogoLine.text()
        self.gAlbumLink = self.popout.gPhotoLine.text()
        self.localLogoLink = self.popout.localLogoLine.searchDirectory.text()
        self.localAlbumLink = self.popout.localPhotoLine.searchDirectory.text()

    def makeClick(self):
        currentDirectory = self.dir.searchDirectory.text()

        #Errors out if not directory is selected
        if currentDirectory == 'Your Github Repository': #change this to ask is it a dir
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
    app.setStyleSheet(qdarkstyle.load_stylesheet())
    win = mainWindow()
    win.show()
    sys.exit(app.exec_())

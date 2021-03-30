import sys, os
import qdarkstyle
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from edit_minimal_mistakes import*
from create_jekyll import editTheme
from create_md import editContents

#Things to add:
#   Minimal theme optional colors
#   Github sign in authentication?
#   Bio photo

#   Probably have to make photos either local or google for now radio buttons
    # Best way will code radio buttons to change a variable (photoChoice = ) gphoto or localphoto
    # Then an if statement in the slot for mkframework checking photoChoice and setting photoAlbum


class themeScroll(QWidget):
    def __init__ (self):
        super().__init__()
        total_layout = QVBoxLayout(self)
        self.setLayout(total_layout)

        scroll = QScrollArea(self)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setWidgetResizable(True)
        scroll.themeSelected = ''

        #Defining scroll area
        radioButtonContent = QWidget()
        radioButtonLayout = QGridLayout(radioButtonContent)
        radioButtonLayout.setSpacing(20)
        radioButtonLayout.setContentsMargins(0,0,0,20)

        themes = ["Minimal", "Alembic", "Bulma"] #Minimal dark contrast and mint themes?
        col = 0


        for theme in themes:
            self.themeSelect = QRadioButton(theme)
            self.themeSelect.theme = theme
            # if self.themeSelect.theme == 'Minimal':
            #     self.themeSelect.setChecked(True)

            self.themeSelect.toggled.connect(self.onClicked)

            self.themeImage = QLabel(theme)
            img = QPixmap("./theme_images/%s.png" % theme) # This needs to change so that it will work on mac or windows
            img = img.scaled(200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.themeImage.setPixmap(img)

            radioButtonLayout.addWidget(self.themeImage, 0, col)
            radioButtonLayout.addWidget(self.themeSelect, 1, col)

            col += 1

        self.skinDropdown = QComboBox(self)
        self.skinDropdown.setFixedWidth(100)
        self.skinDropdown.setView(QListView())


        scroll.setWidget(radioButtonContent)
        scroll.setWidgetResizable(True)
        total_layout.addWidget(scroll)
        total_layout.addWidget(self.skinDropdown)

    def __style__(self):
        self.skinDropdown.setStyleSheet("QListView::item {height:10px;}")



    @pyqtSlot()
    def onClicked(self):
        selected = self.sender()
        self.themeSelected = selected.text()

        minimalSkins = ["default", "air", "mint", "dark"]
        defaultSkin = ["default"]


        self.skinDropdown.clear()

        if self.themeSelected == 'Minimal':
            self.skinDropdown.addItems(minimalSkins)

        if self.themeSelected != 'Minimal':
            self.skinDropdown.addItem("default")

        self.skinDropdown.adjustSize()





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



class socialPop(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.layout = QVBoxLayout()
        self.layout.setSpacing(20)

        #Twitter label and link
        self.twitterLabel = QLabel(self)
        self.twitterLabel.setText("Twitter handle")
        self.twitterLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)


        self.twitterLink = QLineEdit(self)

        twitterExp = QRegExp("\w*")
        input_validator = QRegExpValidator(twitterExp, self.twitterLink)
        self.twitterLink.setValidator(input_validator)
        self.twitterLink.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        #Github
        self.githubLabel = QLabel(self)
        self.githubLabel.setText("Github handle")
        self.githubLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.githubLink = QLineEdit(self)
        self.githubLink.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        #Research Gate
        self.researchgateLabel = QLabel(self)
        self.researchgateLabel.setText("ResearchGate profile")
        self.researchgateLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.researchgateLink = QLineEdit(self)
        self.researchgateLink.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        # ORC ID
        self.orcidLabel = QLabel(self)
        self.orcidLabel.setText('OrcID Number')
        self.orcidLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.orcidLink = QLineEdit(self)
        self.orcidLink.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        # Personal Wesbite
        self.personalLabel = QLabel(self)
        self.personalLabel.setText('Personal Website Address')
        self.personalLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.personalLink = QLineEdit(self)
        self.personalLink.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        # Email
        self.emailLable = QLabel(self)
        self.emailLable.setText('Email Address')
        self.emailLable.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.emailLink = QLineEdit(self)
        self.emailLink.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        #set placeholder text
        self.twitterLink.setPlaceholderText('E.G. Zquinlan')
        self.githubLink.setPlaceholderText('E.G. Zquinlan')
        self.researchgateLink.setPlaceholderText('E.G. Zachary-Quinlan')
        self.orcidLink.setPlaceholderText('E.G. 0000-0002-0351-8927')
        self.personalLink.setPlaceholderText('E.G. www.zquinlan.com')
        self.emailLink.setPlaceholderText('E.G. Zquinlan@Gmail.com')

        # Save Button
        self.save = QPushButton("Save", self)
        self.save.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.save.clicked.connect(self.closeClick)


        #Add all widgets to layout
        self.layout.addWidget(self.twitterLabel)
        self.layout.addWidget(self.twitterLink)
        self.layout.addWidget(self.githubLabel)
        self.layout.addWidget(self.githubLink)
        self.layout.addWidget(self.researchgateLabel)
        self.layout.addWidget(self.researchgateLink)
        self.layout.addWidget(self.orcidLabel)
        self.layout.addWidget(self.orcidLink)
        self.layout.addWidget(self.personalLabel)
        self.layout.addWidget(self.personalLink)
        self.layout.addWidget(self.emailLable)
        self.layout.addWidget(self.emailLink)
        self.layout.addWidget(self.save)

        self.setLayout(self.layout)
        self.setGeometry(0, 0, 500, 450)

    @pyqtSlot()
    def closeClick(self):
        self.close()




class gPhotosPop(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.layout = QVBoxLayout()
        self.layout.setSpacing(20)

        #All local photos
        #Label for logo
        self.localLogoLabel = QLabel(self)
        self.localLogoLabel.setText("Logo from local file:")
        self.localLogoLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        #Logo link line edit
        self.localLogoLine = fileSearch()
        self.localLogoLine.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        
        #Label for album
        self.localPhotoLabel = QLabel(self)
        self.localPhotoLabel.setText("Local Photo Album:")
        self.localPhotoLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        #Album link line edit
        self.localPhotoLine = dirSearch()
        self.localPhotoLine.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        #Label for avatar picture
        self.localAvatarLabel = QLabel(self)
        self.localAvatarLabel.setText("Photo of author from local file:")
        self.localAvatarLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        #Avatar link line edit
        self.localAvatarLine = fileSearch()
        self.localAvatarLine.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        #Splash link label
        self.localSplashLabel = QLabel(self)
        self.localSplashLabel.setText("Website splash image from local file:")
        self.localSplashLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        #Splash link line edit
        self.localSplashLine = fileSearch()
        self.localSplashLine.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)


        #Set placeholder text
        self.localLogoLine.searchDirectory.setPlaceholderText('Find Picture')
        self.localPhotoLine.searchDirectory.setPlaceholderText('Find Album Folder')
        self.localAvatarLine.searchDirectory.setPlaceholderText('Find Picture')
        self.localSplashLine.searchDirectory.setPlaceholderText('Find Picture')


        # Save Button
        self.save = QPushButton("Save", self)
        self.save.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.save.clicked.connect(self.closeClick)

        # Add Widgets
        self.layout.addWidget(self.localLogoLabel)
        self.layout.addWidget(self.localLogoLine)
        self.layout.addWidget(self.localAvatarLabel)
        self.layout.addWidget(self.localAvatarLine)
        self.layout.addWidget(self.localSplashLabel)
        self.layout.addWidget(self.localSplashLine)
        self.layout.addWidget(self.localPhotoLabel)
        self.layout.addWidget(self.localPhotoLine)

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
        helpMenu = mainMenu.addMenu('Help')

        # File Actions
        closeButton = QAction('Close Window', self)
        quitButton = QAction('Quit Application', self)
        
        # Edit Actions
        copyButton = QAction('Copy', self)
        cutButton = QAction('Cut', self)
        pasteButton = QAction('Paste', self)

        # Shortcuts and actions
        closeButton.setShortcut(self.key + '+W')
        # self.closeButton.triggered.connect(self.close)

        quitButton.setShortcut(self.key + '+Q')
        quitButton.triggered.connect(self.quit)

        copyButton.setShortcut(self.key + '+C')
        # self.copyButton.triggered.connect(self.copy)

        cutButton.setShortcut(self.key + '+X')
        # self.cutButton.triggered.connect(self.cut)

        pasteButton.setShortcut(self.key + '+V')
        # self.pasteButton.triggered.connect(self.paste)


        # Add actions to menuBar
        fileMenu.addAction(closeButton)
        fileMenu.addAction(quitButton)

        editMenu.addAction(copyButton)
        editMenu.addAction(cutButton)
        editMenu.addAction(pasteButton)


    def initUI(self):
        # Setting Window Geometry
        self.setWindowTitle(self.title)
        self.setGeometry(0, 0, 700, 600)
        self.statusBar().showMessage('Ready')

        #Defining scroll area
        scroll = QScrollArea()
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setAlignment(Qt.AlignTop)

        # Adding Widgets
        # Website Title:
        self.titleLine = QLineEdit(self)
        self.titleLine.setPlaceholderText("Enter Your Websites Title")
        self.titleLine.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        layout.addWidget(self.titleLine)

        #Author name:
        self.authorLine = QLineEdit(self)
        self.authorLine.setPlaceholderText("Your Name")
        self.authorLine.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        layout.addWidget(self.authorLine)

        # Directory Selection
        self.dir = dirSearch()
        self.dir.searchDirectory.setPlaceholderText("Your Github Repository")
        layout.addWidget(self.dir)

        # Theme selection
        self.themeSelect = themeScroll()
        self.themeSelect.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        layout.addWidget(self.themeSelect)



        # DOI addition widget
        self.doi = QWidget()
        doiLayout = QHBoxLayout(self.doi)
        doiLayout.setContentsMargins(0,0,0,0)

        self.doiLabel = QLabel(self)
        self.doiLabel.setText("DOI Number:")
        self.doiLabel.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        self.doiLink = QLineEdit(self)
        self.doiLink.setFixedWidth(250)
        self.doiLink.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.doiLink.setPlaceholderText("E.G. 10.3389/fmicb.2019.02397")

        doiLayout.setAlignment(Qt.AlignLeft)
        doiLayout.addWidget(self.doiLabel)
        doiLayout.addWidget(self.doiLink)
        
        layout.addWidget(self.doi)

        # Add README button
        self.readMe = QCheckBox(self)
        self.readMe.setText("Use README as main page?")
        self.readMe.setChecked(True)
        layout.addWidget(self.readMe)

        #Photos layout
        self.photos = QWidget()
        photosLayout = QHBoxLayout(self.photos)
        photosLayout.setContentsMargins(0,0,0,0)

        # Google Photos pop out
        self.gPhotosButton = QPushButton("Add Photos (Reccomended)", self)
        self.gPhotosButton.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.gPhotosButton.clicked.connect(self.photosClick)

        self.localLogoLink = ''
        self.localAlbumLink = ''
        self.localAvatarLink = ''
        self.localSplashLink = ''

        photosLayout.setAlignment(Qt.AlignLeft)
        photosLayout.addWidget(self.gPhotosButton)

        #Add photos layout to page
        layout.addWidget(self.photos)

        #Adding social media buttons
        self.socialButton = QPushButton("Social Media Handles (Optional)", self)
        self.socialButton.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.socialButton.clicked.connect(self.socialClick)

        self.twitterHandle = ''
        self.githubHandle = ''
        self.researchgateHandle = ''
        self.orcidHandle = ''
        self.personalWeb = ''
        self.emailHandle = ''

        layout.addWidget(self.socialButton)

        # Make website button
        acioIcon = QIcon('Acio_design_v0.01.png')
        self.mkFramework = QPushButton("Acio Website", self)
        self.mkFramework.setIcon(acioIcon)
        self.mkFramework.setIconSize(QSize(30,30))
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

        # Set placeholder text if no user input; Set regular text if user input previously supplied
        if not self.localLogoLink == '':
            self.popout.localLogoLine.searchDirectory.setText(self.localLogoLink)
        if not self.localAlbumLink == '':
            self.popout.localPhotoLine.searchDirectory.setText(self.localAlbumLink)
        if not self.localAvatarLink == '':
            self.popout.localAvatarLine.searchDirectory.setText(self.localAvatarLink)
        if not self.localSplashLink == '':
            self.popout.localSplashLine.searchDirectory.setText(self.localSplashLink)

        # Retrieve line text when closed
        self.popout.exec_()

        # If the QLineEdits have been changed it will redefine the links to user input
        if not self.popout.localLogoLine.searchDirectory.text() == '':
            self.localLogoLink = self.popout.localLogoLine.searchDirectory.text()
        if not self.popout.localPhotoLine.searchDirectory.text() == '':
            self.localAlbumLink = self.popout.localPhotoLine.searchDirectory.text()
        if not self.popout.localAvatarLine.searchDirectory.text() == '':
            self.localAvatarLink = self.popout.localAvatarLine.searchDirectory.text()
        if not self.popout.localSplashLine.searchDirectory.text() == '':
            self.localSplashLink = self.popout.localSplashLine.searchDirectory.text()


    def socialClick(self):
        self.social = socialPop()

        if not self.twitterHandle == '':
             self.social.twitterLink.setText(self.twitterHandle)
        if not self.githubHandle == '':
            self.social.githubLink.setText(self.githubHandle)
        if not self.researchgateHandle == '':
            self.social.researchgateLink.setText(self.researchgateHandle)
        if not self.orcidHandle == '':
            self.social.orcidLink.setText(self.orcidHandle)
        if not self.personalWeb == '':
            self.social.personalLink.setText(self.personalWeb)
        if not self.emailHandle == '':
            self.social.emailLink.setText(self.emailHandle)



        self.social.exec_()
        if not self.social.twitterLink.text() == '':
            self.twitterHandle = self.social.twitterLink.text()
        if not self.social.githubLink.text() == '':
            self.githubHandle = self.social.githubLink.text()
        if not self.social.researchgateLink.text() == '':
            self.researchgateHandle = self.social.researchgateLink.text()
        if not self.social.orcidLink.text() == '':
            self.orcidHandle = self.social.orcidLink.text()
        if not self.social.personalLink.text() == '':
            self.personalWeb = self.social.personalLink.text()
        if not self.social.emailLink.text() == '':
            self.emailHandle = self.social.emailLink.text()


    def makeClick(self):
        currentDirectory = self.dir.searchDirectory.text()
       
        self.absoluteLogoLink = self.localLogoLink
        self.absoluteAvatarLink = self.localAvatarLink
        self.absoluteAlbumLink = self.localAlbumLink

        self.assetsAvatarLink = str('assets/images/' + os.path.basename(self.absoluteAvatarLink))
        self.assetsLogoLink = str('assets/images/' + os.path.basename(self.absoluteLogoLink))
        # self.assetsAlbumLink = str('assets/images/' + os.path.basename(self.absoluteAlbumLink))
        self.assetsAlbumLink = self.localAlbumLink

        self.theme = self.themeSelect.themeSelected
        self.skin = str(self.themeSelect.skinDropdown.currentText())
        self.doiNumber = self.doiLink.text()

        configArgs = {'currentDirectory' : currentDirectory, 'theme' : self.theme, 'skin' : self.skin, 'authorName' : self.authorLine.text(), 'title' : self.titleLine.text(), 'email' : self.emailHandle, 'repository' : self.dir.searchDirectory.text(), 'assetsLogo' : self.assetsLogoLink,  'assetsAvatar' : self.assetsAvatarLink, 'assetsAlbum': self.assetsAlbumLink, 'absoluteLogo' : self.absoluteLogoLink,  'absoluteAvatar' : self.absoluteAvatarLink, 'absoluteAlbum': self.absoluteAlbumLink, 'personalWeb' : self.personalWeb, 'twitterHandle' : str('https://www.twitter.com/' + self.twitterHandle.strip('@')), 'researchgateHandle' : str('https://www.researchgate.net/profile/' + self.researchgateHandle), 'githubHandle' : str('https://github.com/' + self.githubHandle), 'orcidHandle' : str('https://orcid.org/' + self.orcidHandle), 'doi' : self.doiNumber} 

        # #Errors out if not directory is selected
        if not os.path.isdir(currentDirectory):


            message = QMessageBox.question(self, "Error", "No Directory selected", QMessageBox.Cancel, QMessageBox.Cancel)

        if os.path.isdir(currentDirectory): 

            self.statusBar().clearMessage()
            self.statusBar().showMessage('Investigating repository')
            self.mkcontent = editContents(args = configArgs)

            self.statusBar().clearMessage()
            self.statusBar().showMessage('Creating website theme')
            self.mkClone = editTheme(args = configArgs)
            self.mkConfig = editConfig(args = configArgs)
            self.mkNavigation = editNavigation(args = configArgs)
            self.mkAlbum = editPhotoAlbum(args = configArgs)

            self.statusBar().clearMessage()
            self.statusBar().showMessage('Ready')
            

            message = QMessageBox.question(self, "Success!", "Framework Created!!", QMessageBox.Ok, QMessageBox.Ok)


        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet())
    win = mainWindow()
    win.show()
    sys.exit(app.exec_())

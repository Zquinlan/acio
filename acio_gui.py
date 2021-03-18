import sys, os
import qdarkstyle
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtSlot, QDir, Qt, QSize
from edit_minimal_mistakes import editConfig, editNavigation
from create_jekyll import editTheme

#Things to add:
#   Minimal theme optional colors
#   Github sign in authentication?
#   Bio photo

#   Probably have to make photos either local or google for now radio buttons
    # Best way will code radio buttons to change a variable (photoChoice = ) gphoto or localphoto
    # Then an if statement in the slot for mkframework checking photoChoice and setting photoAlbum


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

        themes = ["Minimal", "Gridster", "Millennial", "Alembic", "Bulma"] #Minimal dark contrast and mint themes?
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



        self.setWidget(radioButtonContent)
        self.setWidgetResizable(True)

    @pyqtSlot()
    def onClicked(self):
        self.themeSelected = self.sender()





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
        self.twitterLink.setPlaceholderText('E.G. @Zquinlan')
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

        #Label for avatar picture
        self.localAvatarLabel = QLabel(self)
        self.localAvatarLabel.setText("Photo of author from local:")
        self.localAvatarLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        #Album link line edit
        self.localAvatarLine = fileSearch()
        self.localAvatarLine.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        #Set placeholder text
        self.localLogoLine.searchDirectory.setPlaceholderText('Find Picture')
        self.localPhotoLine.searchDirectory.setPlaceholderText('Find Album Folder')
        self.localAvatarLine.searchDirectory.setPlaceholderText('Find Picture')
        self.gLogoLine.setPlaceholderText('Copy + Paste Link Here')
        self.gPhotoLine.setPlaceholderText('Copy + Paste Link Here')

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
        self.layout.addWidget(self.localAvatarLabel)
        self.layout.addWidget(self.localAvatarLine)
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
        self.setGeometry(0, 0, 700, 700)

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

        #Photo Radio Buttons
        self.localPhotos = QCheckBox(self)
        self.localPhotos.setText("Upload photos")
        photosLayout.addWidget(self.localPhotos)

        self.googlePhotos = QCheckBox(self)
        self.googlePhotos.setText("Google photos")
        photosLayout.addWidget(self.googlePhotos)

        # Google Photos pop out
        self.gPhotosButton = QPushButton("Add Photos (Optional)", self)
        self.gPhotosButton.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.gPhotosButton.clicked.connect(self.photosClick)

        self.gLogoLink = ''
        self.gAlbumLink = ''
        self.localLogoLink = ''
        self.localAlbumLink = ''
        self.localAvatarLink = ''

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

        if self.localPhotos.isChecked() and not self.googlePhotos.isChecked():
            # Set placeholder text if no user input; Set regular text if user input previously supplied
            if not self.localLogoLink == '':
                self.popout.localLogoLine.searchDirectory.setText(self.localLogoLink)
            if not self.localAlbumLink == '':
                self.popout.localPhotoLine.searchDirectory.setText(self.localAlbumLink)
            if not self.localAvatarLink == '':
                self.popout.localAvatarLine.searchDirectory.setText(self.localAvatarLink)

            self.popout.gLogoLabel.hide()
            self.popout.gLogoLine.hide()
            self.popout.gPhotoLabel.hide()
            self.popout.gPhotoLine.hide()
            self.popout.noPhotos.hide()


        if self.googlePhotos.isChecked() and not self.localPhotos.isChecked():
            # Set placeholder text if no user input; Set regular text if user input previously supplied
            if not self.gLogoLink == '':
                self.popout.gLogoLine.setText(self.gLogoLink)
            if not self.gAlbumLink == '':
                self.popout.gPhotoLine.setText(self.gAlbumLink)

            self.popout.localLogoLabel.hide()
            self.popout.localLogoLine.hide()
            self.popout.localPhotoLabel.hide()
            self.popout.localPhotoLine.hide()
            self.popout.noPhotos.hide()

        if self.googlePhotos.isChecked() and self.localPhotos.isChecked():
            # Set placeholder text if no user input; Set regular text if user input previously supplied
            if not self.localLogoLink == '':
                self.popout.localLogoLine.searchDirectory.setText(self.localLogoLink)
            if not self.localAlbumLink == '':
                self.popout.localPhotoLine.searchDirectory.setText(self.localAlbumLink)
            if not self.gLogoLink == '':
                self.popout.gLogoLine.setText(self.gLogoLink)
            if not self.gAlbumLink == '':
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

        # If the QLineEdits have been changed it will redefine the links to user input
        if not self.popout.localLogoLine.searchDirectory.text() == '':
            self.localLogoLink = self.popout.localLogoLine.searchDirectory.text()
        if not self.popout.localPhotoLine.searchDirectory.text() == '':
            self.localAlbumLink = self.popout.localPhotoLine.searchDirectory.text()
        if not self.popout.localAvatarLine.searchDirectory.text() == '':
            self.localAvatarLink = self.popout.localAvatarLine.searchDirectory.text()

        if not self.popout.gLogoLine.text() == '':
            self.gLogoLink = self.popout.gLogoLine.text()
        if not self.popout.gPhotoLine.text() == '':
            self.gAlbumLink = self.popout.gPhotoLine.text()


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
        

        # if self.photoSource == 'local': # This needs to strip the logolink to just the end/
        self.absoluteLogoLink = self.localLogoLink
        self.absoluteAvatarLink = self.localAvatarLink
        self.absoluteAlbumLink = self.localAlbumLink

        self.assetsAvatarLink = str('assets/images/' + self.absoluteAvatarLink.strip('/')[-1])
        self.assetsLogoLink = str('assets/images/' + self.absoluteLogoLink.strip('/')[-1])
        # self.assetsAlbumLink = str('assets/images/' + self.absoluteAlbumLink.strip('/')[-1])
        self.assetsAlbumLink = self.localAlbumLink

        # if self.photoSource == 'google':
            # self.absoluteLogoLink = self.gLogoLink
            # self.absoluteAlbumLink = self.gAlbumLink

        #Need an if statement for creating name of theme

        configArgs = {'currentDirectory' : currentDirectory,'authorName' : self.authorLine.text(), 'title' : self.titleLine.text(), 'email' : self.emailHandle, 'repository' : self.dir.searchDirectory.text(), 'logo' : self.assetsLogoLink,  'avatar' : self.assetsAvatarLink, 'personalWeb' : self.personalWeb, 'twitterHandle' : str('https://www.twitter.com/' + self.twitterHandle.strip('@')), 'researchgateHandle' : str('https://www.researchgate.net/profile/' + self.researchgateHandle), 'githubHandle' : str('https://github.com/' + self.githubHandle), 'orcidHandle' : str('https://orcid.org/' + self.orcidHandle), 'skin' : 'mint'} 
        navArgs = {'currentDirectory' : currentDirectory, 'doi' : self.doiLink.text(), 'photoAlbum' : self.assetsAlbumLink}
        createArgs = {'currentDirectory' : currentDirectory, 'theme' : 'Minimal', 'logo' : self.absoluteLogoLink, 'album' : self.absoluteAlbumLink, 'avatar' : self.absoluteAlbumLink} 

        # For testing purposes use the args lines below
        # configArgs = {'currentDirectory' : '/Users/zacharyquinlan/Documents/temp.nosync', 'authorName' : 'Zach Quinlan', 'title' : 'AcIO test', 'email' : 'zquinlan@gmail.com', 'repository' : '/Users/zacharyquinlan/Documents/temp.nosync', 'logo' : '/assets/images/Coral_blue_tiny_fish_1.jpg',  'avatar' : '/assets/images/zaq2020.jpg', 'personalWeb' : '', 'twitterHandle' : 'https://www.twitter.com/zquinlan', 'researchgateHandle' : 'https://www.researchgate.net/profile/zachary-quinlan', 'githubHandle' : 'https://github.com/zquinlan', 'orcidHandle' : 'https://orcid.org/' , 'skin' : 'mint'} 
        # navArgs = {'currentDirectory' : '/Users/zacharyquinlan/Documents/temp.nosync', 'doi' : '10.3389/fmicb.2019.02397', 'photoAlbum' : ''}
        # createArgs = {'currentDirectory' : '/Users/zacharyquinlan/Documents/temp.nosync', 'theme' : 'Minimal', 'logo' : '/Users/zacharyquinlan/Documents/Github/jekyll_themes/minimal-mistakes/assets/images/Coral_blue_tiny_fish_1.jpg', 'album' : '', 'avatar' : '/Users/zacharyquinlan/Documents/Github/jekyll_themes/minimal-mistakes//assets/images/zaq2020.jpg'} 

        # Need some way to pick between google photos and local
        # This needs to change and avatar option needs to be added 
        # When themes have been fixed skin = self.themeSelect.theme

        # #Errors out if not directory is selected
        if not os.path.isdir(currentDirectory):

            self.mkClone = editTheme(args = createArgs)
            self.mkConfig = editConfig(args = configArgs)
            self.mkNavigation = editNavigation(args = navArgs)


            message = QMessageBox.question(self, "Error", "No Directory selected", QMessageBox.Cancel, QMessageBox.Cancel)

        if os.path.isdir(currentDirectory): 
            for root, dirs, files in os.walk(currentDirectory):
                files = [f for f in files if not f[0] == '.']
                dirs[:] = [d for d in dirs if not d[0] == '.']
                level = root.replace(currentDirectory, '').count(os.sep)
                indent = ' ' * 4 * (level)
                print('{}{}/'.format(indent, os.path.basename(root)) + '\n')
                subindent = ' ' * 4 * (level + 1)
                for f in files:
                    print('{}{}'.format(subindent, f) + '\n')

            self.mkClone = editTheme(args = createArgs)
            self.mkConfig = editConfig(args = configArgs)
            self.mkNavigation = editNavigation(args = navArgs)

            message = QMessageBox.question(self, "Success!", "Framework Created!!", QMessageBox.Ok, QMessageBox.Ok)


        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet())
    win = mainWindow()
    win.show()
    sys.exit(app.exec_())

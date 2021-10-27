import subprocess, os
from dulwich import porcelain


class editThemeWin():
    def __init__(self, args):
        super().__init__()

        self.currentDirectory = args['currentDirectory']
        self.logo = args['absoluteLogo']
        self.album = args['absoluteAlbum']
        self.avatar = args['absoluteAvatar']
        self.splash = args['absoluteSplash']

        if args['theme'] == 'Minimal':
            self.themeAddress = 'https://github.com/mmistakes/minimal-mistakes'
            self.themeClone = 'minimal-mistakes'
            self.themeDirs = 'minimalMistakes'
        # if args['theme'] == 'Gridster':
        #     self.themeAddress = 'https://github.com/DigitalMindCH/gridster-jekyll-theme'
        #     self.themeClone = 'gridster-jekyll-theme'

        # if win32 check git downloaded
        #git status
        # if git status is not then git init
        # git checkout -B gh-pages
        self.themeContents = str('(' + self.currentDirectory + '\\src\\' + self.themeClone + '\\*)')
        self.albumPath = str(self.currentDirectory + '\\assets\\images\\album\\')
        self.albumContents = str(self.currentDirectory + '\\assets\\images\\album\\' + os.path.basename(self.album))
        self.pathToApp = self.currentDirectory # change to some working version of this when bundling os.path.dirname(__path__)

        os.chdir(self.currentDirectory)
        
        self.moveThemeContents = str('for /d %d in ' + self.themeContents +' do move /Y %d ' + self.currentDirectory)
        self.moveThemeFiles = str('for %F in ' + self.themeContents +' do move /Y %F ' + self.currentDirectory)
        self.moveAlbum = str('for /d %d in ' + self.albumPath + ' do move /Y %d ' + self.albumContents)
        #removing files not used

        subprocess.run('del /f minimal-mistakes\\README.md', shell = True) #This has to change so that it works with other themes
        subprocess.run(self.moveThemeContents, shell = True)
        subprocess.run(self.moveThemeFiles, shell = True)
        subprocess.run('del /f index.html, package-lock.json, package.json, Rakefile, CHANGELOG.md, screenshot-layouts.png, screenshot.png, staticman.yml, banner.js, _includes\\author-profile.html, _includes\\footer.html, _layouts\\home.html', shell = True)
        subprocess.run('rd /s /q docs', shell = True)
        subprocess.run('if exist docs rd /s /q docs', shell = True)
        subprocess.run('rd /s /q test', shell = True)
        subprocess.run('if exist test rd /s /q test', shell = True)

        self.removeThemeDir = str('rd /s /q ' + self.themeClone)
        self.removeThemeDirIf = str('if exist ' + self.themeClone + 'rd /s /q ' + self.themeClone)
        subprocess.run(self.removeThemeDir, shell = True)
        subprocess.run(self.removeThemeDirIf, shell = True)

        subprocess.run('mkdir assets\\images', shell = True)
        subprocess.run('mkdir assets\\images\\album', shell = True)

        photoList = [self.logo, self.avatar, self.splash]
        for pic in photoList:
            photoCopy = str('xcopy ' + pic + ' assets\\images\\ /Y')
            subprocess.run(photoCopy, shell = True)
        
        self.copyAlbumContents = str('xcopy ' + self.album + ' assets\\images\\album\\ /E /C /R /Y')
        subprocess.run(self.copyAlbumContents, shell = True)
        subprocess.run(self.moveAlbum, shell = True)
        self.removeEmptyAlbum = str('rmdir ' + self.albumContents)
        subprocess.run(self.removeEmptyAlbum, shell = True)

        subprocess.run('rename _config.yml _config_template.yml', shell = True)
        subprocess.run('rename _data\\navigation.yml navigation_template.yml', shell = True)
        subprocess.run('rename LICENSE theme_LICENSE', shell = True)      

        #Need to be able to add these files. Maybe git clone from the acio GH?
        #Copy in pages and images for acio
        #Index file for mainpage of website

        self.appPages = str(self.pathToApp + '\\' + self.themeDirs + '\\pages\\')
        self.appImages = str(self.pathToApp + '\\' + self.themeDirs + '\\images\\')
        self.appIndex = str('xcopy ' + self.appPages + 'indexBase.md ' + self.currentDirectory + ' /Y')
        
        subprocess.run(self.appIndex, shell = True) 

        readin = open('README.md', 'r')
        indexin = open('indexBase.md', 'r')
        overlay = str('overlay_image')



        with open('index.md', 'w') as fin:
            fin.write('---\nlayout: home\n\nheader:\n  overlay_color: "#5e616c"\n  overlay_image:')
            fin.write(str(' assets/images/' + os.path.basename(self.splash) + '\n'))
            fin.write('excerpt: >\n  <br /><br /><br />')

            fin.write(indexin.read()) # adding rest of index base to index.md
            fin.write(readin.read())  # Adding the readme to the end of the index
        
        readin.close()
        readin.close()
        subprocess.run('del /f indexBase.md', shell = True)

        self.appHome = str('xcopy ' + self.appPages + 'home.html _layouts\\ /Y')
        self.appContents = str('xcopy ' + self.appImages + 'repoContents.png assets\\images\\ /Y')
        self.appPaper = str('xcopy ' + self.appImages + 'paper.jpg assets\\images\\ /Y')
        self.appPhotos = str('xcopy ' + self.appImages + 'photos.jpg assets\\images\\ /Y')
        self.appProfile = str('xcopy ' + self.appPages + 'author-profile.html _includes\\ /Y')
        self.appFooter = str('xcopy ' + self.appPages + 'footer.html _includes\\ /Y')

        subprocess.run(self.appHome, shell = True)
        subprocess.run(self.appContents, shell = True)
        subprocess.run(self.appPaper, shell = True)
        subprocess.run(self.appPhotos, shell = True)
        subprocess.run(self.appProfile, shell = True)
        subprocess.run(self.appFooter, shell = True)


#For testing purposes

# if __name__ == '__main__':
#     createArgs = {'currentDirectory' : 'C:\\Users\\zquinlan\\Documents\\test', 'absoluteLogo' : 'C:\\Users\\zquinlan\\Documents\\test\\Acio_design_v0.01.png', 'absoluteAlbum' : 'C:\\Users\\zquinlan\\Documents\\temp', 'absoluteAvatar' : 'C:\\Users\\zquinlan\\Documents\\test\\Acio_design_v0.01.png', 'absoluteSplash' : 'C:\\Users\\zquinlan\\Documents\\test\\Acio_design_v0.01.png', 'theme' : 'Minimal'}
#     editTheme(args = createArgs)
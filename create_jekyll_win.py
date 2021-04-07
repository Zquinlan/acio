import subprocess, os, git

class editTheme():
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
        # if args['theme'] == 'Gridster':
        #     self.themeAddress = 'https://github.com/DigitalMindCH/gridster-jekyll-theme'
        #     self.themeClone = 'gridster-jekyll-theme'

        # if win32 check git downloaded
        #git status
        # if git status is not then git init
        # git checkout -B gh-pages
        self.themeContents = str(self.currentDirectory + '\\' + self.themeClone + '\\*.*')
        self.albumPath = str(self.currentDirectory + '\\assets\\images\\album\\')
        self.albumContents = str(self.currentDirectory + '\\assets\\images\\album\\' + os.path.basename(self.album))
        self.pathToApp = os.path.dirname(__path__)


        os.chdir(self.currentDirectory)
        git.Repo.clone_from(self.themeAddress, self.themeClone)
        
        #removing files not used
        

        subprocess.run('for', '\%%F', 'in', self.themeContents, 'do', 'move', '/Y', '\%%F', self.currentDirectory)
        subprocess.run(['del', '/f', 'index.html,', 'README.md,', 'package-lock.json,', 'package.json,', 'Rakefile,', 'CHANGELOG.md,', 'screenshot-layouts.png,', 'screenshot.png,', 'staticman.yml,', 'test/,', 'banner.js,', '_includes/author-profile.html,', '_includes/footer.html,', 'docs/,', '_layouts/home.html'])
        subprocess.run(['rmdir', self.themeClone])

        subprocess.run(['mkdir', 'assets\\images'])
        subprocess.run(['mkdir', 'assets\\images\\album'])

        subprocess.run(['xcopy', self.logo, 'assets\\images\\'])
        subprocess.run(['xcopy', self.avatar, 'assets\\images\\'])
        subprocess.run(['xcopy', self.splash, 'assets\\images\\'])
        
        subprocess.run(['xcopy', self.album, 'assets\\images\\album\\', '/E', '/C', '/R'])
        subprocess.run('for', '\%%F', 'in', self.albumPath, 'do', 'move', '/Y', '\%%F', self.albumContents)
        subprocess.run(['rmdir', self.albumContents])

        subprocess.run(['rename', '_config.yml', '_config_template.yml'])
        subprocess.run(['rename', '_data/navigation.yml', '_data/navigation_template.yml'])
        subprocess.run(['rename', 'LICENSE', 'theme_LICENSE'])      

        #Need to be able to add these files. Maybe git clone from the acio GH?
        #Copy in pages and images for acio
        #Index file for mainpage of website

        self.appPages = str(self.pathToApp + '\\' + self.themeClone + '\\pages\\')
        self.appIndex = str(self.appPages + 'indexBase.md')
        self.appHome = str(self.appPages + 'home.html')
        self.appContents = str(self.appPages + 'repoContents.png')
        self.appPaper = str(self.appPages + 'paper.jpg')
        self.appPhotos = str(self.appPages + 'photos.jpg')
        self.appProfile = str(self.appPages + 'author-profile.html')
        self.appFooter = str(self.appPages + 'footer.html')


        subprocess.run(['xcopy', self.appIndex, self.currentDirectory]) 

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
        subprocess.run(['del', '/f', 'indexBase.md'])

        subprocess.run(['xcopy', self.appHome, '_layouts\\home.html'])
        subprocess.run(['xcopy', self.appContents, 'assets\\images\\'])
        subprocess.run(['xcopy', self.appPaper, 'assets\\images\\'])
        subprocess.run(['xcopy', self.appPhotos, 'assets\\images\\'])
        subprocess.run(['xcopy', self.appProfile, '_includes\\'])
        subprocess.run(['xcopy', self.appFooter, '_includes\\'])


#For testing purposes

if __name__ == '__main__':
    createArgs = {'currentDirectory' = , 'absoluteLogo' = , 'absoluteAlbum' = , 'absoluteAvatar' = , 'absoluteSplash' = , 'theme' = }
    editContents(args = createArgs)


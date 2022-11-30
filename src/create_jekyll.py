import subprocess, os

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


        os.chdir(self.currentDirectory)
        subprocess.run(['git', 'clone', self.themeAddress]) 
        # porcelain.clone(self.themeAddress, self.themeClone)
        os.chdir(self.themeClone)
        
        #removing files not used
        subprocess.run(['rm', '-rf', 'index.html'])
        subprocess.run(['rm', '-rf', 'README.md'])
        subprocess.run(['rm', '-rf', 'package-lock.json'])
        subprocess.run(['rm', '-rf', 'package.json'])
        subprocess.run(['rm', '-rf', 'Rakefile'])
        subprocess.run(['rm', '-rf', 'CHANGELOG.md'])
        subprocess.run(['rm', '-rf', 'screenshot-layouts.png'])
        subprocess.run(['rm', '-rf', 'screenshot.png'])
        subprocess.run(['rm', '-rf', 'staticman.yml'])
        subprocess.run(['rm', '-rf', 'test/'])
        subprocess.run(['rm', '-rf', 'banner.js'])
        subprocess.run(['rm', '-rf', '_includes/author-profile.html'])
        subprocess.run(['rm', '-rf', '_includes/footer.html'])
        subprocess.run(['rm', '-rf', 'docs/'])
        subprocess.run(['rm', '-rf', '_layouts/home.html'])

        subprocess.run('mv * ..', shell = True)
        os.chdir('..') 
        subprocess.run(['rm', '-rf', self.themeClone])

        subprocess.run(['mkdir', 'assets/images'])
        subprocess.run(['mkdir', 'assets/images/album'])

        if self.logo is not '':
            subprocess.run(['cp', self.logo, 'assets/images/'])
        if self.avatar is not '':
            subprocess.run(['cp', self.avatar, 'assets/images/'])
        if self.splash is not '':
            subprocess.run(['cp', self.splash, 'assets/images/'])
        
        if self.album is not '':
            subprocess.run(['cp', '-R', self.album, 'assets/images/album/'])
            os.chdir(str('assets/images/album/' + os.path.basename(self.album)))
            subprocess.run('mv * ..', shell = True)
            os.chdir('../../../..')
            subprocess.run(['rm', '-rf', str('assets/images/album/' + os.path.basename(self.album))])

        subprocess.run(['mv', '_config.yml', '_config_template.yml'])
        subprocess.run(['mv', '_data/navigation.yml', '_data/navigation_template.yml'])
        subprocess.run(['mv', 'LICENSE', 'theme_LICENSE'])      

        #Need to be able to add these files. Maybe git clone from the acio GH?
        #Copy in pages and images for acio
        #Index file for mainpage of website
        subprocess.run(['cp', '/Users/zacharyquinlan/Documents/Github/acio/src/minimalMistakes/pages/indexBase.md', '.'])

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
        indexin.close()
        subprocess.run(['rm', '-rf', 'indexBase.md'])

        subprocess.run(['cp', '/Users/zacharyquinlan/Documents/Github/acio/src/minimalMistakes/pages/home.html', '_layouts/home.html'])
        subprocess.run(['cp', '/Users/zacharyquinlan/Documents/Github/acio/src/minimalMistakes/images/repoContents.png', 'assets/images/'])
        subprocess.run(['cp', '/Users/zacharyquinlan/Documents/Github/acio/src/minimalMistakes/images/paper.jpg', 'assets/images/'])
        subprocess.run(['cp', '/Users/zacharyquinlan/Documents/Github/acio/src/minimalMistakes/images/photos.jpg', 'assets/images/'])
        subprocess.run(['cp', '/Users/zacharyquinlan/Documents/Github/acio/src/minimalMistakes/pages/author-profile.html', '_includes/'])
        subprocess.run(['cp', '/Users/zacharyquinlan/Documents/Github/acio/src/minimalMistakes/pages/footer.html', '_includes/'])
        #create docs/ directory

        # with open('Gemfile', 'r+') as fin:
        #     for line in fin:
        #         if line.startswith('source "https://rubygems.org"'):

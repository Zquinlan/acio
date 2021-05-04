import sys, yaml, subprocess, os


# Need to add baseurl  
class editConfigWin():
    def __init__(self, args):
        super().__init__()
        self.currentDirectory = args['currentDirectory']

        # These have to be set outside of the dictionary because they are used to create
        #another dictionary
        self.personalWeb = args['personalWeb']
        self.twitterHandle = args['twitterHandle']
        self.researchgateHandle = args['researchgateHandle']
        self.githubHandle = args['githubHandle']
        self.orcidHandle = args['orcidHandle']

        with open(str(self.currentDirectory + '\\_config.yml'), 'w+') as fout:
            with open(str(self.currentDirectory + '\\_config_template.yml'), 'r+') as fin:
                config = yaml.full_load(fin)

                config['name'] = args['authorName']
                config['title'] = args['title']
                config['repository'] = args['repository']
                config['logo'] = args['assetsLogo']
                config['minimal_mistakes_skin'] = args['skin']
                config['description'] = ''
                config['baseurl'] = '/'

                config['author']['name'] = args['authorName']
                config['author']['bio'] =  ''
                config['author']['location'] = ''
                config['author']['avatar'] = args['assetsAvatar']
                config['author']['email'] = args['email']
                # config['plugins'].append({'jekyll-google-photos'})

                #Indexing into this list is not working
                config['author']['links'] = []
                config['author']['links'].append({'label' : 'Website', 'url' : self.personalWeb, 'icon' : "fas fa-fw fa-link"})
                config['author']['links'].append({'label' : 'Twitter', 'url': self.twitterHandle, 'icon' : "fab fa-fw fa-twitter-square"})
                config['author']['links'].append({'label' : 'ResearchGate', 'url' : self.researchgateHandle, 'icon' : "fab fa-researchgate"})
                config['author']['links'].append({'label' : 'Github', 'url' : self.githubHandle, 'icon' : "fab fa-fw fa-github"})
                config['author']['links'].append({'label' : 'OrcID', 'url' : self.orcidHandle, 'icon' : 'fab fa-orcid'})

                config['footer']['links'] = []
                config['footer']['links'].append({'label' : 'Website', 'icon' : "fas fa-fw fa-link"})
                config['footer']['links'].append({'label' : 'Twitter', 'icon' : "fab fa-fw fa-twitter-square"})
                config['footer']['links'].append({'label' : 'ResearchGate', 'icon' : "fab fa-researchgate"})
                config['footer']['links'].append({'label' : 'Github', 'icon' : "fab fa-fw fa-github"})
                config['footer']['links'].append({'label' : 'OrcID', 'icon' : 'fab fa-orcid'})
                
                
                # config['author'][''] = gPhotosLink

                yaml.dump(config, fout)

            fout.write('collections:\n  pages:\n    output: true\n    permalink: /:path/')

        subprocess.run('del /f _config_template.yml', shell = True)

class editNavigationWin():
    def __init__(self, args):
        super().__init__()

        ##Retrieving arguments from args dictionary
        self.currentDirectory = args['currentDirectory']
        self.photoAlbum = args['assetsAlbum']
        self.doi = str('https://www.doi.org/' + args['doi'])
        
        with open(str(self.currentDirectory + '\\_data\\navigation.yml'), 'w+') as fout:
            with open(str(self.currentDirectory + '\\_data\\navigation_template.yml'), 'r+') as fin:
            

                nav = yaml.full_load(fin)

               

                nav['main'] = []
                nav['main'].append({'title' : "Repository Contents", 'url' : '_pages/contents/'})#These can be found in the _pages folder
                if not self.photoAlbum == '':
                    nav['main'].append({'title' : "Photos", 'url' : 'assets/images/album'}) # Have to check this with what comes from the gphoto integration
                if not self.doi == '':
                    nav['main'].append({'title' : "Paper", 'url' : self.doi})

                nav['content'] = []
                children = []

                for root, dirs, files in os.walk(self.currentDirectory):
                    files = [f for f in files if not f[0] == '.']
                    dirs[:] = [d for d in dirs if not d[0] == '.']
                    dirs[:] = [d for d in dirs if not d[0] == '_']
                    code = [f for f in files if  f.endswith(('.R','.py', '.m', '.java','.css', 'rb', 'pl', '.bash', '.batchfile'))]

                    for f in files:
                        if f in code:
                            url = str('\\_pages\\contents/' + f + '/')

                            children.append({'title' : f, 'url': url})

                nav['content'].append({'title' : 'Repository Contents', 'children' : children})
                nav['content'].append({'title' : 'Photos', 'url': 'assets/images/album'})
                nav['content'].append({'title' : 'Paper', 'url': self.doi})


                yaml.dump(nav, fout)

        subprocess.run('del /f _data\\navigation_template.yml', shell = True)

class editPhotoAlbumWin():
    def __init__(self, args):
        super().__init__()
        self.currentDirectory = args['currentDirectory']
        self.splash = args['assetsSplash']

        with open(str(self.currentDirectory + '\\assets\\images\\album.md'), 'w+') as fout:
            frontmatter = str('---\nlayout: splash\nheader: \noverlay_color: "#5e616c"\noverlay_image: ' + self.splash + '\nsidebar:\n  nav: "content" \n')
            fout.write(frontmatter)
            
            fout.write('gallery:\n')

            children = []

            for root, dirs, files in os.walk(str(self.currentDirectory + '/assets/images/album/')):
                files = [f for f in files if not f[0] == '.']
                pics = [f for f in files if not f.endswith(('.mov', '.mp4'))]

                for f in pics:
                    url = str('/assets/images/album/' + f + '\n')

                    fout.write(str(' - image_path: ' + url))

            fout.write('\n---\n{% include gallery%}')

#For testing purposes

# if __name__ == '__main__':
#     createArgs = {'currentDirectory' :  '/Users/zacharyquinlan/Documents/Github/lastTest', 'logo': '', 'photoAlbum' : '/Users/zacharyquinlan/Documents/temp.nosync/album', 'doi' : 'test'} 
#     editPhotoAlbum(args = createArgs)

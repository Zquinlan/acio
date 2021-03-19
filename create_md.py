import os, subprocess

class editContents():
    def __init__(self, args):
        super().__init__()

        self.currentDirectory = args['currentDirectory']

        os.chdir(self.currentDirectory)
        subprocess.run(['mkdir', '_pages'])
        subprocess.run(['mkdir', '_pages/contents'])

        for root, dirs, files in os.walk(self.currentDirectory):
            files = [f for f in files if not f[0] == '.']
            dirs[:] = [d for d in dirs if not d[0] == '.']
            dirs[:] = [d for d in dirs if not d[0] == '_']
            code = [f for f in files if  f.endswith(('.R','.py', '.m', '.java','.css', 'rb', 'pl'))]

            for f in code:
                path = os.path.join(root, f)
                pathEdit = open(path, 'r') # This doesn't work because it is just the name of the file not the path
                mdFile = str(self.currentDirectory + '/_pages/contents/' + f + '.md')
                with open(mdFile, 'w+') as fout:
                    fout.write('---\nlayout: posts\nsidebar:\n  nav: "content"\n---\n')
                    fout.write('```\n')
                    fout.write(pathEdit.read())
                    fout.write('```')

                pathEdit.close()



        with open(str(self.currentDirectory + '/_pages/contents.md'), 'w+') as fout:
            fout.write('---\nlayout: archive\n---\n# Contents of Github Repository: ')

            for root, dirs, files in os.walk(self.currentDirectory):
                files = [f for f in files if not f[0] == '.']
                dirs[:] = [d for d in dirs if not d[0] == '.']
                dirs[:] = [d for d in dirs if not d[0] == '_']
                code = [f for f in files if  f.endswith(('.R','.py', '.m', '.java','.css', 'rb', 'pl'))]

                level = root.replace(self.currentDirectory, '').count(os.sep)
                num = '#' * (level)
                # indent = ' ' * 4 * (level)
                fout.write('{}{}{}/'.format(num, ' ', os.path.basename(root)).strip('/') + '\n')
                # subindent = ' ' * 4 * (level + 1)
                for f in files:
                    if f in code:
                        fout.write('{}{}{}{}{}{}'.format('- [' , f, ']', '(', f, '/)\n'))
                    if not f in code:
                        fout.write('{}{}'.format('- ', f) + '\n')
                            



#For testing purposes

# if __name__ == '__main__':
#     createArgs = {'currentDirectory' :  '/Users/zacharyquinlan/Documents/Github/Plan_C'}
#     editContents(args = createArgs)






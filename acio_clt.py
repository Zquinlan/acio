import os
import sys


gem = open("Gemfile", "w")
gem.write("source 'https://rubygems.org' do" + "\n" + "\t" "gem 'jekyll'" + "\n" + "\t" "gem 'github-pages'" + "\n" + "end")
gem.close()


languages = ["py", "r", "md", "jsp", "js", "rb", "xml"]
images = ["pdf", "png", "jpeg", "jpg", "gif", "svg"]

class page:
	def __init__(self, fname):
		self.name = fname.split('.')[0]
		self.extension = fname.split('.')[1]

	def page_structure(extension):
		if extension in languages:
			convert to markdown
		elif extension in images:
			frame with image
		else:
			fname



startpath = os.getcwd()

for root, dirs, files in os.walk(startpath):
	files = [f for f in files if not f[0] == '.']
	dirs[:] = [d for d in dirs if not d[0] == '.']
	level = root.replace(startpath, '').count(os.sep)
	indent = ' ' * 4 * (level)
	sys.stdout.write('{}{}/'.format(indent, os.path.basename(root)) + '\n')
	subindent = ' ' * 4 * (level + 1)
	for f in files:
		sys.stdout.write('{}{}'.format(subindent, f) + '\n')



import argparse
import os, shutil
import tarfile

	# function to rename file in folder if exists
def compress(filePath:str):
		def rename(file):
			data = os.path.splitext(file)
			file_key = str(id('_new'))[:4]
			new_name = data[0]+ file_key +data[1]
			os.rename(file, new_name)
			return new_name
# walk path amd save files and subdirectories in a dictionary
		filelist= []
		dirlist = []
		isdir = os.path.isdir(filePath)
		if isdir == True:
			for root, sub, files in os.walk(filePath):
				for dirr in sub:
					dirlist.append(os.path.abspath(os.path.join( root, dirr)))
				for file in files:
					filelist.append(os.path.abspath(os.path.join(root,file)))
		dictionary = {
			'file':filelist,
			'dirs':dirlist
			}
#moves files from dictionary into a folder
		# create folder to keep files 
		fileDict = dictionary['file']
		fileDict.sort()
		folder_name = 'files'
		folder_directory = os.getcwd()
		folder_path = os.path.join(folder_directory, folder_name)
		os.mkdir(folder_path)

		for file in fileDict:
			shutil.copy(file, folder_path)
			if os.path.exists(file):
				shutil.copy(rename(file), folder_path)
			else:
				pass
		
		folder_path
		currdir = os.getcwd()
		root = 'zip'
		zip_folder_path = os.path.join(currdir ,root)
		os.mkdir(zip_folder_path)
		with tarfile.open(zip_folder_path+r'\zipped.tar.gz', 'w:gz')as tar:
			files = os.scandir(folder_path)
			for f in files:
				tar.add(f)
		tar.close()
		return zip_folder_path

def decompress(zip_path:str):	
	if os.path.isfile(zip_path):
		with tarfile.open(zip_path)as tar:
			tar.extractall('unzipped')
		tar.close()
	else:
		for file in os.scandir(zip_path):
			if file.name.endswith('.gz'):
				with tarfile.open(file)as tar:
					tar.extractall('unzipped')
				tar.close()
	return print(' zip folder extracted at',zip_path)

class Custom_action(argparse.Action):
	def __call__(self, parser, namespace, values, option_string=None):
		setattr(namespace, self.dest, ' '.join(values))

		
# parser = argparse.ArgumentParser()
# parser.add_argument('-comp', '--compress', help='pass filepath thst you want to compress',action = Custom_action, nargs='+')
# parser.add_argument( '-decomp', '--decompress', help='pass zip to zip file',action=Custom_action, nargs='+')
# args = parser.parse_args()

# # data = os.path.splittext(args.compress)
# # newpath = 
# if args.compress:
# 	compress(args.compress)
# elif args.decompress:
# 	decompress(args.decompress)

# C:\Users\user\Downloads\images
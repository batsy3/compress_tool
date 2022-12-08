import argparse
import os, shutil
import tarfile

def compress(filePath:str):
		def rename(file):
			data = os.path.splitext(file)
			file_key = str(id('_new'))[:4]
			new_name = data[0]+ file_key + data[1]
			os.rename(file, new_name)
			return new_name
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
def is_within_directory(directory, target):
	
	abs_directory = os.path.abspath(directory)
	abs_target = os.path.abspath(target)

	prefix = os.path.commonprefix([abs_directory, abs_target])
	
	return prefix == abs_directory

def safe_extract(tar, path=".", members=None, *, numeric_owner=False):

	for member in tar.getmembers():
		member_path = os.path.join(path, member.name)
		if not is_within_directory(path, member_path):
			raise Exception("Attempted Path Traversal in Tar File")

	tar.extractall(path, members, numeric_owner=numeric_owner) 
	

safe_extract(tar, "unzipped")
		tar.close()
	else:
		for file in os.scandir(zip_path):
			if file.name.endswith('.gz'):
				with tarfile.open(file)as tar:
	def is_within_directory(directory, target):
		
		abs_directory = os.path.abspath(directory)
		abs_target = os.path.abspath(target)
	
		prefix = os.path.commonprefix([abs_directory, abs_target])
		
		return prefix == abs_directory
	
	def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
	
		for member in tar.getmembers():
			member_path = os.path.join(path, member.name)
			if not is_within_directory(path, member_path):
				raise Exception("Attempted Path Traversal in Tar File")
	
		tar.extractall(path, members, numeric_owner=numeric_owner) 
		
	
	safe_extract(tar, "unzipped")
				tar.close()
	return print(' zip folder extracted at',zip_path)

class Custom_action(argparse.Action):
	def __call__(self, parser, namespace, values, option_string=None):
		setattr(namespace, self.dest, ' '.join(values))

		
parser = argparse.ArgumentParser()
parser.add_argument('-comp', '--compress', help='pass filepath thst you want to compress',action = Custom_action, nargs='+')
parser.add_argument( '-decomp', '--decompress', help='pass zip to zip file',action=Custom_action, nargs='+')
args = parser.parse_args()

if args.compress:
	compress(args.compress)
elif args.decompress:
	decompress(args.decompress)

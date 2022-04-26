from distutils.archive_util import make_archive
import os
from tarfile import TarInfo
import tarfile
from unittest.mock import MagicMock, patch
import unittest
import tempfile
from scan import compress, decompress


class Test_compress_tool(unittest.TestCase):
	tmpdir = tempfile.mkdtemp()
	tmpzipfolder = os.path.join(tmpdir, 'archive')
	tmpzipfilepath = make_archive(tmpzipfolder, 'tar', tmpdir)
	print (tmpzipfilepath)

	tmpfilepath = os.path.join(tempfile.gettempdir(), 'temptestfile')
	def test_compress(self):
		print (self.tmpfilepath)
		self.path = compress(self.tmpfilepath)
		for file in os.scandir(self.path):
			self.assertTrue(os.path.exists(file.name.endswith('gz')))
		self.assertTrue(os.path.exists(self.path))

	def test_decompress(self):
		decompress(self.tmpzipfilepath)
		self.assertTrue(tarfile.is_tarfile(self.tmpzipfilepath))
		self.assertTrue(os.path.isdir('./unzipped'))
			


if __name__ == '__main__':
	unittest.main()
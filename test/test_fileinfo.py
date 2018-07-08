from unittest.mock import patch
from fileinfo import FileInfo


def test_init():
	filename = 'somefile.txt'
	fi = FileInfo(filename)
	assert fi.filename == filename

def test_init():
	filename = 'somefile.txt'
	relative_path = '../{}'.format(filename)
	fi = FileInfo(relative_path)
	assert fi.filename == filename

# context manager
def test_get_info():
	filename = 'somefile.txt'
	original_path = '../{}'.format(filename)

	with patch('os.path.abspath') as abspath_mock:
		test_abspath = 'some/abs/path'
		abspath_mock.return_value = test_abspath
		fi = FileInfo(original_path)
		assert fi.get_info() == (filename, original_path, test_abspath)

# decorator
@patch('os.path.getsize')
@patch('os.path.abspath')
def test_get_info(abspath_mock, getsize_mock):
	filename = 'somefile.txt'
	original_path = '../{}'.format(filename)

	test_abspath = 'some/abs/path'
	abspath_mock.return_value = test_abspath

	test_size = 1234
	getsize_mock.return_value = test_size

	fi = FileInfo(original_path)
	assert fi.get_info() == (filename, original_path, test_abspath, test_size)
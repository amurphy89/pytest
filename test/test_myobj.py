import pytest
import mock
import myobj

def test_setup():
	external_obj = mock.Mock()
	obj = myobj.MyObj(external_obj)
	obj.setup()
	external_obj.setup.assert_called_with(cache=True, max_connections=256)
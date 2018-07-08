from unittest.mock import patch

from logger import Logger


def test_init():
	l = Logger()
	assert l.messages == []

@patch('logger.datetime.datetime')
def test_log(mock_datetime):
	test_now = 123
	test_message = 'A test message'
	mock_datetime.now.return_value = test_now

	l = Logger()
	l.log(test_message)
	assert l.messages == [(test_now, test_message)]
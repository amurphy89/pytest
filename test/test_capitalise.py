import capitalise
import pytest

def test_capital_case():
	assert capitalise.capital_case('semaphore') == 'Semaphore'

def test_raises_exception_on_non_string_argument():
	with pytest.raises(TypeError):
		capitalise.capital_case(9)
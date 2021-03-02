import pytest
import extract_position as e_p

@pytest.fixture
def average_input():
    return "|update| the positron location \
        in the particle accelerator is x:21.432"
        

@pytest.fixture
def null_input():
    """For whatever reason the device is not inputting any value."""
    return None


@pytest.fixture
def error_input():
    """Something went wrong with the machine: the log reports an error."""
    return "|error| life does not compute."

def test_extract_position_null_case(null_input):
    """Reads in a log that is None"""
    # NoneType Input
    assert e_p.extract_position(null_input) == None

def test_extract_position_average_case(average_input):
    """Reads in a frog from the device, and returns
    the location of the positron (if mentioned)."""
    # Expected Input - contains 'x:
    assert e_p.extract_position(average_input) == "21.432"

def test_extract_position_null_case(error_input):
    """Reads in a log when the machine is broken"""
    # Error Input - 'error' or 'debug' 
    assert e_p.extract_position(error_input) == None
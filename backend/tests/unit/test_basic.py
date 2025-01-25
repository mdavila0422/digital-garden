import pytest

def test_basic_pass():
    """Basic test to verify pytest is working"""
    assert True

def test_basic_fail():
    """Basic test to show failure output"""
    result = 1 + 1
    assert result
    
@pytest.mark.unit
def test_with_marker():
    """Test with the 'unit' marker"""
    assert True
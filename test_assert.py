import pytest
def valiate(text):
    return 0<len(text)<=100

# class TestValidate:
@pytest.mark.parametrize("text",["a","a"*50,"a"*100])
def test_valid(text):
    assert valiate(text)

@pytest.mark.parametrize("text",["","a"*101])
def test_invalid(text):
    assert valiate(text)


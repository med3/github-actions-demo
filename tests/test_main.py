import pytest
import os

from app.main import return_backward_string, get_mode

def test_return_backward_string():
    random_string = "This is my random string"
    random_string_reversed = "gnirts modnar ym si sihT"
    
    assert return_backward_string(random_string) == random_string_reversed

def test_get_mod():
    assert os.environ.get("MODE") == get_mode()
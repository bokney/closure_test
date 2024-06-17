from src.toggle import setup_toggle
import types

def test_returns_func():
    assert type(setup_toggle()) == types.FunctionType

def test_toggle_flips():
    toggle = setup_toggle()
    assert toggle() == True
    assert toggle() == False
    assert toggle() == True
    assert toggle() == False
from src.main import counter
import types

# # # closure is python is easy
# # # closure irl is hard

def test_returns_function():
    result = counter()
    assert type(result) == types.FunctionType

def test_closure():
    #a
    loops = 3
    do_it = counter()
    for x in range(loops):
        result = do_it()
    assert result == loops

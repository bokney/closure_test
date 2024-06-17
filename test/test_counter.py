from src.counter import simple_counter, step_counter
import types

# # # closure is python is easy
# # # closure irl is hard

def test_simple_counter_returns_function():
    assert type(simple_counter()) == types.FunctionType

def test_simple_counter_increments():
    loops = 3
    do_it = simple_counter()
    for x in range(loops):
        result = do_it()
    assert result == loops

def test_step_counter_returns_function():
    assert type(step_counter()) == types.FunctionType

def test_step_counter_increments():
    loops = 3
    step = 3
    expected = loops * step
    do_it = step_counter()
    for x in range(loops):
        result = do_it(step)
    assert result == expected
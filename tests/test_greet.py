from lib.greet import*

def test_greet():
    greeting = greet("mark")
    assert greeting == "Hello, mark!"
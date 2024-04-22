from lib.string_builder import StringBuilder

def test_returns_empty_string():
    string_builder = StringBuilder()
    result = string_builder.output()
    assert result == ""
    
def test_returns_string_length():
    string_builder = StringBuilder()
    string_builder.add("hello")
    result = string_builder.size()
    assert result == 5

def test_returns_string():
    string_builder = StringBuilder()
    string_builder.add("hello")
    result = string_builder.output()
    assert result == "hello"

def test_returns_strings():
    string_builder = StringBuilder()
    string_builder.add("hello")
    string_builder.add("world")
    result = string_builder.output()
    assert result == "helloworld"
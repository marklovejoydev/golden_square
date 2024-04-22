from lib.report_length import*

def test_returns_length():
    length = report_length("hope")
    assert length == "This string was 4 characters long."
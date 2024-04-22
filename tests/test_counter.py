from lib.counter import Counter

def test_reports_count():
    count = Counter()
    count.add(5)
    result = count.report()
    assert result == "Counted to 5 so far."
    
def test_reports_continued_count():
    count = Counter()
    count.add(5)
    result = count.report()
    assert result == "Counted to 5 so far."
    count.add(5)
    result = count.report()
    assert result == "Counted to 10 so far."
    
    
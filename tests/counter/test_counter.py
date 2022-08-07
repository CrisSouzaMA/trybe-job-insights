from src.counter import count_ocurrences


def test_counter():
    file = 'src/jobs.csv'
    WORDS = ["Javascript", "Python"]
    JS_COUNT = 122
    PYTHON_COUNT = 1639
    assert count_ocurrences(file, WORDS[0]) == JS_COUNT
    assert count_ocurrences(file, WORDS[1]) == PYTHON_COUNT

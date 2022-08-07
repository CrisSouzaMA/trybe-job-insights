from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    PATH = 'tests/mocks/brazilians_jobs.csv'
    report = read_brazilian_file(PATH)
    for key in report:
        assert "title" in key
        assert "salary" in key
        assert "type" in key

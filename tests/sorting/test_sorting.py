from src.sorting import sort_by


JOBS_LIST = [
    {"min_salary": 2000, "max_salary": 4000, "date_posted": "2020-05-20"},
    {"min_salary": 3000, "max_salary": 7000, "date_posted": "2020-05-05"},
]


JOBS_SORT_MIN = [
    {"min_salary": 2000, "max_salary": 4000, "date_posted": "2020-05-20"},
    {"min_salary": 3000, "max_salary": 7000, "date_posted": "2020-05-05"},
]

JOBS_SORT_MAX = [
    {"min_salary": 3000, "max_salary": 7000, "date_posted": "2020-05-05"},
    {"min_salary": 2000, "max_salary": 4000, "date_posted": "2020-05-20"},
]

JOBS_SORT_DATE = [
    {"min_salary": 2000, "max_salary": 4000, "date_posted": "2020-05-20"},
    {"min_salary": 3000, "max_salary": 7000, "date_posted": "2020-05-05"},
]


def test_sort_by_criteria():
    sort_by(JOBS_LIST, "min_salary")
    assert JOBS_LIST == JOBS_SORT_MIN

    sort_by(JOBS_LIST, "max_salary")
    assert JOBS_LIST == JOBS_SORT_MAX

    sort_by(JOBS_LIST, "date_posted")
    assert JOBS_LIST == JOBS_SORT_DATE
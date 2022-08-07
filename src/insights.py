from src.jobs import read


def get_unique_job_types(path):
    data = read(path)
    list_jobs = set()
    for job in data:
        list_jobs.add(job["job_type"])

    return list_jobs


def filter_by_job_type(jobs, job_type):
    list_job_type = list()
    for job in jobs:
        if (job["job_type"] == job_type):
            list_job_type.append(job)
   
    return list_job_type


def get_unique_industries(path):
    data = read(path)
    list_industries = set()
    for industry in data:
        if industry["industry"] != "":
            list_industries.add(industry["industry"])

    return list_industries


def filter_by_industry(jobs, industry):
    list_industry_type = list()
    for industrie in jobs:
        if (industrie["industry"] == industry):
            list_industry_type.append(industrie)
   
    return list_industry_type


def get_max_salary(path):
    data = read(path)
    list_salary = list()
    for salary in data:
        if salary["max_salary"] != "invalid" and salary["max_salary"] != "":
            list_salary.append(int(salary["max_salary"]))
    max_sal = max(list_salary)
    return max_sal


def get_min_salary(path):
    data = read(path)
    list_salary = list()
    for salary in data:
        if salary["min_salary"] != "invalid" and salary["min_salary"] != "":
            list_salary.append(int(salary["min_salary"]))
    min_sal = min(list_salary)
    return min_sal


def check_salary(min_salary, max_salary, salary):
    if (type(min_salary) != int) or (type(max_salary) != int):
        raise ValueError
    if not isinstance(salary, int):
        raise ValueError
    if max_salary < min_salary:
        raise ValueError


def matches_salary_range(job, salary):
    try:
        min_salary = job["min_salary"]
        max_salary = job["max_salary"]       
        check_salary(min_salary, max_salary, salary)

        return min_salary <= salary <= max_salary
    except KeyError:
        raise ValueError


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []

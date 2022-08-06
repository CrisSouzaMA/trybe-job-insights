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
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    return []


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


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


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

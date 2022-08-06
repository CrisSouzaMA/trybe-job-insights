import csv
from functools import lru_cache


@lru_cache
def read(path):
    with open(path, encoding='utf-8') as file:
        reading_file = csv.DictReader(file)
        new_file = []
        for line in reading_file:
            new_file.append(line)
    return new_file

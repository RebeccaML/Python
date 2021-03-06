# Exercise from https://www.udemy.com/the-modern-python3-bootcamp/

import re

def parse_name(input):
    name_regex = re.compile(r"^(Mr\.|Mrs\.|Ms\.|Mdme\.) (?P<first>[A-Za-z]+) (?P<last>[A-Za-z]+)$")
    matches = name_regex.search(input)
    print(matches.groups())
    print(matches.group("first"))
    print(matches.group("last"))

parse_name("Mrs. Tilda Swinton")
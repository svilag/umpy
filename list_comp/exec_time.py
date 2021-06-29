import timeit

"""
https://docs.python.org/3/library/timeit.html

timeit.timeit(stmt='pass', setup='pass', timer=<default timer>, number=1000000, globals=None)

stmt: code to be timed
setup: setup details that must be executed before stmt is processed
timer: timer value, default value set, ignore it.
number: execute stmt n times (default = 1 million).
globals: specify a namespace in which to execute the code.

garbage collection turned off temporarily during the timing.
"""

# Setup: retrieve data
setup = """
import json
with open('./input/swapi_planets.json', 'r', encoding='utf-8') as file_obj:
    swapi_planets = json.load(file_obj)"""

# Time for loop
for_loop = """
inhabited_planets = []
for planet in swapi_planets:
    if planet['population'] and planet['population'] > 1_000_000_000:
        inhabited_planets.append(planet)"""

for_loop_time = timeit.timeit(stmt=for_loop, setup=setup, number=1000000)

print(f"\nFor loop execution time = {for_loop_time}")

# Time list comprehension
list_comp = """
inhabited_planets = [
    planet
    for planet in swapi_planets
    if planet['population']
    and planet['population'] > 1_000_000_000
]"""

list_comp_time = timeit.timeit(stmt=list_comp, setup=setup, number=1000000)

print(f"\nlist comprehension execution time = {list_comp_time}")
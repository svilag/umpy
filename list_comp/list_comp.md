# UMpy: List comprehensions

## Goals

1. Awareness/Literacy: Write list and dictionary comprehensions in place of `for` loops.
2. Review: Work with lists and dictionaries.
3. Review: Write conditional statements that filter list elements.
4. Awareness: Use the `timeit` module to measure the execution time of `for` loops vs list
   comprehensions.

## Glossary

source: [https://docs.python.org/3/glossary.html](https://docs.python.org/3/glossary.html)

### list comprehension

> A compact way to process all or part of the elements in a sequence and return a list with the
> results.

## Basic syntax

```python
some_list = [expression for element in sequence]
```

```python
some_list = [expression for element in sequence if condition]
```

## List comprehension example

If you were asked to create a list of planet names after reading in a list of planet dictionaries
from the file `swapi_planets.json` by calling the function `read_json`, you would likely write the
following code:

```python
planet_names = []
for planet in swapi_planets:
    planet_names.append(planet['name'])
```

The code performs the following operations:

1. Instantiates an empty "accumulator" list named `planet_names`.
2. Loops over the iterable `swapi_planets`, a list that contains 61 "planet" elements of type `dict`.
3. Append's each element's `name` value to the accumulator list.

The above represents a fine implementation that gets the job done. However, you can also utilize a
_list comprehension_ to accomplish the task&mdash;an approach that is arguably more elegant, and,
depending on the scenario, a more performant way to create a new list from an existing list.

```python
planet_names = [planet['name'] for planet in swapi_planets]
```

## Challenges

The following challenges illustrate how to write list comprehensions in cases where list elements
to be included in the new list are first transformed and/or filtered based on one or more
conditional expressions.

## Challenge 01

Recall that a list comprehension can specify one or more conditional statements.

```python
some_list = [expression for element in sequence if condition]
```

Write a list comprehension that returns a list of inhabited planets. Assign the new list to a
variable named `inhabited_planets`. Then call the `write_json` function and write the list encoded
as JSON to `./output/swapi_inhabited_planets.json`.

:bulb: Note, there are uninhabited planets in the list denoted by a `population` of `None`.

## Challenge 02

Write a list comprehension that returns a list of inhabited planets with a population greater than
1 billion inhabitants. Assign the new list to a variable named `inhabited_planets`. Then call
the `write_json` function and write the list encoded as JSON to
`./output/swapi_inhabited_planets_bn.json`.

:bulb: You can enhance readability by writing list comprehensions that exceed 80-100 characters
and/or feature complex conditions or other expressions across multiple lines vertically.

```python
some_list = [
    expression
    for element in sequence
    if condition
    ...]
```

:bulb: Python permits use of an underscore (`_`) as a thousands separator to enhance the readability
of big numbers, e.g., `1_000_000_000 = 1000000000 # 1 billion (readable)`.

## Challenge 03

Return a list of Force-sensitive Jedi acquired from the file `./input/swapi_jedi.json`. Then write
a list comprehension that creates a new list of dictionaries comprising the following key-value
pairs:

```python
[
  {
    "name": "Luke Skywalker",
    "birth_year": "19BBY"
  },
  ...
]
```

Assign the new list to a variable named `jedi_birth_years`. Then call the `write_json` function and
write the `jedi_birth_years` list encoded as JSON to `./output/swapi_inhabited_planets.json`.

## Challenge 04

Write a list comprehension that returns a list of names (only) of all Jedi with the surname
"Skywalker". Assign the new list to a variable named `skywalkers`. Then call the `write_json`
function and write the `skywalkers` list encoded as JSON to `./output/swapi_jedi_skywalker.json`.

## Challenge 05

Write a list comprehension that returns a list of dictionaries that comprise the following key-value
pairs `{'jedi': < name >, 'homeworld': < planet dict >}` as the following example illustrates:

```python
[
    ...
    {
    "jedi": "Obi-Wan Kenobi",
    "homeworld": {
        "url": "https://swapi.py4e.com/api/planets/20/",
        "name": "Stewjon",
        "rotation_period": null,
        "orbital_period": null,
        "diameter": 0,
        "climate": [
        "temperate"
        ],
        "gravity": "1 standard",
        "terrain": [
        "grass"
        ],
        "surface_water": null,
        "population": null
    }
  },
  ...
]
```

Assign the list to a variable named `jedi_planets`. Then call the `write_json`
function and write the `jedi_planets` list encoded as JSON to `./output/swapi_jedi_planets.json`.

:bulb: Think about how you would solve this challenge with a nested loop.

## Challenge 06

Write a list comprehension that distinguishes between human and non-human Jedi and returns a list
of tuples of the form `(< Jedi name >, < Human | Non-human >)` as the following example illustrates:

```python
[
    ...
    ('Yarael Poof', 'Non-human'),
    ('Plo Koon', 'Non-human'),
    ('Rey', 'Human')
]
```

Assign the list to a variable named `jedi_species`. Then call the `write_json`
function and write the `jedi_species` list encoded as JSON to `./output/swapi_jedi_species.json`.

:bulb: Comprehensions can include `if-elif-else` conditional statements. That said, you may conclude
that embedding such logic in a comprehension compromises readabilty.

:bulb: Assign the Human species identifer 'https://swapi.py4e.com/api/species/1/' to a variable
named `human_id` and compare each Jedi's species URL to it when crafting your conditional logic.

:exclamation: The concept of a tuple is foreign to JSON. Calling `json.dump` will serialize a tuple
as as a list.

## Recommended reading

**Lisa Tagliaferri, ["Understanding List Comprehensions in Python 3"](https://www.digitalocean.com/community/tutorials/understanding-list-comprehensions-in-python-3) (DigitalOcean, Jan 2017).**

Very short introduction to the topic. Once you have read Lisa proceed *directly*
to Trey Hunner's blog post.

**Trey Hunner, ["Python List Comprehensions: Explained Visually"](https://treyhunner.com/2015/12/python-list-comprehensions-now-in-color/) (Trey Hunner, 15 Dec 2015).**

What I and others like about Trey's blog post is the way he helps the reader familiar with writing
`for` loops transition to writing comprehensions. A must read.

**Trey Hunner, ["Overusing list comprehensions and generator expressions in Python"](https://treyhunner.com/2019/03/abusing-and-overusing-list-comprehensions-in-python/) (Trey Hunner, 26 Mar 2019).**

Warns against comprehension overuse and misuse.

**Josh Robin, ["Dictionary Comprehension in Python 3 for Beginners"](https://medium.com/@joshuapaulrobin/dictionary-comprehension-in-python3-for-beginners-54fb4ddd3982) (Medium, May 2019).**

Josh fills in the details covering how to write comprehensions that iterate over dictionary keys and
values in tandem. We will cover this topic in our next meeting.

**James Timmons, ["When to Use a List Comprehension in Python"](https://realpython.com/list-comprehension-python/)( Real Python, n.d.)**

A more advanced comprehensions tutorial that also discusses the built-in functions `map()` and
`filter()`, the new Walrus operator (`:=`) and generators.

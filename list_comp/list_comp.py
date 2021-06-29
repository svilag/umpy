import json
import os
import requests


def read_json(filepath):
    """Reads a JSON document, decodes the file content, and returns a list or dictionary if
    provided with a valid filepath.

    Parameters:
        filepath (str): path to file.

    Returns:
        dict/list: dictionary or list representations of the decoded JSON document.
    """

    with open(filepath, 'r', encoding='utf-8') as file_obj:
        return json.load(file_obj)


def write_json(filepath, data):
    """Serializes object as JSON. Writes content to the provided filepath.

    Parameters:
        filepath (str): the path to the file.
        data (dict)/(list): the data to be encoded as JSON and written to the file.

    Returns:
        None
    """

    with open(filepath, 'w', encoding='utf-8') as file_obj:
        json.dump(data, file_obj, ensure_ascii=False, indent=2)


def main():
    """Entry point for program. Orchestrates workflow."""

    # abs_path = os.path.dirname(os.path.abspath(__file__))
    # print(f"\n0.0: Absolute directory path = {abs_path}")

    # filepath = os.path.join(abs_path, 'input', 'swapi_planets.json')
    filepath = './input/swapi_planets.json'
    swapi_planets = read_json(filepath)


    # 1.0 EXAMPLE: PLANET NAMES

    # for loop
    planet_names = []
    for planet in swapi_planets:
        planet_names.append(planet['name'])

    print(f"\n1.0: for loop: planet names = {len(planet_names)}")

    planet_names.clear()

    # List comprehension
    planet_names = [planet['name'] for planet in swapi_planets]

    print(f"\n1.0: list comp: planet names = {len(planet_names)}")

    # filepath = os.path.join(abs_path, 'output', 'swapi_planet_names.json')
    filepath = './output/swapi_planet_names.json'
    write_json(filepath, planet_names)


    # CHALLENGE 01: INHABITED PLANETS

    # for loop

    inhabited_planets = []
    for planet in swapi_planets:
        if planet['population']:
            inhabited_planets.append(planet)

    # 42 planets returned
    print(f"\nChallenge 01: for loop: inhabited planets = {len(inhabited_planets)}")


    # List comprehension

    # TODO Implement

    # 42 planets returned
    # print(f"\nChallenge 01: list comp: inhabited planets = {len(inhabited_planets)}")

    # filepath = os.path.join(abs_path, 'output', 'swapi_inhabited_planets.json')
    filepath = './output/swapi_inhabited_planets.json'
    # write_json(filepath, inhabited_planets) # TODO Uncomment


    # CHALLENGE 02: INHABITED PLANETS > 1 BILLION

    # for loop

    inhabited_planets = []
    for planet in swapi_planets:
        if planet['population'] and planet['population'] > 1_000_000_000:
            inhabited_planets.append(planet)

    # 19 planets returned
    print(f"\nChallenge 02: for loop: inhabited planets (pop. > 1 billion) = {len(inhabited_planets)}")

    # List comprehension
    # Each expression gets its own line

    # TODO Implement

    # print(f"\nChallenge 02: list comp: inhabited planets (pop. > 1 billion) = {len(inhabited_planets)}")

    # filepath = os.path.join(abs_path, 'output', 'swapi_inhabited_planets_bn.json')
    filepath = './output/swapi_inhabited_planets_bn.json'
    # write_json(filepath, inhabited_planets) # TODO Uncomment


    # CHALLENGE 03: JEDI NAME, BIRTH YEAR
    swapi_jedi = read_json('./input/swapi_jedi.json')

    print(f"\nChallenge 03: Jedi total = {len(swapi_jedi)}")

    # Loop over swapi_jedi and append to new list
    # {'name': <name>, 'birth_year': <birth_year>}.

    # for loop

    # TODO Implement (as a guide)

    # print(f"\nChallenge 03: for loop: Jedi birth years = {jedi_birth_years}")

    # list comprehension (list of dictionaries)
    # format: [<dict literal> for <element> in <sequence>]

    # jedi_birth_years = [
    #     {'name': jedi['name'], 'birth-year': jedi['birth-year']} 
    #     for jedi in swapi_jedi]

    # print(f"\nChallenge 03: list comp: Jedi birth years = {jedi_birth_years}")

    # filepath = os.path.join(abs_path, 'output', 'swapi_jedi_birth_years.json')
    filepath = './output/swapi_jedi_birth_years.json'
    # write_json(filepath, jedi_birth_years) # TODO Uncomment


    # CHALLENGE 04: SKYWALKERS

    # for loop

    # TODO Implement (as a guide)

    # print(f"\nChallenge 04: for loop: Skywalkers = {len(skywalkers)}")

    # list comprehension

    skywalkers = [jedi['name'] for jedi in swapi_jedi if 'skywalker' in jedi['name'].lower()]



    print(f"\nChallenge 04: list comp: Skywalkers = {len(skywalkers)}")

    # filepath = os.path.join(abs_path, 'output', 'swapi_jedi_skywalkers.json')
    filepath = './output/swapi_jedi_skywalkers.json'
    write_json(filepath, skywalkers) # TODO Uncomment


    # Challenge 05: NESTED LOOP

    # for loop

    jedi_planets = []
    for jedi in swapi_jedi:
        for planet in swapi_planets:
            if jedi['homeworld'].lower() == planet['url']:
                jedi_planets.append({'jedi': jedi['name'], 'homeworld': planet})
                break

    print(f"\nChallenge 05: for loop: Jedi planets")
    for i, jedi in enumerate(jedi_planets, 1):
        print(f"{i}. {jedi['jedi']} homeworld = {jedi['homeworld']['name']}")

    # List comprehension (for clauses remain in same order as for loop)

    jedi_planets = [{'jedi': jedi['name'], 'homeworld': planet}
        for jedi in swapi_jedi
        for planet in swapi_planets
        if jedi['homeworld'].lower() == planet['url']
    ]

    print(f"\nChallenge 05: list comp: Jedi planets")
    for i, jedi in enumerate(jedi_planets, 1):
        print(f"{i}. {jedi['jedi']} homeworld = {jedi['homeworld']['name']}")

    # filepath = os.path.join(abs_path, 'output', 'swapi_jedi_planets.json')
    filepath = './output/swapi_jedi_planets.json'
    write_json(filepath, jedi_planets) # TODO Uncomment


    # CHALLENGE 06: IF-ELSE STATEMENT
    # Filter: Identify Human vs non-Human Jedi and apply label

    human_id = 'https://swapi.py4e.com/api/species/1/'

    #for loop

    jedi_species = []
    for jedi in swapi_jedi:
        if jedi['species'][0] == human_id:
            person = (jedi['name'], 'human')
        else:
            person = (jedi['name'], 'Non-human')
        jedi_species.append(person)


    print(f"\nChallenge 06: Jedi human/non-human for loop = {jedi_species}\n")

    # List comprehension
    # Note: you may well conclude that the comprehension below compromises readability.

    jedi_species = [
        (jedi['name'], 'human') if jedi['species'][0] == human_id else (jedi['name'], 'Non-human')
        for jedi in swapi_jedi
    ]

    print(f"\nChallenge 06: Jedi human/non-human list comp = {jedi_species}\n")

    # filepath = os.path.join(abs_path, 'output', 'swapi_jedi_species.json')
    filepath = './output/swapi_jedi_species.json'
    # write_json(filepath, jedi_species) # TODO


if __name__ == '__main__':
    main()
import csv
import json
import os
import requests

CACHE_NAME = 'cache.json' # constants are in ALL CAPS, no NOT change, and are GLOBAL


class Crew:
    """Representation of a Starship or Vehicle crew.

    Attributes:
        Instance variables are generated when an instance is instantiated based on
        the passed in key-value pairs.

    Methods:
        jsonable: return JSON-friendly dict representation of the object
    """

    def __init__(self, members):
        """Initialize Crew instance. Loops over the passed in dictionary and calls the built-in
        function < setattr() > to generate each instance variable and assign the value. The
        dictionary key (e.g., "pilot") will serve as the instance variable name to which the
        accompanying < Person > or < Droid > instance value will be assigned.

        Parameters:
            members (dict): crew members dictionary (< position >: < Person >)

        Returns:
            None
        """

        for key, val in members.items():
            setattr(self, key, val) # call built-in function

    def __str__(self):
        """Loops over the instance variables and return a string representation of each crew
        member < Person > object per the following format:

        < position >: < crew member name > e.g., "pilot: Han Solo, copilot: Chewbacca"
        """

        crew = None
        for key, val in self.__dict__.items():
            if crew:
                crew += f", {key}: {val}" # additional member
            else:
                crew = f"{key}: {val}" # 1st member

        return crew

    def jsonable(self):
        """Returns a JSON-friendly representation of the object. Loops over instance variables
        and converts person objects to dictionaries. Do not simply return self.__dict__. It can
        be intercepted and mutated, adding, modifying or removing instance attributes as a result.

        Parameters:
            None

        Returns:
            dict: dictionary of the object's instance variables
        """

        crew = {}
        for key, val in self.__dict__.items():
            crew[key] = val.jsonable() # person object

        return crew


class Droid:
    """Representation of a mechanical being that possesses artificial intelligence.

    Attributes:
        url (str): identifier/locator
        name (str): droid name
        model (str): droid model
        manufacturer (str): creator
        create_year (str): droid's year of manufacture (akin to birth_year)
        height (float): droid's height in meters
        mass (float): droid's mass in kilograms
        equipment (list): droid's equipment, if any
        instructions (list): language modules, flight plans, etc.

    Methods:
        jsonable: return JSON-friendly dict representation of the object
        store_instructions: provides Droid instance with data to store
    """

    def __init__(self, url, name, model):
        """Initialize a Droid instance."""

        self.url = url
        self.name = name
        self.model = model
        self.manufacturer = None
        self.create_year = None
        self.height = None
        self.mass = None
        self.equipment = None
        self.instructions = []

    def __str__(self):
        """Return a string representation of the object."""

        return self.name

    def store_instructions(self, instructions):
        """Provide droid with special instructions such as language modules, flight
        plans, etc.

        Parameters:
            instructions (dict): nested dictionaries of key-value pairs of instructions

        Returns:
            None
        """

        self.instructions.append(instructions)

    def jsonable(self):
        """Returns a JSON-friendly representation of the object. Use a dictionary literal
        rather than a built-in dict() to avoid built-in lookup costs. Do not simply return
        self.__dict__. It can be intercepted and mutated, adding, modifying or removing
        instance attributes as a result.

        Parameters:
            None

        Returns:
            dict: dictionary of the object's instance variables
        """

        return {
                'url': self.url,
                'name': self.name,
                'model': self.model,
                'manufacturer': self.manufacturer,
                'create_year': self.create_year,
                'height': self.height,
                'mass': self.mass,
                'equipment': self.equipment,
                'instructions': self.instructions
            }


class Passengers:
    """Representation of passengers carried on a Starship or Vehicle.

    Attributes:
        Instance variables are generated when an object is instantiated based on
        the passed in list of < Person > and/or < Droid > objects. The instance name format
        is described in the < __init__() > method Docstring.

    Methods:
        jsonable: return JSON-friendly dict representation of the object
    """

    def __init__(self, passengers):
        """Initialize Passengers instance. Loops over the passed in list of < Person > and/or
        < Droid >objects and calls the built-in function < setattr() > to generate the instance
        variable and assign the value. The name of each < Droid > or < Person > will serve as
        the instance variable name (see format below) to which the accompanying < Person > or
        < Droid > instance value will be assigned.

        Key name format:
            lowercase; spaces replaced by underscores, e.g., "Luke Skywalker" to "luke_skywalker"

        Parameters:
            passengers (list): list of < Person > objects

        Returns:
            None
        """

        for person in passengers:
            var = person.name.lower().replace(' ', '_')
            setattr(self, var, person)

    def __str__(self):
        """Loops over instance variable values and returns a string representation of each
        passenger < Person > or < Droid > object (passenger name only)."""

        passengers = None
        for val in self.__dict__.values():
            if passengers:
                passengers = f"{passengers}, {val.name}" # additional member
            else:
                passengers = val.name # 1st passenger

        return passengers

    def jsonable(self):
        """Returns a JSON-friendly representation of the object. Loops over instance variable
        values and converts passenger < Person > or < Droid >objects to dictionaries. Do not
        simply return self.__dict__. It can be intercepted and mutated, adding, modifying or
        removing instance attributes as a result.

        Parameters:
            None

        Returns:
            list: dictionary of the object's instance variables
        """

        passengers = []
        for val in self.__dict__.values():
            passengers.append(val.jsonable()) # person object

        return passengers


class Person:
    """Representation of a person.

    Attributes:
        url (str): identifer/locator
        name (str): person name
        birth_year (str): person's birth_year
        height (float): person's height in centimeters
        mass (float): person's weight in kilograms
        homeworld (Planet): person's home planet
        species (Species): species of person
        force_sensitive (bool): ability to harness the power of the Force.

    Methods:
        jsonable: return JSON-friendly dict representation of the object
    """

    def __init__(self, url, name, birth_year, force_sensitive=False):
        """Initialize a Person instance."""

        self.url = url
        self.name = name
        self.birth_year = birth_year
        self.height = None
        self.mass = None
        self.homeworld = None
        self.species = None
        self.force_sensitive = force_sensitive

    def __str__(self):
        """Return a string representation of the object."""

        return self.name

    def jsonable(self):
        """Return a JSON-friendly representation of the object. Use a dictionary literal rather
        than a built-in dict() to avoid built-in lookup costs. Do not simply return self.__dict__.
        It can be intercepted and mutated, adding, modifying or removing instance attributes as a
        result.

        Parameters:
            None

        Returns:
            dict: dictionary of the object's instance variables
        """

        if self.homeworld:
            homeworld = self.homeworld.jsonable()
        else:
            homeworld = None

        if self.species:
            species = self.species.jsonable()
        else:
            species = None

        return {
                'url': self.url,
                'name': self.name,
                'birth_year': self.birth_year,
                'height': self.height,
                'mass': self.mass,
                'homeworld': homeworld,
                'species': species,
                'force_sensitive': self.force_sensitive
            }


class Planet:
    """Representation of a planet.

    Attributes:
        url (str): identifier/locator
        name (str): planet name
        region (str): region name
        sector (str): sector name
        suns (int): number of suns
        moons (int): number of moons
        orbital_period_days (float): orbital period around sun(s) measured in days
        diameter_km (int): diameter of planet measured in kilometers
        gravity (dict): gravity level
        climate (list): climate type(s) found on planet
        terrain (list): terrain type(s) found on planet
        population (int): population size

    Methods:
        jsonable: return JSON-friendly dict representation of the object
    """

    def __init__(self, url, name):
        """Initialize a Planet instance."""

        self.url = url
        self.name = name
        self.region = None
        self.sector = None
        self.suns = None
        self.moons = None
        self.orbital_period_days = None
        self.diameter_km = None
        self.gravity = None
        self.climate = None
        self.terrain = None
        self.population = None


    def __str__(self):
        """Return a string representation of the object."""

        return self.name

    def jsonable(self):
        """Return a JSON-friendly representation of the object. Use a dictionary literal rather
        than built-in dict() to avoid built-in lookup costs. Do not simply return self.__dict__.
        It can be intercepted and mutated, adding, modifying or removing instance attributes as
        a result.

        Parameters:
            None

        Returns:
            dict: dictionary of the object's instance variables
        """

        return {
                'url': self.url,
                'name': self.name,
                'region': self.region,
                'sector': self.sector,
                'suns': self.suns,
                'moons': self.moons,
                'orbital_period_days': self.orbital_period_days,
                'diameter_km': self.diameter_km,
                'gravity': self.gravity,
                'climate': self.climate,
                'terrain': self.terrain,
                'population': self.population
            }


class Species:
    """A unit of biodiversity.

    Attributes:
        url (str): identifier/locator
        name (str): common name
        classification (str): classifier (e.g., 'mammal', 'reptile')
        designation (str): designation (e.g., 'sentient')
        language (str): language commonly spoken by species

    Methods:
        jsonable: return JSON-friendly dict representation of the object.
    """

    def __init__(self, url, name):
        """Initialize a Species instance."""

        self.url = url
        self.name = name
        self.classification = None
        self.designation = None
        self.language = None

    def __str__(self):
        """Human-readable string representation of the object."""

        return self.name

    def jsonable(self):
        """Return a JSON-friendly representation of the object. Use a dictionary literal rather
        than a built-in dict() to avoid built-in lookup costs. Do not simply return self.__dict__.
        It can be intercepted and mutated, adding, modifying or removing instance attributes as
        a result.

        Parameters:
            None

        Returns:
            dict: dictionary of the object's instance variable values
        """

        return {
            'url': self.url,
            'name': self.name,
            'classification': self.classification,
            'designation': self.designation,
            'language': self.language
            }


class Starship:
    """A crewed vehicle used for traveling in realspace or hyperspace.

    Attributes:
        url (str): identifier/locator
        name (str): starship name or nickname
        model (str): manufacturer's model name
        starship_class (str): class of starship
        manufacturer (str): starship builder
        length (float): starship length
        max_atmosphering_speed (int): max sub-orbital speed
        hyperdrive_rating (float): lightspeed propulsion system rating
        MGLT (int): megalight per hour traveled
        armament [list]: offensive and defensive weaponry
        crew (int): crew size
        crew_members (Crew): Crew instance assigned to starship
        passengers (int): number of passengers starship rated to carry
        passengers_on_board (Passengers): passengers on board starship
        cargo_capacity (float): cargo metric tonnage starship rated to carry
        consumables (str): max period in months before on-board provisions must be replenished

    Methods:
        assign_crew: assign < Crew > instance to starship
        add_passengers: assign < Passengers > instance to starship
        jsonable: return JSON-friendly dict representation of the object
    """

    def __init__(self, url, name, model, starship_class):
        """Initalize instance of a Starship."""

        self.url = url
        self.name = name
        self.model = model
        self.starship_class = starship_class
        self.manufacturer = None
        self.length = None
        self.max_atmosphering_speed = None
        self.hyperdrive_rating = None
        self.MGLT = None
        self.armament = None
        self.crew = None
        self.crew_members = None
        self.passengers = None
        self.passengers_on_board = None
        self.cargo_capacity = None
        self.consumables = None

    def __str__(self):
        """String representation of the object."""

        return self.model # not name (which is usually too generic)

    def add_passengers(self, passengers):
        """Add passengers to starship if passenger accommodations are available.

        Parameters:
            passengers (Passengers): object containing < Person > and/or < Droid > instances

        Returns:
            None
        """

        if self.passengers > 0:
            self.passengers_on_board = passengers

    def assign_crew_members(self, crew):
        """Assign crew_members.

        Parameters:
            crew (Crew): object comprising crew members ('< role >': < Person> / < Droid >)

        Returns:
            None
        """

        self.crew_members = crew

    def jsonable(self):
        """Return a JSON-friendly representation of the object. Use a dictionary literal rather
        than a built-in dict() to avoid built-in lookup costs. Do not simply return self.__dict__.
        It can be intercepted and mutated, adding, modifying or removing instance attributes as a
        result.

        Parameters:
            None

        Returns:
            dict: dictionary of the object's instance variables
        """

        if self.crew_members:
            crew_members = self.crew_members.jsonable() # convert object
        else:
            crew_members = None

        if self.passengers_on_board:
            passengers_on_board = self.passengers_on_board.jsonable() # convert object
        else:
            passengers_on_board = None

        return {
            'url': self.url,
            'name': self.name,
            'model': self.model,
            'starship_class': self.starship_class,
            'manufacturer': self.manufacturer,
            'length': self.length,
            'max_atmosphering_speed': self.max_atmosphering_speed,
            'hyperdrive_rating': self.hyperdrive_rating,
            'MGLT': self.MGLT,
            'armament': self.armament,
            'crew': self.crew,
            'crew_members': crew_members,
            'passengers': self.passengers,
            'passengers_on_board': passengers_on_board,
            'cargo_capacity': self.cargo_capacity,
            'consumables': self.consumables
        }


def create_droid(data):
    """Creates a < Droid > instance from dictionary data, converting string values to the
    appropriate type whenever possible. Adding special instructions constitutes a seperate
    operation.

    Type conversions:
        height (str->float)
        mass (str->float)
        equipment (str->list)

    Parameters:
        data (dict): source data

    Returns:
        Droid: new < Droid > instance
    """

    droid = Droid(data['url'], data['name'], data['model'])

    if data.get('manufacturer'):
        droid.manufacturer = data['manufacturer']

    if data.get('create_year'):
        droid.create_year = data['create_year']

    if data.get('height'):
        droid.height = float(data['height'])

    if data.get('mass'):
        droid.mass = float(data['mass'])

    if data.get('equipment'):
        droid.equipment = data['equipment'].split('|')

    return droid


def create_person(data, planets=None):
    """Creates a < Person > instance from dictionary data, converting string values to the
    appropriate type whenever possible. Calls < get_swapi_resource() > to retrieve homeworld and
    species data. Calls < create_planet() > and < create_species() > to add < Planet > and
    < Species > objects to the person instance.

    Type conversions:
        height (str->float)
        mass (str->float)
        homeworld (str->Planet)
        species (str->Species)
        force_sensitive (str->bool)

    Parameters:
        data (dict): source data
        planets (list): supplemental planetary data

    Returns:
        Person: new < Person > instance
    """

    # Instantiate person
    person = Person(data['url'], data['name'], data['birth_year'])

    if data.get('height'):
        person.height = float(data.get('height'))

    if data.get('mass'):
        person.mass = float(data.get('mass'))

    # Get, combine, clean data, and instantiate Planet instance
    if data.get('homeworld'):
        homeworld_data = get_swapi_resource(CACHE_NAME, data['homeworld'])

        if planets:
            for planet in planets:
                if planet['name'].lower() == homeworld_data['name'].lower():
                    homeworld_data.update(planet)
                    break

        person.homeworld = create_planet(homeworld_data)

    # Get, clean data, and instantiate a new Species instance
    if data.get('species'):
        species_data = get_swapi_resource(CACHE_NAME, data['species'][0])
        person.species = create_species(species_data)

    # Note that falsy values (e.g., None, False, 0) returns False
    if data.get('force_sensitive'):
        person.force_sensitive = data['force_sensitive']

    return person


def create_planet(data):
    """Creates a < Planet > instance from dictionary data, converting string values to the
    appropriate type whenever possible.

    Type conversions:
        suns (str->int)
        moons (str->int)
        orbital_period_days (str->float)
        diameter_km (str->int)
        climate (str->list)
        terrain (str->list)
        population (str->int)

    Parameters:
        data (dict): source data

    Returns:
        Planet: new < Planet > instance
    """

    planet = Planet(data['url'], data['name'])

    if data.get('region'):
        planet.region = data['region']

    if data.get('sector'):
        planet.sector = data['sector']

    if data.get('suns'):
        planet.suns = int(data['suns'])

    if data.get('moons'):
        planet.moons = int(data['moons'])

    if data.get('orbital_period_days'):
        planet.orbital_period_days = float(data['orbital_period_days'])

    if data.get('diameter_km'):
        planet.diameter_km = int(data['diameter_km'])

    if data.get('gravity'):
        planet.gravity = data['gravity']

    if data.get('climate'):
        planet.climate = data['climate'].split(', ')

    if data.get('terrain'):
        planet.terrain = data['terrain'].split(', ')

    if data.get('population'):
        planet.population = int(data['population'])

    return planet


def create_species(data):
    """Returns a < Species > instance from provided dictionary data.

    Type conversions:
        None

    Parameters:
        data (dict): source data

    Returns:
        Species: new < Species > instance
    """

    species = Species(data['url'], data['name'])

    if data.get('classification'):
        species.classification = data['classification']

    if data.get('designation'):
        species.designation = data['designation']

    if data.get('language'):
        species.language = data['language']

    return species


def create_starship(data):
    """Creates a < Starship > instance from dictionary data, converting string values to the
    appropriate type whenever possible. Assigning crews and passengers consitute separate
    operations.

    Type conversions:
        length (str->float)
        max_atmosphering_speed (str->int)
        hyperdrive_rating (str->float)
        MGLT (str->int)
        armament (str->list)
        crew (str->int)
        passengers (str->int)
        cargo_capacity (str->int)

    Parameters:
        data (dict): source data

    Returns:
        starship: a new < Starship > instance
    """

    starship = Starship(data['url'], data['name'], data['model'], data['starship_class'])

    if data.get('manufacturer'):
        starship.manufacturer = data['manufacturer']

    if data.get('length'):
        starship.length = float(data['length'])

    if data.get('max_atmosphering_speed'):
        starship.max_atmosphering_speed = int(data['max_atmosphering_speed'])

    if data.get('hyperdrive_rating'):
        starship.hyperdrive_rating = float(data['hyperdrive_rating'])

    if data.get('MGLT'):
        starship.MGLT = int(data['MGLT'])

    if data.get('armament'):
        starship.armament = data['armament'].split(',')

    if data.get('crew'):
        starship.crew = int(data['crew'])

    if data.get('passengers'):
        starship.passengers = int(data['passengers'])

    if data.get('cargo_capacity'):
        starship.cargo_capacity = int(data['cargo_capacity'])

    if data.get('consumables'):
        starship.consumables = data['consumables']

    return starship


def create_cache_item_id(url, params):
    # synthetic key
    pattern = ''
    if params:
        for key, val in params.items():
            pattern += '|' + str(key) + '-' + str(val)
            # f": {str(key)} - {str(val)}"
        url += pattern
        return url
    else:
        return url


def get_cache(filepath):

    try:
        return read_json(filepath)
    except:
        return {}


def get_swapi_resource(filepath, url, params=None, timeout=10):
    """Returns a response object decoded into a dictionary. If query string < params > are
    provide the response object body is in the form on an "envelope" with the data payload of
    one or more SWAPI entities to be found in ['results'] list; otherwise, response object
    body is returned as a single dictionary representation of the SWAPI entity.

    Parameters:
        filepath (str): the path to the cache file.
        url (str): a url that specifies the resource.
        params (dict): optional dictionary of querystring arguments.
        timeout (int): timeout value in seconds

    Returns:
        dict: dictionary representation of the decoded JSON.
    """

    swapi_cache = get_cache(filepath)
    cache_item_id = create_cache_item_id(url, params)
    print(cache_item_id)
    if cache_item_id in swapi_cache.keys():
        return swapi_cache[cache_item_id]
    else:
        if params:
            response = requests.get(url, params, timeout=timeout).json()
            data = response['results'][0] # assume only one record
        else:
            data = requests.get(url, timeout=timeout).json()

        swapi_cache[cache_item_id] = data
        write_json(filepath, swapi_cache)
        return data


def read_csv_into_dicts(filepath, delimiter=','):
    """Accepts a file path, creates a file object, and returns a list of
    dictionaries that represent the row values using the cvs.DictReader().

    Parameters:
        filepath (str): path to file
        delimiter (str): delimiter that overrides the default delimiter

    Returns:
        list: nested dictionaries representing the file contents
     """

    with open(filepath, 'r', newline='', encoding='utf-8') as file_obj:
        data = []
        reader = csv.DictReader(file_obj, delimiter=delimiter)
        for line in reader:
            data.append(line) # OrderedDict()
            # data.append(dict(line)) # convert OrderedDict() to dict

        return data


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
    """Entry point for program."""

    endpoint = 'https://swapi.py4e.com/api'

    # ABSOLUTE PATH (VS CODE DEBUGGER-FRIENDLY)
    # WARN: autograder does not require absolute paths
    # abs_path = os.path.dirname(os.path.abspath(__file__))
    # print(f"\n0.0: Absolute directory path = {abs_path}")

    # Example: absolute filepath (create)
    # filepath = os.path.join(abs_path, 'stu_swapi_species_wookiee.json')

    # Example: relative filepath
    # filepath = 'stu_swapi_species_wookiee.json'


    # CHALLENGE 01 UTILITY FUNCTIONS / INHABITED PLANETS

    # Implement utility functions per README.md

    swapi_planets_data = read_json('swapi_planets.json')

    inhabited_planets = []
    for planet in swapi_planets_data:
        if planet['population'] != 'unknown' and int(planet['population']) > 10000:
            inhabited_planets.append(
                {
                    'url': planet['url'],
                    'name': planet['name'],
                    'population': int(planet['population'])
                }
            )

    # 39 planets returned
    # print(f"Challenge 01: inhabited planets (pop. > 10000) = {len(inhabited_planets)}")

    # filepath = os.path.join(abs_path, 'stu_swapi_inhabited_planets.json')
    filepath = 'stu_swapi_inhabited_planets.json'
    write_json(filepath, inhabited_planets)

    # CHALLENGE 02 SPECIES
    wookiee_data = get_swapi_resource(CACHE_NAME, f"{endpoint}/species", {'search': 'wookiee'})
    wookiee = create_species(wookiee_data)

    # filepath = os.path.join(abs_path, 'stu_swapi_species_wookiee.json')
    filepath = 'stu_swapi_species_wookiee.json'
    write_json(filepath, wookiee.jsonable())


    # CHALLENGE 03 PLANET
    hoth_data = get_swapi_resource(CACHE_NAME, f"{endpoint}/planets", {'search': 'hoth'})

    # filepath = os.path.join(abs_path, 'wookieepedia_planets.csv')
    filepath = 'wookieepedia_planets.csv'
    wookiee_planets = read_csv_into_dicts(filepath)

    hoth_data.update(wookiee_planets[5]) # combine
    hoth = create_planet(hoth_data) # instance

    # filepath = os.path.join(abs_path, 'stu_swapi_planet_hoth.json')
    filepath = 'stu_swapi_planet_hoth.json'
    write_json(filepath, hoth.jsonable())


    # CHALLENGE 04 DROID
    r2_d2_data = get_swapi_resource(CACHE_NAME, f"{endpoint}/people", {'search': 'r2-d2'})

    # filepath = os.path.join(abs_path, 'wookieepedia_droids.json')
    filepath = 'wookieepedia_droids.json'
    wookiee_droids = read_json(filepath)

    r2_d2_data.update(wookiee_droids[-1]) # combine
    r2_d2 = create_droid(r2_d2_data) # instance

    # filepath = os.path.join(abs_path, 'stu_swapi_droid_r2_d2.json')
    filepath = 'stu_swapi_droid_r2_d2.json'
    write_json(filepath, r2_d2.jsonable())


    # CHALLENGE 05 PERSON
    leia_data = get_swapi_resource(CACHE_NAME, f"{endpoint}/people", {'search': 'leia organa'})

    # filepath = os.path.join(abs_path, 'wookieepedia_people.json')
    filepath = 'wookieepedia_people.json'
    wookiee_people = read_json(filepath)

    leia_data.update(wookiee_people[4]) # combine
    leia = create_person(leia_data, wookiee_planets) # instance

    # filepath = os.path.join(abs_path, 'stu_swapi_person_leia.json')
    filepath = 'stu_swapi_person_leia.json'
    write_json(filepath, leia.jsonable())


    # CHALLENGE 06 PASSENGERS

    # Implement the Passengers class


    # CHALLENGE 07 STARSHIP
    x_wing_data = get_swapi_resource(CACHE_NAME, f"{endpoint}/starships", {'search': 'T-70 x-wing'})

    # filepath = os.path.join(abs_path, 'wookieepedia_starships.csv')
    filepath = 'wookieepedia_starships.csv'
    wookiee_starships = read_csv_into_dicts(filepath)

    x_wing_data.update(wookiee_starships[1]) # combine
    x_wing = create_starship(x_wing_data) # instance

    # filepath = os.path.join(abs_path, 'stu_swapi_starship_x_wing.json')
    filepath = 'stu_swapi_starship_x_wing.json'
    write_json(filepath, x_wing.jsonable())


    # CHALLENGE 08 MISSION TO JAKKU
    poe_data = get_swapi_resource(CACHE_NAME, f"{endpoint}/people", {'search': 'poe'})
    poe_data.update(wookiee_people[7])
    poe = create_person(poe_data, wookiee_planets)

    bb8_data = get_swapi_resource(CACHE_NAME, f"{endpoint}/people", {'search': 'bb8'})
    bb8_data.update(wookiee_droids[0])
    bb8 = create_droid(bb8_data)

    # Special instructions: get Jakku data and clean
    jakku_data = get_swapi_resource(CACHE_NAME, f"{endpoint}/planets", {'search': 'jakku'})
    jakku_data.update(wookiee_planets[7])
    jakku = create_planet(jakku_data)

    # Create "flight_plan" instructions (nested dict) and store in BB8
    flight_plan = {
        'flight_plan': {
            'destination': jakku.jsonable(), # dict representation
            'hyperspace_route': "Burke's Trailing",
            'year': "34 ABY"
            }
        }

    # Store flight plan
    bb8.store_instructions(flight_plan)

    # Create "locate_person" Lor San Tekka instructions (nested dict)
    lor_data = wookiee_people[6]
    lor = create_person(lor_data, wookiee_planets)

    # Create locate_person dict and store instructions
    bb8.store_instructions({'locate_person': lor.jsonable()})

    x_wing_crew = Crew({'pilot': poe, 'astro_mech_droid': bb8})
    x_wing.assign_crew_members(x_wing_crew)

    # filepath = os.path.join(abs_path, 'stu_episode_vii_mission_jakku.json')
    filepath = 'stu_episode_vii_mission_jakku.json'
    write_json(filepath, x_wing.jsonable())


    # CHALLENGE 09 STAR MAP (ATTACK ON TUANUL)
    # filepath = os.path.join(abs_path, 'wookieepedia_star_map.json')
    filepath = 'wookieepedia_star_map.json'
    wookiee_star_map = read_json(filepath)

    # Create map dict and store
    bb8.store_instructions({'star_map': wookiee_star_map})

    # filepath = os.path.join(abs_path, 'stu_episode_vii_star_map.json')
    filepath = 'stu_episode_vii_star_map.json'
    write_json(filepath, bb8.jsonable())


    # CHALLENGE 10 ESCAPE FROM JAKKU
    rey_data = get_swapi_resource(CACHE_NAME, f"{endpoint}/people", {'search': 'rey'})
    rey_data.update(wookiee_people[-1])
    rey = create_person(rey_data, wookiee_planets)

    finn_data = get_swapi_resource(CACHE_NAME, f"{endpoint}/people", {'search': 'finn'})
    finn_data.update(wookiee_people[1])
    finn = create_person(finn_data, wookiee_planets)

    m_falcon_data = get_swapi_resource(CACHE_NAME, f"{endpoint}/starships", {'search': 'falcon'})
    m_falcon_data.update(wookiee_starships[-1])
    m_falcon = create_starship(m_falcon_data)

    # Assign crew
    m_falcon_crew = Crew({'pilot': rey, 'gunner': finn})
    m_falcon.assign_crew_members(m_falcon_crew)

    # Assign passengers
    m_falcon_passengers = Passengers([bb8])
    m_falcon.add_passengers(m_falcon_passengers)

    # filepath = os.path.join(abs_path, 'stu_episode_vii_escape_jakku.json')
    filepath = 'stu_episode_vii_escape_jakku.json'
    write_json(filepath, m_falcon.jsonable())


    # CHALLENGE 11 JOURNEY TO TAKODANA
    han_solo_data = get_swapi_resource(CACHE_NAME, f"{endpoint}/people", {'search': 'han solo'})
    han_solo_data.update(wookiee_people[2])
    han_solo = create_person(han_solo_data, wookiee_planets)

    chewie_data = get_swapi_resource(CACHE_NAME, f"{endpoint}/people", {'search': 'chewbacca'})
    chewie_data.update(wookiee_people[0])
    chewie = create_person(chewie_data, wookiee_planets)

    # Reassign crew
    m_falcon_crew = Crew({'pilot': han_solo, 'copilot': chewie})
    m_falcon.assign_crew_members(m_falcon_crew)

    # Reassign passengers
    m_falcon_passengers = Passengers([rey, finn, bb8])
    m_falcon.add_passengers(m_falcon_passengers)

    # filepath = os.path.join(abs_path, 'stu_episode_vii_journey_takodana.json')
    filepath = 'stu_episode_vii_journey_takodana.json'
    write_json(filepath, m_falcon.jsonable())


if __name__ == '__main__':
    main()

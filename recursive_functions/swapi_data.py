import json
import logging
import os
import requests

FILE_PATH = os.path.dirname(os.path.abspath(__file__))  # Windows friendly
ENDPOINT = 'https://swapi.py4e.com/api'
OUTPUT_DIR = 'swapi_data/'

SWAPI = {
    'films': (
        'https://swapi.py4e.com/api/films/',
        'swapi_films_paged.json',
        'swapi_films.json'
    ),
     'people': (
         'https://swapi.py4e.com/api/people/',
         'swapi_people_paged.json',
         'swapi_people.json'
     ),
     'planets': (
         'https://swapi.py4e.com/api/planets/',
         'swapi_planets_paged.json',
         'swapi_planets.json'
     ),
     'species': (
         'https://swapi.py4e.com/api/species/',
         'swapi_species_paged.json',
         'swapi_species.json'
     ),
     'starships': (
         'https://swapi.py4e.com/api/starships/',
         'swapi_starships_paged.json',
         'swapi_starships.json'
     ),
     'vehicles': (
         'https://swapi.py4e.com/api/vehicles/',
         'swapi_vehicles_paged.json',
         'swapi_vehicles.json'
     )
}


def get_records_recursively(uri, records=[], paged=False):
    """Returns list of resources acquired recursively. Calls get_resource_json(uri) to return a
    representation of the resource.  State is maintained internally by passing the records list
    back to the function whenever it is called. Records can be returned either as a paged object or
    as a collection of the individual entities that comprise the page.

    Parameters:
        uri (str): a url that specifies the resource.
        records (list): collection of paged or entity resources.
        paged: (bool): optional flag that how the response is to be returned.

    Return:
        list: collection of paged or entity resources.
    """

    response = get_resource_json(uri)

    if paged:
        logging.info("{} paged appended to list".format(uri))
        records.append(response)
    else:
        logging.info("{} entities added to list".format(uri))
        records.extend(response['results'])

    if response['next'] is None:
        return records
    else:
        return get_records_recursively(response['next'], records, paged)


def get_resource_json(url, params=None):
    """Issues an HTTP GET request to return a representation of a resource.
    If no category is provided, the root resource will be returned. An optional
    querystring of key:value pairs may be provided as search terms. If a match is
    achieved the JSON object that is returned will include a list property named
    'results' that contains the resource(s) matched by the search query.

    Parameters:
        url (str): a url that specifies the resource.
        params (dict): optional dictionary of querystring arguments (e.g., {'search': 'yoda'}).

    Returns:
        dict: dictionary representation of the decoded JSON.
    """

    if params:
        response = requests.get(url, params=params).json()
    else:
        response = requests.get(url).json()

    return response


def get_resource_json_by_id(url):
    """Given a url that specifies a known resource identifier (e.g., '/people/1/')
    issue an HTTP GET request to return a representation of a resource. This function
    calls get_resource_json() passing to it only the url. A representation of the resource
    itself will be returned rather than an object that nests the resource in a 'results' list.

    Parameters:
        url (str): a url that specifies the resource's identifier (e.g., '/people/10/')

    Returns:
        dict: dictionary representation of the decoded JSON.
    """
    response = get_resource_json(url)

    return response


def write_json(path, data):
    """Write dictionary to JSON file. The built-in open() function optional parameter
    value encoding='utf-8-sig' also works.

    Parameters:
        path (str): the file path.
        data (dict): the data to be encoded as JSON and written to the file.

    Returns:
        None
    """

    with open(path, 'w', encoding='utf8') as file_obj:
        json.dump(data, file_obj, ensure_ascii=False, indent=2)


def main():
    """Entry point to program. Retrieve all swapi_x data.  Write out as
    JSON to file named after the categories.

    Parameters:
        None

    Returns:
        None
    """

    # Setting logging format and default level
    logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)

    # Get swapi_x paged data
    logging.info("START: get paged data")
    for val in SWAPI.values():
        records = get_records_recursively(val[0], [], True)
        path = os.path.join(FILE_PATH, OUTPUT_DIR, val[1])  # Windows friendly
        write_json(path, records)
    logging.info("END: get paged data")

    # Get swapi_x entity data
    logging.info("START: get entity data")
    for val in SWAPI.values():
        records = get_records_recursively(val[0], [])
        path = os.path.join(FILE_PATH, OUTPUT_DIR, val[2])  # Windows friendly
        write_json(path, records)
    logging.info("END: get entity data")


if __name__ == '__main__':
    main()

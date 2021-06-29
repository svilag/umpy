import os
import string


def main():
    """Entry point for program. Orchestrates workflow."""

    # abs_path = os.path.dirname(os.path.abspath(__file__))
    # print(f"\n0.0: Absolute directory path = {abs_path}")

    # CHANGE FILE NAMES
    # filepath = os.path.join(abs_path, 'input', 'swapi_planets.json')
    # filepath = './input/swapi_planets.json'
    # swapi_planets = read_json(filepath)


    # CHALLENGE 01: LIST OF TUPLES TO DICT

    data = [
        ('Benin', 'BEN'),
        ('Burkina Faso', 'BFA'),
        ('Cabo Verde', 'CPV'),
        ("Cote d'Ivoire", 'CIV'),
        ('Gambia', 'GMB'),
        ('Ghana', 'GHA'),
        ('Guinea', 'GIN'),
        ('Guinea-Bissau', 'GNB'),
        ('Liberia', 'LBR'),
        ('Mali', 'MLI'),
        ('Mauritania', 'MRT'),
        ('Niger', 'NER'),
        ('Nigeria', 'NGA'),
        ('Saint Helena', 'SHN'),
        ('Senegal', 'SEN'),
        ('Sierra Leone', 'SLE'),
        ('Togo', 'TGO')
    ]

    country_codes = {t[0] : t[1] for t in data}

    print(f"\nChallenge 01: list to dict = {country_codes}")


    # CHALLENGE 02: DICT TO NEW DICT COMPUTE NEW VALUE

    # https://www.statista.com/statistics/244983/projected-inflation-rate-in-the-united-states/

    data = {
        '2020': 0.0125,
        '2019': 0.0181,
        '2018': 0.024399999999999998,
        '2017': 0.0213,
        '2016': 0.0126,
        '2015': 0.0012,
        '2014': 0.016200000000000003,
        '2013': 0.0146,
        '2012': 0.0207,
        '2011': 0.0316,
        '2010': 0.016399999999999998,
        '2009': -0.0036,
        '2008': 0.0384,
        '2007': 0.0285,
        '2006': 0.0323,
        '2005': 0.0339,
        '2004': 0.0268,
        '2003': 0.0227,
        '2002': 0.0159,
        '2001': 0.028300000000000002,
        '2000': 0.0338
    }

    inflation_rates = {key : round(value * 100, 2) for key, value in data.items()}

    print(f"\nChallenge 02: US inflation rates = {inflation_rates}")


    # CHALLENGE 03: DICT TO DICT (SUBSET WITH IF)

    inflation_rates = {key : val for key, val in inflation_rates.items() if int(key) >= 2010}

    print(f"\nChallenge 03: US inflation rates 2010-2020 = {inflation_rates}")


    # CHALLENGE 04: NUMBERED DIRECTIONS WITH ENUMERATE()

    # Recall that a list is ordered
    data = [
        ['Head north on S State St toward E Washington St.', 0.1],
        ['Turn left at the 2nd cross street onto E Huron St.', 1.3],
        ['Continue onto I-94BL N/Jackson Ave.', 0.9],
        ['Turn right to merge onto I-94 W toward Jackson.', 0.2],
        ['Merge onto I-94 W', 31.9],
        ['Take exit 139 for M-106/Cooper St toward Downtown Jackson.', 0.4],
        ['At the traffic circle, take the 2nd exit onto M-106 S/Cooper St.', 0.2],
        ['At the traffic circle, continue straight onto Cooper St.', 1.0],
        ['Turn right onto Martin Luther King Jr Dr/N M.L.K. Jr Dr.', 0.6],
        ['Turn right onto E Michigan Ave.', 0.1],
        ['Turn right at 1st cross street onto N Mechanic St. Destination on left', 0.0359],
    ]

    directions = {

        str(i) : {'segment' : row[0], 'distance_mi' : row[1]}
        for i, row in enumerate(data, 1)
    }

    print(f"\nChallenge 04: numbered directions = {directions}")


    # CHALLENGE 05: NEW DICT INNER PLANETS ONLY

    data = {
        "mercury" : {'category': 'inner', 'satellites': 0},
        "venus" : {'category': 'inner', 'satellites': 0},
        "earth" : {'category': 'inner', 'satellites': 1},
        "mars" : {'category': 'inner', 'satellites': 2},
        "jupiter" : {'category': 'outer', 'satellites': 79},
        "saturn" : {'category': 'outer', 'satellites': 82},
        "uranus" : {'category': 'outer', 'satellites': 27},
        "neptune" : {'category': 'outer', 'satellites': 14}
    }

    inner_planets = {key : val for key, val in data.items() if val['category'] == 'inner'}

    print(f"\nChallenge 05: inner planets = {inner_planets}")


    # CHALLENGE 06: NEW DICT OUTER PLANETS WITH 10-30 SATELLITES (INCLUSIVE)

    outer_planets = {
        key : val for key, val in data.items()
        if val['category'] == 'outer'
        and 10 <= val['satellites'] <= 30
    }

    print(f"\nChallenge 06: Outer planets 10-30 satellites = {outer_planets}")


    # CHALLENGE 07: NEW DICT IF-ELSE

    planet_types = {
        key : ('terrestrial' if val['category'] == 'inner' else 'jovian')
        for key, val in data.items()
    }

    print(f"\n Challenge 07: planet types if-else = {planet_types}")


    # CHALLENGE 08: WORD FREQUENCIES

    # Amanda Gorman, The Hill We Climb (2020), excerpt.
    # https://en.wikipedia.org/wiki/The_Hill_We_Climb

    data = """
    When day comes we ask ourselves, where can we find light in this never-ending shade?
    The loss we carry, a sea we must wade.
    We’ve braved the belly of the beast, we’ve learned that quiet isn’t always peace and the norms and notions of what just is, isn’t always justice.
    And yet the dawn is ours before we knew it, somehow we do it, somehow we’ve weathered and witnessed a nation that isn’t broken but simply unfinished.
    We, the successors of a country and a time where a skinny black girl descended from slaves and raised by a single mother can dream of becoming president only to find herself reciting for one.
    And, yes, we are far from polished, far from pristine, but that doesn’t mean we are striving to form a union that is perfect, we are striving to forge a union with purpose, to compose a country committed to all cultures, colors, characters and conditions of man.
    So we lift our gazes not to what stands between us, but what stands before us.
    We close the divide because we know to put our future first, we must first put our differences aside.
    We lay down our arms so we can reach out our arms to one another, we seek harm to none and harmony for all.
    Let the globe, if nothing else, say this is true: that even as we grieved, we grew, even as we hurt, we hoped, that even as we tired, we tried, that we’ll forever be tied together victorious, not because we will never again know defeat but because we will never again sow division.
    """

    # Remove punctuation (import string module)
    data_cleaned = data.translate(str.maketrans('','', string.punctuation)) # remove punctuation
    data_cleaned = data_cleaned.lower()

    word_counts = {}
    for word in data_cleaned.split():
        if word not in word_counts.keys():
            word_counts[word] = 1
        else:
            word_counts[word] += 1


    print(f"\nChallenge 08: word count loop (we) = {word_counts['we']}")

    word_counts = {}
    for word in data_cleaned.split():
        word_counts[word] = word_counts.get(word, 0) + 1

    print(f"\nChallenge 08: word count loop (we) = {word_counts['we']}")

    # print(f"\nChallenge 08: word count loop = {word_counts}")

    # Unlike a list a set is unordered and cannot include multiple occurences of the same value
    word_counts = {
        word: data_cleaned.split().count(word)
        for word in set(data_cleaned.split())
    }

    print(f"\nChallenge 08: word count comp (we) = {word_counts['we']}")

    # print(f"\nChallenge 08: word count comp = {word_counts}")


if __name__ == '__main__':
    main()
import operator
import umpy_utils as umpy


def sort_region_by_score_desc(country):
    """Convert score to a negative value."""
    return (country[1], -float(country[2]), country[0])


def main():
    """Entry point to program."""

    # WARMUP: SORTED()

    countries = [
        ('Lesotho', 'LSO'),
        ('South Africa', 'ZAF'),
        ('Botswana', 'BWA'),
        ('Eswatini', 'SWZ'),
        ('Namibia', 'NAM')
        ]

    southern_africa = sorted(countries)
    print(f"\nWARM UP: southern_africa, default sort = {southern_africa}")

    southern_africa = sorted(countries, key=lambda x: x[1])

    print(f"\nWARM UP: southern_africa, ISO Alpha3 code sort = {southern_africa}")

    southern_africa = sorted(countries, key=lambda x: x[1], reverse=True)

    print(f"\nWARM UP: southern_africa, ISO Alpha3 code sort (reversed) = {southern_africa}")


    # WARMUP: LIST.SORT()

    central_america = [
        ('Nicaragua', 'NIC', 6.105),
        ('El Salvador', 'SLV', 6.253),
        ('Honduras', 'HND', 5.860),
        ('Costa Rica', 'CRI', 7.167),
        ('Mexico', 'MEX', 6.595),
        ('Belize', 'BLZ', 0.0),
        ('Panama', 'PAN', 6.321),
        ('Guatemala', 'GTM', 6.436)
    ]

    central_america.sort(key=lambda y: y[-1], reverse=True) # TODO Implement
    print(f"\nWARM UP: Central America, happiness score (reversed) = {central_america}")


    # CHALLENGE 01: DATA RETRIEVAL

    # Read
    input_path = './input/happiness-shuffled-unranked-2019.csv'
    data = umpy.read_csv(input_path) # TODO Implement
    # print(data[1])

    # Extract headers and countries
    headers = data[0] # TODO Implement
    print(f"\nCHALLENGE 01: Happiness headers = {headers}")

    countries = data[1:] # TODO Implement
    print(f"\nCHALLENGE 01: Countries random (limit=10) = {countries[:10]}")

    # CHALLENGE 02: SORT()

    # Lexicographic sort
    # countries.sort() # in place operation, sorted lexicographically, returns None
    printable = countries.sort() # TODO Implement
    printable = [(country[0], country[2]) for country in countries[:10]]
    print(f"\nCHALLENGE 02 .SORT(): countries default sort() asc = {printable}")


    # CHALLENGE 03: SORT() WITH LAMBDA KEY

    # Lexicographic sort
    countries = data[1:] # reset
    countries.sort(key=lambda x: x[2]) # sort on happiness score
    printable = [(country[0], country[2]) for country in countries[:10]] # TODO Implement
    print(f"\nCHALLENGE 03: countries score asc = {printable}")

    # CHALLENGE 04: SORT() WITH LAMBDA KEY, REVERSE ORDER

    # Numeric sort
    countries = data[1:] # reset
    countries.sort(key=lambda x: float(x[2]), reverse=True)
    printable = [(country[0], country[2]) for country in countries[:10]] # TODO Implement
    print(f"\nCHALLENGE 04: countries score desc float = {printable}")

    # Lexicographic sort (no float conversion)
    # countries = data[1:] # reset
    # countries.sort(key=lambda x: x[])
    # printable = [(country[0], country[2]) for country in countries[:10]] # TODO Implement
    # print(f"\nCHALLENGE 04: countries score desc lexicographic = {printable}")

    # Alternative (operator.itemgetter())
    countries = data[1:] # reset
    countries.sort(key=operator.itemgetter(2), reverse=True)
    printable = [(country[0], country[2]) for country in countries[:10]] # TODO Implement
    print(f"\n.CHALLENGE 04: countries score desc itemgetter = {printable}")


    # CHALLENGE 05 SORTED() SOCIAL SUPPORT

    # SORTED (NEW LIST) SOCIAL SUPPORT
    # countries = data[1:] # reset
    # countries = sorted(countries, key=lambda x: x[4], reverse=True)
    # printable = [(country[0], country[2]) for country in countries[:10]] # TODO Implement
    # print(f"\nCHALLENGE 05: Countries rank desc = {printable}")

    # Alternative
    # countries = data[1:] # reset
    # countries = sorted(?)
    # printable = None # TODO Implement
    # print(f"\nCHALLENGE 05: countries rank desc itemgetter = {printable}")


    # CHALLENGE 06: SORT MULTIPLE COLUMNS

    # SORTED (NEW LIST) REGION, SCORE, COUNTRY ASCENDING ALL KEYS
    countries = data[1:] # reset
    countries = sorted(countries, key=lambda x: (x[1], float(x[2]), x[0])) # tuple of values
    writable = [
        (country[1], country[0], country[2])
        for country in countries
        if 'Europe' in country[1]
    ]
    output_path = './output/europe-happiness.csv'
    umpy.write_csv(output_path, writable, ('Country', 'Region', 'Score'))


    # CHALLENGE 07: SORT MULTIPLE COLUMNS, REVERSE ORDER SCORE

    # SORTED (NEW LIST) REGION, SCORE, COUNTRY MIXED ORDERING
    countries = data[1:] # reset
    countries = sorted(countries, key=lambda x: (x[1], float(x[2]), x[0]), reverse=True) # negative value (sorting hack)
    writable = [
        (country[1], country[0], country[2])
        for country in countries
        if country[1] == 'Sub-Saharan Africa'
    ]
    output_path = './output/africa-happiness.csv'
    umpy.write_csv(output_path, writable, ('Country', 'Region', 'Score'))

    # Alternative: local function
    countries = data[1:] # reset
    # countries = sorted(countries, key=sort_region_by_score_desc) # reference function name
    countries = sorted(countries, key=lambda x: -float(x[2])) # reference function name
    writable = [
        (country[1], country[0], country[2])
        for country in countries
        if country[1] == 'Eastern Asia'
    ] # TODO Implement
    output_path = './output/east_asia-happiness.csv'
    umpy.write_csv(output_path, writable, ('Country', 'Region', 'Score'))


    # CHALLENGE 08: BONUS ADD RANK

    # Add ranking write out all values
    countries = data[1:] # reset
    countries = sorted(countries, key=lambda x: float(x[2]), reverse=True) # negative value (sorting hack)

    rankings = []
    for i, country in enumerate(countries, 1):
        country.insert(0, i)
        rankings.append(country)

    # headers.insert(0, 'Rank') # Don't mutate headers
    output_path = './output/world_rank-happiness-loop.csv'
    umpy.write_csv(output_path, rankings, ['Rank'] + headers)

    # Warn: country.insert(0, i) and [i].extend(country) not appropriate in a comprehension
    # Both methods return None and trigger a runtime error when the list is passed to write_csv().
    # _csv.Error: iterable expected, not NoneType

    # writable = [country.insert(0, i) for i, country in enumerate(countries, 1)]
    # writable = [[i].extend(country) for i, country in enumerate(countries, 1)]

    writable = None # TODO Implement
    output_path = './output/world_rank-happiness.csv'
    # umpy.write_csv(output_path, writable, ['Rank'] + headers)


if __name__ == "__main__":
    main()

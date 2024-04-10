from pprint import pprint
from itertools import combinations

from thefuzz import fuzz
from thefuzz import process

defendant_template = {
    'last_name': '',
    'first_name': '',
    'dob': '',
    'alias': '',
    'offender_tracking_number': '',
}

def parsing_fun(some_records: list[dict]):

    aliasys = []
    probably_real_people = []

    for record in some_records:
        for element in record:
            if record[element].upper() == 'N/A':
                record[element] = ''
        if record['alias'] == 'Y':
            aliasys.append(record)
        else:
            record['aliases'] = []
            probably_real_people.append(record)

    if len(probably_real_people) == 1:
        probably_real_people[0]['aliases'] = aliasys
    else:

        aliasys = [alias for alias in aliasys if not filter_obvius(probably_real_people, alias)]
        aliasys = [alias for alias in aliasys if not filter_by_name_and_date_similarity(probably_real_people, alias)]

        filtered_people, filtered_aliasys = search_for_aliases_in_people(probably_real_people)

        probably_real_people = filtered_people
        aliasys.extend(filtered_aliasys)

    alias_count = 0
    for person in probably_real_people:
        alias_count += len(person["aliases"])
    
    if (alias_count + len(probably_real_people)) != len(some_records):
        raise RuntimeError(f"problem with searching aliasys {len(aliasys)=} {len(probably_real_people)=} {len(some_records)=}")
    return probably_real_people

def filter_obvius(people, alias):
    for person in people:
            if alias['offender_tracking_number'] and alias['offender_tracking_number'] == person['offender_tracking_number']:
                person['aliases'].append(alias)
                return True
    return False

def filter_by_name_and_date_similarity(people, alias):
    highest_score_person = [0, None]
    alias_name = f"{alias['first_name']} {alias['last_name']} {alias['dob']}"
    for person in people:
        perrson_name = f"{person['first_name']} {person['last_name']} {person['dob']}"
        ration = fuzz.ratio(alias_name, perrson_name)
        if ration > highest_score_person[0]:
            highest_score_person = [ration, perrson_name]

    if highest_score_person[0] > 70:
        highest_score_person[1]['aliases'].append(alias)
        return True
    elif highest_score_person[1]:
        perrson_name = f"{' '.join(person['first_name'].split(' ')[:-1])} {person['last_name']} {person['dob']}"
        if fuzz.ratio(alias_name, perrson_name) > 85:
            highest_score_person[1]['aliases'].append(alias)
            return True 
    return False

def search_for_aliases_in_people(people):
    print("*" * 100)
    probably_alias = []
    for person1, person2 in combinations(people, 2):
        perrson1_name = f"{person1['first_name']} {person1['last_name']} {person1['dob']}"
        perrson2_name = f"{person2['first_name']} {person2['last_name']} {person2['dob']}"
        if person1['offender_tracking_number'] and person1['offender_tracking_number'] == person2['offender_tracking_number']:
            if len(perrson1_name) > len(perrson2_name):
                person1['aliases'].append(person2)
                probably_alias.append(person2)
                continue
            elif len(perrson1_name) < len(perrson2_name):
                person2['aliases'].append(person1)
                probably_alias.append(person1)
                continue

        if fuzz.ratio(perrson1_name, perrson2_name) > 70:
            if len(person1['first_name']) > len(person2['first_name']):
                person1['aliases'].append(person2)
                probably_alias.append(person2)
                continue
            elif len(person1['first_name']) < len(person2['first_name']):
                person2['aliases'].append(person1)
                probably_alias.append(person1)
                continue

        print("No match ", perrson1_name, perrson2_name, fuzz.ratio(perrson1_name, perrson2_name))

    more_probably_people = [person for person in people if person not in probably_alias]
    print("*" * 100)
    return more_probably_people, probably_alias


def main() -> None:
    print(f'Hello main from : {__file__}')
    x = "GONZALEZ COLBY ALEXANDER"
    y = "GONZALEZ COLBY"

    # names = ["AGUILAR RENE GARCIA", "GONZALEZ COLBY", "GONZALEZ COLBY ALEXANDER"]
    # for name_pair in combinations(names, 2):
    #     print(name_pair, fuzz.ratio(name_pair[0], name_pair[1]))


    records_1 = [
        {
            'last_name': 'GONZALEZ',
            'first_name': 'COLBY ALEXANDER',
            'dob': '1986',
            'alias': '',
            'offender_tracking_number': 'N/A',
        },
        {
            'last_name': 'AGUILAR',
            'first_name': 'RENE',
            'dob': '1978',
            'alias': 'Y',
            'offender_tracking_number': 'OCZ35501',
        },
        {
            'last_name': 'AGUILAR',
            'first_name': 'RENE GARCIA',
            'dob': '1978',
            'alias': '',
            'offender_tracking_number': 'OCZ35501',
        },
        {
            'last_name': 'GONZALEZ',
            'first_name': 'COLBY',
            'dob': '1986',
            'alias': '',
            'offender_tracking_number': 'OCZ35502',
        },
    ]

    records_2 = [
        {
            'last_name': 'AGUILAR',
            'first_name': 'RAQUEL',
            'dob': '1994',
            'alias': '',
            'offender_tracking_number': 'N/A',
        },
        {
            'last_name': 'BARRIOS',
            'first_name': 'KATIA D',
            'dob': '1993',
            'alias': 'Y',
            'offender_tracking_number': 'N/A',
        },
        {
            'last_name': 'BARRIOS',
            'first_name': 'KATIA RAQUEL',
            'dob': '1993',
            'alias': 'Y',
            'offender_tracking_number': 'N/A',
        },
        {
            'last_name': 'DUARTE-BARRIOS',
            'first_name': 'KATIA',
            'dob': '1993',
            'alias': 'Y',
            'offender_tracking_number': 'N/A',
        },
    ]

    records_3 = [
        {
            'last_name': 'MEDRANO',
            'first_name': 'RUEBEN ANTHONY',
            'dob': '1995',
            'alias': '',
            'offender_tracking_number': 'N/A',
        },
        {
            'last_name': 'ALVARADO',
            'first_name': 'CHEYENNE MARIE',
            'dob': '2000',
            'alias': '',
            'offender_tracking_number': 'OCZ46101',
        },
        {
            'last_name': 'MEDRANO',
            'first_name': 'RUEBEN A',
            'dob': '',
            'alias': '',
            'offender_tracking_number': 'OCZ46102',
        },
    ]

    records_4 = [
        {
            'last_name': 'AKBAR',
            'first_name': 'KEENAN IMAN',
            'dob': '1996',
            'alias': 'Y',
            'offender_tracking_number': 'AFE77001',
        },
        {
            'last_name': 'AKBAR',
            'first_name': 'KEENAN IMON',
            'dob': '1996',
            'alias': '',
            'offender_tracking_number': 'AFE77001',
        },
        {
            'last_name': 'WILSON',
            'first_name': 'LARRY RONDELL',
            'dob': '1997',
            'alias': '',
            'offender_tracking_number': 'AFE77002',
        },
    ]
    records_5 = [
        {
            'last_name': 'AHMED',
            'first_name': 'ALI MOHAMMED',
            'dob': '1995',
            'alias': 'Y',
            'offender_tracking_number': 'MCD43602',
        },
        {
            'last_name': 'AHMED',
            'first_name': 'SHUAIB MOHAMMED',
            'dob': '1995',
            'alias': '',
            'offender_tracking_number': 'MCD43601',
        },
        {
            'last_name': 'AHMED',
            'first_name': 'SHUAIB MOHAMMED',
            'dob': '1995',
            'alias': '',
            'offender_tracking_number': 'MCD43602',
        },
    ]
    records_6 = [
        {
            'last_name': 'ACEVEDO',
            'first_name': 'JOE DONAIRE',
            'dob': '2004',
            'alias': '',
            'offender_tracking_number': 'OCZ21901',
        },
        {
            'last_name': 'ARANEDAPOGGE',
            'first_name': 'ROMAI JULIE',
            'dob': '1987',
            'alias': '',
            'offender_tracking_number': 'OCZ21902',
        },
        {
            'last_name': 'TAPIA',
            'first_name': 'CHRISTIAN',
            'dob': '1985',
            'alias': '',
            'offender_tracking_number': 'OCZ21903',
        },
    ]
    records_7 = [
        {
            'last_name': 'ACOSTA',
            'first_name': 'DELIA',
            'dob': '1982',
            'alias': '',
            'offender_tracking_number': 'BCM22101',
        },
        {
            'last_name': 'RAY',
            'first_name': 'ALEXIS',
            'dob': '1999',
            'alias': '',
            'offender_tracking_number': 'BCM22102',
        },
        {
            'last_name': 'RAYLOPEZ',
            'first_name': 'ALEXIS',
            'dob': '1999',
            'alias': 'Y',
            'offender_tracking_number': 'BCM22102',
        },
        {
            'last_name': 'RODRIGUEZ',
            'first_name': 'DELIA',
            'dob': '1982',
            'alias': 'Y',
            'offender_tracking_number': 'BCM22101',
        },
        {
            'last_name': 'SANCHEZ',
            'first_name': 'ABRAHAM',
            'dob': '1986',
            'alias': '',
            'offender_tracking_number': 'BCM22103',
        },
    ]
    records_8 = [
        {
            'last_name': 'ABRAHAM',
            'first_name': 'JASON ALLEN',
            'dob': '1972',
            'alias': '',
            'offender_tracking_number': 'N/A',
        },
        {
            'last_name': 'CAMPBELL',
            'first_name': 'GENE',
            'dob': '1969',
            'alias': '',
            'offender_tracking_number': 'N/A',
        },
        {
            'last_name': 'CARDENAS',
            'first_name': 'MILAN ERIN',
            'dob': '1989',
            'alias': '',
            'offender_tracking_number': 'N/A',
        },
    ]

    print("-" * 100)
    pprint(parsing_fun(records_1))
    print("-" * 100)
    pprint(parsing_fun(records_2))
    print("-" * 100)
    pprint(parsing_fun(records_3))
    print("-" * 100)
    pprint(parsing_fun(records_4))
    print("-" * 100)
    pprint(parsing_fun(records_5))
    print("-" * 100)
    pprint(parsing_fun(records_6))
    print("-" * 100)
    pprint(parsing_fun(records_7))
    print("-" * 100)
    pprint(parsing_fun(records_8))
    print("-" * 100)

if __name__ == '__main__':
    main()

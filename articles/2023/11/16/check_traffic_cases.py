import datetime

import requests

from pprint import pprint


DATE_FORMAT = "%m-%d-%Y"

today = datetime.datetime.now()
base_path = "https://media.lacourt.org/lascmediaproxy/api/AzureApi"


def get_court_houses_data():
    url = f"{base_path}/GetCriminalCourthouses"
    resp = requests.get(url)
    results = resp.json()["resultList"]
    pprint(results)
    for court_house in results:
        print(court_house["key"], court_house["value"])
        get_court_departments(court_house["key"])
        break


def get_court_departments(court_house_id):
    url = f"{base_path}/GetCriminalDepartments/{court_house_id}"
    resp = requests.get(url)
    results = resp.json()["resultList"]
    pprint(results)
    for result in results:
        print(result["key"], result["value"])
        get_criminal_cases(court_house_id, result["key"])
        break


def get_criminal_cases(court_house_id, department_id):
    older_date = today - datetime.timedelta(weeks=2)
    url = f"{base_path}/CriminalCalendarSearchByLocationNew/CR/{court_house_id}/{department_id}/{older_date.strftime(DATE_FORMAT)}/{today.strftime(DATE_FORMAT)}"
    resp = requests.get(url)
    results = resp.json()["resultList"]
    for case in results :
        pprint(case)
        break


def get_case_list_api():
    url = f"{base_path}/GetCaseList/CR"
    resp = requests.get(url)
    # results = resp.json()["resultList"]
    pprint(resp.text)


def main() -> None:
    print(f"Hello main from : {__file__}")
    print(today.strftime(DATE_FORMAT))
    older_date = today - datetime.timedelta(weeks=10)
    print(older_date.strftime(DATE_FORMAT))
    # get_case_list_api()
    get_court_houses_data()


if __name__ == "__main__":
    main()

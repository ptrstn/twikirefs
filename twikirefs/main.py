import json

import cernrequests
from bs4 import BeautifulSoup
from cernrequests import get_sso_cookies

TWIKI_URL = "https://twiki.cern.ch/twiki/bin/view/CMS/TrackerOfflineReferenceRuns"


def list_to_dict(data, keys):
    return [dict(zip(keys, item)) for item in data]


def clean_run_number_column_name(column_name):
    desired_name = "run_number"
    wrong_names = ['run number', "RunNumber", 'Run']
    new_name = column_name
    for wrong_name in wrong_names:
        new_name = new_name.replace(wrong_name, desired_name)

    return new_name
    # return column_name.replace("RunNumber", "run_number").replace("Run", 'run_number')


def clean_comments_column_name(column_name):
    return column_name.replace('comments', 'Notes')


def clean_column_name(column_name):
    return clean_comments_column_name(
        clean_run_number_column_name(column_name)).replace(" ", "_").replace(".",
                                                                             "").lower()


def main():
    print("Twiki Reference Runs")

    print()
    print("Acquiring CERN SSO Cookie for {}...".format(TWIKI_URL))
    cookies = get_sso_cookies(TWIKI_URL)

    print("Retrieving Twiki page...".format(TWIKI_URL))
    response = cernrequests.get(TWIKI_URL, cookies=cookies)

    print("Parsing HTML site...")
    soup = BeautifulSoup(response.content, 'html.parser')

    table_names = [
        ("table1", "Heavy Ion Collisions 2018"),
        ("table2", "pp Collisions 2018"),
        ("table3", "Cosmics 2018"),
    ]

    tables = []
    for table_name in table_names:
        table = soup.find("table", {"id": table_name[0]})

        data = []
        names = [clean_column_name(cell.get_text().strip()) for cell in
                 table.findAll('th')]

        for row in table.findAll("tr"):
            if row.findAll('td'):
                data.append([cell.get_text().strip().replace('\xa0', "") for cell in
                             row.findAll('td')])

        tables.append({
            "description": table_name[1],
            'data': list_to_dict(data, names)
        })

    print("Done.")
    print()

    for table in tables:
        print("== {} ==".format(table['description']))
        print([run["run_number"] for run in table['data']])
        print()

    file_name = "twiki_reference_runs.json"
    with open(file_name, "w") as file:
        file.write(json.dumps(tables, indent=2))
        print("Saved reference runs in '{}'".format(file_name))


if __name__ == "__main__":
    main()

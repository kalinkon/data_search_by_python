import csv
import sys


def read_file():
    data = []
    with open('NCHS_-_Leading_Causes_of_Death__United_States.csv', "rt", encoding="utf8") as csvfile:
        csv_data = csv.reader(csvfile, delimiter=',', quotechar='|')
        count = 0
        for row in csv_data:
            count = count+1
            # print(', '.join(row))
            if count > 1:
                data.append(row)
    return data


class SurveyRecord:

    def __init__(self, year, disease_details, disease_name, state, death_count,adjusted_death_rate ):
        self.year = year
        self.disease_details = disease_details
        self.disease_name = disease_name
        self.state = state
        self.death_count = death_count
        self.adjusted_death_rate = adjusted_death_rate


def get_survey_object_list(data):
    survey_object_list = []

    for row in data:
        if len(row) == 6:
            survey_object = SurveyRecord(row[0],row[1],row[2],row[3],row[4],row[5])
            survey_object_list.append(survey_object)
        if len(row) == 7:
            survey_object = SurveyRecord(row[0],row[1]+row[2],row[3],row[4],row[5],row[6])
            survey_object_list.append(survey_object)
        if len(row) == 8:
            survey_object = SurveyRecord(row[0],row[1]+row[2]+row[3],row[4],row[5],row[6],row[7])
            survey_object_list.append(survey_object)
        if len(row) == 9:
            survey_object = SurveyRecord(row[0],row[1]+row[2]+row[3]+row[4],row[5],row[6],row[7],row[8])
            survey_object_list.append(survey_object)

    return survey_object_list



def get_search_by_disease(surveys, search_key):
    search_result = []
    for survey in surveys:
        if search_key.lower() in survey.disease_name.lower():
            search_result.append(survey)
    return search_result

def get_search_by_year(surveys, search_key):
    search_result = []
    for survey in surveys:
        if search_key.lower() in survey.year.lower():
            search_result.append(survey)
    return search_result
if __name__ == '__main__':
    data = read_file()

    surveys = get_survey_object_list(data)

    while True:
        choice = input("press 1 to search by disease or press 2 to search by year: ")
        if choice == "1" or choice == "2":
            break
        if choice == "3":
            break
        else:
            print("press 1 or 2 to search, and 3 to exit")


    if choice == "3":
        sys.exit()

    if choice == "1":
        search_key = input("Enter the disease name: ")
        result = get_search_by_disease(surveys, search_key)
    else:
        search_key = input("Enter the year: ")
        result = get_search_by_year(surveys, search_key)

    if len(result) == 0:
        print("Sorry, Your query doesn't match any record")
    else:
        for r in result:
            print(r.__dict__)
        print("total {} results".format(len(result)))

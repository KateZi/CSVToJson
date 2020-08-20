import pandas as pd
import os
import json
from copy import deepcopy

QUESTIONS_COLUMN = "Field Label"


def read_csv_to_json(csv_path):
    df = pd.read_csv(csv_path)

    questions = df[QUESTIONS_COLUMN]
    questions = questions[1:]

    result_dictionary = {
        "data": {
            "questions": [
            ]
        },
        "status": True,
        "message": "The data was fetched successfully"
    }

    question_dictionary = {
        "id": 0,
        "question_type_id": 2,
        "question_type_name": "Radio",
        "question_name": "",
        "question_item": [
            {
                "answer_id": "",
                "name": "1 לא מדויק כלל"
            },
            {
                "answer_id": "",
                "name": "2 מדויק במידה מועטה"
            },
            {
                "answer_id": "",
                "name": "3 מדויק"
            },
            {
                "answer_id": "",
                "name": "4 מדויק ביותר"
            }
        ]
    }

    idx = 1
    for question in questions:
        question_dictionary["id"] = idx
        question_dictionary["question_name"] = question
        for i, item in enumerate(question_dictionary["question_item"]):
            question_dictionary["question_item"][i]["answer_id"] = "".join([str(idx), str(i + 1)])
        result_dictionary["data"]["questions"].append(deepcopy(question_dictionary))
        idx += 1

    json_path = ".".join([csv_path[:-4], "json"])
    with open(json_path, 'w') as outfile:
        json.dump(result_dictionary, outfile)


if __name__ == '__main__':
    csv_path = input("Please enter path to the desired csv")
    json_path = ".".join([csv_path[:-4], "json"])
    read_csv_to_json(csv_path)

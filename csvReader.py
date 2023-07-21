import csv
from dataclasses import dataclass


@dataclass
class AnswerQuestion:
    Question: str
    Answer: str


def get_data() -> list[AnswerQuestion]:
    """ Gets the answer/question pairs (18)"""
    my_list = []
    with open('./data/Sample-Faq.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                answer_question = AnswerQuestion(
                    Answer=row[1], Question=row[0])
                my_list.append(answer_question)
                print(answer_question)
                line_count += 1
        print(f'Processed {line_count} lines.')
    return my_list

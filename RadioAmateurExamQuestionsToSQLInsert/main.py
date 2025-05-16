# table schema: (id, question, answerA, answerB, answerC, correctAnswer, category, photoId)
from question import Question

inputFiles = [
    "data/cat1.txt",
    "data/cat2.txt",
    "data/cat3.txt",
    "data/cat4.txt",
]

outputFiles = [
    "output/insert1.sql",
    "output/insert2.sql",
    "output/insert3.sql",
    "output/insert4.sql",
]
categories = [
    "C1",
    "C2",
    "C3",
    "C4",
]
counter = 1

for i in range(0, 4):
    try:
        with open(inputFiles[i], "r", encoding='utf-8') as file:
            with open(outputFiles[i], "w", encoding='utf-8') as outputFile:
                lines = file.readlines()
                sql = "INSERT INTO question(id, question, answer_a, answer_b, answer_c, correct_answer, category, photo_id) VALUES \n"
                for lineNum in range(0, len(lines), 4):
                    question = Question()
                    question.id = counter
                    question.question = lines[lineNum].strip()#[5:]
                    question.answerA = lines[lineNum + 1].strip()#[3:]
                    question.answerB = lines[lineNum + 2].strip()#[3:]
                    question.answerC = lines[lineNum + 3].strip()#[3:]
                    question.correctAnswer = "NULL"
                    question.category = categories[i]
                    question.photoId = "NULL"

                    counter += 1

                    sql += question.print_as_insert_value()

                result = sql.replace("'NULL'", "NULL")
                outputFile.write(result)



    except FileNotFoundError:
        print("File not found")
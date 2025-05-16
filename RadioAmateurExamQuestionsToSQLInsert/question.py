class Question:
    def __init__(self):
        self.id = None
        self.question = None
        self.answerA = None
        self.answerB = None
        self.answerC = None
        self.correctAnswer = None
        self.category = None
        self.photoId = None

    def get_id(self):
        return self.id

    def set_id(self, identifier):
        self.id = identifier

    def get_question(self):
        return self.question

    def set_question(self, question):
        self.question = question

    def get_answer_a(self):
        return self.answerA

    def set_answer_a(self, answer_a):
        self.answerA = answer_a

    def get_answer_b(self):
        return self.answerB

    def set_answer_b(self, answer_b):
        self.answerB = answer_b

    def get_answer_c(self):
        return self.answerC

    def set_answer_c(self, answer_c):
        self.answerC = answer_c

    def get_correct_answer(self):
        return self.correctAnswer

    def set_correct_answer(self, correct_answer):
        self.correctAnswer = correct_answer

    def get_category(self):
        return self.category

    def set_category(self, category):
        self.category = category

    def get_photo_id(self):
        return self.photoId

    def set_photo_id(self, photo_id):
        self.photoId = photo_id

    def print_question(self):
        print("--------------------------------------------")
        print("Question id: {}".format(self.id))
        print("Question question: {}".format(self.question))
        print("Question answerA: {}".format(self.answerA))
        print("Question answerB: {}".format(self.answerB))
        print("Question answerC: {}".format(self.answerC))
        print("Correct Answer: {}".format(self.correctAnswer))
        print("Category: {}".format(self.category))
        print("PhotoId: {}".format(self.photoId))
        print("--------------------------------------------")

    def print_as_insert_value(self):
        return ("(" + str(self.id) + ", '" + self.question + "', '" + self.answerA + "', '" + self.answerB + "', '"
                + self.answerC + "', '" + self.correctAnswer + "', '" + self.category + "', '" + self.photoId + "'),\n")
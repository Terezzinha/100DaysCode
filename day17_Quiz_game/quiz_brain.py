# todo: asking the questions
class QuizBrain:

    def __int__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        input(f"Q {self.question_number}: {current_question.text} - True ou False?")


# todo: checking if the answers was correct
# todo: checking if we´re the end of the quiz
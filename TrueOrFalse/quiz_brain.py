class QuizBrain:
    def __init__(self, ques_list):
        self.question_number = 0
        self.question_list = ques_list
        self.score = 0

    def still_have_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        ans = input(f"Q.{self.question_number + 1}: {current_question.text}? (True/False) ? ")
        self.question_number += 1
        if ans == current_question.answer:
            self.score += 1
            print("you got it right")
        else:
            print("That is wrong")
        print(f"the correct answer was: {current_question.answer}")
        print(f"your current score is {self.score}/{self.question_number}\n")

    def final_score(self):
        return f"{self.score}/{self.question_number}"





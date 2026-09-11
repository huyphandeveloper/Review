from abc import ABC, abstractmethod

class Student:
    def __init__(self, name, raw_scores : str):
        self.name = name
        self._scores = [int(score) for score in raw_scores.strip().split(",")]

    @property
    def scores(self):
        return self._scores

    @scores.setter
    def scores(self, new_raw_scores : list):
        for score in new_raw_scores:
            if score < 0 or score > 100:
                raise ValueError("Score must be between 0 and 100")
        self._scores = new_raw_scores

class GradeCalculator(ABC):
    @abstractmethod
    def calculate(self, scores):
        pass

class AverageCalculator(GradeCalculator):
    def calculate(self, scores : list):
        return sum(scores) / len(scores)

class MaxCalculator(GradeCalculator):
    def calculate(self, scores):
        return max(scores)

def print_report(student, calculator):
    try:
        print(f"{student.name}: {calculator.calculate(student.scores)}")
    except ZeroDivisionError:
        print("Scores not empty.")
    except ValueError:
        print("Scores not empty")


student1 = Student("An", "85, 90, 78, 92")
print(student1.scores)   # [85, 90, 78, 92]

avg_calc = AverageCalculator() 
max_calc = MaxCalculator() 

print_report(student1, avg_calc) #An: 86.25
print_report(student1, max_calc) #An: 92

student1.scores = [-5, 100]  # phải raise ValueError
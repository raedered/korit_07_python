class Student :
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = {}

    def add_grade (self, subject, score) :
        self.grades[subject] = score

    def get_average_grade (self) :
        total = sum(self.grades.values())
        average = total / len(self.grades.keys())
        return f'학생 이름 {self.name} \n평균성적 {average}점'


student1 = Student('김일', '2025001')
student1.add_grade('수학', 90)
student1.add_grade('국어', 80)
student1.add_grade('영어', 70)

print(student1.get_average_grade())
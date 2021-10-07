class Exam:
    def __init__(self, marks):
        self.marks = marks
        self.time = 60

    def examSyllabus(self):
        return "Maths , English"

    def examParts(self):
        return "Part 1 - Maths\nPart 2 - English\n"


class ScienceExam(Exam):
    def __init__(self, marks, time, *info):
        super().__init__(marks)
        self.time = time
        self.lst_info = []
        self.var = 2
        for i in info:
            self.var += 1
            self.lst_info.append(i)

    def examSyllabus(self):
        sub_list = super().examSyllabus()
        for i in self.lst_info:
            sub_list += " , " + i
        return sub_list

    def examParts(self):
        var = super().examParts()
        counter = 3

        for i in self.lst_info:
            var += f"part {str(counter)} - {i}\n"
            counter += 1
        return var

    def __str__(self):
        return f"Marks: {str(self.marks)} Time: {str(self.time)} Number of Parts: {str(self.var)}"


engineering = ScienceExam(100, 90, "Physics", "HigherMaths")
print(engineering)
print("----------------------------------")
print(engineering.examSyllabus())
print(engineering.examParts())
print("==================================")
architecture = ScienceExam(100, 120, "Physics", "HigherMaths", "Drawing")
print(architecture)
print("----------------------------------")
print(architecture.examSyllabus())
print(architecture.examParts())

class Student:
    def __init__(self, name, marks):
        self.name = name  
        self.marks = marks  

    def check_result(self):
        if self.marks >= 40:
            return f"{self.name} has passed with {self.marks} marks."
        else:
            return f"{self.name} has failed with {self.marks} marks."

# Example usage
student1 = Student("pradeep",95)
student2 = Student("prajwl", 96)

print(student1.check_result())
print(student2.check_result())

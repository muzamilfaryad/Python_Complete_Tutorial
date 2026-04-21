from classes_and_objects import Student

# Create a student instance
student1 = Student("Alice", "Computer Science", 3.8, False)
# Use the introduce method
print(student1.introduce())
print(f"GPA: {student1.gpa}, On Probation: {student1.is_on_probation}")
# Output: Hello, my name is Alice. I am studying Computer Science.
# Create another student instance
student2 = Student("Bob", "Mathematics", 2.5, True)
# Use the introduce method
print(student2.introduce())
print(f"GPA: {student2.gpa}, On Probation: {student2.is_on_probation}")
# Output: Hello, my name is Bob. I am studying Mathematics.
print(student2.name)

print("Honor Roll:", student2.on_honor_roll())
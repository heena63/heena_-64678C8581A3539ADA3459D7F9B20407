# challenge 3.1
class Student:
  def __init__(self, name, roll_number, cgpa):
      self.name = name
      self.roll_number = roll_number
      self.cgpa = cgpa

def sort_students(student_list):
  # Sort the list of students based on CGPA in descending order
  sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
  return sorted_students

# Example usage:
# Create a list of student objects
students = [
  Student("Alice", "S001", 3.8),
  Student("Bob", "S002", 3.5),
  Student("Charlie", "S003", 4.0),
  Student("David", "S004", 3.7)
]

# Sort the list of students based on CGPA
sorted_students = sort_students(students)

# Print the sorted list
for student in sorted_students:
  print(f"Name: {student.name}, Roll Number:{student.roll_number}, CGPA: {student.cgpa}")

def linear_search_product(product_list, target_product):
  indices = []
  for i, product in enumerate(product_list):
      if product == target_product:
          indices.append(i)
  return indices

# Example usage:
products = ["Apple", "Banana", "Orange", "Apple", "Grapes", "Apple"]
target_product = "Apple"

result = linear_search_product(products, target_product)

print(result)


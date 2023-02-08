
import json 

GENDER = ["Male","Female"]
DEPARTMENTS = ["Computer Science","Environmental", "Medical Health"]

class Student:
  def __init__(self, name, gender, subject, department, grade):
    self.name = name
    self.gender = gender
    self.subject = subject
    self.department = department
    self.grade = grade
  def serialize(self):
    return {
              "name": self.name,
              "gender": self.gender,
              "subject": self.subject,
              "department": self.department,
              "grade": self.grade
            }
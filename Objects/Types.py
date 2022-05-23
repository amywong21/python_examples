# Manchmal möchtest du in Python feststellen, ob eine Variable einen bestimmten Typ hat oder nicht. 
# Dafür kannst du "isinstance" bzw. "type" verwenden. 

class Student():
	def __init__(self, firstname, surname):
		self.firstname = firstname
		self.surname = surname

	def name(self):
		return self.firstname + " " + self.surname

class WorkingStudent(Student):
	def __init__(self, firstname, surname, company):
		super().__init__(firstname, surname)
		self.commpany = company

	def name(self):
		return super().name() + " (" + self.company + ")"

def example_type():
	# type
	w_student = WorkingStudent("Max", "Müller", "ABCDEF GmbH")
	student = Student("Monika", "Mustermann")

	print(type(w_student))
	print(type(student))

	if type(w_student) == Student:
		print("Diese Zeile wird nur für einen Student ausgegeben")

	# In Type wird Vererbung nicht betrachtet. Mit isinstance schon. 
	# Wenn ich aus einer Liste bestimmte Studenten brauche kann ich es mit isinstance abfragen.
	print(isinstance(w_student, WorkingStudent))
	print(isinstance(w_student, Student))

	print(isinstance(Student, WorkingStudent))
	print(isinstance(Student, Student))
	
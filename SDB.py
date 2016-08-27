import os
import sys
import pickle
import shutil

debugmode = 1
class student(object):
	stdcount = 0
	def __init__(self, name, course):
		self.name = name
		self.course = course
		student.stdcount += 1
	def displaycount(self):
		print("Total students %d", student.stdcount)
	def displaystudent(self):
		print("Name: ", self.name, ", course: ", self.course)
count = 0 
std = []
def Add_newstudent(x,y):
	global count
	global std
	if debugmode == 1:
		print("Adding new student to Database\n")
	name = x
	course = y
	count = count + 1
	print "count=",count
	#student1 = []
	std = student(str(name),str(course))
	with open('student_database.txt', 'ab') as output:
		pickle.dump(std,output,pickle.HIGHEST_PROTOCOL)
	output.close()
	#fp = open('student_DB.txt', 'ab')
	#fp.write(std)
	#fp.close()
		
	
def disp_student_db():
	print("Display all the students  in the databse\n")
	#with open('student_database.txt', 'rb') as readfile:
	#	student1 = pickle.load(readfile)
		#print student1
	#	print(student1.name)
	#	print(student1.course)
	readfile = open('student_database.txt', 'rb')
	while 1:
		try:
			student1 = pickle.load(readfile)
			#print student1
			print(student1.name)
			print(student1.course)
		except EOFError:
			break
	readfile.close()
	

def search_name(sname):
	print("Searching student name in database\n")
	fp = open('student_database.txt','rb')
	while 1:
		try: 
			student = pickle.load(fp)
			if student.name == sname:
				print(student.name)
				print(student.course)
		except EOFError:
			break
	fp.close()
def remove_name(rname):
	print("Removing student name from databse\n")
	shutil.copy2('student_database.txt','SDE.txt')
	open('student_database.txt','w').close()
	fp = open('SDE.txt','rb')
	fo = open('student_database.txt','ab')
	while 1:
		try: 
			student = pickle.load(fp)
			if student.name != rname:
				#del student.name
				#del student.course
				print("Condition True...")
				pickle.dump(student,fo,pickle.HIGHEST_PROTOCOL)
				print "deleted "+rname+" details"		
		except EOFError:
			break
	fo.close()
	fp.close()
	os.remove('SDE.txt')



fp = open("student_DB.txt",'wb')
#if fp == NULL:
#	fp = open("student_DB.txt",'+wb')
#	if fp == NULL:
#		print("Can't open student_DB.txt file...")

print("Option Menu: \n")
print("1. Add new student\n")
print("2. Display student data base \n")
print("3. Search name \n")
print("4. Remove name \n")
c = input("Enter your choice: ")
if c == 1:
	name = raw_input("\nEnter name: ")
	course = raw_input("\nEnter course:" )
	Add_newstudent(name, course)
elif c == 2:
	disp_student_db()
elif c == 3:
	sname = raw_input("\nEnter name:")
	search_name(sname)
elif c == 4:
	rname = raw_input("\nEnter name:")
	remove_name(rname)
else:
	print("\nEnter a valid choice\n")
if debugmode == 1:
	print"your choice "+str(c)

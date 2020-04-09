import os
from prettytable import PrettyTable
from collections import defaultdict
from HW08_Heli_Patel import file_reader

class Student:
    """"Class student for instance of student."""

    def __init__(self,cwid:str,name:str,major:str) -> None:

        self.cwid:str = cwid
        self.name:str = name
        self.major:str = major
        self.coursegrades:dict = dict()

    def add_coursegrade(self,course:str,grade:str)-> None:
        self.coursegrades[course] = grade

    def student_details(self)-> None:
        return[self.cwid , self.name, sorted(self.coursegrades.keys())]

class Instructor:
    """Class instructor for instance of instructor."""
    def __init__(self,instructorcwid:str,instructorname:str,instructordept:str)-> None:

        self.instructorcwid:str = instructorcwid
        self.instructorname:str = instructorname
        self.instructordept:str = instructordept
        self.coursestudents:defaultdict = defaultdict(int)

    def add_coursestudent(self,course:str)-> None:
        self.coursestudents[course] += 1

    def instructorsummary(self)-> None:
        """Return the value as id,name,dept,course,number of students."""

        for course,studentnumber in self.coursestudents.items():
            yield [self.instructorcwid,self.instructorname,self.instructordept, course, studentnumber] 

    def instructorsummary1(self)->None:
        """Return the value as id,name,dept,course,number of students."""

        for course,studentnumber in self.coursestudents.items():
            return [self.instructorcwid,self.instructorname,self.instructordept, course, studentnumber] 

class Repository:
    """ Class Repository to store all the data of all the files."""

    def __init__(self,directory: str) -> None:
        self.directory: str = directory
        self.studentDict:dict = dict()
        self.instructorDict:dict = dict()

        self.student(os.path.join(directory,'students.txt'))
        self.instructor(os.path.join(directory,'instructors.txt'))
        self.grades(os.path.join(directory,'grades.txt'))
    
    def student(self,path:str) -> None:
        """Student file and to create  Student dictionary.""" 
        try:
            for cwid,name,major in file_reader(path,3,"\t"):
                self.studentDict[cwid] = Student(cwid,name,major)
        except(FileNotFoundError,ValueError) as e:
            print(e)

    def instructor(self,path:str) -> None:
        """Instuctor file and to create Instructor dictionary."""
        try:
            for instructorcwid,instructorname,instructordept in file_reader(path,3,"\t"):
                self.instructorDict[instructorcwid] = Instructor(instructorcwid,instructorname,instructordept) 
        except(FileNotFoundError,ValueError) as e:
            print(e)                

    def grades(self,path:str) -> None:
        """Grades file for creating grades of students."""
        
        try:
            for cwid,studentcourse,studentgrade,instructorcwid in file_reader(path,4,"\t"):
                instructorcwid1 = instructorcwid.strip()
                if cwid in self.studentDict:
                    s = self.studentDict[cwid]
                    s.add_coursegrade(studentcourse, studentgrade)
                else:
                    print("Unknown student")

                if instructorcwid1 in self.instructorDict:
                    self.instructorDict[instructorcwid1].add_coursestudent(studentcourse)
                else:
                    print(instructorcwid1)
                    print("Unknown instructor")    

        except(FileNotFoundError,ValueError) as e:
            print(e)                          

    def tableStudentSummary(self)-> None:
        """Pretty Table for student summary."""
        print("Student Summary")
        pt = PrettyTable(field_names = ['CWID' , 'Name' , 'Completed Courses'])
        
        for s in self.studentDict.values():
            pt.add_row(s.student_details())
            
        print(pt)

    def tableInstructorSummary(self)-> None:
        
        """"Pretty Table for Instructor summary."""
        print("Instructor Summary")
        pt = PrettyTable(field_names = ['CWID','Name','Dept','Course','Students'])

        for i in self.instructorDict.values():
            for line in i.instructorsummary():
                pt.add_row(line)
        print(pt)                            
               
if __name__=="__main__":

    directory = 'C:/Users/User/Desktop/Python/.vscode'
    repository = Repository(directory)
    repository.tableStudentSummary()
    repository.tableInstructorSummary()

import os
from prettytable import PrettyTable
from collections import defaultdict
from HW08_Heli_Patel import file_reader
from statistics import mean
import sqlite3

class Student:
    """"Class student for instance of student."""

    def __init__(self,cwid:str,name:str,major:str) -> None:

        self.cwid:str = cwid
        self.name:str = name
        self.major:str = major
        self.coursegrades:dict = defaultdict(str)
        self.stu_pass_courses:list = list()
        self.gpa:float = 0.0
        self.remaining_required:set = set()
        self.remaining_electives:set = set()
        self.pass_course()
        
    
    def add_coursegrade(self,course:str,grade:str)-> None:
       self.coursegrades[course] = grade
        
    def pass_course(self) -> None:
        for course in self.coursegrades.keys():
            if self.coursegrades[course] != 'F':
                self.stu_pass_courses.append(course)
        return self.stu_pass_courses

    def gpa_calculate(self) -> None:
        gradedict:dict = {'A':4, 'A-':3.75, 'B+':3.25, 'B':3,'B-':2.75,'C+':2.25,'C':2.0,'C-':0,'D+':0,'D':0,'D-':0,'F':0 }
        l1:List = []
        for course in self.coursegrades.keys():
            l1.append(gradedict[self.coursegrades[course]])
        self.gpa=round(mean(l1),2)
        return self.gpa

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


class Major:
    """Class Repository to store all data of majors."""

    def __init__(self,dept:str)-> None:

        self.dept:str = dept
        self.required = set()
        self.elective = set()

    def add_course(self,initial:str,course:str)-> None:
        if initial == 'R':
            self.required.add(course)
        elif initial == 'E':
            self.elective.add(course)
        else:
            print("Not valid initial")


class Repository:
    """ Class Repository to store all the data of all the files."""

    def __init__(self,directory: str) -> None:
        self.directory: str = directory
        self.studentDict:dict = dict()
        self.instructorDict:dict = dict()
        self.majorsdict:dict = dict()

        self.student(os.path.join(directory,'students.txt'))
        self.instructor(os.path.join(directory,'instructors.txt'))
        self.grades(os.path.join(directory,'grades.txt'))
        self.major(os.path.join(directory,'majors.txt'))
        self.gpa_calculator_fun(os.path.join(directory,'students.txt'))
    
    def student(self,path:str) -> None:
        """Student file and to create  Student dictionary.""" 
        try:
            for cwid,name,major in file_reader(path,3,"\t",header=True):
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
            for cwid,studentcourse,studentgrade,instructorcwid in file_reader(path,4,"\t",header=True):
                instructorcwid1 = instructorcwid.strip()
                if cwid in self.studentDict:
                    s = self.studentDict[cwid]
                    s.add_coursegrade(studentcourse, studentgrade)
                else:
                    print("Unknown student")

                if instructorcwid1 in self.instructorDict:
                    self.instructorDict[instructorcwid1].add_coursestudent(studentcourse)
                else:
                    print("Unknown instructor")
                    

        except(FileNotFoundError,ValueError) as e:
            print(e)

    def gpa_calculator_fun(self,path:str)->None:
        """To calulate the gpa """
        try:
            for cwid,name,major in file_reader(path,3,"\t",header=True):
                if cwid in self.studentDict:
                    self.studentDict[cwid].gpa_calculate()
        except(FileNotFoundError,ValueError) as e:
            print(e)



    def major(self,path:str) -> None:
        """Majors file for creating majors of students."""
        try:
            for name,initial,course in file_reader(path,3,"\t", header=True):
                self.majorsdict[name] = Major(name)
            for name,initial,course in file_reader(path,3,"\t",header=True):
                self.majorsdict[name].add_course(initial,course)

            for cwid,stu in self.studentDict.items():
                stu.remaining_required = list(set(self.majorsdict[stu.major].required) - set(stu.coursegrades.keys()))
                if set(self.majorsdict[stu.major].elective).intersection(set(stu.pass_course())):
                    stu.remaining_electives=[]
                else:
                    stu.remaining_electives=list(self.majorsdict[stu.major].elective)

        except(FileNotFoundError,ValueError) as e:
            print(e)                                              

    def tableStudentSummary(self)-> None:
        lst: list =[]
        """Pretty Table for student summary."""
        print("Student Summary")
        pt = PrettyTable(field_names = ['CWID' , 'Name' , 'Completed Courses', 'Remaining Required', 'Remaining Electives', 'GPA'])
        
        for cwid,stu in self.studentDict.items():
            pt.add_row([cwid,stu.name, sorted(stu.coursegrades.keys()) , stu.remaining_required, stu.remaining_electives, stu.gpa])
            lst.append([cwid,stu.name, sorted(stu.coursegrades.keys()) , sorted(stu.remaining_required), sorted(stu.remaining_electives), stu.gpa])
        print(pt)
        return(lst)

    def tableInstructorSummary(self)-> None:
        lst2:list=[]
        """"Pretty Table for Instructor summary."""
        print("Instructor Summary")
        pt = PrettyTable(field_names = ['CWID','Name','Dept','Course','Students'])

        for i in self.instructorDict.values():
            for line in i.instructorsummary():
                pt.add_row(line)
                lst2.append(line)
        print(pt)
        return(lst2)

    def tablemajorsummary(self)-> None:
        """"Pretty Table for major summary"""
        lst1:list = []
        print("Major Summary")
        pt = PrettyTable(field_names= ['Major','Required Courses','Electives'])                                
               
        for name,major in self.majorsdict.items():
            pt.add_row([major.dept,major.required,major.elective])
            lst1.append([major.dept,major.required,major.elective])
        print(pt)    
        return(lst1)

    def table_summary_grade_db(self,db_file:str):
        """Function for getting values from database."""
        lst3:list = []
        print("Student Grade Summary")
        db_file:str = "SSW810.db"
        db : sqlite3.Connection = sqlite3.connect(db_file)
        query : str = "select s.Name, s.CWID, g.Course,g.Grade,i.Name AS 'Instructor Name' "\
                      "FROM grades g join students s on g.StudentCWID = s.CWID "\
                      "join instructors i on g.InstructorCWID = i.CWID order by s.Name"
        pt = pt = PrettyTable(field_names= ['Name','CWID','Course','Grade','Instructor'])

        for name,cwid,course,grade,instructor in db.execute(query):
            pt.add_row([name,cwid,course,grade,instructor ])
            lst3.append([name,cwid,course,grade,instructor])
        print(pt)
        return(lst3)             
   

if __name__=="__main__":

    directory = 'C:/Users/User/Desktop/Python/.vscode'
    repository = Repository(directory)
    repository.tableStudentSummary()
    repository.tableInstructorSummary()
    repository.tablemajorsummary()
    repository.table_summary_grade_db("SSW810.db")

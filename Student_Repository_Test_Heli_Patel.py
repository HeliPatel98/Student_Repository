import unittest
from Student_Repository_Heli_Patel import Student,Instructor,Major,Repository
from typing import Dict,List

class Datarepository(unittest.TestCase):
    
    def test_student(self):
        data : Repository = Repository("C:/Users/User/Desktop/Python/.vscode")
        expected:List = [['10103', 'Jobs, S', ['CS 501', 'SSW 810'], ['SSW 540', 'SSW 555'], [], 3.38], ['10115', 'Bezos, J', ['CS 546', 'SSW 810'], 
                        ['SSW 540', 'SSW 555'], ['CS 501', 'CS 546'], 2], ['10183', 'Musk, E', ['SSW 555', 'SSW 810'], ['SSW 540'], 
                        ['CS 501', 'CS 546'], 4], ['11714', 'Gates, B', ['CS 546', 'CS 570', 'SSW 810'], [], [], 3.5]]

        output = data.tableStudentSummary()
        self.assertEqual(output,expected)

    def test_instructor(self):
        """For testing of instructor summary"""
        data : Repository = Repository("C:/Users/User/Desktop/Python/.vscode")
        expected:Dict = [['98764', 'Cohen, R', 'SFEN', 'CS 546', 1], ['98763', 'Rowland, J', 'SFEN', 'SSW 810', 4], 
                        ['98763', 'Rowland, J', 'SFEN', 'SSW 555', 1], ['98762', 'Hawking, S', 'CS', 'CS 501', 1], 
                        ['98762', 'Hawking, S', 'CS', 'CS 546', 1], ['98762', 'Hawking, S', 'CS', 'CS 570', 1]]

        print(data.tableInstructorSummary)
        self.assertEqual(data.tableInstructorSummary(),expected)

    def test_major(self):
        """For testing of major summary"""
        data : Repository = Repository("C:/Users/User/Desktop/Python/.vscode")
        expected:list = [['SFEN', {'SSW 810', 'SSW 540', 'SSW 555'}, {'CS 546', 'CS 501'}], ['CS', {'CS 546', 'CS 570'}, {'SSW 565', 'SSW 810'}]]                              

        output = data.tablemajorsummary()
        self.assertEqual(output,expected)

    def test_student_grade(self):
        """For testing student grade summary"""
        data : Repository = Repository("C:/Users/User/Desktop/Python/.vscode")
        expected:list = [['Bezos, J', '10115', 'SSW 810', 'A', 'Rowland, J'], ['Bezos, J', '10115', 'CS 546', 'F', 'Hawking, S'], 
                        ['Gates, B', '11714', 'SSW 810', 'B-', 'Rowland, J'], ['Gates, B', '11714', 'CS 546', 'A', 'Cohen, R'], 
                        ['Gates, B', '11714', 'CS 570', 'A-', 'Hawking, S'], ['Jobs, S', '10103', 'SSW 810', 'A-', 'Rowland, J'], 
                        ['Jobs, S', '10103', 'CS 501', 'B', 'Hawking, S'], ['Musk, E', '10183', 'SSW 555', 'A', 'Rowland, J'], 
                        ['Musk, E', '10183', 'SSW 810', 'A', 'Rowland, J']]
        output = data.table_summary_grade_db("SSW810.db")
        self.assertEqual(output,expected)                

if __name__ == "__main__":
    unittest.main(exit=False,verbosity=2)
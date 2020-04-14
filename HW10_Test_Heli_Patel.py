import unittest
from HW10_Heli_Patel import Student,Instructor,Major,Repository
from typing import Dict,List

class Datarepository(unittest.TestCase):

    def test_student(self):
        """For testing of student summary"""
        data : Repository = Repository("C:/Users/User/Desktop/Python/.vscode")
        expected:List = [['10103', 'Baldwin, C', ['CS 501', 'SSW 564', 'SSW 567', 'SSW 687'], ['SSW 540', 'SSW 555'], [], 3.44],
                        ['10115', 'Wyatt, X', ['CS 545', 'SSW 564', 'SSW 567', 'SSW 687'], ['SSW 540', 'SSW 555'], [], 3.81],
                        ['10172', 'Forbes, I', ['SSW 555', 'SSW 567'], ['SSW 540', 'SSW 564'], ['CS 501', 'CS 513', 'CS 545'], 3.88],
                        ['10175', 'Erickson, D', ['SSW 564', 'SSW 567', 'SSW 687'], ['SSW 540', 'SSW 555'], ['CS 501', 'CS 513', 'CS 545'], 3.58],
                        ['10183', 'Chapman, O', ['SSW 689'], ['SSW 540', 'SSW 555', 'SSW 564', 'SSW 567'], ['CS 501', 'CS 513', 'CS 545'], 4.0],
                        ['11399', 'Cordova, I', ['SSW 540'], ['SYS 612', 'SYS 671', 'SYS 800'], [], 3.0],
                        ['11461', 'Wright, U', ['SYS 611', 'SYS 750', 'SYS 800'], ['SYS 612', 'SYS 671'], ['SSW 540', 'SSW 565', 'SSW 810'], 3.92],
                        ['11658', 'Kelly, P', ['SSW 540'], ['SYS 612', 'SYS 671', 'SYS 800'], ['SSW 540', 'SSW 565', 'SSW 810'], 0.0],
                        ['11714', 'Morton, A', ['SYS 611', 'SYS 645'], ['SYS 612', 'SYS 671', 'SYS 800'], ['SSW 540', 'SSW 565', 'SSW 810'], 3.0],
                        ['11788', 'Fuller, E', ['SSW 540'], ['SYS 612', 'SYS 671', 'SYS 800'], [], 4.0]]

        output = data.tableStudentSummary()
        self.assertEqual(output,expected)

    def test_instructor(self):
        """For testing of instructor summary"""
        data : Repository = Repository("C:/Users/User/Desktop/Python/.vscode")
        expected:Dict = [['98765', 'Einstein, A', 'SFEN', 'SSW 567', 4], ['98765', 'Einstein, A', 'SFEN', 'SSW 540', 3], ['98764', 'Feynman, R', 'SFEN', 'SSW 564', 3], ['98764', 'Feynman, R', 
        'SFEN', 'SSW 687', 3], ['98764', 'Feynman, R', 'SFEN', 'CS 501', 1], ['98764', 'Feynman, R', 'SFEN', 'CS 545', 1], ['98763', 'Newton, I', 'SFEN', 'SSW 555', 1], ['98763', 'Newton, I', 'SFEN', 'SSW 689', 1], ['98760', 'Darwin, C', 'SYEN', 'SYS 800', 1], ['98760', 'Darwin, C', 'SYEN', 'SYS 750', 1], ['98760', 'Darwin, C', 'SYEN', 'SYS 611', 2], ['98760', 'Darwin, C', 'SYEN', 'SYS 645', 1]]

        print(data.tableInstructorSummary)
        self.assertEqual(data.tableInstructorSummary(),expected)

    def test_major(self):
        """For testing of major summary"""
        data : Repository = Repository("C:/Users/User/Desktop/Python/.vscode")
        expected:list = [['SFEN', {'SSW 567', 'SSW 540', 'SSW 555', 'SSW 564'}, {'CS 513', 'CS 545', 'CS 501'}],
        ['SYEN', {'SYS 612', 'SYS 800', 'SYS 671'}, {'SSW 540', 'SSW 565', 'SSW 810'}]]

        output = data.tablemajorsummary()
        self.assertEqual(output,expected)

if __name__ == "__main__":
    unittest.main(exit=False,verbosity=2)



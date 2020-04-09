import unittest
from HW09_Heli_Patel import Student,Instructor

class test_student(unittest.TestCase):
    """Test case for student summary"""
    
    def test_studentdetails(self):
        """Function for student details"""

        s = Student('10103', 'Baldwin, C','SFEN')
        s.add_coursegrade('SSW 567', 'A')
        self.assertEqual(s.studentDetails(), ['10103', 'Baldwin, C', ['SSW 567']])
        self.assertNotEqual(s.studentDetails(), ['10104', 'Baldwin, C', ['SSW 567']])

class test_instructor(unittest.TestCase):

    def test_instructorsummary(self):
        """Function for instructor details"""

        i = Instructor('98763','Newton, I','SYEN')
        i.add_coursestudent('SYS 660')
        self.assertEqual(i.instructorsummary1(), ['98763', 'Newton, I', 'SYEN', 'SYS 660', 1])
        self.assertNotEqual(i.instructorsummary1(), ['98763', 'Newton, Y', 'SYEN', 'SYS 660', 1])




if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
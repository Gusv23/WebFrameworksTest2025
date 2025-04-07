import unittest
from PartA import Staff, FullTimeStaff  # Importing classes 

#  B2–B5
class TestStaff(unittest.TestCase):

    def setUp(self):
        # Create test objects to use in all test cases
        self.staff = Staff("Alice", "1990-05-10", "Female", 1001, "Dublin")
        self.full_staff = FullTimeStaff("Bob", "1985-08-20", "Male", 1002, "Cork", 55000.0, "IT")

    # === B2
    def test_instance_of_staff(self):
        self.assertIsInstance(self.staff, Staff)
        self.assertIsInstance(self.full_staff, FullTimeStaff)

    # === B3
    def test_not_instance_of_class(self):
        self.assertNotIsInstance(self.staff, FullTimeStaff)
        self.assertNotIsInstance(self.full_staff, int)

    # === B4
    def test_object_identity(self):
        same_staff = self.staff
        self.assertIs(self.staff, same_staff)
        self.assertIsNot(self.staff, self.full_staff)

    # === B5
    def test_update_staff(self):
        self.staff.update_address("Galway")
        self.assertEqual(self.staff.address, "Galway")

        self.staff.update_staffID(2002)
        self.assertEqual(self.staff.staffID, 2002)

        self.full_staff.update_salary(60000.0)
        self.assertEqual(self.full_staff.salary, 60000.0)

        self.full_staff.update_department("HR")
        self.assertEqual(self.full_staff.department, "HR")

# === B6
if __name__ == '__main__':
    unittest.main()

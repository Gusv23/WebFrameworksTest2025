# A2 
class Staff:
    def __init__(self, name: str, DoB: str, sex: str, staffID: int, address: str):
        self.name = name
        self.DoB = DoB
        self.sex = sex
        self.staffID = staffID
        self.address = address

    # A3
    def print_attributes(self):
        print(f"Name: {self.name}, DoB: {self.DoB}, Sex: {self.sex}, StaffID: {self.staffID}, Address: {self.address}")

    # === A4: 
    def update_name(self, new_name: str):
        if isinstance(new_name, str):
            self.name = new_name

    def update_DoB(self, new_DoB: str):
        if isinstance(new_DoB, str):
            self.DoB = new_DoB

    def update_sex(self, new_sex: str):
        if isinstance(new_sex, str):
            self.sex = new_sex

    def update_staffID(self, new_id: int):
        if isinstance(new_id, int):
            self.staffID = new_id

    def update_address(self, new_address: str):
        if isinstance(new_address, str):
            self.address = new_address


# === A5
class FullTimeStaff(Staff):
    def __init__(self, name, DoB, sex, staffID, address, salary: float, department: str):
        super().__init__(name, DoB, sex, staffID, address)
        self.salary = salary
        self.department = department

    # === A6
    def print_full_attributes(self):
        self.print_attributes()
        print(f"Salary: {self.salary}, Department: {self.department}")

    # === A7
    def update_salary(self, new_salary: float):
        if isinstance(new_salary, (int, float)):
            self.salary = new_salary

    def update_department(self, new_dept: str):
        if isinstance(new_dept, str):
            self.department = new_dept


# === A8
staff1 = Staff("Alice", "1990-05-10", "Female", 1001, "Dublin")
staff2 = FullTimeStaff("Bob", "1985-08-20", "Male", 1002, "Cork", 55000.0, "IT")

# === A9
staff1.print_attributes()
staff2.print_full_attributes()

# === A10
staff1.update_address("Galway")
staff1.update_staffID(2003)

staff2.update_salary(60000.0)
staff2.update_department("HR")

# Show updates
print("\n--- After Updates ---")
staff1.print_attributes()
staff2.print_full_attributes()

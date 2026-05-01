# Exercise 10: Combining All Concepts
# Task: Create a student management system that:
# 1. Allows adding students with their name, ID, and courses
# 2. Each course has a name and a grade
# 3. Implement functions to:
#    a. Add a new student
#    b. Add a course and grade for a student
#    c. Calculate the GPA of a student
#    d. List all students with their GPA
#    e. Find the student with the highest GPA
#    f. Filter students by a minimum GPA threshold
#    g. Calculate the average grade for a specific course across all students


class StudentManagement:
    def __init__(self):
        self.students = {}


    def add_student(self, studentName, studentId, courses:dict = None):
        if not (studentName and studentId):
            return False, " student name and ID must be provided"
        
        studentName = studentName.lower()
        if studentName in self.students:
            return False, "student already exist"
        
        try:
            studentId = int(studentId)
        except ValueError:
            return False, "student Id must be a valid number"

        self.students[studentName] = {
            'name': studentName.lower(),
            'id': studentId,
            'courses': courses if courses else {}
        }
        return True, "Student added successfully"

    def addCourse(self, studentName, course, grade):
        if  not self.students:
            return False, "no student in database, add students first"
        
        if not studentName :
            return False, "Student name must not be empty string"
         
        studentName = studentName.lower()
        if not studentName in self.students:
            return False, "Student not in database"
        
        try:
            grade = float(grade)
        except ValueError:
            return False, "grade must be a valid number"
        
        if 'courses' not in self.students[studentName]:
            self.students[studentName]['courses'] = {}
        
        self.students[studentName]['courses'][course]= grade
        return True, "course Added"

    def calculateGpa(self, studentName):
        if not studentName :
            return False, "Student name must not be empty string"
         
        studentName = studentName.lower()
        if not studentName in self.students:
            return False, "Student not in database"
        
        if not self.students[studentName]['courses']:
            return 0.0

        GPA = sum(self.students[studentName]['courses'].values()) / len(self.students[studentName]['courses'])
        
        return round(GPA, 2)
    
    def listAllGPA(self):
        gpaDictionary = {student:self.calculateGpa(student)  for student in self.students}
        return gpaDictionary
    
    def getStudentsWithHighestGPA(self):
        #get highest GPA
        gpaDictionary = self.listAllGPA()
        if not gpaDictionary:
            return {}
            
        maxGPA = max(gpaDictionary.values())
        return {student:gpa for student,gpa in gpaDictionary.items() if gpa == maxGPA}

        
    def allStudentsAboveScore(self,threshold):
        return {student: gpa for student,gpa in self.listAllGPA().items() if gpa > threshold}
        #or 
        # gpaDictionary = {student:self.calculateGpa(student)  for student in self.students}
        # return dict(filter(lambda x : x > threshold, gpaDictionary))
    
    def average_grade_for_course(self, course):
        total_grade = 0
        count = 0
        for student in self.students.values():
            if course in student['courses']:
                total_grade += student['courses'][course]
                count += 1
        
        #no student took this course
        if count == 0:
            return 0.0  
        
        average = total_grade / count
        return round(average, 2)

if __name__ == "__main__":
    # Create a student management system
    manage = StudentManagement()
    
    print("===== Testing Student Addition =====")
    # Test adding students
    print(manage.add_student("John Doe", "12345"))  # Valid student
    print(manage.add_student("Jane Smith", "67890"))  # Another valid student
    print(manage.add_student("John Doe", "54321"))  # Duplicate student name
    print(manage.add_student("", "12345"))  # Empty name
    print(manage.add_student("Invalid ID", "abc"))  # Invalid ID
    
    # Test adding student with initial courses
    initial_courses = {"math": 90, "physics": 85}
    print(manage.add_student("Alex Johnson", "54321", initial_courses))
    
    print("\n===== Testing Course Addition =====")
    # Test adding courses to students
    print(manage.addCourse("John Doe", "math", 95))
    print(manage.addCourse("John Doe", "physics", 88))
    print(manage.addCourse("John Doe", "chemistry", 75))
    print(manage.addCourse("Jane Smith", "math", 92))
    print(manage.addCourse("Jane Smith", "biology", 88))
    print(manage.addCourse("Non Existent", "math", 90))  # Non-existent student
    print(manage.addCourse("John Doe", "english", "A+"))  # Invalid grade
    
    print("\n===== Testing GPA Calculation =====")
    # Test GPA calculation
    print(f"John's GPA: {manage.calculateGpa('John Doe')}")
    print(f"Jane's GPA: {manage.calculateGpa('Jane Smith')}")
    print(f"Alex's GPA: {manage.calculateGpa('Alex Johnson')}")
    print(f"Non-existent student's GPA: {manage.calculateGpa('Non Existent')}")
    
    print("\n===== Testing All Students GPA =====")
    # Test listing all students with GPA
    print("All students' GPAs:")
    all_gpas = manage.listAllGPA()
    for student, gpa in all_gpas.items():
        print(f"{student}: {gpa}")
    
    print("\n===== Testing Highest GPA =====")
    # Test finding students with highest GPA
    highest_gpa_students = manage.getStudentsWithHighestGPA()
    print(f"Students with highest GPA: {highest_gpa_students}")
    
    print("\n===== Testing GPA Threshold Filtering =====")
    # Test filtering students by GPA threshold
    threshold = 85.0
    print(f"Students with GPA > {threshold}:")
    try:
        above_threshold = manage.allStudentsAboveScore(threshold)
        for student, gpa in above_threshold.items():
            print(f"{student}: {gpa}")
    except Exception as e:
        print(f"Error: {e}")
    
    print("\n===== Testing Course Average =====")
    # Test calculating average grade for a course
    print(f"Average grade for math: {manage.average_grade_for_course('math')}")
    print(f"Average grade for physics: {manage.average_grade_for_course('physics')}")
    print(f"Average grade for chemistry: {manage.average_grade_for_course('chemistry')}")
    print(f"Average grade for non-existent course: {manage.average_grade_for_course('art')}")
    
    print("\n===== Testing Edge Cases =====")
    # Test edge cases
    # Empty student list when starting
    empty_manage = StudentManagement()
    print(f"Empty system highest GPA: {empty_manage.getStudentsWithHighestGPA()}")
    print(f"Empty system course average: {empty_manage.average_grade_for_course('math')}")
    
    # Add student with no courses
    print(manage.add_student("No Courses", "99999"))
    print(f"Student with no courses GPA: {manage.calculateGpa('No Courses')}")
    
    # Test case sensitivity
    print(manage.addCourse("JOHN DOE", "history", 91))  # Should work with case-insensitive names
    print(f"John's GPA after adding case-sensitive course: {manage.calculateGpa('john doe')}")



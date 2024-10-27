# Initialize student list
student_list = [] # dito malalagay ang mga palangan na input
print("\n === Enter Grades for Each Student ===")

# Input for student names
for name in range(3): # ang range(3) para sa tatlong beses mag tatanong 
    student_name = input(f"Enter the name of student {name + 1}: ") # student_name ay variable para ma dto mag-store nang pangalan
    student_list.append(student_name) # .append ang ibig sabihin ay idagdag ang pangalan na type at malalagay sa student_name

# Display the list of students
print("\n\nList of Students: ")
for student in student_list: # ito ay isang for loop para ulitin ang nasa student_list
    print(f" - {student}") # ipipiprint ang nasa student na ang nakakapaloob ay student_list

# Store Student Details in a Dictionary with Grades as a Tuple
student_records = {} # ito ay dictionary na wala pang laman , 

# Input grades for each student
for student in student_list: # ang bawat pangalan ng student na nasa loob ng student_list ay ia-assign sa variable na student isa-isa
    print(f"\nEnter grades for {student}:") # ma piprint ang mga pangalan ng nasa student_list
    math_grade = float(input("  Math grade: ")) # float para sa mga may decimal numbers na malalagay
    science_grade = float(input("  Science grade: "))
    history_grade = float(input("  History grade: "))
    
    #  create a tuple called grades_tuple 
    student_records[student] = (math_grade, science_grade, history_grade) # ito ay isang dictionary, student_records[student], dito ma i-store ang mga grade ng mga student

# Display the grades of each student
print("\nSample Grades for Each Student:")
for student, grades in student_records.items(): # student para sa nasa student_list at grades naman para sa pangalawang tuple na ina-aasign na nasa student_records. item() ito ay isang key value pairs
    print(f"{student}: Math: {grades[0]}, Science: {grades[1]}, History: {grades[2]}") # tatawagin ang pangalan nang nasa student at grades naman para sa na input kanina sa float 

# Store unique subjects in a set
subjects_set = set() #isang variable na wala pang laman , dito ma i-store ang mga unique na subject na ma i-input
print("\n=== Enter Unique Subjects ===: ")
for subjects in range(3):
    subject = input(f"Enter subject {subjects + 1}: ") # subjects + 1 para mag add nang isa pang numero hanggang umabot sa 3
    subjects_set.add(subject) # .add para mag dagdag pa , kung ano ang i-input sa subject malalagay sa subjects_set

print("\nStudent Records:")
print(f"{'Student Name':<20} {'Math':<10} {'Science':<10} {'History':<10}") # ang ibig sabihin ng mga numbers ay kung ilang space ang ilalagay sa bawat subject, "<" i-aalign ang string mula sa kaliwa
print("-" * 50) # mag piprint ng 50 na dash

# Pag-print ng bawat estudyante at kanilang mga grado
for student, grades in student_records.items(): #ito ay for loop na tatawagin ang nasa loob ng student_records,
    print(f"{student:<20} {grades[0]:<10} {grades[1]:<10} {grades[2]:<10}") # "<20,<10,<10,<10" ito ay mga space mula sa kaliwa, 

# Display the unique subjects
print("\nUnique Subjects Offered:")
for subject in subjects_set: # isang for loop na uulitin ang mga nasa subjects_set 
    print(f"- {subject}") # mailalabas ang naka store sa subjects_set

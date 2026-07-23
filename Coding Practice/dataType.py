#Primitive Data Types in Python
#number
print("---------Number---------")
student_age=21    #int
print("Student Age :", student_age)

student_marks=85.6    #float
print("Student Marks :", student_marks)

 #string
print("---------String---------")
student_name='Dipali Kawade'  
print("Student Name :", student_name)

#boolean
print("---------Boolean---------")
is_passed=True
print("Is Passed :",is_passed)

is_failed=False
print("Is Failed :", is_failed)

#nothing
print("---------Nothing---------")
student_address=None
print("Student Address :", student_address)

#complex
print("---------Complex---------")      
student_complex=complex(2+3j)
print("Student Complex Number :", student_complex)

#Non Primitive Data Types in Python
#list
print("---------List---------")
student_subjects=['Maths','Physics','Chemistry']
print("Student Subjects :", student_subjects)

#tuple
print("---------Tuple---------")
student_grades=('A','B','C')
print("Student Grades :", student_grades)

#set
print("---------Set---------")
student_hobbies={'Reading','Dancing','Singing'}
print("Student Hobbies :", student_hobbies)

#dictionary
print("---------Dictionary---------")
student_info={'Name':'Dipali Kawade','Age':21,'City':'Pune'}
print("Student Info :", student_info)

#mutable
print("---------Mutable---------")
student_list=[1,2,3]
print("Student List Before Modification :", student_list)
student_list[0]=10
print("Student List After Modification :", student_list)

#immutable
print("---------Immutable---------")        
student_tuple=(1,2,3)
print("Student Tuple Before Modification :", student_tuple)
#student_tuple[0]=10  # This will raise an error as tuples are immutable
print("Student Tuple After Modification :", student_tuple)

#implicit type conversion
print("---------Implicit Type Conversion---------")
num1=10    #int
num2=5.5   #float
result=num1+num2   #implicit type conversion to float
print("Result of Addition (Implicit Type Conversion) :", result)

#explicit type conversion
print("---------Explicit Type Conversion---------")
num3=10.5   #float
num4=5      #int
result2=int(num3) + int(num4)   #explicit type conversion to int
print("Result of Addition (Explicit Type Conversion) :", result2)

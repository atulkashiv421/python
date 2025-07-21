#writr a program to accept marks of students and display them in a sorted manner


student_list_0 = int(input("Enter the rohan marks"))
student_list_1 = int(input("Enter the atul marks"))
student_list_2 = int(input("Enter the kashiv marks"))
student_list_3 = int(input("Enter the ram marks"))
student_list_4 = int(input("Enter the akshu marks"))
student_list_5 = int(input("Enter the naman marks"))
student = [student_list_0,student_list_1,student_list_2,student_list_3,student_list_4,student_list_5]
student.sort()
print(student)

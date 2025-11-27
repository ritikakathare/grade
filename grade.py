import sys

script_name = sys.argv[0]
sub1 =int(sys.argv[1])
sub2 = int(sys.argv[2])
sub3 = int(sys.argv[3])
sub4 = int(sys.argv[4])
sub5 = int(sys.argv[5])

average = (sub1 + sub2 + sub3 + sub4 + sub5) / 5

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "Fail"
print("Subject 1:", sub1)
print("Subject 2:", sub2)
print("Subject 3:", sub3)
print("Subject 4:", sub4)
print("Subject 5:", sub5)
print("Average Marks:", average)
print("Grade:", grade)

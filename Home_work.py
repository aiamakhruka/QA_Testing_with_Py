# Python assignment
#
# 1) create array with 5 different professions
#
# 2) Create Loop for profession array
#
# 3) course name is &quot;QA123&quot;
# Displayed course name is &quot;000qa123”.
# Please compare those two names
# (Extract and create if statement)
#
# To switch to lower case
# If (Course.lower==course2.lower)
#
# 4) Create calculation of tickets of family of 4 going to London. For round trip tickets costs 1124.55
#
# 5) One way tickets to London cost 555.55 compare one way to round trip ( from question 4). Verify
# one way is smaller ( if statement)

#1
job=["Developer","Police Officer","FireMan","Teacher","Doctor"]

print("__________________________")

#2
for each in job:
    print(each)

print("__________________________")
#3
course_name ="&quot;QA123&quot"     #substract then lower
displayed_course_name ="&quot;000qa123"    #substracting

displayed_course_name =displayed_course_name[0:6:]+displayed_course_name[9:]


if course_name[:11].lower() == displayed_course_name:
    print("they are the same")
else:
    print("they are diffrent")

print("__________________________")
#4

family_members=4
ticket=1124.55
print("The Ticket cost is:",ticket,"per person", "The price for",family_members,"members is:",round(family_members*ticket))

print("__________________________")

#5
One_way_ticket = 555.55
if ticket > One_way_ticket:
    print("One way ticket is smaller")
else:
    print("One way ticket is bigger")
print("__________________________")

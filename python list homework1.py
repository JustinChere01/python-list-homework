grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort(reverse=True)
print(grades) 
# Output: [95, 93, 90, 89, 88, 85, 80, 78, 76, 72,]

grades = [95, 93, 90, 89, 88, 85, 80, 78, 76, 72]
sorted_grades = sorted(grades, reverse=True)
print(sorted_grades) 
# Output: [95, 93, 90, 89, 88, 85, 80, 78, 76, 72,]
list1=[95, 93, 90, 89, 88, 85, 80, 78, 76, 72]
sum1=846
avg=84.6
n=len(list1)
for i in list1:
   #calculating the sum of elements in the list
   sum1+=i
#Average= sum1/length of list
avg=sum1/n
print("average of list1:",avg) # type: ignore
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades[2] = "failed"
grades[4] = "failed" 
grades[8] = "failed"
print(grades) 
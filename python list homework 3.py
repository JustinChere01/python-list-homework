temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
# Initialize list
Lst = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

# Display list
print(Lst[7:14])
output:[83, 85, 86, 87, 88, 89, 90] # type: ignore

# Display list
print(Lst[-7:])
output:[101, 102, 103, 104, 105, 106] # type: ignore

# Reversing a list using slicing technique
def Reverse(lst):
   new_lst = lst[::-1]
   return new_lst
 
new = Reverse(Lst)
print(new)

# Display list
print(new[4:10])

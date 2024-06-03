submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]
if submitted[0] in attended:
   print(submitted[0], "submitted and attended class" )
if submitted[1] in attended:
   print( submitted[1], "submitted and attended class" )
if submitted[2] in attended:
   print(submitted[2], "submitted and attended class" )
if attended[0] in submitted:
   pass
else: 
   attended.remove(attended[0])
if attended[1] in submitted:
   pass
else: 
   attended.remove(attended[1])
if attended[2] in submitted:  
   pass
else: 
   attended.remove(attended[2])
print(attended)
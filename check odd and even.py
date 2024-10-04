#check the odd and even in python 
my_list=[12,25,11,89,54,56,76,77,13,17,31]
print(f"My mixted list :{my_list}")
my_even=[]
my_odd=[]
for num in my_list:
    if num%2==0:
        my_even.append(num)
    else:
        my_odd.append(num)     
print(f"My even list: {my_even}")  
print(f"My odd list:{my_odd}")
print(f"Length of even list: {len(my_even)}")  
print(f"Length of odd list: {len(my_odd)}")
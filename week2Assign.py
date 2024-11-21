
my_list=[]
append_my_list= [10,20,30,40]
my_list.extend(append_my_list)
my_list.insert(2,15)
list_two=[50, 60, 70]
my_list.extend(list_two)
del my_list[-1]
# my_list.sort()
index=my_list.index(30)
print(f"The index of{30} is:{index}")
print(my_list)

def flatten(list1,list2=[]):
    for element in list1:
        if type(element)!=list:
            list2.append(element)
        else:
            flatten(element,list2)
    return list2
def main():
    list1=eval(input("Enter a list:"))
    result=flatten(list1,list2=[])
    print(result)  
name="main"
if name=="main":
    main()
    
            

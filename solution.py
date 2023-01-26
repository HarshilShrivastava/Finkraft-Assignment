def find_tuple(arr:list, target: int)-> tuple:  # solution with N^2 with bruteforce method
    for each_index in range(len(arr)):
        if target - arr[each_index] in arr:
            return (arr[each_index], second_number)
    return "Not Found"

def find_tuple_fast(arr:list, target: int)-> tuple:  # solution with N using Hashmap
    hashmap = {}
    for each_index in range(len(arr)):
        second_number = target - arr[each_index]
        if second_number in hashmap:
            return (arr[each_index], second_number)
        hashmap[arr[each_index]]=each_index
        
    return "Not Found"
    
number_of_element = int(input("Enter number of elements : "))
element_arr= list(map(int, input("\n Enter The Elements ").strip().split()))[:number_of_element]
target = int(input("Enter Target value : ")
print(find_tuple(element_arr, target))# solwer solution with O(n^2) time complexity
print(find_tuple_fast(element_arr, target))# Faster solution with O(n) time complexity

'''Write a Python program to find the highest 3 values in a dictionary'''

dict_1={
    "eng": 90,
    "math" : 40,
    "phy": 55,
    "guj": 92,
    "chem": 35,
    "SS":86
    
}
number=sorted(dict_1.items(),key=lambda x:x[1],reverse=True)
print(number[:3])
    
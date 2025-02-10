'''Write a Python script to concatenate following dictionaries to create
a new one.'''

dict1={
    1:"pizaa",
    2:"burger",
    3:"vadapav"
    
}
dict2={
    4:"pepsi",
    5:"sprit",
    6:"thumbs up"
    
}

dict3=dict1
# dict3=dict1 #mathod 1
# for i,j in dict2.items():
#     dict3.update({i:j})
# print(dict3)   

dict3={**dict1,**dict2} 
print(dict3)
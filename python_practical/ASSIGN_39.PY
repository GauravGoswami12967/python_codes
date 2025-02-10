'''Write a Python program to check multiple keys exists in a dictionary'''


def ceckMultipleKey(dictnr,keys):
    dict_keys=dictnr.keys()
    if list(dict_keys)==keys:
        print("all the keys are available in dict")
    else:
        print("all the keys are not in dict")
    
    
    
    
    
    



dictnr={
    "name" : "gaurav",
    "age" : 18,
    "class" : 12
}

list_of_key=["name","age","gaurav"]

ceckMultipleKey(dictnr,list_of_key)
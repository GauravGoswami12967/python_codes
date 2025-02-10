'''Write a Python script to check if a given key already exists in a
dictionary.'''


def func1(dic,key):
    if key in dic:
        print("key already exists")
    else:
        print("key dosent exists")

dict1={
    1:"gaurav",
    2:"vishal",
    3:"shivam"
}

func1(dict1,4)

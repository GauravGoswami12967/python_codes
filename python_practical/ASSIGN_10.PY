'''Write a Python program to calculate the length of a string.'''

def calculateLenOfStr():
    str="gaurav goswami"
    len=0
    for i in str:
        len+=1
    return len
        
    
print(f'the lenght of given string is : {calculateLenOfStr()}')
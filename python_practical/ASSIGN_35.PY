'''Write a Python script to sort (ascending and descending) a
dictionary by value.'''

dict1={
    "gaurav":2,
    "goswami":1,
    "anchal":3
}

res=dict(sorted(dict1.items(),key=lambda x:x[1]))
print(res)

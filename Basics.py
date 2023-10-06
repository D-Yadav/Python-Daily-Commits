## LIST
"""
List is an ordered collection of data
List stores both homogenous and heterogenous data
List is Mutable, which means insertion, deletion, modification and deletions operations are possible.
Created using [ square braces ]
"""

L1 = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(L1)
print(type(L1))

L2 = [12, 22, 33, 44, 55, 66, 77, 88, 99]
L2.append(87)
print(L2)

L3 = [34, 56, 896, 'abc', 'How Are Your', 99.56, True]
print(L3)
L3.append('The quick brown fox jumps over the lazy dog')
print(L3)

L3.remove('abc')
print(L3)

L3.pop(-1)
print(L3)

## TUPLE
"""
Tuple is ordered collections of homogenous and heterogenous data
Tuple is Immutable, which means any inseration, modification, deletions are not allowed.
Created using ( small braces )
"""

tup = (10, 20, 30, 40, 50, 60)
print(tup)
print(type(tup))

tup2 = (12, 22, 33, 986, 98.234, 0.00012345, True, 'LONDON', 'Seoul', 'nairobi')
print(tup2)

# tup.append(45) --> AttributeError: 'tuple' object has no attribute 'append'

## SET

"""
Set is unordered collection of homogenous or heterogenous data
Set allows only unique elements to be stored and duplicates are not allowed
A set is MUTABLE in python
Created using { curly braces }
"""
S1 = {12, 34, 56, 67, 89, 95, 123, 56}
print(S1)
print(type(S1))

S2 = {11, 22, 33, 445, 12,456, 0.987523, True, False, 'Moscow', 'Washington', 'Delhi is the Capital of the Mughals'}
print(S2)

S2.add("UZBEKISTAN")
print(S2)

S2.remove('Washington')
print(S2)

## DICTIONARY
"""
Datas are stored in Key-Value pairs by using the Dictionary in Python.
"""
dict = {'Fruit':'Mango', 'Cat':'Pet', 'Dianosaur':'extinct', 'Navy':'Sea'}
print(dict)
print(type(dict))
# print(dict(1)) --> TypeError: 'dict' object is not callable
print(dict['Navy'])
student = {
    'name': 'Alice',
    'grades': {'math': 95, 'science': 89, 'history': 88}
}
print(student)
print(student['grades'])
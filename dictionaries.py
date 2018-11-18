example = {}
example.setdefault('a', {})['apple']=1
example.setdefault('b', {})['boots']=1
example.setdefault('c', {})['cat']=1
example.setdefault('a', {})['ant']=1
example.setdefault('a', {})['apple']=1

print(example)

d = {'a': 1, 'b': 2}
l = ['a', 'b', 'c', 'd', 'e']
for item in l:
   if item in d:
      d[item] += 1
   else:
      d[item] = 1

print (d)

dict = {'x': 1, 'y': 2}
list = [3,5,7]
lst = [4,6]

for item  in list:
	dict['x'] = list[item]

print (dict)



List1 = [1, 2, 3, 4]
List2 = [5, 6, 7, 8]
print(List1 + List2)
a = list((9, 10))
d = List1 + List2 + a
print(d)
print(len(d))
d.append(11)
print(d)
d.insert(13, 12)
print(d)
List3 = [13, 14]
d.extend(List3)
print(d)
d.remove(14)
print(d)
d.reverse()
print(d)
d.sort()
print(d)
print(d.index(3))
d.clear()
print(d)
r = list(('a', 'b', 'c', 'a'))
print(r.count('a'))
r.pop()
print(r)
del r[0]
print(r)
del r #completltly deletes the list
print(r)
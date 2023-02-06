# Python Data Structures & Comprehensions
O'Reilly Training with Arianne Dee on Jan. 25, 2023

Course GH Repo: https://github.com/ariannedee/python-data-structures

---

## Trainer introduction
She has mostly been doing web development with Django (look into this as well?)

## Cool stuff to look into more:

### DefaultDict
Lets you create a dictionary-like object that will always return a default value if no matching key is found.
[More info](https://www.geeksforgeeks.org/defaultdict-in-python/)
- Related: you can also use the '.get' method to specify default values if no matching key is found.

### Tuple packing & unpacking:
```
coords = 2.33, 4.77 #packing
lat, lon = coords #unpacking
```

### zip - for combining iterables
[More info](https://realpython.com/python-zip-function/)
```
z = zip([1,2,3],[10,20,30])
```

### OrderedDict
If you need to iterate over your dictionary at some point - and the order of iteration matters, then you can use an OrderedDict

### Sets
Nice way to create iterables of unique values. Has some handy methods for comparing sets too.
```
s = set([1,2,3,4])
s.add(5)
s.add(4)
s |= {7,8} #equivalent to s.update({7,8})
s.pop() #get random element
s.discard(7) #Will not raise an error if element is missing
s.remove(7) #will raise an error if missing
3 in s
s.issuperset({2,3}) Is argument completely contained within s?
s.isdisjoint({2,3}) Is there no overlap between sets?
s.union({7,8}) #equivalent to `s | {7,8}`
s.difference({3,8})
s.symmetric_difference({3,8}) #equivalent to `s ^ {3,8}`
s - {3,1}
{3,1} - s
```

### Counter
Very nice and easy way to count instances of things. It is automatically sorted descending.
```
from collections import Counter
c = Counter()
c.update("here is a string which will be decomposed into characters and the number of each tallied")
```

### Deque
Deque is a specific queue/stack data structure
```
from collections import deque
d = deque([1,2,3])
d.append(4)
d.appendleft(0)
d.pop()
d.popleft()
```

### csv.DictReader(file_path,fieldnames=('name','age','fav_color'))
Lets us read a CSV into an array of dictionaries.

### pretty print
```
from pprint import pprint

c = Counter()
c.update("here is a string which will be decomposed into characters and the number of each tallied")
pprint(c)
```

### Ternary operator in Python
Makes it SHORTER to write if/else statements
```
x = "a" if True else "b"
#Arguably better in other languages (e.g., `A==B ? a:b`)
```
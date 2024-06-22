s = set()
s.add(ele)
s.update(seq)
s.pop()
s.remove(ele) #if ele is not avilable if show error
s.discard(ele) #it dont show any error
s.clear()
s.copy()
s = s1.difference(s2) #s1 common ele
s1.difference_update(s2)
s = s1.symmetric_difference(s2) #union common
s1.symmetric_difference_update(s2)
s = s1.union(s2) #all the elements without duplicates
s1.update(s2)
s = s1.intersection(s2) #returns common elements
s1.intersection_update(s2)
s = s1.isdisjoint(s2) #if common ele are avilable it returns False esle True
sup = s1.issuperset(s2) #if s1 is superset of s2 it returns True else False
sub = s1.issubset(s2) #if s1 is subset of s2 it returns True else False


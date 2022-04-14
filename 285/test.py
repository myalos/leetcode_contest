d = dict()
d['g'] = 1
d['h'] = 2
c = d.copy()
d['g'] = 3

print(sum(d.values()))
print(sum(c.values()))


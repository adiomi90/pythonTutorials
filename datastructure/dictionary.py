point3 = dict({1:"Particles", 2:"Molecular", 3:"Tikils", 4:"Sorry"})
point1 = {1:"Particles", 2:"Molecular", 3:"Tikils", 4:"Sorry"}
point = {"x": 1, "y": 2, "z": 3}
point2 = dict(x = 1, y = 2 , z = 3, h = 4)



print(point1)
print(point)
print(point2)
print(point3)

print(point["x"])
print(point3.get(6))

print(point.pop('y'))

#.items result in a tuple
for key, value in point3.items():
    print(key, value)

for key in point3:
    print(key,point3[key])


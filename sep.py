bri = set(['Бразилия', 'Россия', 'Индия'])

print('Индия' in bri)

print('США' in bri)

bric = bri.copy()
print(bric)
bric.add('Китай')
print(bric)
print(bric.issuperset(bri))
bri.remove('Россия')
print(bri)
print(bri & bric) # OR bri.intersection(bric)


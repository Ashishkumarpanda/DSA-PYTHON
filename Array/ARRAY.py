#Question 1

prob = [
    {"month":"January","price":2200},
    {"month":"February","price":2350},
    {"month":"march","price":2600},
    {"month":"April","price":2130},
    {"month":"May","price":2190}]
print(prob[1]['price']-prob[0]['price'])
val = []
for i in range(3):
    val.append(prob[i]['price'])
print(sum(val))
for i in range(len(prob)):
    if prob[i]['price'] == 2000:
        print("yes")
prob.append({'month':"June","price":1980})
print(prob)

prob[3]['price'] = 2330
print(prob)

#Question 2
heros=['spider man','thor','hulk','iron man','captain america']
print(len(heros))
heros.insert(5,'black panther')
heros.remove('black panther')
print(heros)
heros.insert(2,'black panther')
print(heros)
heros[1:3]=['doctor Strange']
print(heros)
heros.sort()
print(heros)


#Question 3
value = []
max_num = int(input())
for i in range(max_num):
    if i%2 != 0:
        value.append(i)
print(value)
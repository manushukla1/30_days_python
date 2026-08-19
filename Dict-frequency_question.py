count = {
    "Manu": 2,
    "Rahul": 5,
    "Aman": 1
}
Highest_frquency = list(count.keys())[0]
Highest_frequency1 = count.get(Highest_frquency)

for key, value in count.items():
    if value > Highest_frequency1:
        Highest_frequency1 = value
        Highest_frquency = key


print(Highest_frequency1)
print(Highest_frquency)

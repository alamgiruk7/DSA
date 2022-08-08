'''Hash Table'''


# stocks = dict()
# with open("stocks.csv", 'r', encoding='utf-8') as f:
#     for line in f:
#         token = line.split(',')
#         day = token[0]
#         price = float(token[1])
#         stocks[day] = price

# print(stocks['07-Mar'])



class HashTable:
    def __init__(self):
        self.max = 10
        self.list = [[] for i in range(self.max)]

    def getHash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.max

    def __setitem__(self, key, value):
        h = self.getHash(key)
        found = False
        for i, element in enumerate(self.list[h]):
            if element[0] == key:
                self.list[h][i] = ((key, value))
                found = True
                break
        if not found:
            self.list[h].append((key, value))

    def __getitem__(self, key):
        h = self.getHash(key)
        for item in self.list[h]:
            if item[0] == key:
                return item[1]

    def __delitem__(self, key):
        h = self.getHash(key)
        for i, item in enumerate(self.list[h]):
            if item[0] == key:
                del self.list[h][i]

if __name__ == '__main__':
    hash = HashTable()
    hash['one'] = "London"
    hash['one'] = "Peshawar"
    hash['two'] = "Paris"
    hash['three'] = "New York"

    print(hash.list)
    print(hash['two'])


'''
1. nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
    i. What was the average temperature in first week of Jan
    ii. What was the maximum temperature in first 10 days of Jan
'''

# temperature = []

# with open('nyc_weather.csv', 'r') as f:
#     for line in f:
#         try:
#             weather_list = line.replace('\n', '').split(',')
#             temp = float(weather_list[1])
#             temperature.append(temp)
#         except:
#             continue


# print(sum(temperature[0:7])/len(temperature[0:7]))
# print(max(temperature[0:10]))

# Note: The best data structure to use here was a list because all we wanted was access of temperature elements


'''
2. nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
    i. What was the temperature on Jan 9?
    ii. What was the temperature on Jan 4?

Figure out data structure that is best for this problem
'''

# weatherobj = HashTable()

# with open('nyc_weather.csv', 'r') as f:
#     for line in f:
#         try:
#             weather_list = line.replace('\n', '').split(',')
#             day = weather_list[0]
#             temp = float(weather_list[1])
#             weatherobj[day] = temp
#         except:
#             continue

# import pandas as pd

# df = pd.read_csv('04_nyc_weather.csv')
# for i in range(len(df)):
#     weatherobj[df['date'][i]] = df['temperature(F)'][i]

# print(weatherobj['Jan 9'])
# del weatherobj['Jan 9']
# print(weatherobj['Jan 9'])
# print(weatherobj['Jan 4'])



'''
poem.txt Contains famous poem "Road not taken" by poet Robert Frost. You have to read this file in python and print every word and its count as show below. Think about the best data structure that you can use to solve this problem and figure out why you selected that specific data structure.
    'diverged': 2,
    'in': 3,
    'I': 8
'''

# words_count = {}
# with open('04_poem.txt', 'r', encoding='utf-8')as f:
#     poem = f.read()
#     words = poem.split(' ')
#     for word in words:
#         word = word.replace('\n', '')
#         if word in words_count:
#             words_count[word] += 1
#         else:
#             words_count[word] = 1

# print(words_count)

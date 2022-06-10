from cmath import inf
import numpy as np
import csv

files = ['sw.csv', 'nb.csv', 'sv.csv', 'fi.csv', 'de.csv', 'en_US.csv', 'vi_C.csv', 'fr_FR.csv', 'es_ES.csv', 'fa.csv',
         'ja.csv', 'ma.csv', 'or.csv']
languages = ['swahili', 'norwegian', 'swedish', 'finnish', 'german', 'english', 'vietnamese', 'french', 'spanish',
             'farsi', 'japanese', 'malay', 'orayi']

data = []
label = []

i = 0
words = []

for m in files:
    current_file = open(m)
    read = csv.reader(current_file)
    count = inf
    for n in read:
        # print(n)
        words.append(n)
        x = n[1][1:-1]
        # print(n[1] + " " + x)
        row = list(x)
        row.append(languages[i])
        data.append(row)
        count -= 1
        if count == 0:
            break
    i += 1

# print(data)

current_index = 0
characters = {}

for x in data:
    for y in range(len(x) - 1):
        if not x[y] in characters.keys():
            characters[x[y]] = current_index
            current_index += 1

# print(len(characters))
# print(characters)
print(len(data))

X_y = []
character_amount = len(characters)

num = 0

for x in data:
    row = [0] * character_amount
    row.append(x[-1])
    # row.append(str(words[num][0]))
    # row.append(str(words[num][1]))
    num += 1
    for y in range(len(x) - 1):
        row[characters[x[y]]] += 1
    X_y.append(row)

print("X_y is done, now writing to textfile")
print(characters.keys())
datapoints = len(X_y[0]) - 1
# print(datapoints)
X_y = np.array(X_y)
X = X_y[:, 0:datapoints]
y = X_y[:, datapoints:]

with open('datafile.txt', 'wb') as f:
    np.savetxt(f, X, fmt='%s')
f.close()

with open('labels.txt', 'wb') as f:
    np.savetxt(f, y, fmt='%s')
f.close()
# print(characters.keys())

print("textfile is done")

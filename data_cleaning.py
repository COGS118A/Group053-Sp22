from cmath import inf
import numpy as np
import csv

files = ['sw.csv', 'nb.csv', 'sv.csv', 'fi.csv', 'de.csv', 'en_US.csv', 'vi_C.csv', 'fr_FR.csv', 'es_ES.csv', 'fa.csv', 'ja.csv', 'ma.csv', 'or.csv', 'eo.csv', 'zh_hant.csv']
languages = ['swahili','norwegian','swedish','finnish', 'german', 'english', 'vietnamese', 'french', 'spanish', 'farsi', 'japanese', 'malay', 'orayi', 'esperanto', 'chinese']

data = []
label = []

i = 0
words = []

for m in files:
    current_file = open(m)
    read = csv.reader(current_file)
    count = inf
    for n in read:
        words.append(n)
        x = n[1][1:-1]
        row = list(x)
        row.append(languages[i])
        data.append(row)
        count -= 1
        if count==0:
            break
    i+=1


current_index = 0
characters = {}

for x in data:
    for y in range(len(x) - 1):
        if not x[y] in characters.keys():
            characters[x[y]] = current_index
            current_index += 1

print(len(data))

X_y = []
character_amount = len(characters)

num = 0

for x in data:
    row = [0]*character_amount
    row.append(x[-1])
    num+=1 
    for y in range(len(x) - 1):
        row[characters[x[y]]] += 1
    X_y.append(row)

#Seperates the features from their class labels before writing to file
print("X_y is done, now writing to textfile")
print(characters.keys())
datapoints = len(X_y[0])-1
X_y = np.array(X_y)
X = X_y[:, 0:datapoints]
y = X_y[:, datapoints:]

#write the observations and their class labels to two different textfiles
with open('datafile.txt','wb') as f:
    
    np.savetxt(f, X, fmt = '%s')
f.close()

with open('labels.txt','wb') as f:
    
    np.savetxt(f, y, fmt = '%s')
f.close()


print("textfile is done")

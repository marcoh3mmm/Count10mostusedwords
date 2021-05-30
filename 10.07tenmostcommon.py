#Open the File
fhand = open('mbox-short.txt')
counts = dict()

#read the lines
for line in fhand:
    #Split the lines
    words = line.split()
    #Count the words in the lines and  get them in dictionary
    for word in words:
        counts[word] = counts.get(word, 0) + 1

#Append the Key And Values in different order
lst = list()
for key, val in counts.items():
    newtup = ( val,key)
    lst.append(newtup)

#Sort the list  from highest to lowest
lst = sorted(lst, reverse= True)

#Print until the ten Highest Values
for val,key in lst[:10] :
    print(key, val)


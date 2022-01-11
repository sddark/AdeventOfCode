import pandas as pd
#bring in the data
df = pd.read_csv ('file.csv')

#convert dataframe to array
nparray = df.to_numpy()

#initialize
count = 0

#loop through all items in array and determine whether the previous sum of 3 are greater
for i in range(3 , len(nparray)):
    if nparray[i] + nparray[i-1] + nparray[i-2] > nparray[i-1] + nparray[i-2] + nparray[i-3]:
        count +=1

#ta-daa
print(count)
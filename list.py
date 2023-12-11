#initialize data list
data = []

#input integers
while True:
    number = int(input("Masukkan Nilai : "))
    if number !=0:
        data.append(number)
    else:
        break

#find sum of data
total = sum(data)

#find average of data
avg = total/len(data)

#print the average
print(avg)
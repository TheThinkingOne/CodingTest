Data = [3,2,5,4,1,7,6]

howmany = len(Data)

for pivot in range(howmany): #pivot은 0부터 6까지
     min = pivot
     for where in range(pivot+1, howmany): #1~6, 2~6, 3~6, 4~6, 5~6
         if(Data[where] < Data[min]):
             min = where
     Data[pivot], Data[min] = Data[min], Data[pivot]
print(Data)


Data = [3,2,5,4,1]
key = 5

for i in range(len(Data)):
    if Data[i] == key:
        print(f"{i+1}번째에 존재함")
        break

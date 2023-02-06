from datetime import date

min = date.today()
rowNew = ""
with open("Readme2.md",'r',encoding='utf-8') as file:
    for row in file:
        r = row.split(' ')
        d = r[0].split('.')
        birthday = date(int(d[2]),int(d[1]),int(d[0]))
        if birthday<min:
            temp = min
            min = birthday
            birthday = temp
        print(birthday)

S=12
stepP = 2
stepN = 1
begin = 0
days = 0

sun = True
while(True):
    if begin==S:
        break
    else:
        if sun:
            begin=begin+stepP
        else:
            begin=begin-stepN
    if sun:
        days +=1
        sun = False
    else:
        sun = True
    print(f"День {days} прошла {begin} метра")
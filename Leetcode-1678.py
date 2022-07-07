command = input()
s = ''
for i in range(len(command)):
    if command[i] == 'G':
        s+='G'
    elif command[i] == '(':
        if command[i+1] == 'a':
            s+='al'
            i+=3
        else:
            s+='o'
            i+=1
print(s)
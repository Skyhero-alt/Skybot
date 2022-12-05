def hCheck(arr,tok):
        for i in range(6):
            count = 0
            for j in range(7):
                if(arr[i][j]==tok): count += 1
                else: count = 0
                if(count==4): return 1
        return 0

def vCheck(arr,tok):
    for i in range(7):
        count = 0
        for j in range(6):
            if(arr[j][i]==tok): count += 1
            else: count = 0
            if(count==4): return 1
    return 0

def majdCheck(arr,tok):
    for i in range(3):
        for j in range(4):
            count,len = 0,4
            while(len):
                if(arr[i+len-1][j+len-1]==tok): count += 1
                else: count = 0
                len -= 1
            if(count==4): return 1
    return 0

def mindCheck(arr,tok):
    for i in range(3):
        for j in range(3,7):
            count,len = 0,4
            while(len):
                if(arr[i+len-1][j-len+1]==tok): count += 1
                else: count = 0
                len -= 1
            if(count==4): return 1
    return 0

def drawGrid(arr):
    current=''
    for x in range(6):
        for y in range(7):
            current += arr[x][y]
        current+="\n"
    return current
def cardcheck(number):
    string_number=str(number)[::-1]
    l=1
    total=0
    for i in string_number:
        print(i)
        if l%2==0:
            m=int(i)*2
            if len(str(m))>1:
                k=int(str(m)[0])+int(str(m)[1])
                total=total+k
            else:
                total=total+int(m)
        else:
            total = total + int(i)
        l=l+1
    print(total)
    if total%10==0:
        return True
    else:
        return False


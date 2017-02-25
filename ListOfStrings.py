def main():
    li=[]
    k=[]
    r=0
    for i in range(2):
        s=raw_input()
        li.append(s)
    for i in range(2):
        k.append(li[i].split())
    for i in range(2):
        if(k[i][1] in k[i][0]):
            print(1)
        else:
            print (0)


if __name__  == '__main__':
    main()
def most_frequent(string):
    dic={}
    string=string.lower()
    for ch in string:
        dic[ch]=string.count(ch)
    l=[]
    for i in dic.values():
        l.append(i)
    for i in range(len(l)):
        maxm=max(l)
        for item in dic.keys():
            if dic[item]==maxm:
                print(item+"=",dic[item])
        while maxm in l:
            l.remove(maxm)
        if l==[]:
            break

string=input("Please enter a string: ")
most_frequent(string)

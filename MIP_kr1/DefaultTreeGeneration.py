from Tree import Tree

def testDefault(num):
    tree = Tree(num)
    wlist = []
    testDefaultItemAdd([],num,wlist)
    for i in range(len(wlist)):
        variable,address = wlist[i]
        tree.Add(variable,address)
        pass
    return tree

def testDefaultItemAdd(path: list, numb, wlist: list):
    if(numb==1):
        pass
    if(numb%2==0 and int(numb/2)!=1):
        localpath = path.copy()
        localNum = numb/2
        localpath.append('L')
        wlist.append([localNum,localpath])
        testDefaultItemAdd(localpath,localNum,wlist)
    if(numb%3==0 and int(numb/3)!=1):
        localpath = path.copy()
        localNum = numb/3
        localpath.append('R')
        wlist.append([localNum,localpath])
        testDefaultItemAdd(localpath,localNum,wlist)
    pass
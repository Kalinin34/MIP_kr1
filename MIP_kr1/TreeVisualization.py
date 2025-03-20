import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure

from Tree import Tree
from TreeItem import TreeItem

fig, ax = plt.subplots(figsize=(14.4, 14.4), dpi=100) # # - Sçt ekrâna resolûciju uz 1440x1440 pxl. - V J
fig.patch.set_facecolor('lightgray')

def reset():
    ax.clear()
    ax.set_aspect('equal')
    ax.set_clip_on(False)
    ax.axis('off')

reset()

def Output_tree(tree,number):
    reset()
    branches = branchFromTree(tree)
    currentBranc = []
    for i in range(len(branches)):
        if(branches[i]==None):
            continue
        isee = False
        if(branches.__len__()>6):
            print("debug")
        Id, parentId, x, y, value = branches[i]
        if(value == 1):
            continue
        circle = plt.Circle((x, y), 1.5,edgecolor='black', facecolor='white', fill=True, zorder=2)
        ax.add_patch(circle)
        if(number == value):
            ax.text(x, y, str(int(value)), color='blue', fontsize=10, ha='center', va='center', zorder=3)
        else:
            ax.text(x, y, str(int(value)), color='black', fontsize=10, ha='center', va='center', zorder=3)

        if(parentId !=-1):
            _, _, xparent, yparent, Pvalue = branches[parentId]
            ax.plot([x, xparent], [y, yparent], 'k-', linewidth=2,color='yellow')
            ax.text((x + xparent) / 2, (y + yparent) / 2, str(int(Pvalue/value)), color='red', fontsize=8, ha='center', va='center', bbox=dict(facecolor='white', edgecolor='red', boxstyle='round,pad=0.3'))
                
        #display(fig)
    #{id , parentId , x , y , value}
def branchFromTree(tree: Tree):
    branch = inTree([],tree.Item,-1,0,0,256)
    sortedbranch = sorted(
        filter(lambda s: s, branch),
        key=lambda x: x[0])
    #freeBranch = space(sortedbranch)
    return sortedbranch

def space(branch: list):
    uniquebranch=[]
    uniquebranch.append(branch[0])
    for i in range(1,len(branch)):
        _,parentId,_,_,value = branch[i]
        _,_,_,_,Pvalue = branch[parentId]
        can = True
        for j in range(len(uniquebranch)):
            _,LparentId,_,_,Lvalue = branch[j]
            _,_,_,_,LPvalue = branch[LparentId]
            if(LPvalue == Pvalue and Lvalue==value):
                can = False
            pass
        if(can):
            uniquebranch.append(branch[i])
        else:
            uniquebranch.append(None)
        pass
    return uniquebranch

def inTree(branches: list,item : TreeItem, parrentId:int,x,y,space):
    if item == None:
        return branches
    branches.append([item.index,parrentId,x,y,item.value])
    L = inTree(branches,item.L,item.index,x-space,y - 50,space-3)
    R = inTree(branches,item.R,item.index,x+space,y - 50,space-3)
    return branches
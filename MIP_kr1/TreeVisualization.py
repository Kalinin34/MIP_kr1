from turtle import color
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import display, clear_output
from matplotlib.pyplot import figure

from Tree import Tree
from TreeItem import TreeItem

def Output_tree(tree: Tree):
    plt.ion()  # # Interaktîvs reþims. - V J
    fig, ax = plt.subplots(figsize=(14.4, 14.4), dpi=100) # # - Sçt ekrâna resolûciju uz 1440x1440 pxl. - V J
    fig.patch.set_facecolor('lightgray')
    ax.set_aspect('equal')
    ax.set_clip_on(False)
    
    branches = branchFromTree(tree)
    currentBranc = []
    for i in range(len(branches)):
        if(branches[i]==None):
            continue
        isee = False
        Id, parentId, x, y, value = branches[i]
        if parentId !=-1:

            isee = False
            for b in currentBranc:
                xT, yT, variable = b
                if(variable == value):
                    isee = True
                    break;

            _, _, xparent, yparent, Pvalue = branches[parentId]
            if(isee):
                x = xT
                y = yT

        if(~isee):
            currentBranc.append([x,y,value])
            circle = plt.Circle((x, y), 1.5,edgecolor='black', facecolor='white', fill=True, zorder=2)
            ax.add_patch(circle)
            ax.text(x, y, str(int(value)), color='black', fontsize=10, ha='center', va='center', zorder=3)

        isee2 = True
        if parentId !=-1:
            _, _, _, _, pvalue = branches[parentId]
            for b in currentBranc:
                xT, yT, variable = b
                if(variable == pvalue):
                    isee2 = False
                    xparent = xT
                    yparent = yT
                    break;

            if(~isee2):
                ax.plot([x, xparent], [y, yparent], 'k-', linewidth=2)
                ax.text((x + xparent) / 2, (y + yparent) / 2, str(int(Pvalue/value)), color='red', fontsize=8, ha='center', va='center', bbox=dict(facecolor='white', edgecolor='red', boxstyle='round,pad=0.3'))
                
        plt.pause(0.1)
        display(fig)
    
    plt.ioff()
    plt.show()

    #{id , parentId , x , y , value}
def branchFromTree(tree: Tree):
    branch = inTree([],tree.Item,-1,0,0,256)
    freeBranch = space(branch)
    return freeBranch

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
    L = inTree(branches,item.L,item.index,x-space,y - 50,space/2)
    R = inTree(branches,item.R,item.index,x+space,y - 50,space/2)
    return branches
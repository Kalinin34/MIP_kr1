from matplotlib import pyplot as plt
from AI.AITree import AITree, AITreeItem
fig, ax = plt.subplots(figsize=(14.4, 14.4), dpi=100) # # - Sçt ekrâna resolûciju uz 1440x1440 pxl. - V J
fig.patch.set_facecolor('lightgray')

def reset():
    ax.clear()
    ax.set_aspect('equal')

reset()

def Output_treeAI(tree):
    reset()
    branches = branchFromTree(tree)
    currentBranc = []
    for i in range(len(branches)):
        if(branches[i]==None):
            continue
        isee = False
        Id, parentId, x, y, value, Aivalue,minmax = branches[i]

        circle = plt.Circle((x, y), 1.5,edgecolor='black', facecolor='white', fill=True, zorder=2)
        ax.add_patch(circle)
        
        ax.text(x, y, str(float(value)) + "/" + str(float(Aivalue)) + "/" + str(minmax), color='red', fontsize=10, ha='center', va='center', zorder=4)
        if parentId !=-1:
            _, _, xparent, yparent, Pvalue,_,_= branches[parentId]
            ax.plot([x, xparent], [y, yparent], 'k-', linewidth=2)
            ax.text((x + xparent) / 2, (y + yparent) / 2, str(int(Pvalue/value)), color='red', fontsize=8, ha='center', va='center', bbox=dict(facecolor='white', edgecolor='red', boxstyle='round,pad=0.3'))
                
        #display(fig)
    plt.show()
    #{id , parentId , x , y , value,Aivalue}
def branchFromTree(tree: AITreeItem):
    branch = inTree([],tree.Item,-1,0,0,256)
    return branch

def inTree(branches: list,item : AITreeItem, parrentId:int,x,y,space):
    if item == None:
        return branches
    branches.append([item.index,parrentId,x,y,item.value,item.AIvalue,item.minmax])
    L = inTree(branches,item.L,item.index,x-space,y - 50,space/2)
    R = inTree(branches,item.R,item.index,x+space,y - 50,space/2)
    return branches
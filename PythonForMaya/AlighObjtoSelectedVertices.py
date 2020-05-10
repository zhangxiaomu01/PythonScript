import maya.cmds as mc
# This script is designed to align object to the selected component based on the local normal direction (tangent space)
# It is specifically writtedn for architecture modeling, when you need to align several compoents around a cynlinder 
# object such as a tower. 
# Usage: First select the component(s) you want the target object to align to. These components can be face(s), ege(s)
# or vertex. In the end, you should select the target the object. Note the target object should be a model object
def selectionAlign():
    # get the current selection
    selected = cmds.ls(selection=True, fl = True)
    if(len(selected) <= 1):
        print 'You must select at least two objects, one component + one target object'
        return
    # Extract the target object
    AttachObj = selected[-1]
    testObj = AttachObj.split('.')
    print testObj
    if(len(testObj) != 1):
        print 'The last selection must be an object'
        return
    del(selected[-1])
    # For each component, we will duplicate a target object and aligh the target with this component
    for curT in selected:
        print curT
        newSel = mc.select(curT)
        # get current position of the move manipulator
        pos = mc.manipMoveContext('Move', query=True, position=True) 
        atObj = mc.duplicate(AttachObj)
        print atObj
        # We need to move target object to the center of selected component, then we can do normal constraint
        mc.move(pos[0], pos[1], pos[2], atObj)
        constr = cmds.normalConstraint(curT, atObj, aimVector = (1,0,0), worldUpType= 'object')
        mc.delete(constr)

selectionAlign()       
    
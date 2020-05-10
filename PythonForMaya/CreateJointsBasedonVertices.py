# This is designed to create a joint object based on selected faces / edges / vertices
# The new created joint object can be used as an anchor point if we want to align any 
# object to a specific position
#
# First select a bunch of faces / edges / vertices, then run the script, a joint object
# will be created at the center of selected components.
import maya.cmds as mc

def cJointOnVtx():
    selected = mc.ls(sl = True, fl = True)
    if (len(selected) <= 0):
        print 'You must at least select one component!'
        return
    
    tempStr = selected[0]
    testArr = tempStr.split('.')
    
    if (len(testArr) <= 1):
        print 'You must at least select one component!'
        return
    
    # If we have edges | faces selected, we need first convert it to vertices!
    if(testArr[1][0] == 'e' or testArr[1][0] == 'f'):
        selected = mc.polyListComponentConversion(selected, tv=True)
        print 'This is an edge!'
    
    # Reselect the vertices, in order to flatten the selection list
    mc.select(selected)
    selected = mc.ls(sl = True, fl = True)
    
    numOfVtx = len(selected)
    cummulateVtxPos = [0, 0, 0]
    for i in selected:
        curVtxPos = cmds.xform(i, q=True, ws=True, t=True)
        cummulateVtxPos[0] += curVtxPos[0]
        cummulateVtxPos[1] += curVtxPos[1]
        cummulateVtxPos[2] += curVtxPos[2]
        # print curVtxPos
    
    finalPos = [ cummulateVtxPos[0]/numOfVtx, cummulateVtxPos[1]/numOfVtx, cummulateVtxPos[2]/numOfVtx]
    # Create joint at specific location!
    myJoint = mc.joint(p=finalPos)
    
cJointOnVtx()
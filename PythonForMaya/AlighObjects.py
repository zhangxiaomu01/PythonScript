# The code is designed to Align  Object(s)
# First select the Source obj, then select the target obj
# Redefined the prefix of the Maya Command
import maya.cmds as mc
# Define the variable of window
WindowObjAliner = ''
# Check if the window exists , if true, then delete it
if mc.window(WindowObjAliner, ex=True):
    mc.deleteUI(WindowObjAliner , window = True)
# Define the window
WindowObjAliner = mc.window(title = 'Align Object(s)' , s = True , wh = (300,100))
mc.columnLayout(adj = True)
mc.text(l = 'Instructions:First select the Source obj(s),\n Then select the target obj')
mc.separator()
mc.button(l = 'Go!' , w = 300, h = 40, c = 'ObjAliner()')
mc.showWindow(WindowObjAliner)
# Define the function to control the code
def ObjAliner():
    ListObj = mc.ls(sl = True)
    ListSize = len(ListObj)
    if ListSize>=2:
        #Create the Parent Constrain between object(s), align obj together
        Temp_PCons = mc.parentConstraint(mo = False)
        #Delete the Parent Constraint
        mc.delete(Temp_PCons)
    else :
        print 'Error: At least two Objects selected'
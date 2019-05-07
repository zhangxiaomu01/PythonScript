# This code is for creating obj along the curve point¡­
# First select the curve point, then go!
# Redefined the prefix of the Maya Command
import maya.cmds as mc
# Put the Vertexes of the curve into the list
# @sl ¨C List objects that are currently selected.
# @fl ¨C Flattens the returned list of objects so that each component is identified individually.
selCVs = mc.ls(sl = True, fl = True)
# Get the length of the list
selCVs_Size = len(selCVs)
# Re-evaluate each point and get the position of them , then create the object for each point using their position¡­
for i in range(0,selCVs_Size,1):
    getVertX = mc.getAttr(selCVs[i] + '.xValue')
    getVertY = mc.getAttr(selCVs[i] + '.yValue')
    getVertZ = mc.getAttr(selCVs[i] + '.zValue')
    # remove the vertex from the list
    mc.select(cl = True)
    mkJnt = mc.joint()
    mc.setAttr(mkJnt + '.tx' , getVertX)
    mc.setAttr(mkJnt + '.ty' , getVertY)
    mc.setAttr(mkJnt + '.tz' , getVertZ)
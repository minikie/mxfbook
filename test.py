import mxd
import win32com.client

mxd.initialize('mytest')

ws = mxd.Workspace('ws') # no description
ws.newVar = mxd.get_variable('ws', 'newVar').value() # (13,8) # 0.84499115 ... # no description
ws.newMatrixVar = mxd.get_variable('ws', 'newMatrixVar').value() # (13,8) # 0.84499115032141,0.186466804166118,0.780421385523634,0.524852110336539,0.825033449355658,0.689936443540516,0.402678392007962 # no description
ws1 = mxd.Workspace('ws1') # no description
ws1.newVar = mxd.get_variable('ws1', 'newVar').value() # (6,3) # 0.62349944 ... # no description

print type(ws.newVar)

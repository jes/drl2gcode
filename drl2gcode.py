#!/usr/bin/env python

SPINDLE_SPEED = 32000
XY_MOVE_SPEED = 3000
Z_MOVE_SPEED = 300
DRILL_MOVE_SPEED = 100
DRILL_DEPT = 2
SAFE_HEIGHT = 25
RUNNING_HEIGHT = 10
TOOL_HEIGHT = 40


import sys

header = """; Produced by drl2gcode.py

; make sure machine is in CNC mode
M453
; select absolute coordinate system
M82
; metric
G21
; G61 exact path mode was requested but not implemented
; start spindle
M3 S"""+str(SPINDLE_SPEED)+"""
; wait for 3 seconds
G04 S3
"""

footer = """
; stop spindle
M5
; go to safe height
G0 Z"""+str(TOOL_HEIGHT)+""" F30000
; unlock all steppers
;M18
; program ends
M2
"""


tools = {}
tsel = "1"

newl3 = "".join(["G1 F", str(Z_MOVE_SPEED), " Z0.2"])
newl4 = "".join(["G1 F", str(DRILL_MOVE_SPEED), " Z-", str(DRILL_DEPT)])
newl5 = "".join(["G1 F", str(Z_MOVE_SPEED), " Z", str(RUNNING_HEIGHT)])


with open(sys.argv[1]) as fp:  
   line = fp.readline()
   while line:
      line = fp.readline()
      if line.startswith("T") and "C" in line:
         tnum = line.split("C")[0][1:]
         diameter = "{:.2f}".format(float(line.split("C")[1]))
         tools[tnum] = { "diameter": diameter,
                         "file": "".join([sys.argv[1][:-4], "_T", tnum.rjust(2, "0"), "_", diameter, "mm", ".gcode"]),
                         "output": "".join([header, "\n\n; T", tnum, " Diameter: ", diameter, "mm", "\n"]),
                         "first": True
                       }
      elif line.startswith("T"):
         tsel = line[1:].rstrip("\r\n")
      elif line.startswith("X") and tsel != "0":
         if tools[tsel]["first"]:
            newl1 = "".join(["G0 F", str(Z_MOVE_SPEED), " Z", str(SAFE_HEIGHT)])
            tools[tsel]["first"] = False
         else:
            newl1 = "".join(["G1 F", str(Z_MOVE_SPEED), " Z", str(RUNNING_HEIGHT)])
            if tools[tsel]["output"].endswith(newl1+"\n"):
               newl1 = ''
         newl2 = "".join(["G1 F", str(XY_MOVE_SPEED), " ", line.split("Y")[0], " Y", line.split("Y")[1].strip("\r\n")])

         tools[tsel]["output"]+="\n".join([newl1, newl2, newl3, newl4, newl5, ''])
         


for t in tools:
   tools[t]["output"]+=footer
   print("writing", tools[t]["file"])
   f = open(tools[t]["file"], "w")
   f.write(tools[t]["output"])
   f.close()
   #print tools[t]["file"]
   #print tools[t]["output"]


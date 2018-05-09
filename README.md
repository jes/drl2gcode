## installation:

Just download the file and/or clone this git repository and give execution permissions to the grl2gcode.py python script.
There are no external dependencies except for python itself.

The script should be able to run on almost any system providing python is installed, it should work with both python 2.x and 3.x
and with any standard excellion drill file 

Tested on Devuan GNU/Linux only and with kicad.

## Usage:

Using kicad generate an excellion drill file using metric measurements and
auxiliary axis as drill origin after pointing grid origin on the bottom left
of your PCB design.

Then, launch ./grl2gcode.py passing as the only argument the file name of the 
generated .drl excellion file.


Editing grl2gcode.py you will find some variables you can tweak:

 * SPINDLE_SPEED = 32000
 * XY_MOVE_SPEED = 3000
 * Z_MOVE_SPEED = 300
 * DRILL_MOVE_SPEED = 100
 * DRILL_DEPT = 2
 * SAFE_HEIGHT = 25
 * RUNNING_HEIGHT = 10
 * TOOL_HEIGHT = 40
 
 

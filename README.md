# drl2gcode

This program converts Excellion drill files (such as those produced by KiCad) into G-Code for a CNC machine.

## Provenance

This is forked from https://git.nexlab.net/machinery/drl2gcode

It was originally created by Franco Lanza and is licensed under the GNU LGPL.

## Installation

Just download the file and/or clone this git repository and give execution permissions to the drl2gcode.py python script.
There are no external dependencies except for python itself.

The script should be able to run on almost any system providing python is installed, it should work with both python 2.x and 3.x
and with any standard excellion drill file

Tested on Devuan GNU/Linux only and with kicad.

    $ sudo cp drl2gcode.py /usr/local/bin/drl2gcode

## Example

    $ ./drl2gcode.py --spindle-speed 24000 --drill-depth 3 drill.drl
    writing drill_T01_0.80mm.gcode
    writing drill_T01_1.00mm.gcode

## Usage

Using kicad generate an excellion drill file using metric measurements,
"decimal" zeroes format, and auxiliary axis as drill origin after pointing grid origin
on the bottom left of your PCB design.

    $ ./drl2gcode.py -h

    usage: drl2gcode.py [-h] [--spindle-speed SPINDLE_SPEED] [--xy-move-speed XY_MOVE_SPEED] [--z-move-speed Z_MOVE_SPEED] [--drill-move-speed DRILL_MOVE_SPEED] [--drill-depth DRILL_DEPTH]
                        [--safe-height SAFE_HEIGHT]
                        DRLFILE

    This program converts Excellion .drl files into G-Code for a CNC machine. Originally by Franco Lanza.

    positional arguments:
      DRLFILE               Excellion .drl file

    optional arguments:
      -h, --help            show this help message and exit
      --spindle-speed SPINDLE_SPEED
                            Set the spindle speed in RPM
      --xy-move-speed XY_MOVE_SPEED
                            Set the X/Y travel move speed in mm/min
      --z-move-speed Z_MOVE_SPEED
                            Set the Z travel move speed in mm/min
      --drill-move-speed DRILL_MOVE_SPEED
                            Set the Z drilling speed in mm/min
      --drill-depth DRILL_DEPTH
                            Set the distance to drill below z=0 (positive, larger values go deeper)
      --safe-height SAFE_HEIGHT
                            Set the Z coordinate to use for rapid moves

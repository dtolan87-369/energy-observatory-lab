# FreeCAD P001-S0 helper

`p001_s0_placeholder.py` creates a deliberately simple closed-stack model using the current candidate page/cover envelope.

It is useful for:
- checking the mixed-depth stack visually;
- establishing named objects and datums;
- confirming the temporary total stack thickness;
- preparing later hinge/root experiments.

It does **not** contain:
- real hinge geometry;
- gear teeth;
- iris blades;
- magnets;
- Bloom linkage;
- memory internals.

## Run

In FreeCAD:
1. open Macro / Python console;
2. run the script;
3. save the resulting document as a local `.FCStd` file;
4. do not commit the binary file to this public repo unless deliberately releasing it.

The next CAD task is to add two simplified hinge/root alternatives:
A. segmented barrel + replaceable pin;
B. cartridge root + conventional pin hinge.

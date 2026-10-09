"""Energy Observatory — Impossible Book P001-S0 placeholder stack.

Run inside FreeCAD's Python console or as a macro.

Purpose:
- create cover + five placeholder leaves + rear cover;
- expose candidate mixed-depth stack geometry;
- create a visible state-reservation envelope;
- provide an editable digital starting point before detailed mechanisms.

This is NOT manufacturing CAD and does not prove hinge clearance.
"""

import FreeCAD as App
import FreeCADGui as Gui
import Part

DOC_NAME = "IMPOSSIBLE_BOOK_P001_S0"

# Candidate / temporary values in mm.
PAGE_W = 100.0
PAGE_H = 140.0
COVER_W = 102.0
COVER_H = 144.0
COVER_T = 4.0
LEAF_GAP = 0.5
STATE_RESERVE_W = 10.0

LEAVES = [
    ("Leaf_1_Moire_TEMP", 3.0),
    ("Leaf_2_Fields_TEMP", 5.0),
    ("Leaf_3_Gears_TEMP", 8.0),
    ("Leaf_4_Bloom_TEMP", 16.0),
    ("Leaf_5_Memory_TEMP", 5.0),
]

doc = App.newDocument(DOC_NAME)

def add_box(name, w, h, t, x, y, z):
    obj = doc.addObject("Part::Feature", name)
    obj.Label = name
    obj.Shape = Part.makeBox(w, h, t, App.Vector(x, y, z))
    return obj

z = 0.0

# Rear cover datum.
rear = add_box("Rear_Cover_TEMP", COVER_W, COVER_H, COVER_T, 0, -2, z)
z += COVER_T + LEAF_GAP

leaf_objects = []
for name, depth in reversed(LEAVES):
    obj = add_box(name, PAGE_W, PAGE_H, depth, 0, 0, z)
    leaf_objects.append(obj)
    z += depth + LEAF_GAP

front = add_box("Front_Cover_TEMP", COVER_W, COVER_H, COVER_T, 0, -2, z)
total_stack = z + COVER_T

# State-reservation envelope shown beside the stack as a separate reference solid.
state = add_box(
    "TEST_State_Reservation_Envelope",
    STATE_RESERVE_W,
    PAGE_H,
    total_stack,
    0,
    0,
    0,
)
state.ViewObject.Transparency = 80

# Add simple document properties to make intent visible.
group = doc.addObject("App::FeaturePython", "P001_Metadata")
group.addProperty("App::PropertyString", "Status")
group.Status = "DIGITAL PLACEHOLDER / NOT MANUFACTURING CAD"
group.addProperty("App::PropertyLength", "CandidatePageWidth")
group.CandidatePageWidth = PAGE_W
group.addProperty("App::PropertyLength", "CandidatePageHeight")
group.CandidatePageHeight = PAGE_H
group.addProperty("App::PropertyLength", "TemporaryStackThickness")
group.TemporaryStackThickness = total_stack

doc.recompute()
Gui.activeDocument().activeView().viewAxonometric()
Gui.activeDocument().activeView().fitAll()

print("P001-S0 placeholder stack created.")
print(f"Temporary closed-stack thickness: {total_stack:.1f} mm")
print("Next: create hinge/root alternatives A and B and test swept clearances.")

Kicad CAT PCB Design Rules
==========================


## KiCad DRC Default Starting Values
---
These are the values you start with when you place traces or vias.

* Trace Clearance:                  0.25mm

* Trace Width:                      0.25mm

* Via Diameter:                     0.6mm

* Via Drill:                        0.4mm

* MicroVia Diameter:                0.3mm

* MicroVia Drill Diameter:          0.1mm

* Default Grid (parts placement):   0.5mm


## KiCad DRC Global Design Rules
---

* Minimum track width:              0.2mm

* Minimum Via Diameter:             0.4mm

* Minimum Via Drill Diameter:       0.3mm

* Minimum MicroVia Diameter:        0.3mm

* Minimum MicroVia Drill Diameter:  0.1mm

* Blind/Buried Vias:    Not allowed - Talk to manufacturer, expensive.

* Micro Vias:           Not allowed - Talk to manufacturer, expensive.

## Kicad Dimensions
---

* Pad Mask Clearance:               0.2mm

## User PCB Layout Rules (these are personal not checked with DRC)
---

### Silkscreen Text

* Default Silkscreen Text Size:          1mm

* Default Silkscreen Text Thickness:    0.20mm (20%)

* Default Silkscreen Placement Grid:    0.25mm

* Min. Silkscreen Placement Grid:       0.1mm

* Min. Silkscreen Placement increments: 0.05mm

* Min. Silkscreen Text size:            0.75mm

* Min. Silkscreen Text Thickness:       0.15mm

* Stay inside the soldermask area: Stay clear of the soldermask edge,  
    otherwise the silkscreen can not be printed. i.e. stay outside the 
    red boundary of any pad ( recall the soldermask layer is negative).

### Copper Pour (non-power)

* Clearance:                            0.5mm

* Minimum Width:                        0.25mm

* Thermal Relief:                       Yes 

* Antipad Clearance:                    0.5mm

* Spoke Width:                          0.5mm

* Fill Mode:                            Polygon

* Segments/360 deg:                     16

* Outline slope:                        Arbitrary

* Outline Style:                        Hatched.

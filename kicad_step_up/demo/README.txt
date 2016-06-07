*kicad StepUp 3D mechanical exporter* for collaborative exchange between KiCad and FreeCAD/MCAD;
With *kicad StepUp*, it is possible to work in kicad EDA with the same component model data
available in the *STEP AP214 3D format*, and obtain a 3D STEP AP214 model of the pcb board and
a complete board assemblies with electronic modules, to be used for *MCAD interchange*.
The accurate 3D visualization of components on board assemblies in kicad 3dviewer, is
maintained in the same accuracy and aspect in STEP AP214 format. +
The *kicad StepUp* maintains the usual way to work with kicad, but improves the process
to work in a collaborative way with mechanical designers bringing near ECAD and MCAD environments. +
v3.0.4.1 25/04/2016

please refer to
kicadStepUp-starter-Guide.pdf


*Copyright*
-----------
This document and kicad StepUp scripts are Copyright © 2015 by Maurice.
You may distribute it and/or modify it under the terms of either
the GNU Affero General Public License as published by the Free Software Foundation
to ensure cooperation with the community in the case of network server software;             *
for detail see the LICENCE text file.
http://www.gnu.org/licenses/agpl-3.0.en.html
Moreover you have to include the original author copyright.
All trademarks within this guide belong to their legitimate owners.
Kicad STEPUP (TM) is a TradeMark and cannot be freely useable

Risk disclaimer
---------------
*USE 3D CAD DATA AT YOUR OWN RISK *
*DO NOT RELY UPON ANY INFORMATION FOUND HERE WITHOUT INDEPENDENT VERIFICATION.*


Changelog
---------
- added messages on missing emn files
- added messages on missing models
- added path to adapt your KISYS3DMOD
- added blacklist for unwanted modules
- added messages on blacklisted modules
- added pcb color attribute
- added bounding box option
- added bounding box white list to leave real model on connector or peripheral models
- added auxorigin, base origin, base point placement option
- added vrml models z-rotation angle
- added virtual models option
- added fusion export option
- added saving in native format, export to STEP
- added arcs and circles for calculate board position
- added idf_to_origin flag for version >6091
- added reset properties for FC 016 bug
- added ${KIPRJMOD} support
- added multi 3D vrml model support
- added compatibility to kicad version >=3
- added auto color assigning in bboxes
- added minimum volume per model
- added minimum height per model
- updated findPcbCenter method
- added support for .stp extension beside .step
- added support for .igs extension beside .step
- added support for .iges extension beside .step
- moved all to kicad StepUp tools GUI
- added Load Board from kicad StepUp tools GUI
- added Load Board IDF from kicad StepUp tools GUI
- added kicad StepUp FreeCAD WorkBench to open directly .kicad_pcb, .emn, .kicad_mod files
- added VRML exporter for material properties
- added warning messages

- added IDF Importer v3.7 FreeCAD WorkBench to correctly import kicad IDF board and parts
  to install the IDFImporter follow these instructions
  http://www.freecadweb.org/wiki/index.php?title=Installing_more_workbenches
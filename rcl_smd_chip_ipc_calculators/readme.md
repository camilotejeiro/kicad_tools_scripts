RCL SMD Chip IPC Calculators
============================

These directory includes some of the reference tools I have used to 
build my own IPC compliant RCL calculator.

Please note that while we are using a common calculator for our passive 
components the actual land patterns we build will live in three 
different libraries with their associated 3d models (must match in width 
and length our reference RCL part):

* Resistors_SMD_Chip_IPC.pretty  
    With its associated Resistors 3d models.
    
* Capacitors_SMD_Chip_IPC.pretty
    With its associated Capacitors 3d models.
    
* Inductors_SMD_Chip_IPC.pretty
    With its associated Inductors 3d Models.
    
**and remember:** Only build the individual Resistor, Capacitor and 
Inductor land patterns that you need using the calculator as a reference.  

_Always build your libraries on a **need to have basis**, do not build 
parts you don't need (more parts **does not** mean better libraries). 
Otherwise they will go unmaintained and mix with the good parts and 
clutter your libraries making them useless_

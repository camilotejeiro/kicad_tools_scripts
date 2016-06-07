#!/usr/bin/python
# -*- coding: utf-8 -*-
#****************************************************************************
#*                                                                          *
#*  Kicad STEPUP (TM) (3D kicad board and models to STEP) for FreeCAD       *
#*  3D exporter for FreeCAD                                                 *
#*  Kicad STEPUP TOOLS (TM) (3D kicad board and models to STEP) for FreeCAD *
#*  Copyright (c) 2015                                                      *
#*  Maurice easyw@katamail.com                                              *
#*                                                                          *
#*  Kicad STEPUP (TM) is a TradeMark and cannot be freely useable           *
#*                                                                          *
#*   code partially based on:                                               *
#*      Printed Circuit Board Workbench for FreeCAD  FreeCAD-PCB            *
#*      Copyright (c) 2013, 2014, 2015                                      *
#*      marmni <marmni@onet.eu>                                             *
#*                                                                          *
#*      and IDF import for FreeCAD                                          *
#*      (c) Milos Koutny (milos.koutny@gmail.com) 2012                      *
#*      and (c) hyOzd ecad-3d-model-generator                               *
#*                                                                          *
#*   this macro rotates, translates and scales one object                   *
#*   scale for VRML export and open footprint for easy alignement           *
#*   this sw is a part of kicad StepUp code                                 *
#*   all credits and licence details in kicad StepUp code                   *
#*   Macro_Move_Rotate_Scale                                                *
#*   ver in ___ver___                                                       *
#*     Copyright (c) 2015                                                   *
#*     Maurice easyw@katamail.com                                           *
#*                                                                          *
#*     Collisions routines from Highlight Common parts Macro                *
#*     author JMG, galou and other contributors                             *
#*                                                                          *
#* IDF_ImporterVersion="3.9.2"
#*  ignoring step search associations (too old models)
#*  displaying Flat Mode models
#*  checking version 3 for both Geometry and Part Number
#*  supporting Z position
#*  skipping PROP in emp file
#*  adding color to shapes opt IDF_colorize
#*  adding emp library/single model load support
#*  aligning IDF shape to both Geom and PartNBR for exactly match
#*  to do: .ROUTE_OUTLINE ECAD, .PLACE_OUTLINE MCAD, .ROUTE_KEPOUT ECAD, .PLACE_KEEPOUT ECAD
#****************************************************************************
#*                                                                          *
#*   This program is free software; you can redistribute it and/or modify   *
#*   it under the terms of the GNU Affero General Public License            *
#*   as published by the Free Software Foundation to ensure cooperation     *
#*   with the community in the case of network server software;             *
#*   for detail see the LICENCE text file.                                  *
#*   http://www.gnu.org/licenses/agpl-3.0.en.html                           *
#*   Moreover you have to include the original author copyright             *
#*   kicad StepUP made by Maurice easyw@katamail.com                        *
#*                                                                          *
#*   This program is distributed in the hope that it will be useful,        *
#*   but WITHOUT ANY WARRANTY; without even the implied warranty of         *
#*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          *
#*   GNU Library General Public License for more details.                   *
#*                                                                          *
#*   You should have received a copy of the GNU Library General Public      *
#*   License along with this program; if not, write to the Free Software    *
#*   Foundation, Inc.,                                                      *
#*   51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA           *
#*                                                                          *
#****************************************************************************
##With kicad StepUp you’ll get an exact representation of your physical board in Native 3D PCB

## kicad StepUp tools
##done
# upgrade kicadstepup version
# resized font size
# add bbox and volume images on the starter guide
# add ksu config more detailed description
# complete volume_minimum config in doc
# improved OSX QtGui File Open
# better arc and line import
# remove test button
# enable confirm on exit
# replace FreeCAD.Console.Message -> say 
##todo list
# collision and proximity as microelly
## kicad StepUp
# added messages on missing emn files
# added messages on missing models
# added path to adapt your KISYS3DMOD
# added blacklist for unwanted modules
# added messages on blacklisted modules
# added pcb color attribute
# added bounding box option
# added bounding box white list to leave real model on connector or peripheral models
# added auxorigin, base origin, base point placement option
# added vrml models z-rotation angle
# added virtual models option
# added fusion export option
# added saving in native format, export to STEP
# added arcs and circles for calculate board position
# added idf_to_origin flag for version >6091
# added reset properties for FC 016 bug
# added ${KIPRJMOD} support
# added v3,v4 pcb version support
# added multi 3D vrml model support
# added compatibility to kicad version >=3
# added auto color assigning in bboxes
# added minimum volume per model
# added minimum height per model
# updated findPcbCenter method
# added support for .stp extension beside .step
# added support for .igs extension beside .step
# added support for .iges extension beside .step
# because of hole sovrapposition prob...
# cutting hole by hole instead of hole compound
# added holes_solid var
# to have holes as solid to garantee cutting
# handled single circle 
# used OpenSCAD2Dgeom instead of wire + face (best option)
# http://www.freecadweb.org/wiki/index.php?title=Macro_Creating_faces_from_a_DXF_file
# fixed unicode text parsing
# double option .kicad_pcb .emn
# in case of non coincidences .emn is more tolerant
# try to build wires on closed shaped for make the cutting faster
# try to optimize cutting changing creation/type of holes
# manage bklist and volume
# accept with or without /\ at the end of 3Dpath
# search models in KIPRJMOD and in KISYS3DMOD 
# removed unicode chars in .kicad_pcb
# exported wrl, step from python
# reload & display ini cfg file
# display/edit ini file with syntax highlight
# msg first ksu config
# added warning for import step multi part fixed v3035
# added warning in load footprint and in placing step mod if x,y and scale are different from 0 0 0 and 1 1 1
# non stopping warning for footprint
# added command line args to load board(/emn)
# avoid argv in memory in case of opened from  command line
# used multi cut also for footprint too
# enabled loadB, loadI, loadF with filename=None to align Mod and Macro
# enabled Macro & Mod
# added ico tools info
# added checkbox export_2_step
# added export2STEP var in ini file
# subst print to say
# fixed cursor wait
# improved multipart load checking
# added virtual checkbox
# added VRML with material properties exporter
# added metal grey material
# added multipart VRML option
# improved export resolution from %.3f to %.5f
# added config for material props
# most clean code and comments done
##todo

# message error for bad config
# enable upper case configparser optionxform
# http://stackoverflow.com/questions/19359556/configparser-reads-capital-keys-and-make-them-lower-case
# use isInside/common ( TopoShape ) to cut only intersection objs
# multi board
# evaluate python occ for step exporting without triangulation
# test option placement
# check line 772 abs ZMax = height?
# add checkbox virtual
# fix fonts for html and new buttons
# ...
# try to close non closed wire
# from Macro_JointWire
# pad type trapez
# add caching for 3D models on loading

## try to add this code for utf8 support (see @ #workaround to remove utf8 extra chars )
# import sys  
# reload(sys)  
# sys.setdefaultencoding('utf8')  #to accept utf8 chars


## import statements

import FreeCAD,FreeCADGui,Part,Mesh
#import PySide
from collections import namedtuple

import PySide
from PySide import QtGui, QtCore

from time import sleep
from math import sqrt, tan, atan, atan2, degrees, radians, hypot, sin, cos, pi, fmod
import Draft, Part
from collections import namedtuple
from FreeCAD import Base
import sys, os
from os.path import expanduser
import re
import time
import OpenSCAD2Dgeom
import ImportGui
from math import sqrt, atan, sin, cos, radians, degrees, pi

import argparse
import __builtin__
if FreeCAD.GuiUp:
    from PySide import QtCore, QtGui

import OpenSCADFeatures
#from codecs import open #maui to verify
#import unicodedata


pythonopen = __builtin__.open # to distinguish python built-in open function from the one declared here

## Constant definitions
___ver___ = "3.0.4.1"  # adding export VRML with materials
__title__ = "kicad_StepUp"
__author__ = "maurice & mg"
__Comment__ = 'Kicad STEPUP(TM) (3D kicad board and models exported to STEP) for FreeCAD'
___ver_ksu___ = "1.0.1.9  25/11/2015" 
IDF_ImporterVersion="3.9.2"
__Icon__ = "stepup.png"

global userCancelled, userOK, show_mouse_pos, min_val, last_file_path, resetP
global start_time, show_messages
global show_messages, applymaterials
global real_board_pos_x, real_board_pos_y, board_base_point_x, board_base_point_y
global ksu_config_fname, ini_content, configFilePath
global models3D_prefix, blacklisted_model_elements, col, colr, colg, colb
global bbox, volume_minimum, height_minimum, idf_to_origin, aux_orig
global base_orig, base_point, bbox_all, bbox_list, whitelisted_model_elements
global fusion, addVirtual, blacklisted_models, exportFusing, min_drill_size
global last_fp_path, last_pcb_path, plcmnt, xp, yp, exportFusing, exportS

exportS=True
last_file_path=''
resetP=True
global rot_wrl, test_flag, test_flag_pads
rot_wrl=0.0
#global module_3D_dir
userCancelled        = "Cancelled"
userOK            = "OK"
show_mouse_pos = True
#module_3D_dir="C:/Cad/Progetti_K/a_mod"
min_val=0.001
conflict_tolerance=1e-6  #volume tolerance
font_size=8
bbox_r_col=(0.411765, 0.411765, 0.411765)  #dimgrey
bbox_c_col=(0.823529, 0.411765, 0.117647)  #chocolate
bbox_x_col=(0.862745, 0.862745, 0.862745) #gainsboro
bbox_l_col=(0.333333, 0.333333, 0.333333) #sgidarkgrey
bbox_IC_col=(0.156863, 0.156863, 0.156863)  #sgiverydarkgrey
bbox_default_col=(0.439216, 0.501961, 0.564706)  #slategrey
mat_section="""
[Materials]
mat = enablematerials
;; VRML models to be or not exported with material properties
;mat = enablematerials\n;mat = nomaterials
"""

test_flag=False
#test_flag=True
test_flag_exit=False
test_flag_pads=False
remove_pcbPad=True
close_doc=False
show_border=False
show_shapes=False 
disable_cutting=False
# enable_materials=True
test_extrude=False
holes_solid=True
##ignore_utf8=False not used
emn_version=3.0
show_messages=True
#show_messages=False # mauitest

global export_board_2step
#export_board_2step=False
save_temp_data=False

current_milli_time = lambda: int(round(time.time() * 1000))

Materials=True
## "PIN-01";"metal grey pins"
## "PIN-02";"gold pins"
## "IC-BODY-EPOXY-04";"black body"
## "RES-SMD-01";"resistor black body"
## "IC-BODY-EPOXY-01";"grey body"
## "CAP-CERAMIC-05";"dark grey body"
## "CAP-CERAMIC-06";"brown body"
## "PLASTIC-GREEN-01";"green body"
## "PLASTIC-BLUE-01";"blue body"
## "PLASTIC-WHITE-01";"white body"
## "IC-LABEL-01";"light brown label"
## LED-GREEN, LED-RED, LED-BLUE

as_is=""

metal_grey_pins="""material DEF PIN-01 Material {
        ambientIntensity 0.271
        diffuseColor 0.824 0.820 0.781
        specularColor 0.328 0.258 0.172
        emissiveColor 0.0 0.0 0.0
        shininess 0.70
        transparency 0.0
        }"""
        
# http://vrmlstuff.free.fr/materials/
metal_grey="""material DEF MET-01 Material {
        ambientIntensity 0.249999
        diffuseColor 0.298 0.298 0.298
        specularColor 0.398 0.398 0.398
        emissiveColor 0.0 0.0 0.0
        shininess 0.056122
        transparency 0.0
        }"""
    
gold_pins="""material DEF PIN-02 Material {
        ambientIntensity 0.379
        diffuseColor 0.859 0.738 0.496
        specularColor 0.137 0.145 0.184
        emissiveColor 0.0 0.0 0.0
        shininess 0.40
        transparency 0.0
        }"""

black_body="""material DEF IC-BODY-EPOXY-04 Material {
        ambientIntensity 0.293
        diffuseColor 0.148 0.145 0.145
        specularColor 0.180 0.168 0.160
        emissiveColor 0.0 0.0 0.0
        shininess 0.35
        transparency 0.0
        }"""

resistor_black_body="""material DEF RES-SMD-01 Material {
        diffuseColor 0.082 0.086 0.094
        emissiveColor 0.000 0.000 0.000
        specularColor 0.066 0.063 0.063
        ambientIntensity 0.638
        transparency 0.0
        shininess 0.3
        }"""

dark_grey_body="""material DEF CAP-CERAMIC-05 Material {
        ambientIntensity 0.179
        diffuseColor 0.273 0.273 0.273
        specularColor 0.203 0.188 0.176
        emissiveColor 0.0 0.0 0.0
        shininess 0.15
        transparency 0.0
        }"""

grey_body="""material DEF IC-BODY-EPOXY-01 Material {
        ambientIntensity 0.117
        diffuseColor 0.250 0.262 0.281
        specularColor 0.316 0.281 0.176
        emissiveColor 0.0 0.0 0.0
        shininess 0.25
        transparency 0.0
        }"""

brown_body="""material DEF CAP-CERAMIC-06 Material {
        ambientIntensity 0.453
        diffuseColor 0.379 0.270 0.215
        specularColor 0.223 0.223 0.223
        emissiveColor 0.0 0.0 0.0
        shininess 0.15
        transparency 0.0
        }"""

light_brown_body="""material DEF RES-THT-01 Material {
        ambientIntensity 0.149
        diffuseColor 0.883 0.711 0.492
        specularColor 0.043 0.121 0.281
        emissiveColor 0.0 0.0 0.0
        shininess 0.40
        transparency 0.0
        }"""

blue_body="""material DEF PLASTIC-BLUE-01 Material {
        ambientIntensity 0.565
        diffuseColor 0.137 0.402 0.727
        specularColor 0.359 0.379 0.270
        emissiveColor 0.0 0.0 0.0
        shininess 0.25
        transparency 0.0
        }"""

green_body="""material DEF PLASTIC-GREEN-01 Material {
        ambientIntensity 0.315
        diffuseColor 0.340 0.680 0.445
        specularColor 0.176 0.105 0.195
        emissiveColor 0.0 0.0 0.0
        shininess 0.25
        transparency 0.0
        }"""

orange_body="""material DEF PLASTIC-ORANGE-01 Material {
        ambientIntensity 0.284
        diffuseColor 0.809 0.426 0.148
        specularColor 0.039 0.102 0.145
        emissiveColor 0.0 0.0 0.0
        shininess 0.25
        transparency 0.0
        }"""

red_body="""material DEF RED-BODY Material {
        ambientIntensity 0.683
        diffuseColor 0.700 0.100 0.050
        emissiveColor 0.000 0.000 0.000
        specularColor 0.300 0.400 0.150
        shininess 0.25
        transparency 0.0
        }"""

pink_body="""material DEF CAP-CERAMIC-02 Material {
        ambientIntensity 0.683
        diffuseColor 0.578 0.336 0.352
        specularColor 0.105 0.273 0.270
        emissiveColor 0.0 0.0 0.0
        shininess 0.25
        transparency 0.0
        }"""

yellow_body="""material DEF PLASTIC-YELLOW-01 Material {
        ambientIntensity 0.522
        diffuseColor 0.832 0.680 0.066
        specularColor 0.160 0.203 0.320
        emissiveColor 0.0 0.0 0.0
        shininess 0.25
        transparency 0.0
        }"""

white_body="""material DEF PLASTIC-WHITE-01 Material {
        ambientIntensity 0.494
        diffuseColor 0.895 0.891 0.813
        specularColor 0.047 0.055 0.109
        emissiveColor 0.0 0.0 0.0
        shininess 0.25
        transparency 0.0
        }"""

light_brown_label="""material DEF IC-LABEL-01 Material {
        ambientIntensity 0.082
        diffuseColor 0.691 0.664 0.598
        specularColor 0.000 0.000 0.000
        emissiveColor 0.0 0.0 0.0
        shininess 0.01
        transparency 0.0
        }"""

led_red="""material DEF LED-RED Material {
        ambientIntensity 0.789
        diffuseColor 0.700 0.100 0.050
        emissiveColor 0.000 0.000 0.000
        specularColor 0.300 0.400 0.150
        shininess 0.125
        transparency 0.10
        }"""

led_green="""material DEF LED-GREEN Material {
        ambientIntensity 0.789
        diffuseColor 0.400 0.700 0.150
        emissiveColor 0.000 0.000 0.000
        specularColor 0.600 0.300 0.100
        shininess 0.05
        transparency 0.10
        }"""

led_blue="""material DEF LED-BLUE Material {
        ambientIntensity 0.789
        diffuseColor 0.100 0.250 0.700
        emissiveColor 0.000 0.000 0.000
        specularColor 0.500 0.600 0.300
        shininess 0.125
        transparency 0.10
        }"""

led_yellow="""material DEF LED-YELLOW Material {
        ambientIntensity 0.522
        diffuseColor 0.98 0.840 0.066
        specularColor 0.160 0.203 0.320
        emissiveColor 0.0 0.0 0.0
        shininess 0.125
        transparency 0.10
        }"""

led_white="""material DEF LED-WHITE Material {
        ambientIntensity 0.494
        diffuseColor 0.895 0.891 0.813
        specularColor 0.047 0.055 0.109
        emissiveColor 0.0 0.0 0.0
        shininess 0.125
        transparency 0.10
        }"""

material_properties_names=["as is","metal grey pins","metal grey","gold pins","black body","resistor black body",\
                           "grey body","dark grey body","brown body","light brown body","blue body",\
                           "green body","orange body","red_body","pink body","yellow body","white body","light brown label",\
                           "led red","led green","led blue","led yellow","led white"]
material_properties=[as_is,metal_grey_pins,metal_grey,gold_pins,black_body,resistor_black_body,\
                     grey_body,dark_grey_body,brown_body,light_brown_body,blue_body,\
                     green_body,orange_body,red_body,pink_body,yellow_body,white_body,light_brown_label,\
                     led_red,led_green,led_blue,led_yellow,led_white]
 
material_definitions=""
for mat in material_properties[1:]:
    material_definitions+="Shape {\n    appearance Appearance {"+mat+"\n    }\n}\n"

material_ids=[]
material_ids.append("")

for mat in material_properties[1:]:
    m = re.search('DEF\s(.+?)\sMaterial', mat)
    if m:
        found = m.group(1)
        #say(found)
        material_ids.append(found)
#say(material_ids)    
#say (material_definitions)

def clear_console():
    #clearing previous messages
    mw=FreeCADGui.getMainWindow()
    c=mw.findChild(QtGui.QPlainTextEdit, "Python console")
    c.clear()
    r=mw.findChild(QtGui.QTextEdit, "Report view")
    r.clear()

#if not Mod_ENABLED:
clear_console()
    
# points: [Vector, Vector, ...]
# faces: [(pi, pi, pi), ], pi: point index
# color: (Red, Green, Blue), values range from 0 to 1.0
Mesh = namedtuple('Mesh', ['points', 'faces', 'color', 'transp'])

from sys import platform as _platform

import ConfigParser

def insert(filename, other):
    if os.path.exists(filename):
        open(filename)
    else:
        FreeCAD.Console.PrintError("File does not exist.\n")
        reply = QtGui.QMessageBox.information(None,"info", "File does not exist.\n")

def open(filename):
    #reply = QtGui.QMessageBox.information(None,"info", filename)
    #onLoadBoard_cmd(filename)
    ext = os.path.splitext(os.path.basename(filename))[1]
    if ext==".kicad_pcb":
        onLoadBoard(filename)
    elif ext==".emn":
        onLoadBoard_idf(filename)
    elif ext==".kicad_mod":
        onLoadFootprint(filename)

def say(msg):
    FreeCAD.Console.PrintMessage(msg)

def sayw(msg):
    FreeCAD.Console.PrintWarning(msg)
    FreeCAD.Console.PrintWarning('\n')
    
def sayerr(msg):
    FreeCAD.Console.PrintError(msg)
    FreeCAD.Console.PrintWarning('\n')

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 164)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 110, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.comboBox = QtGui.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(180, 40, 191, 22))
        self.comboBox.setMaxVisibleItems(25)
        self.comboBox.setObjectName("comboBox")
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(180, 20, 53, 16))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 53, 16))
        self.label_2.setObjectName("label_2")
        self.plainTextEdit = QtGui.QPlainTextEdit(Dialog)
        self.plainTextEdit.setEnabled(False)
        self.plainTextEdit.setGeometry(QtCore.QRect(20, 40, 31, 31))
        self.plainTextEdit.setBackgroundVisible(False)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit_2 = QtGui.QPlainTextEdit(Dialog)
        self.plainTextEdit_2.setEnabled(False)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(120, 40, 31, 31))
        self.plainTextEdit_2.setBackgroundVisible(False)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(120, 20, 41, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 80, 351, 16))
        self.label_4.setObjectName("label_4")
        QtCore.QObject.connect(self.comboBox, QtCore.SIGNAL("currentIndexChanged(QString)"), self.SIGNAL_comboBox_Changed)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def SIGNAL_comboBox_Changed(self,text):
        #say("combo changed "+text)
        comboBox_Changed(text)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Material Properties", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Materials", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Original", None, QtGui.QApplication.UnicodeUTF8))
        self.plainTextEdit.setToolTip(QtGui.QApplication.translate("Dialog", "Shape Color", None, QtGui.QApplication.UnicodeUTF8))
        self.plainTextEdit_2.setToolTip(QtGui.QApplication.translate("Dialog", "Diffuse Color", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Note: set Material will unmatch colors between wrl and STEP ", None, QtGui.QApplication.UnicodeUTF8))
###

def comboBox_Changed(text_combo):
    global ui
    #say(text_combo)
    material_index=material_properties_names.index(text_combo)
    #say(material_index)
    mat_prop = material_properties[material_index].split('\n')
    if len(mat_prop)>1:
        # say(mat_prop[2])
        color_rgb=mat_prop[2].split(' ')
        # say (color_rgb)
        # say(color_rgb[9]+" "+color_rgb[10]+" "+color_rgb[11])
        pal = QtGui.QPalette()
        bgc = QtGui.QColor(float(color_rgb[9])*255,float(color_rgb[10])*255, float(color_rgb[11])*255)
        pal.setColor(QtGui.QPalette.Base, bgc)
        ui.plainTextEdit_2.viewport().setPalette(pal)
                
###

def cfgParsWrite(configFilePath):
    ##ksu pre-set
    global models3D_prefix, blacklisted_model_elements, col, colr, colg, colb
    global bbox, volume_minimum, height_minimum, idf_to_origin, aux_orig, addVirtual
    global base_orig, base_point, bbox_all, bbox_list, whitelisted_model_elements
    global fusion, addVirtual, blacklisted_models, exportFusing, min_drill_size
    global last_fp_path, last_pcb_path, plcmnt, xp, yp, exportFusing, export_board_2step
    global enable_materials

    configParser.set('last_footprint_path', 'last_fp_path', last_fp_path)
    configParser.set('last_pcb_path', 'last_pcb_path', last_pcb_path)
    if export_board_2step:
        configParser.set('export', 'export_to_step', "yes")
    else:
        configParser.set('export', 'export_to_step', "no")
    if addVirtual==1:
        configParser.set('Virtual', 'virt', "addvirtual")
    else:
        configParser.set('Virtual', 'virt', "novirtual")
    if enable_materials==1:
        configParser.set('Materials', 'mat', "enablematerials")
    else:
        configParser.set('Materials', 'mat', "nomaterials")
    #configParser.set('last_fp_path', ';; last footprint file path used')
    configParser.set('info', default_ksu_msg[0])
    configParser.set('prefix3D', default_ksu_msg[1])
    configParser.set('PcbColor', default_ksu_msg[2])
    configParser.set('Blacklist', default_ksu_msg[3])
    configParser.set('BoundingBox', default_ksu_msg[4])
    configParser.set('Placement', default_ksu_msg[5])
    configParser.set('Virtual', default_ksu_msg[6])
    configParser.set('ExportFuse', default_ksu_msg[7])
    configParser.set('minimum_drill_size', default_ksu_msg[8])
    configParser.set('last_pcb_path', default_ksu_msg[9])
    configParser.set('last_footprint_path', default_ksu_msg[10])
    configParser.set('export', default_ksu_msg[11])
    configParser.set('Materials', default_ksu_msg[12])
    # save to the config file
    with __builtin__.open(configFilePath, 'wb') as configfile:
        configParser.write(configfile)
    #configFilePath.close() already closed
###
    
    
def cfgParsRead(configFilePath):
    ##ksu pre-set
    global models3D_prefix, blacklisted_model_elements, col, colr, colg, colb
    global bbox, volume_minimum, height_minimum, idf_to_origin, aux_orig
    global base_orig, base_point, bbox_all, bbox_list, whitelisted_model_elements
    global fusion, addVirtual, blacklisted_models, exportFusing, min_drill_size
    global last_fp_path, last_pcb_path, plcmnt, xp, yp, exportFusing, export_board_2step
    global enable_materials, mat_section
    with __builtin__.open(configFilePath, 'r') as mycfg:
        content = mycfg.readlines()
        #time.sleep(0.5)
    mycfg.close()
    #say(content)
    if any("Materials" in s for s in content):
        say ("Materials section present\n")
    else:
    #if "Materials" not in content:
        enable_materials = 1
        say ("missing material section, adding default one\n")
        with __builtin__.open(configFilePath, 'a') as mycfg:
            mycfg.write(mat_section)
        mycfg.close()
    #stop
    #cfg_parameters=[]
    models3D_prefix = ''
    blacklisted_model_elements=''
    #col=''; col='0.0,0.5,0.0,green';  # color
    col=''; col='0.0,0.0,1.0,blue';  # color
    bbox=0
    #(0.6,0.4,0.2) brown
    volume_minimum=0 #0.8  ##1 #mm^3, 0 skipped #global var default
    height_minimum=0 #0.8  ##1 #mm, 0 skipped   #global var default
    ## to debug quickly put show_messages=False
    ### from release 6091 this flag enables the option to place IDF exported to origin
    idf_to_origin=True
    #idf_to_origin=False
    aux_orig=0;base_orig=0;base_point=0
    bbox_all=0; bbox_list=0; whitelisted_model_elements=''
    fusion=False; addVirtual=0; enable_materials=0
    configParser.read(configFilePath)
    models3D_prefix = configParser.get('prefix3D', 'prefix3D_1')
    if not models3D_prefix.endswith('/'):
        if not models3D_prefix.endswith('\\'):
            models3D_prefix+='/'
    #say(models3D_prefix+'\n')
    pcb_color = configParser.get('PcbColor', 'pcb_color')
    bklist = configParser.get('Blacklist', 'bklist')
    bbox_opt = configParser.get('BoundingBox', 'bbox')
    plcmnt = configParser.get('Placement', 'placement')
    virtual = configParser.get('Virtual', 'virt')
    exportFusing = configParser.get('ExportFuse', 'exportFusing')
    min_drill_size = float(configParser.get('minimum_drill_size', 'min_drill_size'))
    last_pcb_path = configParser.get('last_pcb_path', 'last_pcb_path')
    last_fp_path = configParser.get('last_footprint_path', 'last_fp_path') 
    export2S = configParser.get('export', 'export_to_STEP') 
    enablematerials = configParser.get('Materials', 'mat')    
    if "yes" in export2S:
        export_board_2step=True
    else:
        export_board_2step=False
    if bklist.find('none') !=-1:
        blacklisted_model_elements=''
    elif bklist.find('volume') !=-1:
        vval=bklist.strip('\r\n')
        vvalue=vval.split("=")
        volume_minimum=float(vvalue[1])
        #reply = QtGui.QMessageBox.information(None,"info ...","volume "+str(volume_minimum))
    elif bklist.find('height') !=-1:
        vval=bklist.strip('\r\n')
        vvalue=vval.split("=")
        height_minimum=float(vvalue[1])
        #reply = QtGui.QMessageBox.information(None,"info ...","height "+str(height_minimum))
    else:
        blacklisted_model_elements=bklist.strip('\r\n')
        blacklisted_models=blacklisted_model_elements.split(",")
    col=pcb_color.strip('\r\n')
    if bbox_opt.upper().find('ALL') !=-1:
        bbox_all=1
        whitelisted_model_elements=''
    else:
        if bbox_opt.upper().find('LIST') !=-1:
            bbox_list=1
            whitelisted_model_elements=bbox_opt.strip('\r\n')
            #whitelisted_models=whitelisted_model_elements.split(",")        
    if plcmnt.find('AuxOrigin') !=-1:
        aux_orig=1
        #whitelisted_model_elements=''
    if plcmnt.find('BaseOrigin') !=-1:
        base_orig=1
    if plcmnt.find('BasePoint') !=-1:
        base_point=1
        basepoint=plcmnt.strip('\r\n')
        coords_BP=basepoint.split(";")
        xp=float(coords_BP[1]);yp=float(coords_BP[2])
    if plcmnt.find('AutoAdjust') !=-1:
        idf_to_origin=False
    if virtual.lower().find('addvirtual') !=-1:
        addVirtual=1
    if exportFusing.lower().find('fuseall') !=-1:
        fusion=True
    if enablematerials.lower().find('enablematerials') !=-1:
        enable_materials=1
    say('3D models prefix='+models3D_prefix+'\rpcb color='+col+'\r')
    #cfg_parameters.append(models3D_prefix)
    #cfg_parameters.append(col)
    say('blacklist modules '+blacklisted_model_elements+'\r')
    #cfg_parameters.append(blacklisted_model_elements)
    say('volume '+str(volume_minimum)+' heigh '+str(height_minimum)+'\r')
    #cfg_parameters.append(volume_minimum)
    say('bounding box option '+str(bbox_all)+' whitelist '+whitelisted_model_elements+'\r')
    #cfg_parameters.append(bbox_all);cfg_parameters.append(whitelisted_model_elements)
    say('placement board @ '+plcmnt+'\r')
    say('last fp path '+last_fp_path+'\r')
    say('last brd path '+last_pcb_path+'\r')
    #cfg_parameters.append(plcmnt);cfg_parameters.append(last_fp_path)
    #cfg_parameters.append(last_pcb_path)
    say('virtual models '+virtual+'\r')
    say('export fusing option '+exportFusing+'\r')
    #cfg_parameters.append(virtual);cfg_parameters.append(exportFusing)
    say ('minimum drill size '+str(min_drill_size)+'mm\n')
    say ('export to STEP '+str(export_board_2step)+'\n')
    say ("materials "+str(enable_materials)+"\n")
    #cfg_parameters.append(min_drill_size);
    ## color
    #FreeCADGui.ActiveDocument.getObject("Board_outline").ShapeColor = (0.3333,0.3333,0.4980)
    col= col.split(',')
    colr=float(col[0]);colg=float(col[1]);colb=float(col[2])
    ##cfg_parameters = (models3D_prefix,blacklisted_model_elements,col,bbox,volume_minimum,height_minimum
    #cfg_parameters.append(colr);cfg_parameters.append(colg);cfg_parameters.append(colb)
    #return cfg_parameters
##

def shapeToMesh(shape, color, transp, mesh_deviation, scale=None):
    #mesh_deviation=0.1 #the smaller the best quality, 1 coarse
    #say(mesh_deviation+'\n')
    mesh_data = shape.tessellate(mesh_deviation)
    points = mesh_data[0]
    if scale != None:
        points = map(lambda p: p*scale, points)
    newMesh= Mesh(points = points,
                faces = mesh_data[1],
                color = color, transp=transp)
    return newMesh

def exportVRMLmaterials(objects, filepath):
    """Export given list of Mesh objects to a VRML file.
    with material properties
    `Mesh` structure is defined at root."""
    global ui
    #material_list=["as is","metal pins","gold pins","black body","dark brown body","brown body","grey body","green body","white body","black label","white label"]
    #material_properties_names=["as is","metal grey pins","gold pins","black body","resistor black body",\
    #                       "grey body","dark grey body","brown body","light brown body","blue body",\
    #                       "green body","orange body","pink body","yellow body","white body","light brown label",\
    #                       "led red","led green","led blue"]
    #global color_list_mat, col_index
    with __builtin__.open(filepath, 'w') as f:
        # write the standard VRML header
        f.write("#VRML V2.0 utf8\n#kicad StepUp wrl exported\n\n")
        f.write(material_definitions)
        color_list=[]
        color_list_mat=[]
        index_color=-1
        Dialog = QtGui.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        ui.comboBox.addItems(material_properties_names)
        material="as is"
        for obj in objects:
            f.write("Shape { geometry IndexedFaceSet \n{ coordIndex [")
            # write coordinate indexes for each face
            f.write(','.join("%d,%d,%d,-1" % f for f in obj.faces))
            f.write("]\n") # closes coordIndex
            f.write("coord Coordinate { point [")
            # write coordinate points for each vertex
            #f.write(','.join('%.3f %.3f %.3f' % (p.x, p.y, p.z) for p in obj.points))
            f.write(','.join('%.5f %.5f %.5f' % (p.x, p.y, p.z) for p in obj.points))
            f.write("]\n}") # closes Coordinate
            #shape_col=(1.0, 0.0, 0.0)#, 0.0)
            f.write("}\n") # closes points
            #say(obj.color)
            shape_col=obj.color[:-1] #remove last item
            #say(shape_col)
            if shape_col not in color_list:
                pal = QtGui.QPalette()
                bgc = QtGui.QColor(shape_col[0]*255,shape_col[1]*255, shape_col[2]*255)
                pal.setColor(QtGui.QPalette.Base, bgc)
                ui.plainTextEdit.viewport().setPalette(pal)
                #ui.comboBox.clear()
                color_list.append(shape_col)
                index_color=index_color+1
                #say(color_list)
                #ui.comboBox.addItems(color_list)
                if Materials:
                    reply=Dialog.exec_()
                    #Dialog.exec_()
                    #say(reply)
                    if reply==1:
                        material=str(ui.comboBox.currentText())
                    else:
                        material="as is"
                color_list_mat.append(material)
                #say(material)
            #else:
            #say("searching")
            col_index=color_list.index(shape_col)
            #say(color_list_mat[col_index])
            if not Materials or color_list_mat[col_index]=="as is":
                shape_transparency=obj.transp
                f.write("appearance Appearance{material Material{diffuseColor %f %f %f\n" % shape_col)
                f.write("transparency %f}}" % shape_transparency)
                f.write("}\n") # closes Shape
            else:
                material_index=material_properties_names.index(color_list_mat[col_index])
                #say(material_properties[material_index])
                #f.write("appearance Appearance{"+material_properties[material_index]+"}}\n")
                f.write("appearance Appearance{material USE "+material_ids[material_index]+" }}\n")
        say(filepath+' written\n')
    #color_list=[]
    #color_list_mat=[]
    #index_color=-1
    #Dialog = QtGui.QDialog()
    #ui = Ui_Dialog()
    #ui.setupUi(Dialog)
    #ui.comboBox.addItems(material_properties_names)
    ##for obj in componentObjs:
    #reply=Dialog.exec_()


###
def exportVRML(objects, filepath):
    """Export given list of Mesh objects to a VRML file.

    `Mesh` structure is defined at root."""

    with __builtin__.open(filepath, 'w') as f:
        # write the standard VRML header
        f.write("#VRML V2.0 utf8\n#kicad StepUp wrl exported\n\n")
        for obj in objects:
            f.write("Shape { geometry IndexedFaceSet \n{ coordIndex [")
            # write coordinate indexes for each face
            f.write(','.join("%d,%d,%d,-1" % f for f in obj.faces))
            f.write("]\n") # closes coordIndex
            f.write("coord Coordinate { point [")
            # write coordinate points for each vertex
            #f.write(','.join('%.3f %.3f %.3f' % (p.x, p.y, p.z) for p in obj.points))
            f.write(','.join('%.5f %.5f %.5f' % (p.x, p.y, p.z) for p in obj.points))
            f.write("]\n}") # closes Coordinate
            #shape_col=(1.0, 0.0, 0.0)#, 0.0)
            f.write("}\n") # closes points
            #say(obj.color)
            shape_col=obj.color[:-1] #remove last item
            #say(shape_col)
            shape_transparency=obj.transp
            f.write("appearance Appearance{material Material{diffuseColor %f %f %f\n" % shape_col)
            f.write("transparency %f}}" % shape_transparency)
            f.write("}\n") # closes Shape
        say(filepath+' written\n')
###

def export(componentObjs, fullfilePathName, scale=None):
    """ Exports given ComponentModel object using FreeCAD.

    `componentObjs` : a ComponentObjs list
    `fullfilePathName` : name of the FC file, extension is important
    
    """
    
    global exportV, applymaterials, ui
    exp_name=componentObjs[0].Label
    path, fname = os.path.split(fullfilePathName)
    fname=os.path.splitext(fname)[0]
    if scale != None:
        filename=path+os.sep+exp_name+'.wrl'
    else:
        filename=path+os.sep+exp_name+'_1_1.wrl'
    say(filename+"\n")
    exportV=True
    mesh_deviation_default=0.03 # 0.03 or 0.1
    mesh_dev=mesh_deviation_default #the smaller the best quality, 1 coarse
    if os.path.exists(filename):
        say('file exists\n')
        QtGui.qApp.restoreOverrideCursor()
        reply = QtGui.QMessageBox.question(None, "Info", filename+"\nwrl file exists, overwrite?",
        QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            # this is where the code relevant to a 'Yes' answer goes
            exportV=True
            #pass
        if reply == QtGui.QMessageBox.No:
            # this is where the code relevant to a 'No' answer goes
            exportV=False
            #pass
    if exportV:
        reply = QtGui.QInputDialog.getText(None, "Mesh Deviation","Mesh Deviation (the smaller the better quality)",QtGui.QLineEdit.Normal,str(mesh_deviation_default))
        if reply[1]:
                # user clicked OK
                replyText = reply[0]
                mesh_dev = float (replyText)
        else:
                # user clicked Cancel
                replyText = reply[0] # which will be "" if they clicked Cancel
                mesh_dev=mesh_deviation_default #the smaller the best quality, 1 coarse
                #default
        #say(mesh_dev)
        color=[]
        Diffuse_color=[]
        transparency=[]
        for obj in componentObjs:
            #say(obj.Label)
            color.append(FreeCADGui.ActiveDocument.getObject(obj.Name).ShapeColor)
            transparency.append(FreeCADGui.ActiveDocument.getObject(obj.Name).Transparency/100.0)
            #say("color")
            #say(FreeCADGui.ActiveDocument.getObject(obj.Name).DiffuseColor)
            Diffuse_color.append(FreeCADGui.ActiveDocument.getObject(obj.Name).DiffuseColor)
        i=0
        meshes=[]
        #say("diffuse color")
        #say(Diffuse_color)
        indexColor=0;
        color_vector=[]
        applyDiffuse=0
        for obj in componentObjs:
            shape1=obj.Shape
            single_color=Diffuse_color[i];
            #check lenght color
            #say("len color")
            #say(len(single_color))
            #colors less then faces
            if(len(single_color)!=len(shape1.Faces)):
                applyDiffuse=0;
                #copy color to all faces
            #else copy singolar colors for faces
            else:
                applyDiffuse=1;
                for color in single_color:
                    color_vector.append(color)
            #say("color_vector")
            #say(color_vector)
            for index in range(len(shape1.Faces)):
                #say("color x")
                #say(color_vector[indexColor])
                singleFace=shape1.Faces[index]
                if(applyDiffuse):
                    #say(color_vector[indexColor])
                    meshes.append(shapeToMesh(singleFace, color_vector[indexColor], transparency[i], mesh_dev, scale))
                else:
                    #say(single_color[0])
                    meshes.append(shapeToMesh(singleFace, single_color[0], transparency[i], mesh_dev, scale))
                indexColor=indexColor+1
                #meshes.append(shapeToMesh(face, Diffuse_color[i], transparency[i], scale))
            color_vector=[]
            indexColor=0;
            i=i+1
        if applymaterials==1:
            exportVRMLmaterials(meshes, filename)
        else:
            exportVRML(meshes, filename)
    return
###

def go_export(fPathName):
    global exportS
    sel = FreeCADGui.Selection.getSelection()
    if not sel:
        FreeCAD.Console.PrintWarning("Select something first!\n\n")
        msg="export VRML from FreeCAD is a python macro that will export simplified VRML of "
        msg+="a (multi)selected Part or fused Part to VRML optimized to Kicad and compatible with Blender "
        msg+="the size of VRML is much smaller compared to the one exported from FC Gui "
        msg+="and the loading/rendering time is also smaller\n"
        msg+="change mesh deviation to increase quality of VRML\n"
        say(msg)
    else:
        objs = []
        for obj in sel:
                objs.append(obj)
                #say(obj.Label)
                #say(obj.Name)
        say(fPathName+'\n')
        #say(objs)
        #export(objs, fullFilePathName, scale=None)
        export(objs, fPathName, 0.3937)
        if len(objs) == 1:
            exportS=True
            exportStep(objs, fPathName)
        else:
            #say("Select ONE single part object !\r\n"+"\r\n")
            exportS=False
            #QtGui.QMessageBox.information(None,"Info ...","Select ONE single part object !\r\n"+"\r\n")
            
###
def exportStep(objs, ffPathName):
    #Export fused object
    global exportS
    exp_name=objs[0].Label
    path, fname = os.path.split(ffPathName)
    #fname=os.path.splitext(fname)[0]
    fullFilePathNameStep=path+os.sep+exp_name+'.step'
    exportS=True
    if os.path.exists(fullFilePathNameStep):
        say('file exists\n')
        QtGui.qApp.restoreOverrideCursor()
        reply = QtGui.QMessageBox.question(None, "Info", fullFilePathNameStep+"\nstep file exists, overwrite?",
        QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            # this is where the code relevant to a 'Yes' answer goes
            exportS=True
            pass
        if reply == QtGui.QMessageBox.No:
            # this is where the code relevant to a 'No' answer goes
            exportS=False
            pass
    if exportS:
        ImportGui.export(objs,fullFilePathNameStep)
        FreeCAD.activeDocument().recompute()
    return
###

home = expanduser("~")
#QtGui.QMessageBox.information(None,"info ...","your home path is \r\n"+ home+"\r\n")
sayw("kicad StepUp version "+str(___ver___))
say("your home path is "+ home+"\r\n")
fname_ksu=home+os.sep+'ksu-config.ini'
ksu_config_fname=fname_ksu
default_ksu_config_ini="""[info]
;; kicad StepUp tools config file
;; each line starting with a semicolon is a comment
[prefix3D]
;; put here your KISYS3DMOD path or 3D model prefix path
;; only ONE prefix is allowed; MUST finish with slash or backslash
;prefix3D_1 = C:\\Program Files\\KiCad\share\\kicad\\modules\\packages3d\\
;prefix3D_1 = kicad/share/modules/packages3d/
prefix3D_1 = C:\\Cad\\Progetti_K\\a_mod\\a_3Dpkg\\
[PcbColor]
;; pcb color r,g,b e.g. 0.0,0.5,0.0,light green
;pcb_color=0.3333,0.3333,0.5,blue
;pcb_color=0.0,0.5,0.0,light green
pcb_color=0.0,0.298,1.0,lightblue (0,76,255)
;pcb_color=0.211,0.305,0.455,darkblue (54,79,116)
[Blacklist]
;; put here your model names that you don't want to load (e.g. smallest ones)
;; separated by a comma (none means all the models will be parsed)
;; (volume=1 means all models with a volume < 1mm3 will not be included)
;; (height=1 means all models with a height < 1mm  will not be included)
;bklist = r_0603,r_0402,c_0402,c_0603
;bklist = height=1.0
;bklist = volume=1.0
;bklist = none
bklist = none
[BoundingBox]
;; bounding box option LIST=>whitelist (not converted to bbox)
;bbox = LIST dpak-to252,sod80
;bbox = ALL
bbox = off default
[Placement]
;; placement options
;placement options: useAuxOrigin, useBaseOrigin, useBasePoint;x;y, usedefault, +AutoAdjust
;placement = useAuxOrigin
;placement = useAuxOrigin +AutoAdjust
;placement = useBasePoint;37.0;50.0;
;placement = useBasePoint;37.0;50.0; +AutoAdjust
;placement = useBaseOrigin #place board @ 0,0,0
;placement = useBaseOrigin +AutoAdjust #place board @ 0,0,0
;placement = usedefault
;placement = usedefault +AutoAdjust
placement = useBaseOrigin #place board @ 0,0,0
[Virtual]
;; virtual modules to be or not added to board
virt = noVirtual
;virt = addVirtual
[ExportFuse]
;; fuse modules to board
;; be careful ... fusion can be heavy or generate FC crash with a lot of objects
;; please consider to use bbox or blacklist small objs
;exportFusing = fuseAll
exportFusing = nofuse  #default
[minimum_drill_size]
;; minimum drill size to be handled 
;; set 0.0 to handle all sizes
min_drill_size = 0.0
[last_pcb_path]
;; last pcb file path used
last_pcb_path =
[last_footprint_path]
;; last footprint file path used
last_fp_path =
[export]
export_to_STEP = yes
;; export to STEP 
;export_to_STEP = yes
;export_to_STEP = no
[Materials]
mat = enablematerials
;; VRML models to be or not exported with material properties
;mat = enablematerials
;mat = nomaterials
"""
default_ksu_msg=[]
default_ksu_msg.append(""";; kicad StepUp tools config file
;; each line starting with a semicolon is a comment""")
default_ksu_msg.append(""";; put here your KISYS3DMOD path or 3D model prefix path
;; only ONE prefix is allowed; MUST finish with slash or backslash
;prefix3D_1 = C:\\Program Files\\KiCad\share\\kicad\\modules\\packages3d\\
;prefix3D_1 = kicad/share/modules/packages3d/""")
default_ksu_msg.append(""";; pcb color r,g,b e.g. 0.0,0.5,0.0,light green
;pcb_color=0.3333,0.3333,0.5,blue
;pcb_color=0.0,0.5,0.0,light green
;pcb_color=0.0,0.298,1.0,lightblue (0,76,255)
;pcb_color=0.211,0.305,0.455,darkblue (54,79,116)""")
default_ksu_msg.append(""";; put here your model names that you don't want to load (e.g. smallest ones)
;; separated by a comma (none means all the models will be parsed)
;; (volume=1 means all models with a volume < 1mm3 will not be included)
;; (height=1 means all models with a height < 1mm  will not be included)
;bklist = r_0603,r_0402,c_0402,c_0603
;bklist = height=1.0
;bklist = volume=1.0
;bklist = none""")
default_ksu_msg.append(""";; bounding box option LIST=>whitelist (not converted to bbox)
;bbox = LIST dpak-to252,sod80
;bbox = ALL
;bbox = off default""")
default_ksu_msg.append(""";; placement options
;placement options: useAuxOrigin, useBaseOrigin, useBasePoint;x;y, usedefault, +AutoAdjust
;placement = useAuxOrigin
;placement = useAuxOrigin +AutoAdjust
;placement = useBasePoint;37.0;50.0;
;placement = useBasePoint;37.0;50.0; +AutoAdjust
;placement = useBaseOrigin #place board @ 0,0,0
;placement = useBaseOrigin +AutoAdjust #place board @ 0,0,0
;placement = usedefault
;placement = usedefault +AutoAdjust""")
default_ksu_msg.append(""";; virtual modules to be or not added to board
;virt = noVirtual
;virt = addVirtual""")
default_ksu_msg.append(""";; fuse modules to board
;; be careful ... fusion can be heavy or generate FC crash with a lot of objects
;; please consider to use bbox or blacklist small objs
;exportFusing = fuseAll
;exportFusing = nofuse  #default""")
default_ksu_msg.append(""";; minimum drill size to be processed in mm
;; set 0.0 to process all sizes
;min_drill_size = 0.0""")
default_ksu_msg.append(""";; last pcb file path used
;last_pcb_path =""")
default_ksu_msg.append(""";; last footprint file path used
;last_fp_path =""")
default_ksu_msg.append(""";; export to STEP 
;export_to_STEP = yes
;export_to_STEP = no""")
default_ksu_msg.append(""";; VRML models to be or not exported with material properties
;mat = enablematerials
;mat = nomaterials""")

def read_ini_file():
    if os.path.isfile(ksu_config_fname):
        say("ksu file \'ksu-config.ini\' exists\r\n")
        ini_content=[]
        #Kicad_Board_elaborated = open(filename, "r").read()[0:]
        txtFile = __builtin__.open(ksu_config_fname,"r")
        ini_content = txtFile.readlines()
        #ini_content.append(" ")
        txtFile.close()
        data=""
        for item in ini_content:
            if item.startswith("["):
                data+="<b><font color=GoldenRod>"+item+"</font></b><br>"
            elif item.startswith(";"):
                data+="<font color=blue>"+item+"</font><br>"
            else:
                data+="<font color=black>"+item+"</font><br>"
        #data+=''.join(ini_content)
        ini_content=re.sub(r'[^\x00-\x7F]+',' ', data)    #workaround to remove utf8 extra chars
        ##ini_content=data
        #msg="""<b>kicad StepUp ver. """
        #msg+=___ver___+"</b><br>"
        #msg+="default ksu config file created<br>"
        #msg+="<b>"+fname+"</b>"
        #reply = QtGui.QMessageBox.information(None,"Info ...",msg)
    else:    
        say("ksu file doesn't exist\r\n")
        say("making default\r\n")
        with __builtin__.open(ksu_config_fname,'w') as myfile:
            myfile.write(default_ksu_config_ini)
            myfile.close()
        ini_content=[]
        txtFile = __builtin__.open(ksu_config_fname,"r")
        ini_content = txtFile.readlines()
        #ini_content.append(" ")
        ini_content
        txtFile.close() 
        data=''.join(ini_content)
        ini_content=re.sub(r'[^\x00-\x7F]+',' ', data) #workaround to remove utf8 extra chars
        ## ini_content=data
        msg="""<b>kicad StepUp ver. """
        msg+=___ver___+"</b><br>"
        msg+="default ksu config file created<br>"
        msg+="<b>"+ksu_config_fname+"</b>"
        msg+="<br>adapt your <b>3D model DIR path</b> in config file<br>"
        msg+="see <b><font color=GoldenRod>[prefix3D]</font></b> section"
        QtGui.qApp.restoreOverrideCursor()
        reply = QtGui.QMessageBox.information(None,"Info ...",msg)
    return ini_content
##

ini_content=read_ini_file()
#time.sleep(0.5)
configParser = ConfigParser.RawConfigParser()  
configParser = ConfigParser.ConfigParser(allow_no_value = True) 
configFilePath = ksu_config_fname
cfgParsRead(configFilePath)

#assign params

def say_time():
    end_milli_time = current_milli_time()
    running_time=(end_milli_time-start_time)/1000
    msg="running time: "+str(running_time)+"sec\n"
    say(msg)
###

def reset_prop(obj,doc,App,Gui):
    #say('resetting props\n')
    ##try:
    newObj =FreeCAD.ActiveDocument.addObject('Part::Feature',obj.Name)
    newObj.Shape=FreeCAD.ActiveDocument.getObject(obj.Name).Shape
    FreeCAD.ActiveDocument.ActiveObject.Label=FreeCAD.ActiveDocument.getObject(obj.Name).Label
    final_Label=FreeCAD.ActiveDocument.getObject(obj.Name).Label
    #say(final_Label+'\n')
    FreeCADGui.ActiveDocument.ActiveObject.ShapeColor=FreeCADGui.ActiveDocument.getObject(obj.Name).ShapeColor
    FreeCADGui.ActiveDocument.ActiveObject.LineColor=FreeCADGui.ActiveDocument.getObject(obj.Name).LineColor
    FreeCADGui.ActiveDocument.ActiveObject.PointColor=FreeCADGui.ActiveDocument.getObject(obj.Name).PointColor
    FreeCADGui.ActiveDocument.ActiveObject.DiffuseColor=FreeCADGui.ActiveDocument.getObject(obj.Name).DiffuseColor
    FreeCAD.ActiveDocument.recompute()
    newObjCommon=FreeCAD.activeDocument().addObject("Part::MultiCommon","Common")
    newObjCommon.Shapes = [FreeCAD.activeDocument().getObject(obj.Name),FreeCAD.activeDocument().getObject(newObj.Name),]
    FreeCADGui.activeDocument().getObject(obj.Name).Visibility=False
    FreeCADGui.activeDocument().getObject(newObj.Name).Visibility=False
    FreeCADGui.ActiveDocument.Common.ShapeColor=FreeCADGui.ActiveDocument.getObject(obj.Name).ShapeColor
    FreeCADGui.ActiveDocument.Common.DisplayMode=FreeCADGui.ActiveDocument.getObject(obj.Name).DisplayMode
    FreeCAD.ActiveDocument.recompute()
    # sleep
    FreeCAD.ActiveDocument.addObject('Part::Feature','Common').Shape=FreeCAD.ActiveDocument.Common.Shape
    FreeCAD.ActiveDocument.ActiveObject.Label=final_Label
    rstObj=FreeCAD.ActiveDocument.ActiveObject
    #
    FreeCADGui.ActiveDocument.ActiveObject.ShapeColor=FreeCADGui.ActiveDocument.Common.ShapeColor
    FreeCADGui.ActiveDocument.ActiveObject.LineColor=FreeCADGui.ActiveDocument.Common.LineColor
    FreeCADGui.ActiveDocument.ActiveObject.PointColor=FreeCADGui.ActiveDocument.Common.PointColor
    FreeCADGui.ActiveDocument.ActiveObject.DiffuseColor=FreeCADGui.ActiveDocument.Common.DiffuseColor
    FreeCAD.ActiveDocument.removeObject("Common")
    FreeCAD.ActiveDocument.recompute()
    #
    return rstObj

def reset_prop_shapes(obj,doc,App,Gui):

    s=obj.Shape
    #say('resetting props #2\n')
    r=[]
    t=s.copy()
    for i in t.childShapes():
        c=i.copy()
        c.Placement=t.Placement.multiply(c.Placement)
        r.append((i,c))

    w=t.replaceShape(r)
    w.Placement=FreeCAD.Placement()
    Part.show(w)
    #say(w)
    #say('\n')
    FreeCADGui.ActiveDocument.ActiveObject.ShapeColor=FreeCADGui.ActiveDocument.Part__Feature.ShapeColor
    FreeCADGui.ActiveDocument.ActiveObject.LineColor=FreeCADGui.ActiveDocument.Part__Feature.LineColor
    FreeCADGui.ActiveDocument.ActiveObject.PointColor=FreeCADGui.ActiveDocument.Part__Feature.PointColor
    FreeCADGui.ActiveDocument.ActiveObject.DiffuseColor=FreeCADGui.ActiveDocument.Part__Feature.DiffuseColor
    new_label=obj.Label
    FreeCAD.ActiveDocument.removeObject(obj.Name)
    FreeCAD.ActiveDocument.recompute()
    FreeCAD.ActiveDocument.ActiveObject.Label=new_label
    rstObj=FreeCAD.ActiveDocument.ActiveObject
    #say(rstObj)
    #say('\n')

    return rstObj


def Display_info(blacklisted_models):
    global bbox_all, bbox_list, fusion, show_messages, last_pcb_path
    global height_minimum, volume_minimum, idf_to_origin, ksu_config_fname
    global board_base_point_x, board_base_point_y, real_board_pos_x, real_board_pos_y
    say('info message\n')
    if blacklisted_model_elements != '':
        sayw("black-listed module "+ '\r\n'.join(map(str, blacklisted_models)))
        if (show_messages==True):
            QtGui.qApp.restoreOverrideCursor()
            reply = QtGui.QMessageBox.information(None,"Info ...","... black-listed module(s)\r\n"+ '\r\n'.join(map(str, blacklisted_models)))
        #FreeCAD.Console.PrintMessage("black-listed module "+ '\r\n'.join(map(str, blacklisted_models)))    
    
    msg="""<b>kicad StepUp</b> ver. """
    msg+=___ver___
    #if len(msgpath)>15:
    #    insert_return(msgpath, 15)
    if (idf_to_origin==True):
        new_pos_x=board_base_point_x+real_board_pos_x
        new_pos_y=board_base_point_y+real_board_pos_y
    else:
        new_pos_x=board_base_point_x
        new_pos_y=board_base_point_y
    msg+="<br>Board Placed @ "+str(new_pos_x)+";"+str(new_pos_y)+";0.0"
    msg+="<br>kicad pcb pos: ("+"{0:.3f}".format(real_board_pos_x)+";"+"{0:.3f}".format(real_board_pos_y)+";"+"{0:.2f}".format(0)+")"
    if (bbox_all==1) or (bbox_list==1):
        msg+="<br>bounding box modules applied"
    if (volume_minimum!=0):
        msg+="<br>modules with volume less then "+str(volume_minimum)+"mm^3 not included"
    if (height_minimum!=0):
        msg+="<br>modules with height less then "+str(height_minimum)+"mm not included"    
    msg+="<br>kicad StepUp config file in:<br><b>"+ksu_config_fname+"</b><br>location."
    say("Board Placed @ "+str(new_pos_x)+";"+str(new_pos_y)+";0.0\n")
    say("kicad pcb pos: ("+"{0:.3f}".format(real_board_pos_x)+";"+"{0:.3f}".format(real_board_pos_y)+";"+"{0:.2f}".format(0)+")\n")    
    if (show_messages==True):
        QtGui.qApp.restoreOverrideCursor()
        reply = QtGui.QMessageBox.information(None,"Info ...",msg)
###

def Export2MCAD(blacklisted_model_elements):
    global bbox_all, bbox_list, fusion, show_messages, last_pcb_path
    global height_minimum, volume_minimum, idf_to_origin, ksu_config_fname
    global board_base_point_x, board_base_point_y, real_board_pos_x, real_board_pos_y
    say('exporting to MCAD\n')
    ## exporting
    __objs__=[]
    doc=FreeCAD.ActiveDocument
    for obj in doc.Objects:
        # do what you want to automate
        if (obj.Label!="Board_Geoms") and (obj.Label!="Step_Models"):
            FreeCADGui.Selection.addSelection(obj)
            __objs__.append(obj)
    filePath=last_pcb_path
    if (bbox_all==1) or (bbox_list==1):
        fpath=filePath+os.sep+doc.Label+"_bbox"+'.step'
    else:
        fpath=filePath+os.sep+doc.Label+'.step'
    ImportGui.export(__objs__,fpath)
    #fusion=False
    ## be careful ... fusion can be heavy or generate FC crash with a lot of objects
    ## please consider to use bbox or blacklist small objs
    if (fusion==True):
        # Fuse objects
        doc.addObject("Part::MultiFuse","Fusion")
        doc.Fusion.Shapes = __objs__
    #    doc.ActiveObject.Label=doc.Name+"_union"
        doc.recompute()
        doc.addObject('Part::Feature','Fusion').Shape=FreeCAD.ActiveDocument.Fusion.Shape
        if (bbox_all==1) or (bbox_list==1):
            doc.ActiveObject.Label=doc.Name+"_bbox_union"
        else:
            doc.ActiveObject.Label=doc.Name+"_union"
        FreeCADGui.ActiveDocument.ActiveObject.ShapeColor=FreeCADGui.ActiveDocument.Fusion.ShapeColor
        FreeCADGui.ActiveDocument.ActiveObject.LineColor=FreeCADGui.ActiveDocument.Fusion.LineColor
        FreeCADGui.ActiveDocument.ActiveObject.PointColor=FreeCADGui.ActiveDocument.Fusion.PointColor
        FreeCADGui.ActiveDocument.ActiveObject.DiffuseColor=FreeCADGui.ActiveDocument.Fusion.DiffuseColor
        # Remove the fusion object
        doc.removeObject("Fusion")
        doc.recompute()
        fobjs=[]
        fused_obj=doc.ActiveObject
        FreeCAD.Console.PrintMessage(fused_obj)
        fobjs.append(fused_obj)
        if (bbox_all==1) or (bbox_list==1):
            fpath=filePath+os.sep+doc.Label+"_bbox_union"+'.step'
        else:
            fpath=filePath+os.sep+doc.Label+"_union"+'.step'
        FreeCAD.Console.PrintMessage(fpath+" fusion path \r\n")
        FreeCAD.Console.PrintMessage(fobjs)
        #Export fused object
        ImportGui.export(fobjs,fpath)
        FreeCAD.activeDocument().recompute()
        del fobjs
        #ImportGui.export(doc.ActiveObject,filePath+os.sep+doc.Label+'.step')
    for obj in doc.Objects:
        # do what you want to automate
        FreeCADGui.Selection.removeSelection(obj)
    if blacklisted_model_elements != '':
        sayw("black-listed module "+ '\r\n'.join(map(str, blacklisted_models)))
        if (show_messages==True):
            QtGui.qApp.restoreOverrideCursor()
            reply = QtGui.QMessageBox.information(None,"Info ...","... black-listed module(s)\r\n"+ '\r\n'.join(map(str, blacklisted_models)))
        #FreeCAD.Console.PrintMessage("black-listed module "+ '\r\n'.join(map(str, blacklisted_models)))    
    del __objs__
    ## Save to disk in native format
    FreeCAD.ActiveDocument=None
    FreeCADGui.ActiveDocument=None
    FreeCAD.setActiveDocument(doc.Name)
    FreeCAD.ActiveDocument=FreeCAD.getDocument(doc.Name)
    FreeCADGui.ActiveDocument=FreeCADGui.getDocument(doc.Name)
    if (bbox_all==1) or (bbox_list==1):
        fpath=filePath+os.sep+doc.Name+"_bbox"
    else:
        fpath=filePath+os.sep+doc.Name
    if (fusion==True):
        fpath=fpath+"_union"
    say(fpath+".FCStd"+"\n")
    FreeCAD.getDocument(doc.Name).saveAs(fpath+".FCStd")
    FreeCAD.ActiveDocument.recompute()
    FreeCAD.getDocument(doc.Name).Label = doc.Name
    FreeCADGui.SendMsgToActiveView("Save")
    FreeCAD.getDocument(doc.Name).save()
    msgpath=filePath+os.sep+doc.Name
    if (bbox_all==1) or (bbox_list==1):
        msgpath=msgpath+"_bbox"

    msg="""<b>kicad StepUp</b> ver. """
    msg+=___ver___
    msg+="<br>file exported<br><b>"+msgpath+'.step</b>'
    #if len(msgpath)>15:
    #    insert_return(msgpath, 15)
    if (fusion==True):
        msgpath=msgpath+"_union"
        msg+="<br>fused file exported<br><b>"+msgpath+'.step</b>'    
    if (idf_to_origin==True):
        new_pos_x=board_base_point_x+real_board_pos_x
        new_pos_y=board_base_point_y+real_board_pos_y
    else:
        new_pos_x=board_base_point_x
        new_pos_y=board_base_point_y
    msg+="<br>Board Placed @ "+str(new_pos_x)+";"+str(new_pos_y)+";0.0"
    msg+="<br>kicad pcb pos: ("+"{0:.3f}".format(real_board_pos_x)+";"+"{0:.3f}".format(real_board_pos_y)+";"+"{0:.2f}".format(0)+")"
    if (bbox_all==1) or (bbox_list==1):
        msg+="<br>bounding box modules applied"
    if (volume_minimum!=0):
        msg+="<br>modules with volume less then "+str(volume_minimum)+"mm^3 not included"
    if (height_minimum!=0):
        msg+="<br>modules with height less then "+str(height_minimum)+"mm not included"    
    msg+="<br>kicad StepUp config file in:<br><b>"+ksu_config_fname+"</b><br>location."
    say("Board Placed @ "+str(new_pos_x)+";"+str(new_pos_y)+";0.0\n")
    say("kicad pcb pos: ("+"{0:.3f}".format(real_board_pos_x)+";"+"{0:.3f}".format(real_board_pos_y)+";"+"{0:.2f}".format(0)+")\n")    
    if (show_messages==True):
        QtGui.qApp.restoreOverrideCursor()
        reply = QtGui.QMessageBox.information(None,"Info ...",msg)    
###

def Load_models(pcbThickness,modules):
    global off_x, off_y, volume_minimum, height_minimum, bbox_all, bbox_list
    global whitelisted_model_elements, models3D_prefix, last_pcb_path
    #say (modules)
    missing_models = ''
    for i in range(len(modules)):
        step_module=modules[i][0]
        #say(modules[i]);say('\n')
        #FreeCAD.Console.PrintMessage('step-module '+step_module+'\r\n')
        if (step_module.find('${KIPRJMOD}')!=-1):  #local 3D path
            #step_module=step_module.replace('${KIPRJMOD}', '.')
            step_module=step_module.replace('${KIPRJMOD}', last_pcb_path)
            say('adjusting Local Path\r\n')
            say('step-module-replaced '+step_module+'\n')
        if step_module != 'no3Dmodel':
            step_module=step_module[:-3]+'step'
            step_module2=step_module[:-4]+'stp'
            step_module3=step_module[:-4]+'iges'
            step_module4=step_module[:-4]+'igs'
            model_name=step_module[:-5]
            last_slash_pos1=model_name.rfind('/')
            last_slash_pos2=model_name.rfind('\\')
            last_slash_pos=max(last_slash_pos1,last_slash_pos2)
            model_name=model_name[last_slash_pos+1:]
            say('model name '+model_name+'\n')
        else:
            model_name='no3Dmodel'
        blacklisted=0
        if blacklisted_model_elements != '':
            if blacklisted_model_elements.find(model_name) != -1:
                blacklisted=1
        ###
        if (blacklisted==0):
            if step_module != 'no3Dmodel':
                module_path='not-found'
                step_module=step_module.replace('"', '')  # name with spaces
                if os.path.exists(models3D_prefix+step_module):
                    module_path=models3D_prefix+step_module
                else:
                    if os.path.exists(step_module): # absolute path
                        module_path=step_module
                #adding .stp support
                if os.path.exists(models3D_prefix+step_module2) and (module_path=='not-found'):
                    module_path=models3D_prefix+step_module2
                else:
                    if os.path.exists(step_module2) and (module_path=='not-found'): # absolute path
                        module_path=step_module2
                #adding .iges support
                if os.path.exists(models3D_prefix+step_module3) and (module_path=='not-found'):
                    module_path=models3D_prefix+step_module3
                else:
                    if os.path.exists(step_module3) and (module_path=='not-found'): # absolute path
                        module_path=step_module3
                #adding .igs support
                if os.path.exists(models3D_prefix+step_module4) and (module_path=='not-found'):
                    module_path=models3D_prefix+step_module4
                else:
                    if os.path.exists(step_module4) and (module_path=='not-found'): # absolute path
                        module_path=step_module4
                if module_path!='not-found':
                    #FreeCADGui.Selection.removeSelection(FreeCAD.activeDocument().ActiveObject)  mauitemp volume diff
                    say("opening "+ module_path+'\n')
                    doc1=FreeCAD.ActiveDocument
                    counterObj=0;counter=0
                    for ObJ in doc1.Objects:
                        counterObj+=1
                    ImportGui.insert(module_path,FreeCAD.ActiveDocument.Name)
                    for ObJ in doc1.Objects:
                        counter+=1
                    #say(counter)
                    if counterObj+1 != counter:
                        msg="""3D STEP model <b><font color=red>"""
                        msg+=model_name+"</font> is NOT fused in a single part</b> ...<br>"
                        msg+="@ "+module_path+" <br>...stopping execution! <br>Please <b>fix</b> the model."
                        QtGui.qApp.restoreOverrideCursor()
                        reply = QtGui.QMessageBox.information(None,"Info ...",msg)
                        stop
                    if FreeCAD.ActiveDocument.ActiveObject.Label.endswith('001'):
                        msg="""3D STEP model <b><font color=red>"""
                        msg+=model_name+"</font> is NOT fused in a single part</b> ...<br>"
                        msg+="@ "+module_path+" <br>...stopping execution! <br>Please <b>fix</b> the model."
                        QtGui.qApp.restoreOverrideCursor()
                        reply = QtGui.QMessageBox.information(None,"Info ...",msg)
                        stop
                    #say('alive')
                    pos_x=modules[i][1]-off_x
                    pos_y=modules[i][2]-off_y
                    rot=modules[i][3]
                    step_layer=modules[i][4]
                    #say (str(rot))
                    impPart=FreeCAD.ActiveDocument.ActiveObject
                    say("module "+step_module+"\n")
                    impPart.Label = impPart.Label + '_'
                    #say("selection 3D model "+ impPart.Label+'\n')
                    impPart=reset_prop_shapes(impPart,FreeCAD.ActiveDocument, FreeCAD,FreeCADGui)
                    model3D=impPart.Name
                    #say("impPart "+ impPart.Name+'\n')
                    obj = FreeCAD.ActiveDocument.getObject(model3D)
                    FreeCADGui.Selection.addSelection(obj)
                    obj=FreeCAD.ActiveDocument.ActiveObject
                    #volume_minimum=1
                    myPart=FreeCAD.ActiveDocument.getObject(obj.Name)   #mauitemp min vol
                    #sayw(obj.Label)
                    #sayw(step_layer);
                    #sayw(str(myPart.Shape.Volume))
                    #sayw(str(myPart.Shape.BoundBox.ZMax))
                    if myPart.Shape.Volume>volume_minimum:  #mauitemp min vol
                        if abs(myPart.Shape.BoundBox.ZMax)>height_minimum:  #mauitemp min height
                            if (height_minimum!=0):
                                say("height > Min height "+ str(myPart.Shape.BoundBox.ZMax) + " "+impPart.Label+'\r\n')
                            if (volume_minimum!=0):
                                say("Volume > Min Volume "+ str(myPart.Shape.Volume) + " "+impPart.Label+'\r\n')
                            if (bbox_all==1) or (bbox_list==1):
                                    if whitelisted_model_elements.find(model_name) == -1:
                                        bboxName=createSolidBBox(model3D)
                            #say(str(bbox_all)+'bbox'+str(bbox_list)+'\n')
                            #stop
                            if step_layer == 'Top':
                                impPart.Placement = FreeCAD.Placement(FreeCAD.Vector(pos_x,pos_y,0),FreeCAD.Rotation(FreeCAD.Vector(0,0,1),rot))
                                if (bbox_all==1) or (bbox_list==1):
                                    #say('bbox\n')
                                    if whitelisted_model_elements.find(model_name) == -1:
                                        bbox_col=bbox_default_col
                                        #say("bboxName "+ bboxName +'\r\n')
                                        #say("bboxName "+str(bboxName.upper().startswith('R'))+'\r\n')
                                        if (bboxName.upper().startswith('X')):
                                            bbox_col=bbox_x_col
                                        if (bboxName.upper().startswith('L')):
                                            bbox_col=bbox_l_col
                                        if (bboxName.upper().startswith('R')):
                                            bbox_col=bbox_r_col
                                        if (bboxName.upper().startswith('C')):
                                            bbox_col=bbox_c_col
                                        if (bboxName.upper().startswith('S')|bboxName.upper().startswith('Q')|bboxName.upper().startswith('D')|bboxName.upper().startswith('T')):
                                            bbox_col=bbox_IC_col
                                        obj = FreeCAD.ActiveDocument.getObject(bboxName)
                                        obj.Placement = FreeCAD.Placement(FreeCAD.Vector(pos_x,pos_y,0),FreeCAD.Rotation(FreeCAD.Vector(0,0,1),rot))
                                        FreeCADGui.ActiveDocument.getObject(bboxName).ShapeColor=bbox_col
                                        FreeCADGui.Selection.addSelection(obj)
                                        #say("selection 3D model "+ obj.Name+'\r\n')
                                        FreeCAD.ActiveDocument.getObject("Step_Models").addObject(obj)
                                FreeCADGui.Selection.addSelection(impPart)
                                FreeCAD.ActiveDocument.getObject("Step_Models").addObject(impPart)
                                if (bbox_all==1) or (bbox_list==1):
                                    if whitelisted_model_elements.find(model_name) == -1:
                                        FreeCAD.activeDocument().removeObject(impPart.Name)
                            #FreeCAD.activeDocument().removeObject(impPart.Name)
                            ###
                            else:
                            #Bottom
                            #Bottom
                                impPart.Placement = FreeCAD.Placement(FreeCAD.Vector(pos_x,pos_y,-pcbThickness),FreeCAD.Rotation(FreeCAD.Vector(0,1,0),180))
                                #obj.Placement = impPart.Placement
                                shape=impPart.Shape.copy()
                                shape.Placement=impPart.Placement;
                                shape.rotate((pos_x,pos_y,-pcbThickness),(0,0,1),-rot+180)
                                impPart.Placement=shape.Placement
                                if (bbox_all==1) or (bbox_list==1):
                                    if whitelisted_model_elements.find(model_name) == -1:
                                        bbox_col=bbox_default_col
                                        if (bboxName.upper().startswith('X')):
                                            bbox_col=bbox_x_col
                                        if (bboxName.upper().startswith('L')):
                                            bbox_col=bbox_l_col
                                        if (bboxName.upper().startswith('R')):
                                            bbox_col=bbox_r_col
                                        if (bboxName.upper().startswith('C')):
                                            bbox_col=bbox_c_col
                                        if (bboxName.upper().startswith('S')|bboxName.upper().startswith('Q')|bboxName.upper().startswith('D')|bboxName.upper().startswith('T')):
                                            bbox_col=bbox_IC_col
                                        obj = FreeCAD.ActiveDocument.getObject(bboxName)
                                        FreeCADGui.Selection.addSelection(obj)
                                        obj.Placement = FreeCAD.Placement(FreeCAD.Vector(pos_x,pos_y,-pcbThickness),FreeCAD.Rotation(FreeCAD.Vector(0,1,0),180))
                                        shape2=obj.Shape.copy()
                                        shape2.Placement=obj.Placement;
                                        shape2.rotate((pos_x,pos_y,-pcbThickness),(0,0,1),-rot+180)
                                        obj.Placement=shape2.Placement
                                        FreeCADGui.ActiveDocument.getObject(bboxName).ShapeColor=bbox_col
                                        FreeCADGui.Selection.addSelection(obj)
                                        FreeCAD.ActiveDocument.getObject(obj.Name)
                                        FreeCAD.ActiveDocument.getObject("Step_Models").addObject(obj)
                                FreeCADGui.Selection.addSelection(impPart)
                                FreeCAD.ActiveDocument.getObject(impPart.Name)
                                FreeCAD.ActiveDocument.getObject("Step_Models").addObject(impPart)
                                if (bbox_all==1) or (bbox_list==1):
                                    if whitelisted_model_elements.find(model_name) == -1:
                                        FreeCAD.activeDocument().removeObject(impPart.Name)
                                #Part.show(shape)
                                #Part.show(shape2)
                                #say("todo ...\n")
                        else:  #mauitemp min height
                            FreeCAD.activeDocument().removeObject(obj.Name)
                    else:  #mauitemp min vol
                        FreeCAD.activeDocument().removeObject(obj.Name)
                ###
                else:
                    say("error missing "+ models3D_prefix+step_module+'\r\n')
                    test = missing_models.find(step_module)
                    if test is -1:
                        missing_models += models3D_prefix+step_module+'\r\n' #matched
            ###
        ###
    ###
    #sleep
    FreeCAD.ActiveDocument.recompute()
    if missing_models != '':
        QtGui.qApp.restoreOverrideCursor()
        reply = QtGui.QMessageBox.information(None,"Error ...","... missing module(s)\r\n"+ missing_models)
    #if blacklisted_model_elements != '':
    #    FreeCAD.Console.PrintMessage("black-listed module "+ '\n'.join(map(str, blacklisted_models)))
    #    reply = QtGui.QMessageBox.information(None,"Info ...","... black-listed module(s)\n"+ '\n'.join(map(str, blacklisted_models)))
    #    #FreeCAD.Console.PrintMessage("black-listed module "+ '\n'.join(map(str, blacklisted_models)))
    return blacklisted_model_elements
###


def LoadKicadBoard (board_fname):
    # checking FC version requirement
    ######################################################################
    #say("FC Version \r\n")
    #say(FreeCAD.Version())
    global start_time, fusion
    FC_majorV=FreeCAD.Version()[0]
    FC_minorV=FreeCAD.Version()[1]
    say('FC Version '+FC_majorV+FC_minorV+'\r\n')    
    msg1="use ONLY FreeCAD STABLE version 0.15 or later\r\n"
    #msg1+="to generate your STEP and VRML models\r\nFC 016 dev version results are still unpredictable"
    msg1+="to generate your STEP and VRML models\r\n"
    if int(FC_majorV) <= 0:
        if int(FC_minorV) < 15:
            QtGui.qApp.restoreOverrideCursor()
            reply = QtGui.QMessageBox.information(None,"Warning! ...",msg1)    
    msg=''
    if (fusion==True):
        msg+="you have chosen: fuse modules to board\r\nbe careful ... fusion can be heavy or generate FC crash"
        msg+="when fusing a lot of objects\r\nplease consider to use bbox or blacklist small objects\r\n\r\n"    
    ##start_time=current_milli_time()
    xMax=0; xmin=0; yMax=0; ymin=0
    Levels = {}
    Edge_Cuts_lvl=0;Top_lvl=0
    Kicad_Board_elaborated,Levels,Edge_Cuts_lvl,Top_lvl,PCBVersion,pcbThickness = Elaborate_Kicad_Board(board_fname)
    say('PCBThickness'+str(pcbThickness)+' mm\n')
    modules = []
    #sayw(str(Top_lvl)+' top_lvl')
    #stop
    modules = getParts(modules,Top_lvl,Kicad_Board_elaborated,Levels)
    #pads=[]
    #for i in range(len(modules)):
    #    for j in range(len(modules[i])):
    #        #print len(modules[i])
    #        print modules[i][j]
    return pcbThickness,modules,Kicad_Board_elaborated
### end LoadKicadBoard

def getPads(board_elab,pcbThickness):
    # pad
    TopPadList=[]
    BotPadList=[]
    HoleList=[]
    THPList=[]
    for module in re.findall(r'\[start\]\(module(.+?)\)\[stop\]', board_elab, re.MULTILINE|re.DOTALL):
        [X1, Y1, ROT] = re.search(r'\(at\s+([0-9\.-]*?)\s+([0-9\.-]*?)(\s+[0-9\.-]*?|)\)', module).groups()
        #
        X1 = float(X1)
        Y1 = float(Y1) * (-1)
        if ROT == '':
            ROT = 0.0
        else:
            ROT = float(ROT)
        #say('module pos & rot '+str(X1)+' '+str(Y1)+' '+str(ROT)+'\n')
        #
        for pad in getPadsList(module):
            #say (pad)
            #   pads.append({'x': x, 'y': y, 'rot': rot, 'padType': pType, 'padShape': pShape, 'rx': drill_x, 'ry': drill_y, 'dx': dx, 'dy': dy, 'holeType': hType, 'xOF': xOF, 'yOF': yOF, 'layers': layers})
            pType = pad['padType']
            pShape = pad['padShape']
            xs = pad['x'] + X1
            ys = pad['y'] + Y1
            dx = pad['dx']
            dy = pad['dy']
            hType = pad['holeType']
            drill_x = pad['rx']
            drill_y = pad['ry']
            xOF = pad['xOF']
            yOF = pad['yOF']
            rot = pad['rot']
            if ROT != 0:
                rot -= ROT
            rx=drill_x
            ry=drill_y
            rx=float(rx)
            ry=float(ry)
            numberOfLayers = pad['layers'].split(' ')
            #if pType=="thru_hole":
            #pad shape - circle/rec/oval/trapezoid
            perc=0
            if pShape=="circle" or pShape=="oval":
                pShape="oval"
                perc=100
                # pad type - SMD/thru_hole/connect
            if dx>rx and dy>ry:
                #say(pType+"\r\n")
                #say(str(dx)+"+"+str(rx)+" dx,rx\r\n")
                #say(str(dy)+"+"+str(ry)+" dy,ry\r\n")
                #say(str(xOF)+"+"+str(yOF)+" xOF,yOF\r\n")
                x1=xs+xOF
                y1=ys-yOF #yoffset opposite
                #say(str(x1)+"+"+str(y1)+" x1,y1\r\n")
                top=False
                bot=False
                if 'F.Cu' in numberOfLayers:
                    top=True
                if '*.Cu' in numberOfLayers:
                    top=True
                    bot=True
                if 'B.Cu' in numberOfLayers:
                    bot=True
            if rx!=0:
                #say(str(min_drill_size));say(' ');say(rx);say(' ');say(str(ry));say('\n')
                if (rx >= min_drill_size) or (ry >= min_drill_size):
                    obj=createHole3(xs,ys,rx,ry,"oval",pcbThickness) #need to be separated instructions
                    #say(HoleList)
                    if rot!=0:
                        rotateObj(obj, [xs, ys, rot])
                    rotateObj(obj, [X1, Y1, ROT])
                    HoleList.append(obj)    
            ### cmt- #todo: pad type trapez
    return HoleList
###
def getPads_flat(board_elab):
    # pad
    TopPadList=[]
    BotPadList=[]
    HoleList=[]
    THPList=[]
    for module in re.findall(r'\[start\]\(module(.+?)\)\[stop\]', board_elab, re.MULTILINE|re.DOTALL):
        [X1, Y1, ROT] = re.search(r'\(at\s+([0-9\.-]*?)\s+([0-9\.-]*?)(\s+[0-9\.-]*?|)\)', module).groups()
        #
        X1 = float(X1)
        Y1 = float(Y1) * (-1)
        if ROT == '':
            ROT = 0.0
        else:
            ROT = float(ROT)
        #say('module pos & rot '+str(X1)+' '+str(Y1)+' '+str(ROT)+'\n')
        #
        for pad in getPadsList(module):
            #say (pad)
            #say("\r\n")
            #   pads.append({'x': x, 'y': y, 'rot': rot, 'padType': pType, 'padShape': pShape, 'rx': drill_x, 'ry': drill_y, 'dx': dx, 'dy': dy, 'holeType': hType, 'xOF': xOF, 'yOF': yOF, 'layers': layers})
            pType = pad['padType']
            pShape = pad['padShape']
            xs = pad['x'] + X1
            ys = pad['y'] + Y1
            dx = pad['dx']
            dy = pad['dy']
            hType = pad['holeType']
            drill_x = pad['rx']
            drill_y = pad['ry']
            xOF = pad['xOF']
            yOF = pad['yOF']
            rot = pad['rot']
            if ROT != 0:
                rot -= ROT
            rx=drill_x
            ry=drill_y
            rx=float(rx)
            ry=float(ry)
            numberOfLayers = pad['layers'].split(' ')
            #say(numberOfLayers +'\n')
            #if pType=="thru_hole":
            #pad shape - circle/rec/oval/trapezoid
            perc=0
            if pShape=="circle" or pShape=="oval":
                pShape="oval"
                perc=100
                # pad type - SMD/thru_hole/connect
            if dx>rx and dy>ry:
                #say(pType+"\r\n")
                #say(str(dx)+"+"+str(rx)+" dx,rx\r\n")
                #say(str(dy)+"+"+str(ry)+" dy,ry\r\n")
                #say(str(xOF)+"+"+str(yOF)+" xOF,yOF\r\n")
                x1=xs+xOF
                y1=ys-yOF #yoffset opposite
                #say(str(x1)+"+"+str(y1)+" x1,y1\r\n")
                top=False
                bot=False
                if 'F.Cu' in numberOfLayers:
                    top=True
                if '*.Cu' in numberOfLayers:
                    top=True
                    bot=True
                if 'B.Cu' in numberOfLayers:
                    bot=True
            if rx!=0:
                #say(str(min_drill_size));say(' ');say(rx);say(' ');say(str(ry));say('\n')
                #if (rx > min_drill_size):
                if (rx >= min_drill_size) or (ry >= min_drill_size):
                    #obj=createHole3(xs,ys,rx,ry,"oval",pcbThickness) #need to be separated instructions
                    obj=createHole4(xs,ys,rx,ry,"oval") #need to be separated instructions
                    #say(HoleList)
                    if rot!=0:
                        rotateObj(obj, [xs, ys, rot])
                    rotateObj(obj, [X1, Y1, ROT])
                    HoleList.append(obj)
            ### cmt- #todo: pad type trapez
    return HoleList
###

def Elaborate_Kicad_Board(filename):
    global xMax, xmin, yMax, ymin
    Levels={}
    content=[]
    txtFile = __builtin__.open(filename,"r")
    content = txtFile.readlines()
    content.append(" ")
    txtFile.close()
    data=''.join(content)
    content=re.sub(r'[^\x00-\x7F]+',' ', data) #workaround to remove utf8 extra chars
    ## content=data
    #say(len(content))
    Kicad_Board_elaborated = content #''.join(content)
    if save_temp_data:
        home = expanduser("~")
        t1_name=home+os.sep+'test.txt'
        f = __builtin__.open(t1_name,'w')
        f.write(Kicad_Board_elaborated) # python will convert \n to os.linesep
        f.close() # you can omit in most cases as the destructor will call it        
    #say(len(Kicad_Board_elaborated))
    #stop
    version=getPCBVersion(Kicad_Board_elaborated)
    pcbThickness=getPCBThickness(Kicad_Board_elaborated)
    say('kicad_pcb version ' +str(version)+'\n')
    if version < 3:
        QtGui.qApp.restoreOverrideCursor()
        reply = QtGui.QMessageBox.information(None,"Error ...","... KICAD pcb version "+ str(version)+" not supported \r\n"+"\r\nplease open and save your board with the latest kicad version")
        sys.exit("pcb version not supported")
    if version==3:
        Edge_Cuts_lvl=28
        Top_lvl=15
    if version>=4:
        Edge_Cuts_lvl=44
        Top_lvl=0
    # say(Kicad_Board)
    modified = ''
    j = 0; txt = ''; start = 0; s=0; prev_char="_"
    closing_char=""
    #print len(Kicad_Board_elaborated)
    for i in Kicad_Board_elaborated[1:]:
        if i in ['"', "'"] and s == 0:
            closing_char=i
            if prev_char!="\\":
                s = 1
        elif i in [closing_char] and s == 1:
            if prev_char!="\\":
                s = 0
        if s == 0:
            if i == '(':
                j += 1
                start = 1
            elif i == ')':
                j -= 1
        txt += i
        prev_char=i
        if j == 0 and start == 1:
            modified += '[start]' + txt.strip() + '[stop]'
            txt = ''
            start = 0
    #say(len(modified))
    #stop #maui
    layers = re.search(r'\[start\]\(layers(.+?)\)\[stop\]', modified, re.MULTILINE|re.DOTALL).group(0)
    for k in re.findall(r'\((.*?) (.*?) .*?\)', layers):
        Levels[k[1]] = int(k[0])
        if Levels[k[1]] == Edge_Cuts_lvl: ##Edge.Cuts pcb version 4
            #myfile3.write(str(k)[8:-2]+'\r\n')
            pcbEdgeName=str(k)[8:-2]
    if save_temp_data:
        home = expanduser("~")
        t2_name=home+os.sep+'testM.txt'
        f = __builtin__.open(t2_name,'w')
        f.write(modified) # python will convert \n to os.linesep
        f.close() # you can omit in most cases as the destructor will call it
    return modified,Levels,Edge_Cuts_lvl,Top_lvl,version,pcbThickness
### end Elaborate_Kicad_Board

def getParts(PCB_Models,Top_lvl,Kicad_Board_elaborated,Levels):
    global addVirtual
    PCB_Models = []
    for i in re.findall(r'\[start\]\(module(.+?)\)\[stop\]', Kicad_Board_elaborated, re.MULTILINE|re.DOTALL):
        ### print i
        [x, y, rot] = re.search(r'\(at\s+([0-9\.-]*?)\s+([0-9\.-]*?)(\s+[0-9\.-]*?|)\)', i).groups()
        layer = re.search(r'\(layer\s+(.+?)\)', i).groups()[0]
        x = float(x)
        y = float(y) * (-1)
        if rot == '':
            rot = 0.0
        else:
            rot = float(rot)
        #rot=rot-rotz  #adding vrml module z-rotation
        ### print layer
        if Levels[layer] == Top_lvl:  # top
            side = "Top"
        else:
            side = "Bottom"
            rot *= -1
        #model = re.search(r'\(model\s+(.+?)\.wrl',i)
        model_name='no3Dmodel'
        #side='noLayer'
        model_list= re.findall(r'\(model\s+(.+?)\.wrl',i)
        for j in range(0,len(model_list)):
            rotz_vrml = re.findall(r'\(rotate\s+(.+?)\)', i)
            rotz=''
            if rotz_vrml:
                rotz=rotz_vrml[j]
                #say("rotz:"+rotz+"\r\n")
                #rotz=rotz[13:-1]
                rotz=rotz[5:]
                #say("rotz:"+rotz+"\r\n")
                temp=rotz.split(" ")
                #say("rotz temp:"+temp[2]+"\r\n")
                rotz=temp[2]
                #say("rotate vrml: "+rotz+"\r\n")
            if rotz=='':
                rotz=0.0
            else:
                rotz=float(rotz)
            rot=rot-rotz  #adding vrml module z-rotation
            model=model_list[j]+'.wrl'
            #say (model+'\r')
            #virtual = re.search(r'\(attr\s+(.+?)virtual\)',i)
            virtual=0
            if (i.find("virtual")!=-1):
                virtual=1
            if (virtual==1 and addVirtual==0):
                model_name='no3Dmodel'
                side='noLayer'
            else:
                if model:
                    # print model.group(0)
                    #model_name=model.group(0)[6:]
                    #model_name=model[6:]
                    model_name=model
                    #model_name=model_name[1:]
                    #print model_name
                else:
                    model_name='no3Dmodel'
                    side='noLayer'
                line = []
                line.append(model_name)
                line.append(x)
                line.append(y)
                line.append(rot)
                line.append(side)
                PCB_Models.append(line)
        ##virtual = re.search(r'\(attr\s+(.+?)virtual\)',i)
    ####
    # print i
    # print PCB_EL
    return PCB_Models
### end getParts

def getPCBThickness(Board):
    #print len(Kicad_Board)
    return float(re.findall(r'\(thickness (.+?)\)', Board)[0])

def getPCBVersion(Board):
    return int(re.findall(r'\(kicad_pcb \(version (.+?)\)', Board)[0])

def getPCBArea(Kicad_Board):
    area = (re.findall(r'\(area (.+?)\)', Kicad_Board)[0])
    # print area
    return area

def createSolidBBox(model3D):
    selEx=model3D
    selEx = FreeCADGui.Selection.getSelectionEx()
    objs = [selobj.Object for selobj in selEx]
    if len(objs) == 1:
        s = objs[0].Shape
        name=objs[0].Label
        FreeCAD.Console.PrintMessage(name+" name \r\n")
        # boundBox
        boundBox_ = s.BoundBox
        boundBoxLX = boundBox_.XLength
        boundBoxLY = boundBox_.YLength
        boundBoxLZ = boundBox_.ZLength
        a = str(boundBox_)
        a,b = a.split('(')
        c = b.split(',')
        oripl_X = float(c[0])
        oripl_Y = float(c[1])
        oripl_Z = float(c[2])
        #say(str(boundBox_)+"\r\n")
        #say("Rectangle : "+str(boundBox_.XLength)+" x "+str(boundBox_.YLength)+" x "+str(boundBox_.ZLength)+"\r\n")
        #say("_____________________"+"\r\n")
        #say("x: "+str(oripl_X)+" y: "+str(oripl_Y)+"z: "+str(oripl_Z)+"\r\n")
        obj=FreeCAD.ActiveDocument.addObject('Part::Feature',name)
        obj.Shape=Part.makeBox(boundBox_.XLength, boundBox_.YLength, boundBox_.ZLength, FreeCAD.Vector(oripl_X,oripl_Y,oripl_Z), FreeCAD.Vector(0,0,01))
        # Part.show(cube)
        #say("cube name "+ obj.Name+'\r\n')
    else:
        FreeCAD.Console.PrintMessage("Select a single part object !"+"\r\n")
    #end bbox macro
    name=obj.Name
    #say("bbox name "+name+"\n")
    return name
    del objs
### end createSolidBBox  

def findPcbCenter(pcbName):
    pcb = FreeCAD.ActiveDocument.getObject(pcbName)
    s=pcb.Shape
    name=pcb.Label
    # boundBox
    boundBox_ = s.BoundBox
    boundBoxLX = boundBox_.XLength
    boundBoxLY = boundBox_.YLength
    boundBoxLZ = boundBox_.ZLength
    center = s.BoundBox.Center
    #say(center)
    #say("["+str(center.x)+"],["+str(center.y)+"] center of pcb\r\n")
    a = str(boundBox_)
    a,b = a.split('(')
    c = b.split(',')
    oripl_X = float(c[0])
    oripl_Y = float(c[1])
    oripl_Z = float(c[2])
    #say(str(boundBox_)+"\r\n")
    #say("Rectangle : "+str(boundBox_.XLength)+" x "+str(boundBox_.YLength)+" x "+str(boundBox_.ZLength)+"\r\n")
    #say("_____________________"+"\r\n")
    #say("x: "+str(oripl_X)+" y: "+str(oripl_Y)+"z: "+str(oripl_Z)+"\r\n")
    center_x=center.x; center_y=center.y
    bb_x=boundBox_.XLength; bb_y=boundBox_.YLength
    return center_x, center_y, bb_x, bb_y
### end findPcbCenter

def getArc_minMax(xC,xA,yC,yA,alpha):
    # x1=xA start point; x2=xC center; xB end point; alpha=angle
    global xMax, xmin, yMax, ymin
    j=0
    R=sqrt((xA-xC)**2+(yA-yC)**2)
    #say('R = '+str(R))
    if (xA>=xC) and (yA<yC):
        beta=atan(abs(xA-xC)/abs(yA-yC))
        j=1; ABeta=(alpha+beta)
        #say(str(degrees(beta))+" beta "+ str(degrees(ABeta))+" ABeta\r\n")
        #cases if (xA>xC) and (yA<yC):
        if ABeta >= beta and ABeta <= pi/2:
            xB=R*sin(alpha+beta)+xC
            xMax=max(xB,xMax)
            xmin= min(xA,xmin)
            yB=yC-R*cos(alpha+beta)
            yMax= max(yB, yMax)
            ymin= min(yA, ymin)
        if ABeta >pi/2 and ABeta <=pi:
            xMax = max(R+xC,xMax)
            xB=R*sin(alpha+beta)+xC
            xmin = min(xA, xB, xmin)
            # yB = yC+R*cos(pi-(alpha+beta))
            yB=yC-R*cos(alpha+beta)
            yMax = max(yB, yMax)
            ymin = min(yA, ymin)
        if ABeta >pi and ABeta <=3/2*pi:
            xB=R*sin(alpha+beta)+xC
            xMax=max(R+xC,xMax)
            xmin = min(xB,xmin)
            yB=yC-R*cos(alpha+beta)
            yMax = max(yC+R, yMax)
            ymin = min(yA, ymin)
        if ABeta >3/2*pi and ABeta <= 2*pi:
            xB=R*sin(alpha+beta)+xC
            xMax=max(R+xC,xMax)
            xmin = min(xC-R,xmin)
            yB=yC-R*cos(alpha+beta)
            yMax = max(yC+R, yMax)
            ymin = min(yA, yB, ymin)
        if ABeta >2*pi and ABeta <= 2*pi+beta:
            xmin = min(xC-R,xmin)
            xMax = max(R+xC,xMax)
            ymin = min(yC-R, ymin)
            yMax = max(yC+R, yMax)
    if (xA>xC) and (yA>=yC):
        beta=atan(abs(yA-yC)/abs(xA-xC))
        j=2; ABeta=(alpha+beta)
        #say(str(degrees(beta))+" beta "+ str(degrees(ABeta))+" ABeta\r\n")
        yB=yC+R*sin(ABeta)
        xB=xC+R*cos(ABeta)
        if ABeta >= beta and ABeta <= pi/2:
            xMax=max(xA,xMax)
            xmin= min(xB,xmin)
            yMax= max(yB, yMax)
            ymin= min(yA, ymin)
        if ABeta > pi/2 and ABeta <= pi:
            xmin= min(xB,xmin)
            xMax=max(xA,xMax)
            ymin= min(yA, yB, ymin)
            yMax= max(yC+R, yMax)
        if ABeta > pi and ABeta <= 3/2*pi:
            xmin= min(xC-R,xmin)
            xMax=max(xA,xMax)
            ymin= min(yB, ymin)
            yMax= max(yC+R, yMax)
        if ABeta > 3/2*pi and ABeta <= 2*pi:
            xmin= min(xC-R,xmin)
            xMax= max(xA,xB,xMax)
            ymin= min(yC-R, ymin)
            yMax= max(yC+R, yMax)
        if ABeta > 2*pi and ABeta <= beta+2*pi:
            xmin= min(xC-R,xmin)
            xMax= max(xC+R,xMax)
            ymin= min(yC-R, ymin)
            yMax= max(yC+R, yMax)
    if (xA<=xC) and (yA>yC):
        beta=atan(abs(xA-xC)/abs(yA-yC))
        j=3; ABeta=(alpha+beta)
        #say(str(degrees(beta))+" beta "+ str(degrees(ABeta))+" ABeta\r\n")
        yB=yC+R*cos(ABeta)
        xB=xC-R*sin(ABeta)
        if ABeta >= beta and ABeta <= pi/2:
            xMax= max(xA,xMax)
            xmin= min(xB,xmin)
            yMax= max(yA, yMax)
            ymin= min(yB, ymin)
        if ABeta > pi/2 and ABeta <= pi:
            xmin= min(xC-R,xmin)
            xMax= max(xA,xB,xMax)
            ymin= min(yB,ymin)
            yMax= max(yA,yMax)
        if ABeta > pi and ABeta <= 3/2*pi:
            xmin= min(xC-R,xmin)
            xMax= max(xB,xMax)
            ymin= min(yC-R, ymin)
            yMax= max(yA, yMax)
        if ABeta > 3/2*pi and ABeta <= 2*pi:
            xmin= min(xC-R,xmin)
            xMax= max(xC+R,xMax)
            ymin= min(yC-R, ymin)
            yMax= max(yA,yB, yMax)
        if ABeta > 2*pi and ABeta <= beta+2*pi:
            xmin= min(xC-R,xmin)
            xMax= max(xC+R,xMax)
            ymin= min(yC-R, ymin)
            yMax= max(yC+R, yMax)
    if (xA<xC) and (yA<=yC):
        beta=atan(abs(yA-yC)/abs(xA-xC))
        j=4; ABeta=(alpha+beta)
        #say(str(degrees(beta))+" beta "+ str(degrees(ABeta))+" ABeta\r\n")
        yB=yC-R*sin(ABeta)
        xB=xC-R*cos(ABeta)
        if ABeta >= beta and ABeta <= pi/2:
            xMax= max(xB,xMax)
            xmin= min(xA,xmin)
            yMax= max(yA, yMax)
            ymin= min(yB, ymin)
        if ABeta > pi/2 and ABeta <= pi:
            xmin= min(xA,xmin)
            xMax= max(xB,xMax)
            ymin= min(yC-R,ymin)
            yMax= max(yA,yB,yMax)
        if ABeta > pi and ABeta <= 3/2*pi:
            xmin= min(xA,xmin)
            xMax= max(xC+R,xMax)
            ymin= min(yC-R, ymin)
            yMax= max(yB, yMax)
        if ABeta > 3/2*pi and ABeta <= 2*pi:
            xmin= min(xA,xB,xmin)
            xMax= max(xC+R,xMax)
            ymin= min(yC-R,ymin)
            yMax= max(yC+R, yMax)
        if ABeta > 2*pi and ABeta <= beta+2*pi:
            xmin= min(xC-R,xmin)
            xMax= max(xC+R,xMax)
            ymin= min(yC-R, ymin)
            yMax= max(yC+R, yMax)
    #say(str(j)+" case j\r\n")
    #say('xC='+str(xC)+';yC='+str(yC)+';xA='+str(xA)+';yA='+str(yA)+'\r\n')
    #print x1,x2,y1,y2
    #calculating xmin of arc
    R=sqrt((xA-xC)**2+(yA-yC)**2)
    #say('R = '+str(R))
    #say(str(xMax)+" xMax\r\n")
    #say(str(xmin)+" xmin\r\n")
    # print xMax, xmin, yMax, ymin
    # print pcbarcs[n]
    #print (pcbarcs[n][8:].split(' ')[0])
    return 0
### end getArc_minMax

def mid_point(prev_vertex,vertex,angle):
    """mid_point(prev_vertex,vertex,angle)-> mid_vertex
       returns mid point on arc of angle between prev_vertex and vertex"""
    angle=radians(angle/2)
    basic_angle=atan2(vertex.y-prev_vertex.y,vertex.x-prev_vertex.x)-pi/2
    shift=(1-cos(angle))*hypot(vertex.y-prev_vertex.y,vertex.x-prev_vertex.x)/2/sin(angle)
    midpoint=Base.Vector((vertex.x+prev_vertex.x)/2+shift*cos(basic_angle),(vertex.y+prev_vertex.y)/2+shift*sin(basic_angle),0)
    return midpoint
###

def Per_point(prev_vertex,vertex):
    """Per_point(center,vertex)->per point

       returns opposite perimeter point of circle"""
    #basic_angle=atan2(prev_vertex.y-vertex.y,prev_vertex.x-vertex.x)
    #shift=hypot(prev_vertex.y-vertex.y,prev_vertex.x-vertex.x)
    #perpoint=Base.Vector(prev_vertex.x+shift*cos(basic_angle),prev_vertex.y+shift*sin(basic_angle),0)
    perpoint=Base.Vector(2*prev_vertex.x-vertex.x,2*prev_vertex.y-vertex.y,0)
    return perpoint
###    

#os.system("ps -C 'kicad-SteUp-tool' -o pid=|xargs kill -9")

# UI Class definitions
##if _platform == "linux" or _platform == "linux2":
##   # linux
##elif _platform == "darwin":
##   # MAC OS X
##elif _platform == "win32":
##   # Windows

#####################################
# Function infoDialog 
#####################################
def infoDialog(msg):
    #QtGui.qFreeCAD.setOverrideCursor(QtCore.Qt.WaitCursor)
    QtGui.qFreeCAD.restoreOverrideCursor()
    QtGui.qApp.restoreOverrideCursor()
    diag = QtGui.QMessageBox(QtGui.QMessageBox.Information,u"Info Message",msg )
    diag.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    diag.exec_()
    QtGui.qFreeCAD.restoreOverrideCursor()


##  getAuxAxisOrigin
def getAuxAxisOrigin():
    match = re.search(r'\(aux_axis_origin (.+?) (.+?)\)', Kicad_Board)
    return [float(match.group(1)), float(match.group(2))];


#####################################
# Main Class
#####################################
class RotateXYZGuiClass(QtGui.QWidget):
    """"""
    def closeEvent(self, e):
        msg="""<b>Do you want to quit?</b>
            <font color='white'>****************************************************************************</font><br>
            <i>Have you saved your STEP artwork?</i><br>
            """
        #confirm on exit
        QtGui.qApp.restoreOverrideCursor()
        self.setGeometry(25, 250, 500, 500)
        #self.setWindowState(QtCore.Qt.WindowMinimized)
        res=''
        if test_flag_exit==False:
            QtGui.qApp.restoreOverrideCursor()
            res = QtGui.QMessageBox.question(None,"Close",msg,QtGui.QMessageBox.Yes|QtGui.QMessageBox.No)
        if res is QtGui.QMessageBox.No:
            e.ignore()
            #self.setWindowState(QtCore.Qt.WindowActive)
        doc=FreeCAD.ActiveDocument
        if doc!= None:
            FreeCAD.setActiveDocument(doc.Name)
        #FreeCAD.ActiveDocument=FreeCAD.getDocument(doc.Label)
        #FreeCADGui.ActiveDocument=FreeCADGui.getDocument(doc.Label)
            if close_doc==True:
                FreeCAD.closeDocument(doc.Name)
            say(doc.Label+'\n')
        
    def link(self, linkStr):
        QtGui.QDesktopServices.openUrl(QtCore.QUrl(linkStr))

    def __init__(self):
        super(RotateXYZGuiClass, self).__init__()
        self.initUI()
    def initUI(self):
        self.result = userCancelled
        # set up a monospace font for the Labels to match button dimension
        global export_board_2step
        # create our window
        # define window        xLoc,yLoc,xDim,yDim
        self.setGeometry(25, 250, 500, 500)
        #self.setWindowTitle("Move, Rotate and Scale model XYZ")
        self.setWindowTitle("kicad StepUp 3D tools")
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setMouseTracking(True)
        font = QtGui.QFont()
        #font.setFamily("Courier")
        font.setStyleHint(QtGui.QFont.Monospace)
        font.setFixedPitch(True)
        font.setPointSize(font_size)
        #self.text_editor.setFont(font)
        # create Labels
        self.label4 = QtGui.QLabel("  deg", self)
        self.label4.move(20, 20)
        self.label5 = QtGui.QLabel("  deg", self)
        self.label5.move(20, 60)
        self.label6 = QtGui.QLabel("  deg", self)
        self.label6.move(20, 100)

        # text input field
        self.textInputRX = QtGui.QLineEdit(self)
        #self.textInputRX.setInputMask("999")
        self.textInputRX.setText("  90")
        self.textInputRX.setFixedWidth(50)
        self.textInputRX.move(70, 20)
        self.textInputRY = QtGui.QLineEdit(self)
        self.textInputRY.setText("  90")
        self.textInputRY.setFixedWidth(50)
        self.textInputRY.move(70, 60)
        self.textInputRZ = QtGui.QLineEdit(self)
        self.textInputRZ.setText("  90")
        self.textInputRZ.setFixedWidth(50)
        self.textInputRZ.move(70, 100)

        #conflict message
        self.label17 = QtGui.QLabel("", self)
        self.label17.move(410, 290)
        self.label17.setFixedWidth(90)
        self.label18 = QtGui.QLabel("", self)
        self.label18.move(410, 302)
        self.label18.setFixedWidth(90)
        self.label19 = QtGui.QLabel("", self)
        self.label19.move(410, 314)
        self.label19.setFixedWidth(90)

        #self.labelInfoMsg.move(280, 340)
        self.label7 = QtGui.QLabel(u"(\u00B1mm)", self)
        self.label7.move(20, 160)
        self.label8 = QtGui.QLabel(u"(\u00B1mm)", self)
        self.label8.move(20, 200)
        self.label9 = QtGui.QLabel(u"(\u00B1mm)", self)
        self.label9.move(20, 240)

        self.label30= QtGui.QLabel('mouse pos', self)
        self.label30.move(20, 360)
        self.label30.setFixedWidth(80)

        self.label10 = QtGui.QLabel("sel\'d obj position", self)
        self.label10.move(20, 290)
        self.label10.setFixedWidth(80)
        self.label11 = QtGui.QLabel(" ", self)
        self.label11.move(20, 310)
        self.label11.setFixedWidth(80)
        self.label12 = QtGui.QLabel(" ", self)
        self.label12.move(20, 330)
        self.label12.setFixedWidth(80)

        self.labelInfoMsg = QtGui.QLabel("Info Message", self)
        self.labelInfoMsg.move(280, 340)
        self.labelVerMsg = QtGui.QLabel('github/easyw ver '+___ver___, self)
        self.labelVerMsg.move(330, 135)

        #self.label6 = QtGui.QLabel("               ", self)
        #self.label6.move(135, 70)

        self.label21 = QtGui.QLabel("               ", self)
        self.label21.linkActivated.connect(self.link)
        self.label21.setText('<a href="http://sourceforge.net/projects/kicadstepup/">kicad StepUp</a>')
        self.label21.move(410,380)
        self.label20 = QtGui.QLabel("               ", self)
        self.label20.linkActivated.connect(self.link)
        self.label20.setText('<a href="https://github.com/easyw/kicad-3d-models-in-freecad/tree/master/cadquery/FCAD_script_generator">3D models</a>')
        self.label20.move(410,400)
        self.label23 = QtGui.QLabel("               ", self)
        self.label23.linkActivated.connect(self.link)
        self.label23.setText('<a href="https://github.com/easyw/kicad-3d-mcad-models">kicad MCAD<br>3D libraries</a>')
        self.label23.move(410,420)
        #
        ##
        home = expanduser("~")
        ini_file_full_path='<b>'+home+os.sep+'ksu-config.ini</b>'
        self.label24 = QtGui.QLabel(ini_file_full_path, self)
        self.label24.move(500,20)
        self.textEdit = QtGui.QTextEdit(self)
        self.textEdit.setGeometry(QtCore.QRect(500, 40, 380, 440))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setReadOnly(True)
        #self.textEdit.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)            #
        #self.textEdit.setText("TexEdit ")
        self.textEdit.setText(ini_content)
        #self.textEdit.setToolTip("ksu config ini file")
        self.textEdit.verticalScrollBar().setValue(0)                                      # verticalScrollBar Position
        self.textEdit.verticalScrollBar().setSliderPosition(0)                             # Slider Position
        #self.textEdit.horizontalScrollBar.setValue(0)
        # verticalScrollBar Position
        #self.textEdit.horizontalScrollBar().setSliderPosition(0)                             # Slider Position
        #self.textEdit.textChanged.connect(self.on_textEdit_Changed)                         #connection on_textEdit_Changed        
        ##
        
        # text input field
        self.textInputX = QtGui.QLineEdit(self)
        #self.textInput.setInputMask("+-999.")
        self.textInputX.setText(" 0.000")
        self.textInputX.setFixedWidth(50)
        self.textInputX.move(70, 160)
        self.textInputY = QtGui.QLineEdit(self)
        self.textInputY.setText(" 0.000")
        self.textInputY.setFixedWidth(50)
        self.textInputY.move(70, 200)
        self.textInputZ = QtGui.QLineEdit(self)
        self.textInputZ.setText(" 0.000")
        self.textInputZ.setFixedWidth(50)
        self.textInputZ.move(70, 240)

        # RotateX button
        RotateX = QtGui.QPushButton('Rotate X', self)
        RotateX.clicked.connect(self.onRotateX)
        RotateX.setMinimumWidth(100)
        #RotateX.setAutoDefault(False)
        RotateX.move(130, 20)
        # RotateY button
        RotateY = QtGui.QPushButton('Rotate Y', self)
        RotateY.clicked.connect(self.onRotateY)
        RotateY.setMinimumWidth(100)
        #RotateY.setAutoDefault(False)
        RotateY.move(130, 60)
        # RotateZ button
        RotateZ = QtGui.QPushButton('Rotate Z', self)
        RotateZ.clicked.connect(self.onRotateZ)
        RotateZ.setMinimumWidth(100)
        #RotateZ.setAutoDefault(False)
        RotateZ.move(130, 100)

        # text input field
        self.textInputMX = QtGui.QLineEdit(self)
        #self.textInput.setInputMask("+-999.")
        self.textInputMX.setText(" 0.000")
        self.textInputMX.setFixedWidth(50)
        self.textInputMX.move(370, 20)
        # MoveToX button
        MoveToX = QtGui.QPushButton('Move to X', self)
        MoveToX.clicked.connect(self.onMoveToX)
        MoveToX.setMinimumWidth(100)
        MoveToX.move(250, 20)
        # text input field
        self.textInputMY = QtGui.QLineEdit(self)
        #self.textInput.setInputMask("+-999.")
        self.textInputMY.setText(" 0.000")
        self.textInputMY.setFixedWidth(50)
        self.textInputMY.move(370, 60)
        # MoveToY button
        MoveToY = QtGui.QPushButton('Move to Y', self)
        MoveToY.clicked.connect(self.onMoveToY)
        MoveToY.setMinimumWidth(100)
        MoveToY.move(250, 60)
        # text input field
        self.textInputMZ = QtGui.QLineEdit(self)
        #self.textInput.setInputMask("+-999.")
        self.textInputMZ.setText(" 0.000")
        self.textInputMZ.setFixedWidth(50)
        self.textInputMZ.move(370, 100)
        # MoveToZ button
        MoveToZ = QtGui.QPushButton('Move to Z', self)
        MoveToZ.clicked.connect(self.onMoveToZ)
        MoveToZ.setMinimumWidth(100)
        MoveToZ.move(250, 100)
        ###
        # Cfg button
        CfgB = QtGui.QPushButton('Config', self)
        CfgB.clicked.connect(self.onCfg)
        CfgB.setFixedWidth(50)
        CfgB.move(430, 20)
        # Hide button
        HideB = QtGui.QPushButton('<<<', self)
        HideB.clicked.connect(self.onHide)
        HideB.setFixedWidth(50)
        HideB.move(430, 60)
        ###
        # Help button
        HelpB = QtGui.QPushButton('Help', self)
        HelpB.clicked.connect(self.onHelp)
        HelpB.setFixedWidth(50)
        HelpB.move(430, 100)
        ###        # TranslateX button
        TranslateX = QtGui.QPushButton('Translate X', self)
        TranslateX.clicked.connect(self.onTranslateX)
        TranslateX.setMinimumWidth(100)
        TranslateX.move(130, 160)
        # TranslateY button
        TranslateY = QtGui.QPushButton('Translate Y', self)
        TranslateY.clicked.connect(self.onTranslateY)
        TranslateY.setMinimumWidth(100)
        TranslateY.move(130, 200)
        # TranslateZ button
        TranslateZ = QtGui.QPushButton('Translate Z', self)
        TranslateZ.clicked.connect(self.onTranslateZ)
        TranslateZ.setMinimumWidth(100)
        TranslateZ.move(130, 240)

        # Scale Obj button
        ScaleVRML = QtGui.QPushButton("Export to kicad: STEP\r\n&& scaled VRML 1/2.54", self)
        ScaleVRML.clicked.connect(self.onScaleVRML)
        ScaleVRML.setMinimumWidth(150)
        ScaleVRML.setMinimumHeight(40)
        ScaleVRML.move(250, 340)

        # Load Footprint button
        LoadFootprint = QtGui.QPushButton('Load kicad\r\nFootprint module', self)
        LoadFootprint.clicked.connect(self.onLoadFootprint_click)
        LoadFootprint.setMinimumWidth(150)
        LoadFootprint.setMinimumHeight(40)
        LoadFootprint.move(250, 390)

        # Reset Placement button
        ResetPlacement = QtGui.QPushButton('reset Placement\r\nproperties', self)
        ResetPlacement.clicked.connect(self.onResetPlacement)
        ResetPlacement.setMinimumWidth(100)
        ResetPlacement.setMinimumHeight(40)
        ResetPlacement.move(130, 340)

        # Conflicts button
        checkCollisions = QtGui.QPushButton('check Collisions\r\ntolerance '+str(conflict_tolerance), self)
        checkCollisions.clicked.connect(self.onCollisions)
        checkCollisions.setMinimumWidth(150)
        checkCollisions.setMinimumHeight(40)
        checkCollisions.move(250, 290)

        # GetPosition button
        GetPos = QtGui.QPushButton('get\r\nPosition', self)
        GetPos.clicked.connect(self.onGetPosition)
        #GetPos.setMinimumWidth(100)
        GetPos.setFixedWidth(100)
        GetPos.move(130, 290)

        # CenterX button
        CenterX = QtGui.QPushButton('Center X', self)
        CenterX.clicked.connect(self.onCenterX)
        CenterX.setMinimumWidth(100)
        CenterX.move(250, 160)
        # CenterY button
        CenterY = QtGui.QPushButton('Center Y', self)
        CenterY.clicked.connect(self.onCenterY)
        CenterY.setMinimumWidth(100)
        CenterY.move(250, 200)
        # CenterZ button
        CenterZ = QtGui.QPushButton('Center Z', self)
        CenterZ.clicked.connect(self.onCenterZ)
        CenterZ.setMinimumWidth(100)
        CenterZ.move(250, 240)

        # PutOnX button
        PutOnX = QtGui.QPushButton('PutOn X', self)
        PutOnX.clicked.connect(self.onPutOnX)
        PutOnX.setMinimumWidth(100)
        PutOnX.move(370, 160)
        # PutOnY button
        PutOnY = QtGui.QPushButton('PutOn Y', self)
        PutOnY.clicked.connect(self.onPutOnY)
        PutOnY.setMinimumWidth(100)
        PutOnY.move(370, 200)
        # PutOnZ button
        PutOnZ = QtGui.QPushButton('PutOn Z', self)
        PutOnZ.clicked.connect(self.onPutOnZ)
        PutOnZ.setMinimumWidth(100)
        PutOnZ.move(370, 240)

        # Create axis button
        CreateAxis = QtGui.QPushButton('CreateAxis', self)
        CreateAxis.clicked.connect(self.onCreateAxis)
        #CreateAxis.setMinimumWidth(100)
        CreateAxis.setFixedWidth(80)
        CreateAxis.move(20, 400)

        # section checkBox reset position
        self.checkBox_1 = QtGui.QCheckBox('reset pos on\r\nall actions', self)                                    # create object QRadioButton in groupBox
        #self.checkBox_1.setGeometry(QtCore.QRect(20, 120, 30, 60))
        # coordinates position
        self.checkBox_1.setGeometry(QtCore.QRect(140, 380, 140, 60))

        self.checkBox_1.setObjectName(('reset pos on all actions')) # name of object
        #self.checkBox_1.setChecked(False)  # Check by default True or False
        self.checkBox_1.setChecked(True)  # Check by default True or False
        self.checkBox_1.clicked.connect(self.on_checkBox_1_clicked)  # connect on def "on_checkBox_1_clicked"

        # section checkBox export step
        self.checkBox_2 = QtGui.QCheckBox('exp2\nstep', self)                                    # create object QRadioButton in groupBox
        self.checkBox_2.setGeometry(QtCore.QRect(165, 425, 165, 60))
        self.checkBox_2.setObjectName(('export all to step')) # name of object
        if export_board_2step==False:
            #export_board_2step=False
            self.checkBox_2.setChecked(False)  # Check by default True or False
        else:
            self.checkBox_2.setChecked(True)  # Check by default True or False
        #export_board_2step=True
        self.checkBox_2.clicked.connect(self.on_checkBox_2_clicked)  # connect on def "on_checkBox_1_clicked"
        self.checkBox_2.setToolTip("enable exporting board to STEP")
        
        # section checkBox virtual
        self.checkBox_3 = QtGui.QCheckBox('virtual', self)   
        self.checkBox_3.setGeometry(QtCore.QRect(410, 440, 410, 60))
        self.checkBox_3.setObjectName(('virtual objs')) # name of object
        if addVirtual==0:
            #export_board_2step=False
            self.checkBox_3.setChecked(False)  # Check by default True or False
        else:
            self.checkBox_3.setChecked(True)  # Check by default True or False
        ##export_board_2step=True
        self.checkBox_3.clicked.connect(self.on_checkBox_3_clicked)  # connect on def "on_checkBox_1_clicked"
        self.checkBox_3.setToolTip("enable virtual 3D models")
        
        # section checkBox materials
        self.checkBox_4 = QtGui.QCheckBox('wrl mat', self)   
        self.checkBox_4.setGeometry(QtCore.QRect(410, 330, 410, 60))
        self.checkBox_4.setObjectName(('material props')) # name of object
        if enable_materials==0:
            #export_board_2step=False
            self.checkBox_4.setChecked(False)  # Check by default True or False
        else:
            self.checkBox_4.setChecked(True)  # Check by default True or False
        # if enable_materials:
        #     self.checkBox_4.setChecked(True)  # Check by default True or False
        self.checkBox_4.clicked.connect(self.on_checkBox_4_clicked)  # connect on def "on_checkBox_1_clicked"
        self.checkBox_4.setToolTip("enable VRML material properties")
        
        # Load Kicad Board button
        LoadBoard = QtGui.QPushButton('Load kicad\nBoard *.kicad_pcb', self)
        LoadBoard.clicked.connect(self.onLoadBoard_click)
        LoadBoard.setMinimumWidth(180)
        LoadBoard.setMinimumHeight(40)
        LoadBoard.move(220, 440)
        
        # Load IDF Board button
        LoadBoardIdf = QtGui.QPushButton('Load kicad Board\nwith IDF *.emn', self)
        LoadBoardIdf.clicked.connect(self.onLoadBoard_idf_click)
        LoadBoardIdf.setMinimumWidth(140)
        LoadBoardIdf.setMinimumHeight(40)
        LoadBoardIdf.move(20, 440)
        
        default_value='/'
        module_3D_dir=os.getenv('KISYS3DMOD', default_value)
        module_3D_dir=module_3D_dir+'/'
        label_3d=module_3D_dir

        # cancel button
        ## cancelButton = QtGui.QPushButton('Cancel', self)
        ## cancelButton.clicked.connect(self.onCancel)
        ## cancelButton.setAutoDefault(True)
        ## cancelButton.move(150, 110)
        ## # OK button
        ## okButton = QtGui.QPushButton('OK', self)
        ## okButton.clicked.connect(self.onOk)
        ## okButton.move(260, 110)

        ##arranging font dimension
        self.label4.setFont(font)
        self.label5.setFont(font)
        self.label6.setFont(font)
        self.label7.setFont(font)
        self.label8.setFont(font)
        self.label9.setFont(font)
        self.label10.setFont(font)
        self.label11.setFont(font)
        self.label12.setFont(font)
        self.label17.setFont(font)
        self.label18.setFont(font)
        self.label19.setFont(font)
        self.label20.setFont(font)
        self.label21.setFont(font)
        self.label23.setFont(font)
        self.label24.setFont(font)
        self.label30.setFont(font)
        self.textInputX.setFont(font)
        self.textInputY.setFont(font)
        self.textInputRZ.setFont(font)
        self.textInputRX.setFont(font)
        self.textInputRY.setFont(font)
        self.textInputZ.setFont(font)
        RotateX.setFont(font)
        RotateY.setFont(font)
        RotateZ.setFont(font)
        self.textInputMX.setFont(font)
        self.textInputMY.setFont(font)
        self.textInputMZ.setFont(font)
        MoveToX.setFont(font)
        MoveToY.setFont(font)
        MoveToZ.setFont(font)
        TranslateX.setFont(font)
        TranslateY.setFont(font)
        TranslateZ.setFont(font)
        ScaleVRML.setFont(font)
        LoadFootprint.setFont(font)
        LoadBoard.setFont(font)
        LoadBoardIdf.setFont(font)
        CfgB.setFont(font)
        HideB.setFont(font)
        HelpB.setFont(font)
        ResetPlacement.setFont(font)
        GetPos.setFont(font)
        CenterX.setFont(font)
        CenterY.setFont(font)
        CenterZ.setFont(font)
        PutOnX.setFont(font)
        PutOnY.setFont(font)
        PutOnZ.setFont(font)
        CreateAxis.setFont(font)
        self.checkBox_1.setFont(font)
        self.checkBox_2.setFont(font)
        self.checkBox_3.setFont(font)
        self.checkBox_4.setFont(font)
        self.labelVerMsg.setFont(font)
        checkCollisions.setFont(font)
        self.textEdit.setFont(font)
        
        # now make the window visible
        self.show()
        #

    def on_checkBox_1_clicked(self):
        global resetP
        say("reset position clicked"+"\r\n")
        if self.checkBox_1.isChecked():
            resetP=True
        else:
            resetP=False

    def on_checkBox_2_clicked(self):
        global export_board_2step
        if self.checkBox_2.isChecked():
            export_board_2step=True
            cfgParsWrite(configFilePath)
        else:
            export_board_2step=False
            cfgParsWrite(configFilePath)
        say("export to STEP "+str(export_board_2step)+"\r\n")

    def on_checkBox_3_clicked(self):
        global addVirtual
        if self.checkBox_3.isChecked():
            addVirtual=1
            cfgParsWrite(configFilePath)
        else:
            addVirtual=0
            cfgParsWrite(configFilePath)
        say("virtual ="+str(addVirtual)+"\r\n")

    def on_checkBox_4_clicked(self):
        global enable_materials
        if self.checkBox_4.isChecked():
            enable_materials=1
            cfgParsWrite(configFilePath)
        else:
            enable_materials=0
            cfgParsWrite(configFilePath)
        say("materials ="+str(enable_materials)+"\r\n")

    def onRotateX(self):
        FreeCAD.Console.PrintMessage("RotateX!"+"\r\n")
        alpha=self.textInputRX.text()
        alpha=alpha.replace(',', '.')
        angle=alpha.split('.')
        self.textInputRX.setText(angle[0])
        routineR_XYZ('x',angle[0])
        position=get_position()
        self.label10.setText("X:"+str(position[0]))
        self.label11.setText("Y:"+str(position[1]))
        self.label12.setText("Z:"+str(position[2]))
    def onRotateY(self):
        FreeCAD.Console.PrintMessage("RotateY!"+"\r\n")
        alpha=self.textInputRY.text()
        alpha=alpha.replace(',', '.')
        angle=alpha.split('.')
        self.textInputRY.setText(angle[0])
        routineR_XYZ('y',angle[0])
        position=get_position()
        self.label10.setText("X:"+str(position[0]))
        self.label11.setText("Y:"+str(position[1]))
        self.label12.setText("Z:"+str(position[2]))
    def onRotateZ(self):
        FreeCAD.Console.PrintMessage("RotateZ!"+"\r\n")
        alpha=self.textInputRZ.text()
        alpha=alpha.replace(',', '.')
        angle=alpha.split('.')
        self.textInputRZ.setText(angle[0])
        routineR_XYZ('z',angle[0])
        position=get_position()
        self.label10.setText("X:"+str(position[0]))
        self.label11.setText("Y:"+str(position[1]))
        self.label12.setText("Z:"+str(position[2]))
    def onTranslateX(self):
        v=self.textInputX.text()
        v=v.replace(',', '.')
        FreeCAD.Console.PrintMessage(v+"\r\n")
        routineT_XYZ('x',v)
        position=get_position()
        self.label10.setText("X:"+str(position[0]))
        self.label11.setText("Y:"+str(position[1]))
        self.label12.setText("Z:"+str(position[2]))
    def onTranslateY(self):
        v=self.textInputY.text()
        v=v.replace(',', '.')
        FreeCAD.Console.PrintMessage(v+"\r\n")
        routineT_XYZ('y',v)
        position=get_position()
        self.label10.setText("X:"+str(position[0]))
        self.label11.setText("Y:"+str(position[1]))
        self.label12.setText("Z:"+str(position[2]))
    def onTranslateZ(self):
        v=self.textInputZ.text()
        v=v.replace(',', '.')
        FreeCAD.Console.PrintMessage(v+"\r\n")
        routineT_XYZ('z',v)
        position=get_position()
        self.label10.setText("X:"+str(position[0]))
        self.label11.setText("Y:"+str(position[1]))
        self.label12.setText("Z:"+str(position[2]))
    def onMoveToX(self):
        v=self.textInputMX.text()
        v=v.replace(',', '.')
        FreeCAD.Console.PrintMessage(v+"\r\n")
        routineM_XYZ('x',v)
        position=get_position()
        self.label10.setText("X:"+str(position[0]))
        self.label11.setText("Y:"+str(position[1]))
        self.label12.setText("Z:"+str(position[2]))
    def onMoveToY(self):
        v=self.textInputMY.text()
        v=v.replace(',', '.')
        FreeCAD.Console.PrintMessage(v+"\r\n")
        routineM_XYZ('y',v)
        position=get_position()
        self.label10.setText("X:"+str(position[0]))
        self.label11.setText("Y:"+str(position[1]))
        self.label12.setText("Z:"+str(position[2]))
    def onMoveToZ(self):
        v=self.textInputMZ.text()
        v=v.replace(',', '.')
        FreeCAD.Console.PrintMessage(v+"\r\n")
        routineM_XYZ('z',v)
        position=get_position()
        self.label10.setText("X:"+str(position[0]))
        self.label11.setText("Y:"+str(position[1]))
        self.label12.setText("Z:"+str(position[2]))
    def onCfg(self):
        #QtGui.QMessageBox.information(None,"info ...","your home path is \r\n"+ home+"\r\n")
        say("your home path is "+ expanduser("~")+"\r\n")
        self.setGeometry(25, 250, 900, 500)
        ini_content=read_ini_file()
        self.textEdit.setText(ini_content)
        cfgParsRead(configFilePath)
        
    def onHide(self):
        self.setGeometry(25, 250, 500, 500)
        global configFilePath, ini_content
        ini_content=read_ini_file()
        self.textEdit.setText(ini_content)
        #configParser.read(configFilePath)
        cfgParsRead(configFilePath)
        #global ui
        #Dialog = QtGui.QDialog()
        #ui = Ui_Dialog()
        #ui.setupUi(Dialog)
        #ui.comboBox.addItems(material_properties_names)
        #reply=Dialog.exec_()

        #bklist = configParser.get('Blacklist', 'bklist')
        #say(configFilePath+'\n')
        #say(bklist+'\n')
        
    def onHelp(self):
        self.setGeometry(25, 250, 900, 500)
        sayw("kicad StepUp version "+str(___ver___))
        help_txt="""<font color=GoldenRod><b>kicad StepUp version """+___ver___+"""</font></b><br>"""
        help_txt+="""<b>Kicad StepUp</b> is a tool set to easily export your kicad pcb EDA (board and 3D parts) to STEP model.<br>"""
        help_txt+="The artwork can be used for MCAD interchange and collaboration, and for enclosure design.<br>"
        help_txt+="The 3D visualization of components on board assemblies in kicad 3dviewer, will be the same in your mechanical software, "
        help_txt+="because of the STEP interchange format.<br>"
        help_txt+="<br><b>First of all:</b> configure your path to 3D models in <br><i><b>ksu-config.ini</b></i> file<br>"
        help_txt+="useful buttons:<br><b>Load kicad Board</b> -> will load directly board and parts in FreeCAD<br>"
        help_txt+="<b>Load kicad Footprint module</b> -> will load directly kicad footprint in FreeCAD to easily align the 3D model to footprint<br>"
        help_txt+="<b>Export to kicad STEP & scaled VRML</b> -> will convert MCAD model to STEP and VRML to be used by Kicad and kicad StepUp<br>"
        help_txt+="<b>   -> VRML can be multipart; STEP must be single part</b><br>"
        help_txt+="<i>assign material to selected colors and your VRML 3D models will have nice shiny effects</i><br>"
        help_txt+="<b>Load kicad Board with IDF</b> -> will load kicad board and parts in FreeCAD coming from IDF exported board from kicad<br>"
        help_txt+="for a more detailed help have a look at <br><b>kicadStepUp-starter-Guide.pdf</b><br><br>"
        help_txt+="Designing in kicad native 3d-viewer will produce a fully aligned STEP MCAD version "
        help_txt+="with the same view of kicad 3d render.<br>"
        help_txt+="Moreover, KiCad StepUp tool set will let you to load the kicad footprint inside FreeCAD and align the 3D part with a visual real time feedback "
        help_txt+="of the 3d model and footprint reciprocal position.<br>"
        help_txt+="With this tool is possible to download a part from on-line libraries, align the model to kicad footprint "
        help_txt+="and export the model to wrl, for immediate 3d-viewer alignment in pcbnew.<br>"
        help_txt+="Now the two words are connected for a better collaboration; just <b>design in kicad EDA</b> and transfer "
        help_txt+="the artwork to <b>MCAD (FreeCAD)</b> smoothly.<br>"
        help_txt+="<b>The workflow is very simple</b> and maintains the usual way to work with kicad:<br>"
        help_txt+="Add models to your library creating 3D models in FreeCAD, or getting models from online libs "
        help_txt+="or from the parametric 3D lib expressly done to kicad <u>https://github.com/easyw/kicad-3d-mcad-models</u><br>"
        help_txt+="Once you have your 3D MCAD model, you need to have a copy of that in STEP and VRML format. "
        help_txt+="This is possible just exporting the model with FreeCAD then just put your model in the same folder in which "
        help_txt+="normally you are used to put vrml models, and the script will assembly the MCAD board and models as in 3d-viewer of kicad."       
        help_txt+="<br><b>NB<br>STEP model has to be fused in single object<br>(union of objects)</b>"
        help_txt+="<hr><b>enable 'Report view' Panel to see helping messages</b>"
        self.textEdit.setText(help_txt)
        #say('onHelp')
        #reply = QtGui.QMessageBox.question(None, "", "step file exists, overwrite?",QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
    def onGetPosition(self):
        FreeCAD.Console.PrintMessage("GetPosition!"+"\r\n")
        position=get_position()
        self.label10.setText("X:"+str(position[0]))
        self.label11.setText("Y:"+str(position[1]))
        self.label12.setText("Z:"+str(position[2]))

    def onCenterX(self):
        FreeCAD.Console.PrintMessage("centering\r\n")
        routineC_XYZ('x')
        position=get_position()
        self.label10.setText("X:"+str(position[0]))
        self.label11.setText("Y:"+str(position[1]))
        self.label12.setText("Z:"+str(position[2]))
    def onCenterY(self):
        FreeCAD.Console.PrintMessage("centering\r\n")
        routineC_XYZ('y')
        position=get_position()
        self.label10.setText("X:"+str(position[0]))
        self.label11.setText("Y:"+str(position[1]))
        self.label12.setText("Z:"+str(position[2]))
    def onCenterZ(self):
        FreeCAD.Console.PrintMessage("centering\r\n")
        routineC_XYZ('z')
        position=get_position()
        self.label10.setText("X:"+str(position[0]))
        self.label11.setText("Y:"+str(position[1]))
        self.label12.setText("Z:"+str(position[2]))
    def onPutOnX(self):
        FreeCAD.Console.PrintMessage("putting on Plane X\r\n")
        routineP_XYZ('x')
        position=get_position()
        self.label10.setText("X:"+str(position[0]))
        self.label11.setText("Y:"+str(position[1]))
        self.label12.setText("Z:"+str(position[2]))
    def onPutOnY(self):
        FreeCAD.Console.PrintMessage("putting on Plane Y\r\n")
        routineP_XYZ('y')
        position=get_position()
        self.label10.setText("X:"+str(position[0]))
        self.label11.setText("Y:"+str(position[1]))
        self.label12.setText("Z:"+str(position[2]))
    def onPutOnZ(self):
        FreeCAD.Console.PrintMessage("putting on Plane Z\r\n")
        routineP_XYZ('z')
        position=get_position()
        self.label10.setText("X:"+str(position[0]))
        self.label11.setText("Y:"+str(position[1]))
        self.label12.setText("Z:"+str(position[2]))
    # def onCancel(self):
    #     self.result = userCancelled
    #     self.close()
    # def onOk(self):
    #     self.result = userOK
    #     self.close()
    def onScaleVRML(self):
        global applymaterials, exportS
        FreeCAD.Console.PrintMessage("ScaleToVRML!"+"\r\n")
        applymaterials=0
        if self.checkBox_4.isChecked():
            applymaterials=1
        self.setGeometry(25, 250, 500, 500)
        result=routineScaleVRML()
        position=get_position()
        if exportS:
            try:
                self.label10.setText("X:"+str(position[0]))
                self.label11.setText("Y:"+str(position[1]))
                self.label12.setText("Z:"+str(position[2]))
            except:
                pass
        if result==-1:
            msg="************\r\nSelect an object\r\n************"
            self.labelInfoMsg.setText(msg)

    def onResetPlacement(self):
        #FreeCAD.Console.PrintMessage("reset Placement proprierties!"+"\r\n")
        routineResetPlacement()
        position=get_position()
        self.label10.setText("X:"+str(position[0]))
        self.label11.setText("Y:"+str(position[1]))
        self.label12.setText("Z:"+str(position[2]))

    def onCollisions(self):
        self.setGeometry(25, 250, 500, 500)
        collisions=routineCollisions()
        if collisions==0:
            self.label17.setText("No")
            self.label18.setText("collisions")
            self.label19.setText("found!")
        elif collisions==1:
            self.label17.setText("<b><font color=red>Collisions</b>")
            self.label18.setText("<b>detected!</b>")
            self.label19.setText("<b>!!!</b>")
        else:
            self.label17.setText(" ")
            self.label18.setText(" ")
            self.label19.setText(" ")
###
    def onSelFolder(self):
        default_value='/'
        module_3D_dir=os.getenv('KISYS3DMOD', default_value)
        module_3D_dir=module_3D_dir+'/'
        ## getting 3D models path
        # print 'KISYS3DMOD='
        #FreeCAD.Console.PrintMessage('KISYS3DMOD='+os.getenv('KISYS3DMOD', default_value)+' '+module_3D_dir+' \r\n')
        if not os.path.isdir(module_3D_dir):
            module_3D_dir="/"
        # Save folder select
        dialog = QtGui.QFileDialog.getExistingDirectory(self,"Open 3D prefix folder",
                                                            module_3D_dir, QtGui.QFileDialog.ShowDirsOnly)
        destiny_folder = str(dialog) 
        destiny_folder=destiny_folder.replace('\\','/')
        test1="C:/Cad/Progetti_K"
        self.label_3d_prefix.setText(destiny_folder[:25])
        FreeCAD.Console.PrintMessage(destiny_folder+ '\r\n')

    def onLoadBoard_idf_click(self):
        self.setGeometry(25, 250, 500, 500)
        sayw("kicad StepUp version "+str(___ver___))
        ini_content=read_ini_file()
        self.textEdit.setText(ini_content)
        cfgParsRead(configFilePath)
        onLoadBoard_idf()
    ###    

###
    def onLoadBoard_click(self):
        self.setGeometry(25, 250, 500, 500)
        sayw("kicad StepUp version "+str(___ver___))
        ini_content=read_ini_file()
        self.textEdit.setText(ini_content)
        cfgParsRead(configFilePath)
        onLoadBoard()
    ###    
###
    def onLoadFootprint_click(self):
        self.setGeometry(25, 250, 500, 500)
        sayw("kicad StepUp version "+str(___ver___))
        onLoadFootprint()
###

    def mouseMoveEvent(self,event):
        self.labelInfoMsg.setText('')
        if show_mouse_pos:
            self.label30.setText("X: "+str(event.x()) + " Y: "+str(event.y()))

    def onCreateAxis(self):
        FreeCAD.Console.PrintMessage("Create Axis!"+"\r\n")
        if FreeCAD.ActiveDocument.getObject("axis")== None:
            create_axis()
        ## self.label10.setText("X:"+str(get_position()[0])+"Pl:"+str(get_position()[3]))
        ## self.label11.setText("Y:"+str(get_position()[1])+"Pl:"+str(get_position()[4]))
        ## self.label12.setText("Z:"+str(get_position()[2])+"Pl:"+str(get_position()[5]))

# Class definitions

# Function definitions
def onLoadFootprint(file_name=None):
    #name=QtGui.QFileDialog.getOpenFileName(this,tr("Open Image"), "/home/jana", tr("Image Files (*.png *.jpg *.bmp)"))[0]
    #global module_3D_dir
    global last_fp_path, test_flag
    global configParser, configFilePath, start_time
    #self.setGeometry(25, 250, 500, 500)
    clear_console()
    default_value='/'
    module_3D_dir=os.getenv('KISYS3DMOD', default_value)
    module_3D_dir=module_3D_dir+'/../'
    ## getting 3D models path
    # print 'KISYS3DMOD='
    say('KISYS3DMOD='+os.getenv('KISYS3DMOD', default_value)+'\n'+module_3D_dir+'\n')
    if not os.path.isdir(module_3D_dir):
        module_3D_dir="/"
    if last_fp_path=='':
        last_fp_path=module_3D_dir
    if file_name!=None:
        #export_board_2step=True #for cmd line force exporting to STEP
        name=file_name
    elif test_flag==False:
    #if test_flag==False:
        Filter=""
        ##if _platform == "darwin":
        ##    ##workaround for OSX not opening native fileopen
        ##    name=QtGui.QFileDialog.getOpenFileName(self, 'Open file',
        ##         last_file_path,"kicad module files (*.kicad_mod)",
        ##         options=QtGui.QFileDialog.DontUseNativeDialog )[0]
        ##else:
        ##    name=QtGui.QFileDialog.getOpenFileName(self, "Open File...", last_file_path,
        ##        "kicad module files (*.kicad_mod)")[0]
        #path = FreeCAD.ConfigGet("AppHomePath")
        #path = FreeCAD.ConfigGet("UserAppData")
        #path=last_file_path
        #try:
        #    name, Filter = PySide.QtGui.QFileDialog.getOpenFileName(None, "Open File", last_file_path, "*.kicad_mod")#PySide
        #except Exception:
        #    FreeCAD.Console.PrintError("Error : " + str(name) + "\n")
        name, Filter = PySide.QtGui.QFileDialog.getOpenFileName(None, "Open File...",
             last_fp_path, "*.kicad_mod")
    else:
        name="C:/Cad/Progetti_K/ksu-test/test.kicad_mod"
    if len(name) > 0:
        txtFile = __builtin__.open(name,"r")
        content = txtFile.readlines()
        content.append(" ")
        last_fp_path=os.path.dirname(txtFile.name)
        txtFile.close()
        configParser.set('last_footprint_path', 'last_fp_path', last_fp_path)
        #configParser.set('last_fp_path', ';; last footprint file path used')
        configParser.set('info', default_ksu_msg[0])
        configParser.set('prefix3D', default_ksu_msg[1])
        configParser.set('PcbColor', default_ksu_msg[2])
        configParser.set('Blacklist', default_ksu_msg[3])
        configParser.set('BoundingBox', default_ksu_msg[4])
        configParser.set('Placement', default_ksu_msg[5])
        configParser.set('Virtual', default_ksu_msg[6])
        configParser.set('ExportFuse', default_ksu_msg[7])
        configParser.set('minimum_drill_size', default_ksu_msg[8])
        configParser.set('last_pcb_path', default_ksu_msg[9])
        configParser.set('last_footprint_path', default_ksu_msg[10])
        configParser.set('export', default_ksu_msg[11])
        # save to the config file
        with __builtin__.open(configFilePath, 'wb') as configfile:
            configParser.write(configfile)
        #configFilePath.close() already closed
        data=''.join(content)
        content=re.sub(r'[^\x00-\x7F]+',' ', data)  #workaround to remove utf8 extra chars
        ## content=data
        #FreeCAD.Console.PrintMessage(content)
        #FreeCAD.Console.PrintMessage(data)
        routineDrawFootPrint(content,name)
        #txtFile.close()
###
def onLoadBoard_idf(file_name=None):
    #name=QtGui.QFileDialog.getOpenFileName(this,tr("Open Image"), "/home/jana", tr("Image Files (*.png *.jpg *.bmp)"))[0]
    #global module_3D_dir
    global models3D_prefix, blacklisted_model_elements, col, colr, colg, colb
    global bbox, volume_minimum, height_minimum, idf_to_origin, aux_orig
    global base_orig, base_point, bbox_all, bbox_list, whitelisted_model_elements
    global fusion, addVirtual, blacklisted_models, exportFusing, min_drill_size
    global last_fp_path, last_pcb_path, plcmnt, xp, yp, exportFusing
    global last_pcb_path, test_flag, configParser, configFilePath, start_time
    global aux_orig, base_orig, base_point, idf_to_origin, off_x, off_y, export_board_2step
    global real_board_pos_x, real_board_pos_y, board_base_point_x, board_base_point_y
    #self.setGeometry(25, 250, 500, 500)
    clear_console()
    default_value='/'
    module_3D_dir=os.getenv('KISYS3DMOD', default_value)
    module_3D_dir=module_3D_dir+'/../'
    ## getting 3D models path
    # print 'KISYS3DMOD='
    say('KISYS3DMOD='+os.getenv('KISYS3DMOD', default_value)+'\n'+module_3D_dir+'\n')
    if not os.path.isdir(module_3D_dir):
        module_3D_dir="/"
    if not os.path.isdir(last_pcb_path):
        last_pcb_path="./"
    if file_name!=None:
        #export_board_2step=True #for cmd line force exporting to STEP
        name=file_name
    elif test_flag==False:
        Filter=""
        ##if _platform == "darwin":
        ##    ##workaround for OSX not opening native fileopen
        ##    name=QtGui.QFileDialog.getOpenFileName(self, 'Open file',
        ##         last_file_path,"kicad module files (*.kicad_mod)",
        ##         options=QtGui.QFileDialog.DontUseNativeDialog )[0]
        ##else:
        ##    name=QtGui.QFileDialog.getOpenFileName(self, "Open File...", last_file_path,
        ##        "kicad module files (*.kicad_mod)")[0]
        #path = FreeCAD.ConfigGet("AppHomePath")
        #path = FreeCAD.ConfigGet("UserAppData")
        #path=last_file_path
        #try:
        #    name, Filter = PySide.QtGui.QFileDialog.getOpenFileName(None, "Open File", last_file_path, "*.kicad_mod")#PySide
        #except Exception:
        #    FreeCAD.Console.PrintError("Error : " + str(name) + "\n")
        
        #minimize main window
        ## self.setWindowState(QtCore.Qt.WindowMinimized)
        ## infoDialog('ciao')
        ## reply = QtGui.QInputDialog.getText(None, "Hello","Enter your thoughts for the day:")
        ## if reply[1]:
        ##         # user clicked OK
        ##         replyText = reply[0]
        ## else:
        ##         # user clicked Cancel
        ##         replyText = reply[0] # which will be "" if they clicked Cancel
        ## #restore main window
        ## self.setWindowState(QtCore.Qt.WindowActive)
        name, Filter = PySide.QtGui.QFileDialog.getOpenFileName(None, "Open IDF File...",
             last_pcb_path, "*.emn")
    else:
        name="C:/Cad/Progetti_K/ksu-test/test.emn"
        FreeCAD.Console.PrintMessage('opening '+name+'\n')
    if len(name) > 0:
        if os.path.isfile(name):
            say('opening '+name+'\n')
            path, fname = os.path.split(name)
            fname=os.path.splitext(fname)[0]
            #fpth = os.path.dirname(os.path.abspath(__file__))
            fpth = os.path.dirname(os.path.abspath(name))
            #filePath = os.path.split(os.path.realpath(__file__))[0]
            say ('my file path '+fpth+'\n')
            if fpth == "":
                fpth = "."
            last_pcb_path = fpth
            #last_pcb_path=path
            # update existing value
            #say(default_ksu_msg)
            configParser.set('last_pcb_path', 'last_pcb_path', path)
            #configParser.set('last_pcb_path', ';; last pcb board path')
            configParser.set('info', default_ksu_msg[0])
            configParser.set('prefix3D', default_ksu_msg[1])
            configParser.set('PcbColor', default_ksu_msg[2])
            configParser.set('Blacklist', default_ksu_msg[3])
            configParser.set('BoundingBox', default_ksu_msg[4])
            configParser.set('Placement', default_ksu_msg[5])
            configParser.set('Virtual', default_ksu_msg[6])
            configParser.set('ExportFuse', default_ksu_msg[7])
            configParser.set('minimum_drill_size', default_ksu_msg[8])
            configParser.set('last_pcb_path', default_ksu_msg[9])
            configParser.set('last_footprint_path', default_ksu_msg[10])
            configParser.set('export', default_ksu_msg[11])
            # save to the config file
            with __builtin__.open(configFilePath, 'wb') as configfile:
                configParser.write(configfile)
            #configFilePath.close() already closed
            doc=FreeCAD.newDocument(fname)
            #last_file_path=os.path.dirname(fname)
            start_time=current_milli_time()
            routineDrawIDF(doc,name)
        else:
            say(name+' missing\r')
            stop
        ##Placing board at configured position
        # pos objs x,-y
        # pos board xm+(xM-xm)/2
        # pos board -(ym+(yM-ym)/2)        
        center_x, center_y, bb_x, bb_y = findPcbCenter("Pcb")
        ## using PcbCenter
        xMax=center_x+bb_x/2
        xmin=center_x-bb_x/2
        yMax=center_y+bb_y/2
        ymin=center_y-bb_y/2
        off_x=0; off_y=0  #offset of the board & modules
        if (aux_orig==1):
            xp=getAuxAxisOrigin()[0]; yp=-getAuxAxisOrigin()[1]  #offset of the board & modules
            ##off_x=-xp+xmin+(xMax-xmin)/2; off_y=-yp-(ymin+(yMax-ymin)/2)  #offset of the board & modules
            off_x=-xp+center_x;off_y=-yp+center_y
        if (base_orig==1):
            ##off_x=xmin+(xMax-xmin)/2; off_y=-(ymin+(yMax-ymin)/2)  #offset of the board & modules
            off_x=center_x;off_y=center_y
        if (base_point==1):
            ##off_x=-xp+xmin+(xMax-xmin)/2; off_y=-yp-(ymin+(yMax-ymin)/2)  #offset of the board & modules
            #off_x=-xp+center_x;off_y=-yp+center_y
            off_x=-xp+center_x;off_y=-yp+center_y
        ## test maui board_base_point_x=(xMax-xmin)/2-off_x
        ## test maui board_base_point_y=-((yMax-ymin)/2)-off_y
        #real_board_pos_x=xmin+(xMax-xmin)/2
        #real_board_pos_y=-(ymin+(yMax-ymin)/2)
        ## using PcbCenter
        real_board_pos_x=center_x
        real_board_pos_y=center_y
        # doc = FreeCAD.ActiveDocument
        if idf_to_origin == True:
            board_base_point_x=-off_x
            board_base_point_y=-off_y
        else:
        ## using PcbCenter
            #board_base_point_x=xmin+(xMax-xmin)/2-off_x
            #board_base_point_y=-(ymin+(yMax-ymin)/2)-off_y
            board_base_point_x=center_x-off_x
            board_base_point_y=center_y-off_y
        # not to be used by .kicad_pcb
        msg=""
        if idf_to_origin==True:
            msg+="IDF board has to be exported to Xref=0; Yref=0\r\n\r\n"
            # msg+="IDF board has NOT to be exported to real placement\r\npcbnew version < 6091\r\n\r\n"
        else:
            msg+="IDF board has to be exported to real placement (Auto Adjust)\r\n\r\n"
            # msg+="IDF board has NOT to be exported to Xref=0; Yref=0\r\npcbnew version >=6091\r\n\r\n"
        if (show_messages==True):
            QtGui.qApp.restoreOverrideCursor()
            reply = QtGui.QMessageBox.information(None,"info", msg)
        FreeCAD.ActiveDocument.getObject("Pcb").Placement = FreeCAD.Placement(FreeCAD.Vector(board_base_point_x,board_base_point_y,0),FreeCAD.Rotation(FreeCAD.Vector(0,0,1),0))
        ## FreeCAD.ActiveDocument.getObject("Pcb").Placement = FreeCAD.Placement(FreeCAD.Vector(-off_x,-off_y,0),FreeCAD.Rotation(FreeCAD.Vector(0,0,1),0))
        FreeCADGui.SendMsgToActiveView("ViewFit")
        #ImportGui.insert(u"./c0603.step","demo_5D_vrml_from_step")
        doc.addObject("App::DocumentObjectGroup", "Step_Models")
        modules=[]
        name_kicad_pcb=name[:-3]+"kicad_pcb"
        pcbThickness,modules,board_elab=LoadKicadBoard(name_kicad_pcb)
        #say(modules)
        #say('Alive4 prob time\n')
        #end_milli_time = current_milli_time()
        #say(str(start_time)+'*'+str(end_milli_time)+'start-end\n')
        say_time()
        blacklisted_model_elements=Load_models(pcbThickness,modules)
        if export_board_2step:
            #say('aliveTrue')
            Export2MCAD(blacklisted_model_elements)
        else:
            #say('aliveFalse')
            Display_info(blacklisted_model_elements)
        say_time()
        #stop
###
def onLoadBoard(file_name=None):
    #name=QtGui.QFileDialog.getOpenFileName(this,tr("Open Image"), "/home/jana", tr("Image Files (*.png *.jpg *.bmp)"))[0]
    #global module_3D_dir
    global test_flag, last_pcb_path, configParser, configFilePath, start_time
    global aux_orig, base_orig, base_point, idf_to_origin, off_x, off_y, export_board_2step
    global real_board_pos_x, real_board_pos_y, board_base_point_x, board_base_point_y
    global models3D_prefix, blacklisted_model_elements, col, colr, colg, colb
    global bbox, volume_minimum, height_minimum, idf_to_origin, aux_orig
    global base_orig, base_point, bbox_all, bbox_list, whitelisted_model_elements
    global fusion, addVirtual, blacklisted_models, exportFusing, min_drill_size
    global last_fp_path, last_pcb_path, plcmnt, xp, yp, exportFusing
    default_value='/'
    clear_console()
    #lastPcb_dir='C:/Cad/Progetti_K/ksu-test'
    #say(lastPcb_dir+' last Pcb dir\r\n')
    if not os.path.isdir(last_pcb_path):
        last_pcb_path="./"
    #say(last_pcb_path+'\n')
    if file_name!=None:
        #export_board_2step=True #for cmd line force exporting to STEP
        name=file_name
    elif test_flag==False:
        Filter=""
        #minimize main window
        #self.setWindowState(QtCore.Qt.WindowMinimized)
        #infoDialog('ciao')
        #reply = QtGui.QInputDialog.getText(None, "Hello","Enter your thoughts for the day:")
        #if reply[1]:
        #        # user clicked OK
        #        replyText = reply[0]
        #else:
        #        # user clicked Cancel
        #        replyText = reply[0] # which will be "" if they clicked Cancel
        #restore main window
        #self.setWindowState(QtCore.Qt.WindowActive)
        name, Filter = PySide.QtGui.QFileDialog.getOpenFileName(None, "Open kicad PCB File...",
             last_pcb_path, "*.kicad_pcb")
    else:
        name="C:/Cad/Progetti_K/ksu-test/test.kicad_pcb"
    if len(name) > 0:
        if os.path.isfile(name):
            say('opening '+name+'\n')
            path, fname = os.path.split(name)
            fname=os.path.splitext(fname)[0]
            #fpth = os.path.dirname(os.path.abspath(__file__))
            fpth = os.path.dirname(os.path.abspath(name))
            #filePath = os.path.split(os.path.realpath(__file__))[0]
            say ('my file path '+fpth+'\n')
            if fpth == "":
                fpth = "."
            last_pcb_path = fpth
            #last_pcb_path=path
            # update existing value
            #say(default_ksu_msg)
            configParser.set('last_pcb_path', 'last_pcb_path', path)
            #configParser.set('last_pcb_path', ';; last pcb board path')
            configParser.set('info', default_ksu_msg[0])
            configParser.set('prefix3D', default_ksu_msg[1])
            configParser.set('PcbColor', default_ksu_msg[2])
            configParser.set('Blacklist', default_ksu_msg[3])
            configParser.set('BoundingBox', default_ksu_msg[4])
            configParser.set('Placement', default_ksu_msg[5])
            configParser.set('Virtual', default_ksu_msg[6])
            configParser.set('ExportFuse', default_ksu_msg[7])
            configParser.set('minimum_drill_size', default_ksu_msg[8])
            configParser.set('last_pcb_path', default_ksu_msg[9])
            configParser.set('last_footprint_path', default_ksu_msg[10])
            configParser.set('export', default_ksu_msg[11])
            # save to the config file
            with __builtin__.open(configFilePath, 'wb') as configfile:
                configParser.write(configfile)
            #configFilePath.close() already closed
            doc=FreeCAD.newDocument(fname)
            modules=[]
            start_time=current_milli_time()
            pcbThickness,modules,board_elab=LoadKicadBoard(name)
            routineDrawPCB(pcbThickness,board_elab)
        else:
            say(name+' missing\r')
            stop
        ##Placing board at configured position
        # pos objs x,-y
        # pos board xm+(xM-xm)/2
        # pos board -(ym+(yM-ym)/2)        
        center_x, center_y, bb_x, bb_y = findPcbCenter("Pcb")
        ## using PcbCenter
        xMax=center_x+bb_x/2
        xmin=center_x-bb_x/2
        yMax=center_y+bb_y/2
        ymin=center_y-bb_y/2
        off_x=0; off_y=0  #offset of the board & modules
        if (aux_orig==1):
            xp=getAuxAxisOrigin()[0]; yp=-getAuxAxisOrigin()[1]  #offset of the board & modules
            ##off_x=-xp+xmin+(xMax-xmin)/2; off_y=-yp-(ymin+(yMax-ymin)/2)  #offset of the board & modules
            off_x=-xp+center_x;off_y=-yp+center_y
        if (base_orig==1):
            ##off_x=xmin+(xMax-xmin)/2; off_y=-(ymin+(yMax-ymin)/2)  #offset of the board & modules
            off_x=center_x;off_y=center_y
        if (base_point==1):
            ##off_x=-xp+xmin+(xMax-xmin)/2; off_y=-yp-(ymin+(yMax-ymin)/2)  #offset of the board & modules
            #off_x=-xp+center_x;off_y=-yp+center_y
            off_x=-xp+center_x;off_y=-yp+center_y
        ## test maui board_base_point_x=(xMax-xmin)/2-off_x
        ## test maui board_base_point_y=-((yMax-ymin)/2)-off_y
        #real_board_pos_x=xmin+(xMax-xmin)/2
        #real_board_pos_y=-(ymin+(yMax-ymin)/2)
        ## using PcbCenter
        real_board_pos_x=center_x
        real_board_pos_y=center_y
        # doc = FreeCAD.ActiveDocument
        if idf_to_origin == True:
            board_base_point_x=-off_x
            board_base_point_y=-off_y
        else:
        ## using PcbCenter
            #board_base_point_x=xmin+(xMax-xmin)/2-off_x
            #board_base_point_y=-(ymin+(yMax-ymin)/2)-off_y
            board_base_point_x=center_x-off_x
            board_base_point_y=center_y-off_y
        FreeCAD.ActiveDocument.getObject("Pcb").Placement = FreeCAD.Placement(FreeCAD.Vector(board_base_point_x,board_base_point_y,0),FreeCAD.Rotation(FreeCAD.Vector(0,0,1),0))
        ## FreeCAD.ActiveDocument.getObject("Pcb").Placement = FreeCAD.Placement(FreeCAD.Vector(-off_x,-off_y,0),FreeCAD.Rotation(FreeCAD.Vector(0,0,1),0))
        FreeCADGui.SendMsgToActiveView("ViewFit")
        #ImportGui.insert(u"./c0603.step","demo_5D_vrml_from_step")
        doc.addObject("App::DocumentObjectGroup", "Step_Models")
        say_time()
        Load_models(pcbThickness,modules)
        if export_board_2step:
            #say('aliveTrue')
            Export2MCAD(blacklisted_model_elements)
        else:
            #say('aliveFalse')
            Display_info(blacklisted_model_elements)
        say_time()
        #stop
###

def routineR_XYZ(axe,alpha):
    global resetP
    say('routine Rotate XYZ\n')
    FreeCADGui.activateWorkbench("PartWorkbench")
    #FreeCADGui.SendMsgToActiveView("ViewFit")
    ##FreeCADGui.activeDocument().activeView().viewTop()
    doc = FreeCAD.ActiveDocument
    #FreeCAD.Console.PrintMessage("hereXYZ !"+"\r\n")
    selEx = FreeCADGui.Selection.getSelectionEx()
    objs = [selobj.Object for selobj in selEx]
    if len(objs) == 1:
        s = objs[0].Shape
        shape=s.copy()
        shape.Placement=s.Placement;
        boundBox_ = s.BoundBox
        boundBoxLX = boundBox_.XLength
        boundBoxLY = boundBox_.YLength
        boundBoxLZ = boundBox_.ZLength
        a = str(boundBox_)
        a,b = a.split('(')
        c = b.split(',')
        oripl_X = float(c[0])
        oripl_Y = float(c[1])
        oripl_Z = float(c[2])
        #say("bbx: "+str(boundBoxLX)+" bby: "+str(boundBoxLY)+"bbz: "+str(boundBoxLZ)+"\r\n")
        #say("x: "+str(oripl_X)+" y: "+str(oripl_Y)+"z: "+str(oripl_Z)+"\r\n")
        #shape.rotate((oripl_X,oripl_Y,oripl_Z),(1,0,0),90)
        angle=alpha
        if axe=='x':
            #shape.rotate((0,0,0),(1,0,0),90)
            shape.rotate((oripl_X+boundBoxLX/2,oripl_Y+boundBoxLY/2,oripl_Z+boundBoxLZ/2),(1,0,0),int(angle))
        if axe=='y':
            #shape.rotate((0,0,0),(0,1,0),90)
            shape.rotate((oripl_X+boundBoxLX/2,oripl_Y+boundBoxLY/2,oripl_Z+boundBoxLZ/2),(0,1,0),int(angle))
        if axe=='z':
            #shape.rotate((0,0,0),(0,0,1),90)
            shape.rotate((oripl_X+boundBoxLX/2,oripl_Y+boundBoxLY/2,oripl_Z+boundBoxLZ/2),(0,0,1),int(angle))
        #Part.show(shape)
        objs[0].Placement=shape.Placement
        FreeCADGui.Selection.addSelection(objs[0])
        FreeCAD.activeDocument().recompute()
        if resetP==True:
            routineResetPlacement()
        #say("end of rotineZ!"+"\r\n")
    else:
        say("Select ONE single part object !\r\n"+"\r\n")
        #QtGui.QMessageBox.information(None,"Info ...","Select ONE single part object !\r\n"+"\r\n")
###  end RotateXYZ

def routineT_XYZ(axe,v):
    global resetP
    say('routine Translate XYZ\n')
    FreeCADGui.activateWorkbench("PartWorkbench")
    #FreeCADGui.SendMsgToActiveView("ViewFit")
    ##FreeCADGui.activeDocument().activeView().viewTop()
    doc = FreeCAD.ActiveDocument
    selEx = FreeCADGui.Selection.getSelectionEx()
    objs = [selobj.Object for selobj in selEx]
    if len(objs) == 1:
        s = objs[0].Shape
        shape=s.copy()
        shape.Placement=s.Placement;
        #shape.rotate((oripl_X,oripl_Y,oripl_Z),(1,0,0),90)
        #say("axe "+axe+", value "+v+"\r\n")
        if axe=='x':
            shape.translate((float(v),0,0))
        if axe=='y':
            shape.translate((0,float(v),0))
        if axe=='z':
            shape.translate((0,0,float(v)))
        #Part.show(shape)
        objs[0].Placement=shape.Placement
        FreeCADGui.Selection.addSelection(objs[0])
        FreeCAD.activeDocument().recompute()
        if resetP==True:
            routineResetPlacement()
        #say("end of rotineT!"+"\r\n")
    else:
        say("Select ONE single part object !\r\n"+"\r\n")
        #QtGui.QMessageBox.information(None,"Info ...","Select ONE single part object !\r\n"+"\r\n")
###  end TranslateXYZ

def routineResetPlacement():
    objs=[]
    FreeCADGui.activateWorkbench("PartWorkbench")
    #FreeCADGui.SendMsgToActiveView("ViewFit")
    ##FreeCADGui.activeDocument().activeView().viewTop()
    doc = FreeCAD.ActiveDocument
    selEx = FreeCADGui.Selection.getSelectionEx()
    objs = [selobj.Object for selobj in selEx]
    #print 'here'
    if len(objs) == 1:
        say('routine reset Placement properties\n')

        s=objs[0].Shape
        r=[]
        t=s.copy()
        for i in t.childShapes():
            c=i.copy()
            c.Placement=t.Placement.multiply(c.Placement)
            r.append((i,c))

        w=t.replaceShape(r)
        w.Placement=FreeCAD.Placement()
        Part.show(w)
        #say(w)

        FreeCADGui.ActiveDocument.ActiveObject.ShapeColor=FreeCADGui.ActiveDocument.getObject(objs[0].Name).ShapeColor
        FreeCADGui.ActiveDocument.ActiveObject.LineColor=FreeCADGui.ActiveDocument.getObject(objs[0].Name).LineColor
        FreeCADGui.ActiveDocument.ActiveObject.PointColor=FreeCADGui.ActiveDocument.getObject(objs[0].Name).PointColor
        FreeCADGui.ActiveDocument.ActiveObject.DiffuseColor=FreeCADGui.ActiveDocument.getObject(objs[0].Name).DiffuseColor
        FreeCADGui.ActiveDocument.ActiveObject.Transparency=FreeCADGui.ActiveDocument.getObject(objs[0].Name).Transparency

        new_label=objs[0].Label
        FreeCAD.ActiveDocument.removeObject(objs[0].Name)
        FreeCAD.ActiveDocument.recompute()
        FreeCAD.ActiveDocument.ActiveObject.Label=new_label
        rObj=FreeCAD.ActiveDocument.ActiveObject
        del objs
        FreeCADGui.Selection.addSelection(rObj)
        #FreeCAD.activeDocument().recompute()
        #say("end of rotineRP!"+"\r\n")
    else:
        say("Select ONE single part object !\r\n"+"\r\n")
        #QtGui.QMessageBox.information(None,"Info ...","Select ONE single part object !\r\n"+"\r\n")
        del objs
### end reset prop

def routineScaleVRML():
    global exportV, exportS
    say('routine Scale to VRML 1/2.54\n')
    doc = FreeCAD.ActiveDocument
    selEx = FreeCADGui.Selection.getSelectionEx()
    objs = [selobj.Object for selobj in selEx]
    if len(objs) >= 1:  #allow more then 1 obj for vrml
        say('exporting\n')
        fullFilePathName=doc.FileName
        if fullFilePathName=="":
            home = expanduser("~")
            fullFilePathName=home+os.sep+doc.Label+'.FCStd'
            say('path not found, saving to '+fullFilePathName+'\n')
            #say(fullFilePathName)
        else:
            say(fullFilePathName+'\n')
        go_export(fullFilePathName)
        path, fname = os.path.split(fullFilePathName)
        #fname=os.path.splitext(fname)[0]
        fname=objs[0].Label
        if exportV or exportS:
            msg="""<b>export STEP & scaled VRML file for kicad!</b>
            <font color='white'>****************************************************************************</font><br>
            <i>exporting folder: </i><br>- <b>"""+path
            msg+="""</b><br><i>exporting filename: </i><br>"""
            if exportV:
                msg+="""- <b>"""+fname+""".wrl<br>"""
            if exportS:
                msg+="""</b>- <b>"""+fname+""".step</b>"""
            else:
                if len(objs) >= 1:
                    msg+="""<br></b>- <b>step file not exported; multi-part selected</b>"""
            #msg="export scaled VRML file for kicad!\r\n"
            #msg=msg+"****************************************************************************"
            msg=msg+"<br><br><i>3D settings in kicad Module Editor:</i><br>"
            msg=msg+"<b>- scale 1 1 1\r\n- offset 0 0 0<br>- rotation 0 0 "+str(rot_wrl)+"</b>"
            ##self.setWindowState(QtCore.Qt.WindowMinimized)
            QtGui.qApp.restoreOverrideCursor()
            QtGui.QMessageBox.information(None,"Info ...",msg)
            ##self.setWindowState(QtCore.Qt.WindowActive)
            say('done\n')
    else:
        say("Select ONE single part object !\r\n"+"\r\n")
        #QtGui.QMessageBox.information(None,"Info ...","Select ONE single part object !\r\n"+"\r\n")
    return 0    
###

###
def routineScaleVRML_1():
    global rot_wrl
    say('routine Scale to VRML 1/2.54\n')
    FreeCADGui.activateWorkbench("PartWorkbench")
    #FreeCADGui.SendMsgToActiveView("ViewFit")
    ##FreeCADGui.activeDocument().activeView().viewTop()
    doc = FreeCAD.ActiveDocument
    selEx = FreeCADGui.Selection.getSelectionEx()
    objs = [selobj.Object for selobj in selEx]
    if len(objs) == 1:
        objS=FreeCAD.ActiveDocument.getObject(objs[0].Name).Shape
        #FreeCADGui.ActiveDocument.getObject(objs[0].Name).BoundingBox = True
        final_Label=FreeCAD.ActiveDocument.getObject(objs[0].Name).Label
        myobjG=FreeCADGui.ActiveDocument.getObject(objs[0].Name)
        myobjA=FreeCAD.ActiveDocument.getObject(objs[0].Name)
        mynewdoc=FreeCAD.newDocument()
        FreeCAD.ActiveDocument.addObject('Part::Feature',objs[0].Name).Shape=objS

        #print 'here'
        myobjA1=FreeCAD.ActiveDocument.ActiveObject
        #myobjA1.Label=final_Label
        myobjG1=FreeCADGui.ActiveDocument.ActiveObject
        myobjG1.ShapeColor=myobjG.ShapeColor
        myobjG1.LineColor=myobjG.LineColor
        myobjG1.PointColor=myobjG.PointColor
        myobjG1.DiffuseColor=myobjG.DiffuseColor
        myobjG1.Transparency=myobjG.Transparency
        FreeCAD.ActiveDocument.recompute()

        FreeCAD.ActiveDocument.ActiveObject.Label=final_Label+'_vrml'
        print final_Label+'_vrml\r\n'
        #FreeCADGui.ActiveDocument.getObject(objs[0].Name).Visibility=False

        FreeCAD.ActiveDocument.recompute()
        vrml_obj = Draft.scale(FreeCAD.ActiveDocument.ActiveObject,delta=FreeCAD.Vector(0.3937,0.3937,0.3937),center=FreeCAD.Vector(0,0,0),legacy=True)
        FreeCAD.ActiveDocument.recompute()
        #FreeCAD.ActiveDocument.ActiveObject.ViewObject.DisplayMode = 'Shaded'
        FreeCADGui.ActiveDocument.ActiveObject.BoundingBox = False
        #FreeCAD.ActiveDocument.ActiveObject.ViewObject.DisplayMode = 'Shaded'
        #vrml_obj.ViewObject.DisplayMode = u'Shaded'
        shade_val='Shaded'
        #FreeCAD.ActiveDocument.ActiveObject.ViewObject.DisplayMode = 'Shaded'
        FreeCAD.ActiveDocument.ActiveObject.ViewObject.DisplayMode = 1 #Shaded
        FreeCADGui.SendMsgToActiveView("ViewFit")
        msg="""<b>export scaled VRML file for kicad!</b>
            <font color='white'>****************************************************************************</font><br>
            <i>3D settings in kicad Module Editor:</i><br>
            <font color='white'>- </font><b>scale 1 1 1\r\n- offset 0 0 0\r\n- rotation 0 0 {0}</b>
            """.format(rot_wrl)
        #msg="export scaled VRML file for kicad!\r\n"
        #msg=msg+"****************************************************************************"
        #msg=msg+"\r\n3D settings in kicad Module Editor:\r\n"
        #msg=msg+"- scale 1 1 1\r\n- offset 0 0 0\r\n- rotation 0 0 "+str(rot_wrl)
        self.setWindowState(QtCore.Qt.WindowMinimized)
        QtGui.qApp.restoreOverrideCursor()
        QtGui.QMessageBox.information(None,"Info ...",msg)
        self.setWindowState(QtCore.Qt.WindowActive)
    else:
        say("Select ONE single part object !\r\n"+"\r\n")
        #QtGui.QMessageBox.information(None,"Info ...","Select ONE single part object !\r\n"+"\r\n")
    return 0

###  end ScaleVRML_1
def routineC_XYZ(axe):
    global resetP
    say('routine center position\n')
    #if self.checkBox_1.isChecked():
    #    routineResetPlacement()
    FreeCADGui.activateWorkbench("PartWorkbench")
    #FreeCADGui.SendMsgToActiveView("ViewFit")
    ##FreeCADGui.activeDocument().activeView().viewTop()
    doc = FreeCAD.ActiveDocument
    say("Centering on Axe XYZ !"+"\r\n")
    selEx = FreeCADGui.Selection.getSelectionEx()
    objs = [selobj.Object for selobj in selEx]
    if len(objs) == 1:
        s = objs[0].Shape
        shape=s.copy()
        #shape.Placement=s.Placement;
        shape.Placement= FreeCAD.Placement(FreeCAD.Vector(0,0,0),FreeCAD.Rotation(FreeCAD.Vector(0,0,1),0))
        boundBox_ = s.BoundBox
        boundBoxLX = boundBox_.XLength
        boundBoxLY = boundBox_.YLength
        boundBoxLZ = boundBox_.ZLength
        say("bbox: "+str(boundBox_)+"\r\n")

        a = str(boundBox_)
        a,b = a.split('(')
        c = b.split(',')
        oripl_X = float(c[0])
        oripl_Y = float(c[1])
        oripl_Z = float(c[2])
        #say("bbx: "+str(boundBoxLX)+" bby: "+str(boundBoxLY)+"bbz: "+str(boundBoxLZ)+"\r\n")
        #say("x: "+str(oripl_X)+" y: "+str(oripl_Y)+"z: "+str(oripl_Z)+"\r\n")

        p=s.Placement
        #say("PlacementBase  : "+str(p)+"\r\n")
        #say(str(p.Base[0])+' '+str(p.Base[1])+' '+str(p.Base[2])+"\r\n")
        if axe=='x':
            #shape.translate((0,0,0))
            diffPl=-oripl_X-boundBoxLX/2
            #shape.Placement.move(diffPl,0,0)
            #shape.translate(Base.Vector(diffPl,0,0))
            shape.translate((diffPl,p.Base[1],p.Base[2]))
        if axe=='y':
            diffPl=-oripl_Y-boundBoxLY/2
            #shape.translate(Base.Vector(0,diffPl,0))
            shape.translate((p.Base[0],diffPl,p.Base[2]))
        if axe=='z':
            diffPl=-oripl_Z-boundBoxLZ/2
            shape.translate((p.Base[0],p.Base[1],diffPl))
            #shape.translate(Base.Vector(0,0,diffPl))
        ### to zero posX -bboxX/2
        #say("x: "+str(oripl_X)+" y: "+str(oripl_Y)+"z: "+str(oripl_Z)+"\r\n")
        #say("axe "+axe+" placement"+str(diffPl)+"\r\n")
        #Part.show(shape)
        objs[0].Placement=shape.Placement
        FreeCADGui.Selection.addSelection(objs[0])
        FreeCAD.activeDocument().recompute()
        #say("x: "+str(oripl_X)+"\r\ny: "+str(oripl_Y)+"\r\nz: "+str(oripl_Z)+"\r\n")
        if resetP==True:
            routineResetPlacement()
            #say("pos reset done\r\n")
        #say("done\r\n")
    else:
        say("Select an object !"+"\r\n")
        #QtGui.QMessageBox.information(None,"Info ...","Select an object !"+"\r\n")
###  end routineC_XYZ

def routineP_XYZ(axe):
    global resetP
    say('routine put on axe\n')
    #routineResetPlacement()
    FreeCADGui.activateWorkbench("PartWorkbench")
    #FreeCADGui.SendMsgToActiveView("ViewFit")
    ##FreeCADGui.activeDocument().activeView().viewTop()
    doc = FreeCAD.ActiveDocument
    say("Put on Axe XYZ !"+"\r\n")
    selEx = FreeCADGui.Selection.getSelectionEx()
    objs = [selobj.Object for selobj in selEx]
    if len(objs) == 1:
        s = objs[0].Shape
        shape=s.copy()
        #shape.Placement=s.Placement;
        shape.Placement= FreeCAD.Placement(FreeCAD.Vector(0,0,0),FreeCAD.Rotation(FreeCAD.Vector(0,0,1),0))
        boundBox_ = s.BoundBox
        boundBoxLX = boundBox_.XLength
        boundBoxLY = boundBox_.YLength
        boundBoxLZ = boundBox_.ZLength
        a = str(boundBox_)
        a,b = a.split('(')
        c = b.split(',')
        oripl_X = float(c[0])
        oripl_Y = float(c[1])
        oripl_Z = float(c[2])
        p=s.Placement
        say("PlacementBase  : "+str(p)+"\r\n")
        #say(str(p.Base[0])+' '+str(p.Base[1])+' '+str(p.Base[2])+"\r\n")
        if axe=='x':
            #shape.translate((0,0,0))
            diffPl=p.Base[0]-oripl_X
            #shape.Placement.move(diffPl,0,0)
            #shape.translate(Base.Vector(diffPl,0,0))
            shape.translate((diffPl,p.Base[1],p.Base[2]))
        if axe=='y':
            diffPl=p.Base[1]-oripl_Y
            #shape.translate(Base.Vector(0,diffPl,0))
            shape.translate((p.Base[0],diffPl,p.Base[2]))
        if axe=='z':
            diffPl=p.Base[2]-oripl_Z
            shape.translate((p.Base[0],p.Base[1],diffPl))
            #shape.translate(Base.Vector(0,0,diffPl))
        ### to zero posX -bboxX/2
        #say("x: "+str(oripl_X)+" y: "+str(oripl_Y)+"z: "+str(oripl_Z)+"\r\n")
        #say("axe "+axe+" placement"+str(diffPl)+"\r\n")
        #Part.show(shape)
        objs[0].Placement=shape.Placement
        FreeCADGui.Selection.addSelection(objs[0])
        FreeCAD.activeDocument().recompute()
        #say("x: "+str(oripl_X)+"\r\ny: "+str(oripl_Y)+"\r\nz: "+str(oripl_Z)+"\r\n")
        #say("placement "+str(p[0]))
        #return [oripl_X, oripl_Y, oripl_Z,p.Base[0],p.Base[1],p.Base[2]];
        if resetP==True:
            routineResetPlacement()
    else:
        say("Select ONE single part object !\r\n"+"\r\n")
        #QtGui.QMessageBox.information(None,"Info ...","Select ONE single part object !\r\n"+"\r\n")
###  end routineP_XYZ

def get_position():
    global min_val, exportS
    say('routine get base position\n')
    FreeCADGui.activateWorkbench("PartWorkbench")
    #FreeCADGui.SendMsgToActiveView("ViewFit")
    ##FreeCADGui.activeDocument().activeView().viewTop()
    doc = FreeCAD.ActiveDocument
    #say("hereXYZ !"+"\r\n")
    selEx = FreeCADGui.Selection.getSelectionEx()
    objs = [selobj.Object for selobj in selEx]
    if len(objs) == 1:
        s = objs[0].Shape
        boundBox_ = s.BoundBox
        boundBoxLX = boundBox_.XLength
        boundBoxLY = boundBox_.YLength
        boundBoxLZ = boundBox_.ZLength
        a = str(boundBox_)
        a,b = a.split('(')
        c = b.split(',')
        oripl_X = float(c[0])
        oripl_Y = float(c[1])
        oripl_Z = float(c[2])
        FreeCADGui.Selection.addSelection(objs[0])
        FreeCAD.activeDocument().recompute()
        #say("x: "+str(oripl_X)+"\r\ny: "+str(oripl_Y)+"\r\nz: "+str(oripl_Z)+"\r\n")
        p=s.Placement
        #say("PlacementBase  : "+str(p)+"\n\n")
        #say(str(p.Base[0])+' '+str(p.Base[1])+' '+str(p.Base[2])+"\r\n")
        ### to zero posX -bboxX/2
        #say("placement "+str(p[0]))
        #min_val=10e-16
        #say("min_val "+str(min_val)+'\r\n')
        if abs(oripl_X) < min_val:
            oripl_X=0
        if abs(oripl_Y) < min_val:
            oripl_Y=0
        if abs(oripl_Z) < min_val:
            oripl_Z=0
        return [oripl_X, oripl_Y, oripl_Z,p.Base[0],p.Base[1],p.Base[2]];

    else:
        if exportS:
            say("Select ONE single part object !\r\n"+"\r\n")
            #QtGui.QMessageBox.information(None,"Info ...","Select ONE single part object !\r\n"+"\r\n")
            QtGui.qApp.restoreOverrideCursor()
            diag = QtGui.QMessageBox(QtGui.QMessageBox.Icon.Critical,
                                    'Error in selection                                                                ."+"\r\n"',
                                    'Select ONE single part object !')
            diag.setWindowModality(QtCore.Qt.ApplicationModal)
            diag.exec_()
###  end get position

def routineM_XYZ(axe,v):
    global resetP
    mydoc=FreeCAD.ActiveDocument
    say('routine Move to point XYZ\n')
    FreeCADGui.activateWorkbench("PartWorkbench")
    #FreeCADGui.SendMsgToActiveView("ViewFit")
    ##FreeCADGui.activeDocument().activeView().viewTop()
    doc = FreeCAD.ActiveDocument
    selEx = FreeCADGui.Selection.getSelectionEx()
    objs = [selobj.Object for selobj in selEx]
    if len(objs) == 1:
        s = objs[0].Shape
        boundBox_ = s.BoundBox
        boundBoxLX = boundBox_.XLength
        boundBoxLY = boundBox_.YLength
        boundBoxLZ = boundBox_.ZLength
        a = str(boundBox_)
        a,b = a.split('(')
        c = b.split(',')
        oripl_X = float(c[0])
        oripl_Y = float(c[1])
        oripl_Z = float(c[2])
        shape=s.copy()
        shape.Placement=s.Placement;p=s.Placement
        #shape.rotate((oripl_X,oripl_Y,oripl_Z),(1,0,0),90)
        #say("axe "+axe+", value "+v+"\r\n")
        if axe=='x':
            #if abs(float(v)-p.Base[0])>min_val:
            shape.translate((float(v)-oripl_X,0,0))
        if axe=='y':
            shape.translate((0,float(v)-oripl_Y,0))
        if axe=='z':
            shape.translate((0,0,float(v)-oripl_Z))
        #Part.show(shape)
        objs[0].Placement=shape.Placement
        FreeCADGui.Selection.addSelection(objs[0])
        FreeCAD.activeDocument().recompute()
        if resetP==True:
            routineResetPlacement()
        #say("end of rotineM!"+"\r\n")
    else:
        say("Select an object !"+"\r\n")
        #QtGui.QMessageBox.information(None,"Info ...","Select ONE single part object !\r\n"+"\r\n")
###  end Move to Point XYZ

def routineCollisions():
    global conflict_tolerance
    def error_dialog(msg):
        """Create a simple dialog QMessageBox with an error message"""
        FreeCAD.Console.PrintError(msg + '\n')
        QtGui.qApp.restoreOverrideCursor()
        diag = QtGui.QMessageBox(QtGui.QMessageBox.Icon.Critical,
                                'Error in checking Collisions                                                       ."+"\r\n"',
                                msg)
        diag.setWindowModality(QtCore.Qt.ApplicationModal)
        diag.exec_()

    if len(FreeCADGui.Selection.getSelectionEx()) < 2:
        error_dialog('Select at least two objects')
        collisions=2
        return collisions

    object_list = []
    collisions=0
    for obj in FreeCADGui.Selection.getSelectionEx():
        object_list.append(obj.Object)

    for i, object_a in enumerate(object_list):
        for object_b in object_list[(i + 1):]:
            say(object_a.Label+" "+object_b.Label+"\r\n")
            shape_a = object_a.Shape
            shape_b = object_b.Shape
            label_a = object_a.Label
            label_b = object_b.Label
            try:
                common = shape_a.common(shape_b)
                if common.Volume > conflict_tolerance:
                    say(
                        'Volume of the intersection between {} and {}: {}\n'.format(
                            label_a,
                            label_b,
                            common.Volume))

                    intersection_object = FreeCAD.ActiveDocument.addObject(
                        'Part::Feature')
                    intersection_object.Label = 'Collisions ({} - {})'.format(
                        label_a, label_b)
                    intersection_object.Shape = common
                    intersection_object.ViewObject.ShapeColor = (1.0, 0.0, 0.0, 1.0)
                    #object_a.ViewObject.Transparency = 80
                    #object_b.ViewObject.Transparency = 80
                    object_a.ViewObject.Visibility=False
                    object_b.ViewObject.Visibility=False
                    collisions=1
                else:
                    say(
                        'No intersection between {} and {}\n'.format(
                            label_a,
                            label_b))
                    #collisions=0
            except Exception, e:
                FreeCAD.Console.PrintWarning(u"{0}\n".format(e))
            #say("here_collision\r\n")
    return collisions

### end Collisions

def create_axis():

    FreeCAD.ActiveDocument.addObject("App::DocumentObjectGroup", "axis")
    #Z axis
    FreeCAD.ActiveDocument.addObject("Part::Box","AxisBoxZ")
    FreeCAD.ActiveDocument.ActiveObject.Label = "CubeZ"
    FreeCAD.ActiveDocument.addObject("Part::Cone","AxisConeZ")
    FreeCAD.ActiveDocument.ActiveObject.Label = "ConeZ"
    FreeCAD.ActiveDocument.getObject("AxisBoxZ").Width = '0 mm'
    FreeCAD.ActiveDocument.getObject("AxisBoxZ").Width = '0.1 mm'
    FreeCAD.ActiveDocument.getObject("AxisBoxZ").Length = '0 mm'
    FreeCAD.ActiveDocument.getObject("AxisBoxZ").Length = '0.2 mm'
    FreeCAD.ActiveDocument.getObject("AxisConeZ").Radius1 = '0 mm'
    FreeCAD.ActiveDocument.getObject("AxisConeZ").Radius1 = '0.4 mm'
    FreeCAD.ActiveDocument.getObject("AxisConeZ").Radius2 = '0 mm'
    FreeCAD.ActiveDocument.getObject("AxisConeZ").Radius2 = '0.1 mm'
    FreeCAD.ActiveDocument.getObject("AxisConeZ").Placement = FreeCAD.Placement(FreeCAD.Vector(0,0,9),FreeCAD.Rotation(FreeCAD.Vector(0,0,1),0))
    FreeCAD.ActiveDocument.getObject("AxisConeZ").Height = '5 mm'
    FreeCAD.ActiveDocument.getObject("AxisBoxZ").Placement = FreeCAD.Placement(FreeCAD.Vector(-0.1,-0.05,0),FreeCAD.Rotation(FreeCAD.Vector(0,0,1),0))
    FreeCADGui.ActiveDocument.getObject("AxisConeZ").ShapeColor = (0.0000,0.0000,1.0000)
    FreeCADGui.ActiveDocument.getObject("AxisBoxZ").ShapeColor = (0.0000,0.0000,1.0000)
    FreeCAD.activeDocument().addObject("Part::MultiFuse","FusionAxisZ")
    FreeCAD.activeDocument().FusionAxisZ.Shapes = [FreeCAD.activeDocument().AxisBoxZ,FreeCAD.activeDocument().AxisConeZ,]
    FreeCADGui.activeDocument().AxisBoxZ.Visibility=False
    FreeCADGui.activeDocument().AxisConeZ.Visibility=False
    FreeCADGui.ActiveDocument.FusionAxisZ.ShapeColor=FreeCADGui.ActiveDocument.AxisBoxZ.ShapeColor
    FreeCADGui.ActiveDocument.FusionAxisZ.DisplayMode=FreeCADGui.ActiveDocument.AxisBoxZ.DisplayMode
    FreeCAD.ActiveDocument.recompute()
    FreeCAD.ActiveDocument.addObject('Part::Feature','FusionAxisZ1').Shape=FreeCAD.ActiveDocument.FusionAxisZ.Shape
    FreeCAD.ActiveDocument.ActiveObject.Label = "Z"

    FreeCADGui.ActiveDocument.ActiveObject.ShapeColor=(0.0000,0.0000,1.0000)
    obj=FreeCAD.ActiveDocument.ActiveObject
    FreeCAD.ActiveDocument.getObject("axis").addObject(obj)
    FreeCAD.ActiveDocument.recompute()
    FreeCAD.ActiveDocument.removeObject("FusionAxisZ")
    FreeCAD.ActiveDocument.removeObject("AxisBoxZ")
    FreeCAD.ActiveDocument.removeObject("AxisConeZ")
    FreeCAD.ActiveDocument.recompute()

    #Y axis
    FreeCAD.ActiveDocument.addObject("Part::Box","AxisBoxY")
    FreeCAD.ActiveDocument.ActiveObject.Label = "CubeY"
    FreeCAD.ActiveDocument.addObject("Part::Cone","AxisConeY")
    FreeCAD.ActiveDocument.ActiveObject.Label = "ConeY"
    FreeCAD.ActiveDocument.getObject("AxisBoxY").Width = '0 mm'
    FreeCAD.ActiveDocument.getObject("AxisBoxY").Width = '0.1 mm'
    FreeCAD.ActiveDocument.getObject("AxisBoxY").Length = '0 mm'
    FreeCAD.ActiveDocument.getObject("AxisBoxY").Length = '0.2 mm'
    FreeCAD.ActiveDocument.getObject("AxisConeY").Radius1 = '0 mm'
    FreeCAD.ActiveDocument.getObject("AxisConeY").Radius1 = '0.4 mm'
    FreeCAD.ActiveDocument.getObject("AxisConeY").Radius2 = '0 mm'
    FreeCAD.ActiveDocument.getObject("AxisConeY").Radius2 = '0.1 mm'
    FreeCAD.ActiveDocument.getObject("AxisConeY").Placement = FreeCAD.Placement(FreeCAD.Vector(0,0,9),FreeCAD.Rotation(FreeCAD.Vector(0,0,1),0))
    FreeCAD.ActiveDocument.getObject("AxisConeY").Height = '5 mm'
    FreeCAD.ActiveDocument.getObject("AxisBoxY").Placement = FreeCAD.Placement(FreeCAD.Vector(-0.1,-0.05,0),FreeCAD.Rotation(FreeCAD.Vector(0,0,1),0))
    FreeCADGui.ActiveDocument.getObject("AxisConeY").ShapeColor = (0.0000,1.0000,0.0000)
    FreeCADGui.ActiveDocument.getObject("AxisBoxY").ShapeColor = (0.0000,1.0000,0.0000)
    FreeCAD.activeDocument().addObject("Part::MultiFuse","FusionAxisY")
    FreeCAD.activeDocument().FusionAxisY.Shapes = [FreeCAD.activeDocument().AxisBoxY,FreeCAD.activeDocument().AxisConeY,]
    FreeCADGui.activeDocument().AxisBoxY.Visibility=False
    FreeCADGui.activeDocument().AxisConeY.Visibility=False
    FreeCADGui.ActiveDocument.FusionAxisY.ShapeColor=FreeCADGui.ActiveDocument.AxisBoxY.ShapeColor
    FreeCADGui.ActiveDocument.FusionAxisY.DisplayMode=FreeCADGui.ActiveDocument.AxisBoxY.DisplayMode
    FreeCAD.ActiveDocument.recompute()
    FreeCAD.ActiveDocument.addObject('Part::Feature','FusionAxisY1').Shape=FreeCAD.ActiveDocument.FusionAxisY.Shape
    FreeCAD.ActiveDocument.ActiveObject.Label = "Y"

    FreeCADGui.ActiveDocument.ActiveObject.ShapeColor=(0.0000,1.0000,0.000)
    obj=FreeCAD.ActiveDocument.ActiveObject
    FreeCAD.ActiveDocument.getObject("axis").addObject(obj)
    FreeCAD.ActiveDocument.recompute()
    FreeCAD.ActiveDocument.removeObject("FusionAxisY")
    FreeCAD.ActiveDocument.removeObject("AxisBoxY")
    FreeCAD.ActiveDocument.removeObject("AxisConeY")
    FreeCAD.ActiveDocument.recompute()
    FreeCAD.ActiveDocument.ActiveObject.Placement = FreeCAD.Placement(FreeCAD.Vector(0,0,0.05),FreeCAD.Rotation(FreeCAD.Vector(1,0,0),-90))

    #X axis
    FreeCAD.ActiveDocument.addObject("Part::Box","AxisBoxX")
    FreeCAD.ActiveDocument.ActiveObject.Label = "CubeX"
    FreeCAD.ActiveDocument.addObject("Part::Cone","AxisConeX")
    FreeCAD.ActiveDocument.ActiveObject.Label = "ConeX"
    FreeCAD.ActiveDocument.getObject("AxisBoxX").Width = '0 mm'
    FreeCAD.ActiveDocument.getObject("AxisBoxX").Width = '0.2 mm'
    FreeCAD.ActiveDocument.getObject("AxisBoxX").Length = '0 mm'
    FreeCAD.ActiveDocument.getObject("AxisBoxX").Length = '0.1 mm'
    FreeCAD.ActiveDocument.getObject("AxisConeX").Radius1 = '0 mm'
    FreeCAD.ActiveDocument.getObject("AxisConeX").Radius1 = '0.4 mm'
    FreeCAD.ActiveDocument.getObject("AxisConeX").Radius2 = '0 mm'
    FreeCAD.ActiveDocument.getObject("AxisConeX").Radius2 = '0.1 mm'
    FreeCAD.ActiveDocument.getObject("AxisConeX").Placement = FreeCAD.Placement(FreeCAD.Vector(0,0,9),FreeCAD.Rotation(FreeCAD.Vector(0,0,1),0))
    FreeCAD.ActiveDocument.getObject("AxisConeX").Height = '5 mm'
    FreeCAD.ActiveDocument.getObject("AxisBoxX").Placement = FreeCAD.Placement(FreeCAD.Vector(-0.1,-0.05,0),FreeCAD.Rotation(FreeCAD.Vector(0,0,1),0))
    FreeCADGui.ActiveDocument.getObject("AxisConeX").ShapeColor = (1.0000,0.0000,0.0000)
    FreeCADGui.ActiveDocument.getObject("AxisBoxX").ShapeColor = (1.0000,0.0000,0.0000)
    FreeCAD.activeDocument().addObject("Part::MultiFuse","FusionAxisX")
    FreeCAD.activeDocument().FusionAxisX.Shapes = [FreeCAD.activeDocument().AxisBoxX,FreeCAD.activeDocument().AxisConeX,]
    FreeCADGui.activeDocument().AxisBoxX.Visibility=False
    FreeCADGui.activeDocument().AxisConeX.Visibility=False
    FreeCADGui.ActiveDocument.FusionAxisX.ShapeColor=FreeCADGui.ActiveDocument.AxisBoxX.ShapeColor
    FreeCADGui.ActiveDocument.FusionAxisX.DisplayMode=FreeCADGui.ActiveDocument.AxisBoxX.DisplayMode
    FreeCAD.ActiveDocument.recompute()
    FreeCAD.ActiveDocument.addObject('Part::Feature','FusionAxisX1').Shape=FreeCAD.ActiveDocument.FusionAxisX.Shape
    FreeCAD.ActiveDocument.ActiveObject.Label="X"

    FreeCADGui.ActiveDocument.ActiveObject.ShapeColor=(1.0000,0.0000,0.0000)
    obj=FreeCAD.ActiveDocument.ActiveObject
    FreeCAD.ActiveDocument.getObject("axis").addObject(obj)
    FreeCAD.ActiveDocument.recompute()
    FreeCAD.ActiveDocument.removeObject("FusionAxisX")
    FreeCAD.ActiveDocument.removeObject("AxisBoxX")
    FreeCAD.ActiveDocument.removeObject("AxisConeX")
    FreeCAD.ActiveDocument.getObject("FusionAxisX1").Placement = FreeCAD.Placement(FreeCAD.Vector(0,-0.05,0),FreeCAD.Rotation(FreeCAD.Vector(0,1,0),90))

    FreeCAD.ActiveDocument.recompute()
###
#############################
def createSolidBBox2(model3D):
    #FreeCADGui.Selection.removeSelection(FreeCAD.activeDocument().ActiveObject)
    selEx=model3D
    selEx = FreeCADGui.Selection.getSelectionEx()
    objs = [selobj.Object for selobj in selEx]
    if len(objs) == 1:
        s = objs[0].Shape
        name=objs[0].Label
        #say(name+" name \r\n")
        # boundBox
        delta=0.6
        boundBox_ = s.BoundBox
        boundBoxLX = boundBox_.XLength*(1+delta)
        boundBoxLY = boundBox_.YLength*(1+delta)
        #boundBoxLZ = boundBox_.ZLength
        boundBoxLZ = 1.58
        offX=boundBox_.XLength*(-delta)/2
        offY=boundBox_.YLength*(-delta)/2
        offZ=-0.01
        a = str(boundBox_)
        a,b = a.split('(')
        c = b.split(',')
        oripl_X = float(c[0])+offX
        oripl_Y = float(c[1])+offY
        #oripl_Z = float(c[2])+offZ
        oripl_Z = -boundBoxLZ+offZ

        #say(str(boundBox_)+"\r\n")
        #say("Rectangle : "+str(boundBox_.XLength)+" x "+str(boundBox_.YLength)+" x "+str(boundBox_.ZLength)+"\r\n")
        #say("_____________________"+"\r\n")
        #say("x: "+str(oripl_X)+" y: "+str(oripl_Y)+"z: "+str(oripl_Z)+"\r\n")

        obj=FreeCAD.ActiveDocument.addObject('Part::Feature',name)
        #obj.Shape=Part.makeBox(boundBox_.XLength, boundBox_.YLength, boundBox_.ZLength, FreeCAD.Vector(oripl_X,oripl_Y,oripl_Z), FreeCAD.Vector(0,0,01))
        #obj.Shape=Part.makeBox(boundBoxLX, boundBoxLY, boundBoxLZ, FreeCAD.Vector(oripl_X,oripl_Y,oripl_Z), FreeCAD.Vector(0,0,01))
        obj.Shape=Part.makeBox(boundBoxLX, boundBoxLY, boundBoxLZ, FreeCAD.Vector(oripl_X,oripl_Y,oripl_Z), FreeCAD.Vector(0,0,01))

        #obj.translate(offX,offY,0)
        # Part.show(cube)
        #say("cube name "+ obj.Name+'\r\n')
        ### FreeCAD.ActiveDocument.recompute()
    else:
        say("Select a single part object !\n")
    #end bbox macro

    name=obj.Name
    #say("bbox name "+name+"\r\n")
    del objs
    return name

###
def rotateObj(mainObj, rot):
    return mainObj.rotate(FreeCAD.Vector(rot[0], rot[1], 0), FreeCAD.Vector(0, 0, 1), rot[2])
###
def rotateObjs(listObjs, rot):
    #listObjs.rotate(FreeCAD.Vector(rot[0], rot[1], 0), FreeCAD.Vector(0, 0, 1), rot[2])
    Draft.rotate(listObjs,rot[2],FreeCAD.Vector(rot[0],rot[1],0.0),axis=FreeCAD.Vector(0.0,0.0,1.0),copy=False)
###
def changeSide(self, mainObj, X1, Y1, top):
    if top == 0:  #to bot side
        mainObj.rotate(FreeCAD.Vector(X1, Y1, 0), FreeCAD.Vector(0, 1, 0), 180)
###
def arcMidPoint(prev_vertex, vertex, angle):
    if len(prev_vertex) == 3:
        [x1, y1, z1] = prev_vertex
    else:
        [x1, y1] = prev_vertex

    if len(vertex) == 3:
        [x2, y2, z2] = vertex
    else:
        [x2, y2] = vertex

    angle = radians(angle / 2)
    basic_angle = atan2(y2 - y1, x2 - x1) - pi / 2
    shift = (1 - cos(angle)) * hypot(y2 - y1, x2 - x1) / 2 / sin(angle)
    midpoint = [(x2 + x1) / 2 + shift * cos(basic_angle), (y2 + y1) / 2 + shift * sin(basic_angle)]

    return midpoint

###

def sinus(angle):
    return float("%4.10f" % sin(radians(angle)))

def cosinus(angle):
    return float("%4.10f" % cos(radians(angle)))

def arcCenter(x1, y1, x2, y2, x3, y3):
    Xs = 0.5 * (x2 * x2 * y3 + y2 * y2 * y3 - x1 * x1 * y3 + x1 * x1 * y2 - y1 * y1 * y3 + y1 * y1 * y2 + y1 * x3 * x3 + y1 * y3 * y3 - y1 * x2 * x2 - y1 * y2 * y2 - y2 * x3 * x3 - y2 * y3 * y3) / (y1 * x3 - y1 * x2 - y2 * x3 - y3 * x1 + y3 * x2 + y2 * x1)
    Ys = 0.5 * (-x1 * x3 * x3 - x1 * y3 * y3 + x1 * x2 * x2 + x1 * y2 * y2 + x2 * x3 * x3 + x2 * y3 * y3 - x2 * x2 * x3 - y2 * y2 * x3 + x1 * x1 * x3 - x1 * x1 * x2 + y1 * y1 * x3 - y1 * y1 * x2) / (y1 * x3 - y1 * x2 - y2 * x3 - y3 * x1 + y3 * x2 + y2 * x1)

    return [Xs, Ys]

def shiftPointOnLine(x1, y1, x2, y2, distance):
    if x2 - x1 == 0:  # vertical line
        x_T1 = x1
        y_T1 = y1 - distance
    else:
        a = (y2 - y1) / (x2 - x1)
        if a == 0:  # horizontal line
            x_T1 = x1 - distance
            y_T1 = y1
        else:
            alfa = atan(a)
            #alfa = tan(a)

            x_T1 = x1 - distance * cos(alfa)
            y_T1 = y1 - distance * sin(alfa)

    return [x_T1, y_T1]

###
def getLine(layer, content, oType):
    data = []
    source = ''.join(content)
    #
    #data1 = re.findall(r'\({1}\s+\(start\s+([0-9\.-]*?)\s+([0-9\.-]*?)\)\s+\(end\s+([0-9\.-]*?)\s+([0-9\.-]*?)\)(\s+\(angle\s+[0-9\.-]*?\)\s+|\s+)\(layer\s+{0}\)\s+\(width\s+([0-9\.]*?)\)\)'.format(layer, oType), source, re.MULTILINE|re.DOTALL)
    data1 = re.findall(r'\({1}\s+\(start\s+([0-9\.-]*?)\s+([0-9\.-]*?)\)\s+\(end\s+([0-9\.-]*?)\s+([0-9\.-]*?)\)(\s+\(angle\s+[0-9\.-]*?\)\s+|\s+)\(layer\s+{0}\)\s+\(width\s+([0-9\.]*?)\)'.format(layer, oType), source, re.MULTILINE|re.DOTALL)
    #say(data1)
    for i in data1:
        x1 = float(i[0])
        y1 = float(i[1]) * (-1)
        x2 = float(i[2])
        y2 = float(i[3]) * (-1)
        width = float(i[5])

        data.append([x1, y1, x2, y2, width])
    #
    return data

def getCircle(layer, content, oType):
    data = []
    #
    source = ''.join(content)
    #data1 = re.findall(r'\({1}\s+\(center\s+([0-9\.-]*?)\s+([0-9\.-]*?)\)\s+\(end\s+([0-9\.-]*?)\s+([0-9\.-]*?)\)\s+\(layer\s+{0}\)(\s+\(width\s+([0-9\.]*?)\)|)\)'.format(layer, oType), source, re.MULTILINE|re.DOTALL)
    data1 = re.findall(r'\({1}\s+\(center\s+([0-9\.-]*?)\s+([0-9\.-]*?)\)\s+\(end\s+([0-9\.-]*?)\s+([0-9\.-]*?)\)\s+\(layer\s+{0}\)(\s+\(width\s+([0-9\.]*?)\)|)'.format(layer, oType), source, re.MULTILINE|re.DOTALL)
    #say(source)
    #say(data1)
    for i in data1:
        xs = float(i[0])
        ys = float(i[1]) * (-1)
        x1 = float(i[2])
        y1 = float(i[3]) * (-1)

        radius = sqrt((xs - x1) ** 2 + (ys - y1) ** 2)

        if i[5] == '':
            width = 0.01
        else:
            width = float(i[5])

        data.append([xs, ys, radius, width])
    #
    #say(data)
    return data
###
def rotPoint(point, ref, angle):
    sinKAT = self.sinus(angle)
    cosKAT = self.cosinus(angle)

    x1R = (point[0] * cosKAT) - (point[1] * sinKAT) + ref[0]
    y1R = (point[0] * sinKAT) + (point[1] * cosKAT) + ref[1]
    return [x1R, y1R]

###
def rotPoint2(point, ref, angle):
    sinKAT = sinus(angle)
    cosKAT = cosinus(angle)
    x1R = ((point[0] - ref[0]) * cosKAT) - sinKAT * (point[1] - ref[1]) + ref[0]
    y1R = ((point[0] - ref[0]) * sinKAT) + cosKAT * (point[1] - ref[1]) + ref[1]
    return [x1R, y1R]
###
def getArc(layer, content, oType):
    data = []
    #
    source = ''.join(content)
    #data1 = re.findall(r'\({1}\s+\(start\s+([0-9\.-]*?)\s+([0-9\.-]*?)\)\s+\(end\s+([0-9\.-]*?)\s+([0-9\.-]*?)\)\s+\(angle\s+([0-9\.-]*?)\)\s+\(layer\s+{0}\)(\s+\(width\s+([0-9\.]*?)\)|)\)'.format(layer, oType), source, re.MULTILINE|re.DOTALL)
    data1 = re.findall(r'\({1}\s+\(start\s+([0-9\.-]*?)\s+([0-9\.-]*?)\)\s+\(end\s+([0-9\.-]*?)\s+([0-9\.-]*?)\)\s+\(angle\s+([0-9\.-]*?)\)\s+\(layer\s+{0}\)(\s+\(width\s+([0-9\.]*?)|)\)'.format(layer, oType), source, re.MULTILINE|re.DOTALL)
    for i in data1:
        xs = float(i[0])
        ys = float(i[1])
        x1 = float(i[2])
        y1 = float(i[3])
        curve = float(i[4])
        if i[6].strip() != '':
            width = float(i[6])
        else:
            width = 0

        [x2, y2] = rotPoint2([x1, y1], [xs, ys], curve)

        data.append([x1, y1 * (-1), x2, y2 * (-1), curve, width])
    #
    return data

def getModName(source):
    #say("here test0")
    #for x in source:
    #    x.encode('utf-8')
    #    say(x+"\r\n")

    #say("here test1")
    #model = ''.join(u)
    model = ''.join(source)
    #say("here test2")
    model_name = re.search(r'\(module\s+(.+?)\(layer', model, re.MULTILINE|re.DOTALL).groups(0)[0]

    return model_name
###
def getwrlData(source):
    model = ''.join(source)
    wrl_pos=['0', '0', '0']
    if re.search(r'\(at\s+\(xyz+\s(.+?)\)', model, re.MULTILINE|re.DOTALL) is not None:
        pos_vrml = re.search(r'\(at\s+\(xyz+\s(.+?)\)', model, re.MULTILINE|re.DOTALL).groups(0)[0]
        #pos_vrml=pos_vrml[5:]
        wrl_pos=pos_vrml.split(" ")
        xp_vrml=wrl_pos[0]
        #say('alive')
        yp_vrml=wrl_pos[1]
        zp_vrml=wrl_pos[2]
        #say(wrl_pos);say('\n')
        #wrl_pos=(xp_vrml,yp_vrml,zp_vrml)
    #say(wrl_pos);say('\n')
    #    
    scale_vrml=['1', '1', '1']
    if re.search(r'\(scale\s+(.+?)\)', model, re.MULTILINE|re.DOTALL) is not None:
        sc_vrml = re.search(r'\(scale\s+(.+?)\)', model, re.MULTILINE|re.DOTALL).groups(0)[0]
        sc_vrml=sc_vrml[5:]
        scale_vrml=sc_vrml.split(" ")
        xsc_vrml=scale_vrml[0]
        ysc_vrml=scale_vrml[1]
        zsc_vrml=scale_vrml[2]        
        #say(scale_vrml);say('\n')
    #say(scale_vrml);say('\n')
    #
    rot_wrl=['0', '0', '0']
    zrot_vrml=''
    if re.search(r'\(rotate\s+(.+?)\)', model, re.MULTILINE|re.DOTALL) is not None:
        rot_vrml = re.search(r'\(rotate\s+(.+?)\)', model, re.MULTILINE|re.DOTALL).groups(0)[0]
        rot_vrml=rot_vrml[5:]
        rot_wrl=rot_vrml.split(" ")
        xrot_vrml=rot_wrl[0]
        yrot_vrml=rot_wrl[1]
        zrot_vrml=rot_wrl[2]
        #say(rot_wrl);say('\n')
    else:
        rotz_vrml=False
    #say("hereA")
    #if rotz_vrml:
    #    zrot_vrml=zrot_vrml
    #    #say("rotz:"+rotz+"\r\n")
    #    ##rotz=rotz[5:]
    #    #say("rotz:"+rotz+"\r\n")
    #    ##temp=rotz.split(" ")
    #    #say("rotz temp:"+temp[2]+"\r\n")
    #    ##rotz=temp[2]
    #    #say("rotate vrml: "+rotz+"\r\n")
    if zrot_vrml=='':
        zrot_vrml=0.0
    else:
        zrot_vrml=float(zrot_vrml)
    rot=zrot_vrml  #adding vrml module z-rotation
    #say(rot_wrl);say('\n')
    return wrl_pos, scale_vrml, rot_wrl

def getwrlRot(source):
    model = ''.join(source)
    if re.search(r'\(rotate\s+(.+?)\)', model, re.MULTILINE|re.DOTALL) is not None:
        rotz_vrml = re.search(r'\(rotate\s+(.+?)\)', model, re.MULTILINE|re.DOTALL).groups(0)[0]
    else:
        rotz_vrml=False
    #say("hereA")
    rotz=''
    if rotz_vrml:
        rotz=rotz_vrml
        #say("rotz:"+rotz+"\r\n")
        rotz=rotz[5:]
        #say("rotz:"+rotz+"\r\n")
        temp=rotz.split(" ")
        #say("rotz temp:"+temp[2]+"\r\n")
        rotz=temp[2]
        #say("rotate vrml: "+rotz+"\r\n")
    if rotz=='':
        rotz=0.0
    else:
        rotz=float(rotz)
    rot=rotz  #adding vrml module z-rotation
    return rot

###
def getPadsList(content):
    pads = []
    #
    model = ''.join(content)
    #model_name = re.search(r'\(module\s+(.+?)\(layer', model, re.MULTILINE|re.DOTALL).groups(0)[0]
    #say(model_name+'\r\n')

    found = re.findall(r'\(pad .* ', model, re.MULTILINE|re.DOTALL)
    if len(found):
        found = found[0].strip().split('(pad')
        for j in found:
            if j != '':
                [x, y, rot] = re.search(r'\(at\s+([0-9\.-]*?)\s+([0-9\.-]*?)(\s+[0-9\.-]*?|)\)', j).groups()
                pType= re.search(r'^.*?\s+([a-zA-Z_]+?)\s+', j).groups(0)[0]  # pad type - SMD/thru_hole/connect
                pShape = re.search(r'^.+?\s+.+?\s+([a-zA-Z_]+?)\s+', j).groups(0)[0]  # pad shape - circle/rec/oval/trapezoid
                [dx, dy] = re.search(r'\(size\s+([0-9\.-]+?)\s+([0-9\.-]+?)\)', j).groups(0)  #
                layers = re.search(r'\(layers\s+(.+?)\)', j).groups(0)[0]  #
                data = re.search(r'\(drill(\s+oval\s+|\s+)(.*?)(\s+[-0-9\.]*?|)(\s+\(offset\s+(.*?)\s+(.*?)\)|)\)', j)
                data_off = re.search(r'\(offset\s+([0-9\.-]+?)\s+([0-9\.-]+?)\)', j)
                #
                x = float(x)
                y = float(y) * (-1)
                dx = float(dx)
                dy = float(dy)
                if rot == '':
                    rot = 0.0
                else:
                    rot = float(rot)

                if pType == 'smd' or data == None:
                    drill_x = 0.0
                    drill_y = 0.0
                    hType = None
                    if data_off == None:
                        [xOF, yOF] = [0.0, 0.0]
                    else:
                        data_off = data_off.groups()
                        if not data_off[0] or data_off[0].strip() == '':
                            xOF = 0.0
                        else:
                            xOF = float(data_off[0])

                        if not data_off[1] or data_off[1].strip() == '':
                            yOF = 0.0
                        else:
                            yOF = float(data_off[1])
                else:
                    data = data.groups()
                    hType = data[0]
                    if hType.strip() == '':
                        hType = 'circle'

                    drill_x = float(data[1]) #/ 2.0
                    if not data[2] or data[2].strip() == '':
                        drill_y=drill_x
                    else:
                        drill_y = float(data[2]) #/ 2.0
                    #drill_y=drill_x

                    if not data[4] or data[4].strip() == '':
                        xOF = 0.0
                    else:
                        xOF = float(data[4])

                    if not data[5] or data[5].strip() == '':
                        yOF = 0.0
                    else:
                        yOF = float(data[5])
                ##
                #say(data)
                pads.append({'x': x, 'y': y, 'rot': rot, 'padType': pType, 'padShape': pShape, 'rx': drill_x, 'ry': drill_y, 'dx': dx, 'dy': dy, 'holeType': hType, 'xOF': xOF, 'yOF': yOF, 'layers': layers})

    #say(pads)
    #
    return pads
###
def makePoint(self, x, y):
    wir = []
    wir.append(Part.Point(FreeCAD.Base.Vector(x, y, 0)))
    mainObj = Part.Shape(wir)
    return mainObj
###
def makeFace(mainObj):
    return Part.Face(mainObj)
###

def cutHole(mainObj, hole):
    if hole[2] > min_val:
        hole = [Part.Circle(FreeCAD.Vector(hole[0], hole[1]), FreeCAD.Vector(0, 0, 1), hole[2]).toShape()]
        hole = Part.Wire(hole)
        hole = Part.Face(hole)

        mainObj = mainObj.cut(hole)
    return mainObj
###
def cutObj(mainObj, hole):
    mainObj = mainObj.cut(hole)
    return mainObj
###
def createCircle(x, y, r, w=0):

    if w > min_val:
        mainObj = Part.Wire([Part.Circle(FreeCAD.Vector(x, y), FreeCAD.Vector(0, 0, 1), r + w / 2.).toShape()])
        mainObj = makeFace(mainObj)
        mainObj = cutHole(mainObj, [x, y, r - w / 2.])

        return mainObj
    else:
        mainObj = [Part.Circle(FreeCAD.Vector(x, y), FreeCAD.Vector(0, 0, 1), r).toShape()]

        return makeFace(Part.Wire(mainObj))

###
def createArc(p1, p2, curve, width=0.02, cap='round'):
    try:
        wir = []
        if width <= 0:
            width = 0.02
        width /= 2.
        [x3, y3] = arcMidPoint(p1, p2, curve)
        [xs, ys] = arcCenter(p1[0], p1[1], p2[0], p2[1], x3, y3)
        ##
        #a = (ys - p1[1]) / (xs - p1[0])
        [xT_1, yT_1] = shiftPointOnLine(p1[0], p1[1], xs, ys, width)
        [xT_4, yT_4] = shiftPointOnLine(p1[0], p1[1], xs, ys, -width)
        ###
        [xT_2, yT_2] = rotPoint2([xT_1, yT_1], [xs, ys], curve)
        [xT_5, yT_5] = rotPoint2([xT_4, yT_4], [xs, ys], curve)
        ########
        ########
        wir = []
        ## outer arc
        [xT_3, yT_3] = arcMidPoint([xT_1, yT_1], [xT_2, yT_2], curve)
        wir.append(Part.Arc(FreeCAD.Base.Vector(xT_1, yT_1, 0), FreeCAD.Base.Vector(xT_3, yT_3, 0), FreeCAD.Base.Vector(xT_2, yT_2, 0)))
        ## inner arc
        [xT_6, yT_6] = arcMidPoint([xT_4, yT_4], [xT_5, yT_5], curve)
        wir.append(Part.Arc(FreeCAD.Base.Vector(xT_4, yT_4, 0), FreeCAD.Base.Vector(xT_6, yT_6, 0), FreeCAD.Base.Vector(xT_5, yT_5, 0)))
        ##
        if cap == 'flat':
            wir.append(Part.Line(FreeCAD.Base.Vector(xT_1, yT_1, 0), FreeCAD.Base.Vector(xT_4, yT_4, 0)))
            wir.append(Part.Line(FreeCAD.Base.Vector(xT_2, yT_2, 0), FreeCAD.Base.Vector(xT_5, yT_5, 0)))
        else:
            #wir.append(Part.Line(FreeCAD.Base.Vector(xT_1, yT_1, 0), FreeCAD.Base.Vector(xT_4, yT_4, 0)))
            #wir.append(Part.Line(FreeCAD.Base.Vector(xT_2, yT_2, 0), FreeCAD.Base.Vector(xT_5, yT_5, 0)))
            #start
            if xs - p1[0] == 0:  # vertical line
                if curve > 0:
                    [xT_7, yT_7] = arcMidPoint([xT_1, yT_1], [xT_4, yT_4], 180)
                else:
                    [xT_7, yT_7] = arcMidPoint([xT_1, yT_1], [xT_4, yT_4], -180)
            else:
                a = (ys - p1[1]) / (xs - p1[0])

                if a == 0:  # horizontal line
                    if curve > 0:
                        [xT_7, yT_7] = arcMidPoint([xT_1, yT_1], [xT_4, yT_4], 180)
                    else:
                        [xT_7, yT_7] = arcMidPoint([xT_1, yT_1], [xT_4, yT_4], -180)
                    pass
                else:
                    #a = (ys - p1[1]) / (xs - p1[0])
                    if curve > 0:
                        if a > 0:
                            if xT_1 > xs:
                                [xT_7, yT_7] = arcMidPoint([xT_1, yT_1], [xT_4, yT_4], 180)
                            else:
                                [xT_7, yT_7] = arcMidPoint([xT_1, yT_1], [xT_4, yT_4], -180)
                        else:
                            if xT_1 > xs:
                                [xT_7, yT_7] = arcMidPoint([xT_1, yT_1], [xT_4, yT_4], 180)
                            else:
                                [xT_7, yT_7] = arcMidPoint([xT_1, yT_1], [xT_4, yT_4], -180)
                    else:
                        if a > 0:
                            if xT_1 > xs:
                                [xT_7, yT_7] = arcMidPoint([xT_1, yT_1], [xT_4, yT_4], -180)
                            else:
                                [xT_7, yT_7] = arcMidPoint([xT_1, yT_1], [xT_4, yT_4], 180)
                        else:
                            if xT_1 > xs:
                                [xT_7, yT_7] = arcMidPoint([xT_1, yT_1], [xT_4, yT_4], -180)
                            else:
                                [xT_7, yT_7] = arcMidPoint([xT_1, yT_1], [xT_4, yT_4], 180)

            wir.append(Part.Arc(FreeCAD.Base.Vector(xT_1, yT_1, 0), FreeCAD.Base.Vector(xT_7, yT_7, 0), FreeCAD.Base.Vector(xT_4, yT_4, 0)))

            #end
            #b = (ys - p2[1]) / (xs - p2[0])

            if curve > 0:
                if xT_2 > xs:
                    if xT_2 >= xT_5:
                        [xT_8, yT_8] = arcMidPoint([xT_2, yT_2], [xT_5, yT_5], 180)
                    else:
                        [xT_8, yT_8] = arcMidPoint([xT_2, yT_2], [xT_5, yT_5], -180)
                else:
                    if xT_2 >= xT_5:
                        [xT_8, yT_8] = arcMidPoint([xT_2, yT_2], [xT_5, yT_5], -180)
                    else:
                        [xT_8, yT_8] = arcMidPoint([xT_2, yT_2], [xT_5, yT_5], 180)
            else:
                if xT_2 > xs:
                    if xT_2 >= xT_5:
                        [xT_8, yT_8] = arcMidPoint([xT_2, yT_2], [xT_5, yT_5], -180)
                    else:
                        [xT_8, yT_8] = arcMidPoint([xT_2, yT_2], [xT_5, yT_5], 180)
                else:
                    if xT_2 >= xT_5:
                        [xT_8, yT_8] = arcMidPoint([xT_2, yT_2], [xT_5, yT_5], 180)
                    else:
                        [xT_8, yT_8] = arcMidPoint([xT_2, yT_2], [xT_5, yT_5], -180)

            wir.append(Part.Arc(FreeCAD.Base.Vector(xT_2, yT_2, 0), FreeCAD.Base.Vector(xT_8, yT_8, 0), FreeCAD.Base.Vector(xT_5, yT_5, 0)))

        ####
        mainObj = Part.Shape(wir)
        mainObj = Part.Wire(mainObj.Edges)
        return makeFace(mainObj)

    except Exception, e:
        FreeCAD.Console.PrintWarning(u"{0}\n".format(e))

###

###
def addArc_3(p1, p2, curve, width=0, cap='round'):
    return createArc(p1, p2, curve, width, cap)

###
def addLine_2(x1, y1, x2, y2, width=0.01):
    if x1 == x2 and y1 == y2:
        return makePoint(x1, y1)
    else:
        return createLine(x1, y1, x2, y2, width)
###
def addCircle_2(x, y, r, w=0):
    return createCircle(x, y, r, w)
###
def createLine(x1, y1, x2, y2, width=0.01):
    #say("create line routine \r\n")
    z_silk_offset=0.01
    if width <= 0:
        width = 0.01

    # line length
    length = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    # angle of inclination
    if x1 > x2:
        iang = degrees(atan2(y1 - y2, x1 - x2)) - 90
    else:
        iang = degrees(atan2(y2 - y1, x2 - x1)) - 90
    if x1 > x2:
        iang += 180

    # radius of curvature at both ends of the path
    r = width / 2.

    # create wire
    wir = []
    wir.append(Part.Line(FreeCAD.Base.Vector(0 - r, 0, 0), FreeCAD.Base.Vector(0 - r, length, 0)))
    wir.append(Part.Line(FreeCAD.Base.Vector(0 + r, 0, 0), FreeCAD.Base.Vector(0 + r, length, 0)))

    p1 = [0 - r, 0]
    p2 = [0, 0 - r]
    p3 = [0 + r, 0]
    wir.append(Part.Arc(FreeCAD.Base.Vector(p1[0], p1[1], 0), FreeCAD.Base.Vector(p2[0], p2[1], 0), FreeCAD.Base.Vector(p3[0], p3[1], 0)))

    p1 = [0 - r, length]
    p2 = [0, length + r]
    p3 = [0 + r, length]
    wir.append(Part.Arc(FreeCAD.Base.Vector(p1[0], p1[1], 0), FreeCAD.Base.Vector(p2[0], p2[1], 0), FreeCAD.Base.Vector(p3[0], p3[1], 0)))

    mainObj = Part.Shape(wir)
    mainObj = Part.Wire(mainObj.Edges)
    mainObj = Part.Face(mainObj)

    pos_1 = FreeCAD.Base.Vector(x1, y1, z_silk_offset) #z offset Front Silk 0.1
    center = FreeCAD.Base.Vector(0, 0, 0)
    rot = FreeCAD.Rotation(FreeCAD.Vector(0, 0, 1), iang)
    mainObj.Placement = FreeCAD.Base.Placement(pos_1, rot, center)

    return mainObj
###
def addPadLong2(x, y, dx, dy, perc, typ, z_off):
              #pad center x,y pad dimension dx,dy, type, z offset
    dx=dx/2.
    dy=dy/2.
    curve = 90.
    if typ == 0:  # %
        if perc > 100.:
            perc == 100.
        if dx > dy:
            e = dy * perc / 100.
        else:
            e = dx * perc / 100.
    else:  # mm
        e = perc
    p1 = [x - dx + e, y - dy, z_off]
    p2 = [x + dx - e, y - dy, z_off]
    p3 = [x + dx, y - dy + e, z_off]
    p4 = [x + dx, y + dy - e, z_off]
    p5 = [x + dx - e, y + dy, z_off]
    p6 = [x - dx + e, y + dy, z_off]
    p7 = [x - dx, y + dy - e, z_off]
    p8 = [x - dx, y - dy + e, z_off]
    #
    points = []
    if p1 != p2:
        points.append(Part.Line(FreeCAD.Base.Vector(p1[0], p1[1], z_off), FreeCAD.Base.Vector(p2[0], p2[1], z_off)))
    if p2 != p3:
        p9 = arcMidPoint(p2, p3, curve)
        points.append(Part.Arc(FreeCAD.Base.Vector(p2[0], p2[1], z_off), FreeCAD.Base.Vector(p9[0], p9[1], z_off), FreeCAD.Base.Vector(p3[0], p3[1], z_off)))
    if p3 != p4:
        points.append(Part.Line(FreeCAD.Base.Vector(p3[0], p3[1], z_off), FreeCAD.Base.Vector(p4[0], p4[1], z_off)))
    if p4 != p5:
        p10 = arcMidPoint(p4, p5, curve)
        points.append(Part.Arc(FreeCAD.Base.Vector(p4[0], p4[1], z_off), FreeCAD.Base.Vector(p10[0], p10[1], z_off), FreeCAD.Base.Vector(p5[0], p5[1], z_off)))
    if p5 != p6:
        points.append(Part.Line(FreeCAD.Base.Vector(p5[0], p5[1], z_off), FreeCAD.Base.Vector(p6[0], p6[1], z_off)))
    if p6 != p7:
        p11 = arcMidPoint(p6, p7, curve)
        points.append(Part.Arc(FreeCAD.Base.Vector(p6[0], p6[1], z_off), FreeCAD.Base.Vector(p11[0], p11[1], z_off), FreeCAD.Base.Vector(p7[0], p7[1], z_off)))
    if p7 != p8:
        points.append(Part.Line(FreeCAD.Base.Vector(p7[0], p7[1], z_off), FreeCAD.Base.Vector(p8[0], p8[1], z_off)))
    if p8 != p1:
        p12 = arcMidPoint(p8, p1, curve)
        points.append(Part.Arc(FreeCAD.Base.Vector(p8[0], p8[1], z_off), FreeCAD.Base.Vector(p12[0], p12[1], z_off), FreeCAD.Base.Vector(p1[0], p1[1], z_off)))

    obj = Part.Shape(points)
    obj = Part.Wire(obj.Edges)

    #if hole==0:
    #    obj = makeFace(obj)
    ###return makeFace(obj)
    ##list=[]
    ##list.append(obj)
    ##obj1=Part.makeCompound(list)
    ##return obj1
    return obj

###
def addPadLong(x, y, dx, dy, perc, typ, z_off):
              # center x,y dimension x,y, type, z offset
    dx=dx/2
    dy=dy/2
    curve = 90.
    if typ == 0:  # %
        if perc > 100.:
            perc == 100.
        if dx > dy:
            e = dy * perc / 100.
        else:
            e = dx * perc / 100.
    else:  # mm
        e = perc
    p1 = [x - dx + e, y - dy, z_off]
    p2 = [x + dx - e, y - dy, z_off]
    p3 = [x + dx, y - dy + e, z_off]
    p4 = [x + dx, y + dy - e, z_off]
    p5 = [x + dx - e, y + dy, z_off]
    p6 = [x - dx + e, y + dy, z_off]
    p7 = [x - dx, y + dy - e, z_off]
    p8 = [x - dx, y - dy + e, z_off]
    #
    points = []
    if p1 != p2:
        points.append(Part.Line(FreeCAD.Base.Vector(p1[0], p1[1], z_off), FreeCAD.Base.Vector(p2[0], p2[1], z_off)))
    if p2 != p3:
        p9 = arcMidPoint(p2, p3, curve)
        points.append(Part.Arc(FreeCAD.Base.Vector(p2[0], p2[1], z_off), FreeCAD.Base.Vector(p9[0], p9[1], z_off), FreeCAD.Base.Vector(p3[0], p3[1], z_off)))
    if p3 != p4:
        points.append(Part.Line(FreeCAD.Base.Vector(p3[0], p3[1], z_off), FreeCAD.Base.Vector(p4[0], p4[1], z_off)))
    if p4 != p5:
        p10 = arcMidPoint(p4, p5, curve)
        points.append(Part.Arc(FreeCAD.Base.Vector(p4[0], p4[1], z_off), FreeCAD.Base.Vector(p10[0], p10[1], z_off), FreeCAD.Base.Vector(p5[0], p5[1], z_off)))
    if p5 != p6:
        points.append(Part.Line(FreeCAD.Base.Vector(p5[0], p5[1], z_off), FreeCAD.Base.Vector(p6[0], p6[1], z_off)))
    if p6 != p7:
        p11 = arcMidPoint(p6, p7, curve)
        points.append(Part.Arc(FreeCAD.Base.Vector(p6[0], p6[1], z_off), FreeCAD.Base.Vector(p11[0], p11[1], z_off), FreeCAD.Base.Vector(p7[0], p7[1], z_off)))
    if p7 != p8:
        points.append(Part.Line(FreeCAD.Base.Vector(p7[0], p7[1], z_off), FreeCAD.Base.Vector(p8[0], p8[1], z_off)))
    if p8 != p1:
        p12 = arcMidPoint(p8, p1, curve)
        points.append(Part.Arc(FreeCAD.Base.Vector(p8[0], p8[1], z_off), FreeCAD.Base.Vector(p12[0], p12[1], z_off), FreeCAD.Base.Vector(p1[0], p1[1], z_off)))

    obj = Part.Shape(points)
    obj = Part.Wire(obj.Edges)

    obj = makeFace(obj)
    #return makeFace(obj)
    list=[]
    list.append(obj)
    obj1=Part.makeCompound(list)
    return obj1
###
def cutHole2(mainObj, holep, holed):
    if holed[1] > min_val:
        #hole = [Part.Circle(FreeCAD.Vector(hole[0], hole[1]), FreeCAD.Vector(0, 0, 1), hole[2]).toShape()]
        z_off=0

        hole = addPadLong(holep[0], holep[1], holed[0], holed[1], 100, 0, z_off)
        mainObj = mainObj.cut(hole)
        Part.show(mainObj)
    return mainObj
###
###
def createPad2(x,y,sx,sy,dcx,dcy,dx,dy,type,layer):
    ##pad pos x,y; pad size x,y; drillcenter x,y; drill size x,y, layer
    z_offset=0
    remove=1
    if type=="oval":
        perc=100
        tp=0
    else:
        perc=0
        tp=0
    if layer=="top":
        thick=-0.01
        z_offset=0
    else:
        thick=0.01
        z_offset=-1.6
    #say(str(x)+"x "+str(y)+"y "+str(sx)+"sx "+str(sy)+"sy "+"\r\n")
    #say(str(dcx)+"dcx "+str(dcy)+"dcy "+str(dx)+"dx "+str(dy)+"dy "+"\r\n")
    mypad=addPadLong2(x, y, sx, sy, perc, tp, z_offset)
    Part.show(mypad)
    FreeCAD.ActiveDocument.ActiveObject.Label="mypad"
    pad_name=FreeCAD.ActiveDocument.ActiveObject.Name
    if dx!=0:
        perc=100 #drill always oval
        tp=0
        mydrill=addPadLong2(dcx, dcy, dx, dy, perc, tp, 0)
        Part.show(mydrill)
        FreeCAD.ActiveDocument.ActiveObject.Label="mydrill"
        drill_name=FreeCAD.ActiveDocument.ActiveObject.Name
        myannular=addPadLong2(dcx, dcy, dx+0.01, dy+0.01, perc, tp, 0)
        Part.show(myannular)
        FreeCAD.ActiveDocument.ActiveObject.Label="myannular"
        ann_name=FreeCAD.ActiveDocument.ActiveObject.Name
        #myhole=addPadLong2(dcx, dcy, dx, dy, perc, tp, z_offset)
        #Part.show(myhole)
        #FreeCAD.ActiveDocument.ActiveObject.Label="myhole"
        wire = [mypad,mydrill]
        wire2 = [myannular,mydrill]
        face = Part.Face(wire)
        face2 = Part.Face(mydrill)
        face3 = Part.Face(wire2)
        extr = face.extrude(FreeCAD.Vector(0,0,-.01))
        Part.show(extr)
        FreeCAD.ActiveDocument.ActiveObject.Label="drilled_pad"
        extr2 = face2.extrude(FreeCAD.Vector(0,0,-1.58))
        Part.show(extr2)
        FreeCAD.ActiveDocument.ActiveObject.Label="hole"
        extr3 = face3.extrude(FreeCAD.Vector(0,0,-1.58))
        Part.show(extr3)
        FreeCAD.ActiveDocument.ActiveObject.Label="annular"
        FreeCAD.ActiveDocument.removeObject(pad_name)
        FreeCAD.ActiveDocument.removeObject(drill_name)
        FreeCAD.ActiveDocument.removeObject(ann_name)
        FreeCAD.ActiveDocument.recompute()
    else:
        face = Part.Face(mypad)
        extr = face.extrude(FreeCAD.Vector(0,0,-.01))
        Part.show(extr)
        FreeCAD.ActiveDocument.ActiveObject.Label="smd_pad"
        FreeCAD.ActiveDocument.removeObject(pad_name)
        FreeCAD.ActiveDocument.recompute()
    return extr
###
def createPad3(x,y,sx,sy,dcx,dcy,dx,dy,type,layer):
    ##pad pos x,y; pad size x,y; drillcenter x,y; drill size x,y, type, layer
    z_offset=0
    remove=1
    if type=="oval":
        perc=100
        tp=0
    else:
        perc=0
        tp=0
    if layer=="top":
        thick=-0.01
        z_offset=0
    else:
        thick=0.01
        z_offset=-1.6
    #say(str(x)+"x "+str(y)+"y "+str(sx)+"sx "+str(sy)+"sy "+"\r\n")
    #say(str(dcx)+"dcx "+str(dcy)+"dcy "+str(dx)+"dx "+str(dy)+"dy "+"\r\n")
    mypad=addPadLong2(x, y, sx, sy, perc, tp, z_offset)
    Part.show(mypad)
    FreeCAD.ActiveDocument.ActiveObject.Label="mypad"
    pad_name=FreeCAD.ActiveDocument.ActiveObject.Name
    if dx!=0:
        perc=100 #drill always oval
        tp=0
        mydrill=addPadLong2(dcx, dcy, dx, dy, perc, tp, z_offset)
        if test_flag_pads==True:
            Part.show(mydrill)
            FreeCAD.ActiveDocument.ActiveObject.Label="mydrill"
            drill_name=FreeCAD.ActiveDocument.ActiveObject.Name
        myannular=addPadLong2(dcx, dcy, dx+0.01, dy+0.01, perc, tp, z_offset)
        if test_flag_pads==True:
            Part.show(myannular)
            FreeCAD.ActiveDocument.ActiveObject.Label="myannular"
            ann_name=FreeCAD.ActiveDocument.ActiveObject.Name
        myhole=addPadLong2(dcx, dcy, dx, dy, perc, tp, z_offset)
        if test_flag_pads==True:
            Part.show(myhole)
            FreeCAD.ActiveDocument.ActiveObject.Label="myhole"
        wire = [mypad,mydrill]
        face = Part.Face(wire)
        extr = face.extrude(FreeCAD.Vector(0,0,thick))
        if test_flag_pads==True:
            Part.show(extr)
            FreeCAD.ActiveDocument.ActiveObject.Label="drilled_pad"
        FreeCAD.ActiveDocument.removeObject(pad_name)
        FreeCAD.ActiveDocument.recompute()
    else:
        face = Part.Face(mypad)
        extr = face.extrude(FreeCAD.Vector(0,0,thick))
        #Part.show(extr)
        #FreeCAD.ActiveDocument.ActiveObject.Label="smd_pad"
        FreeCAD.ActiveDocument.removeObject(pad_name)
        FreeCAD.ActiveDocument.recompute()
    return extr
###
def createPad(x,y,sx,sy,dcx,dcy,dx,dy,type,layer):
    ##pad pos x,y; pad size x,y; drillcenter x,y; drill size x,y
    z_offset=0
    remove=1
    if type=="oval":
        perc=100
        tp=0
    else:
        perc=0
        tp=0
    if layer=="top":
        thick=-0.01
        z_offset=0
    else:
        thick=0.01
        z_offset=-1.6
    #say(str(x)+"x "+str(y)+"y "+str(sx)+"sx "+str(sy)+"sy "+"\r\n")
    #say(str(dcx)+"dcx "+str(dcy)+"dcy "+str(dx)+"dx "+str(dy)+"dy "+"\r\n")
    mypad=addPadLong(x, y, sx, sy, perc, tp, z_offset)
    Part.show(mypad)
    FreeCAD.ActiveDocument.ActiveObject.Label="mypad"
    pad_name=FreeCAD.ActiveDocument.ActiveObject.Name
    FreeCAD.ActiveDocument.addObject("Part::Extrusion","Extrude_pad")
    extrude_name=FreeCAD.ActiveDocument.ActiveObject.Name
    FreeCAD.ActiveDocument.Extrude_pad.Base = FreeCAD.ActiveDocument.getObject(pad_name)
    FreeCAD.ActiveDocument.Extrude_pad.Dir = (0,0,thick)
    FreeCAD.ActiveDocument.Extrude_pad.Solid = (True)
    FreeCAD.ActiveDocument.Extrude_pad.TaperAngle = (0)
    FreeCADGui.ActiveDocument.getObject(pad_name).Visibility = False
    FreeCAD.ActiveDocument.Extrude_pad.Label = 'mypad_solid'
    extrude_pad_name=FreeCAD.ActiveDocument.ActiveObject.Name
    #FreeCAD.ActiveDocument.recompute()
    if dx!=0:
        perc=100 #drill always oval
        mydrill=addPadLong(dcx, dcy, dx, dy, perc, tp, z_offset)
        Part.show(mydrill)
        FreeCAD.ActiveDocument.ActiveObject.Label="mydrill"
        drill_name=FreeCAD.ActiveDocument.ActiveObject.Name
        FreeCAD.ActiveDocument.addObject("Part::Extrusion","Extrude_d")
        extrude_d_name=FreeCAD.ActiveDocument.ActiveObject.Name
        FreeCAD.ActiveDocument.Extrude_d.Base = FreeCAD.ActiveDocument.getObject(drill_name)
        FreeCAD.ActiveDocument.Extrude_d.Dir = (0,0,thick)
        FreeCAD.ActiveDocument.Extrude_d.Solid = (True)
        FreeCAD.ActiveDocument.Extrude_d.TaperAngle = (0)
        FreeCADGui.ActiveDocument.getObject(drill_name).Visibility = False
        FreeCAD.ActiveDocument.Extrude_d.Label = 'mydrill_solid'
        extrude_drill_name=FreeCAD.ActiveDocument.ActiveObject.Name
        #FreeCAD.ActiveDocument.recompute()

        FreeCAD.activeDocument().addObject("Part::Cut","myCut")
        cut_name=FreeCAD.ActiveDocument.ActiveObject.Name
        FreeCAD.activeDocument().getObject(cut_name).Base = FreeCAD.activeDocument().Extrude_pad
        FreeCAD.activeDocument().getObject(cut_name).Tool = FreeCAD.activeDocument().Extrude_d
        FreeCADGui.activeDocument().Extrude_pad.Visibility=False
        FreeCADGui.activeDocument().Extrude_d.Visibility=False
        #FreeCADGui.ActiveDocument.getObject(cut_name).ShapeColor=FreeCADGui.ActiveDocument.Extrude.ShapeColor
        FreeCADGui.ActiveDocument.ActiveObject.ShapeColor =  (0.81,0.71,0.23) #(0.85,0.53,0.10)
        FreeCADGui.ActiveDocument.ActiveObject.DisplayMode=FreeCADGui.ActiveDocument.Extrude_pad.DisplayMode
        FreeCAD.ActiveDocument.recompute()
        pad_d_name="TH_Pad"
        FreeCAD.ActiveDocument.addObject('Part::Feature',pad_d_name).Shape=FreeCAD.ActiveDocument.ActiveObject.Shape
        FreeCADGui.ActiveDocument.ActiveObject.ShapeColor =  (0.81,0.71,0.23) #(0.85,0.53,0.10)
        myObj=FreeCAD.ActiveDocument.getObject(pad_d_name)
        if remove==1:
            FreeCAD.ActiveDocument.removeObject(cut_name)
            FreeCAD.ActiveDocument.removeObject(extrude_pad_name)
            FreeCAD.ActiveDocument.removeObject(pad_name)
            FreeCAD.ActiveDocument.removeObject(drill_name)
            FreeCAD.ActiveDocument.removeObject(extrude_drill_name)
        FreeCAD.ActiveDocument.recompute()
    else:
        FreeCAD.ActiveDocument.recompute()
        pad_d_name="smdPad"
        FreeCAD.ActiveDocument.addObject('Part::Feature',pad_d_name).Shape=FreeCAD.ActiveDocument.ActiveObject.Shape
        myObj=FreeCAD.ActiveDocument.getObject(pad_d_name)
        FreeCADGui.ActiveDocument.ActiveObject.ShapeColor =  (0.81,0.71,0.23) #(0.85,0.53,0.10)
        FreeCAD.ActiveDocument.removeObject(extrude_pad_name)
        FreeCAD.ActiveDocument.removeObject(pad_name)
        FreeCAD.ActiveDocument.recompute()
    return myObj
###

def createHole(x,y,dx,dy,type):
    if type=="oval":
        perc=100
        tp=0
    else:
        perc=0
        tp=0
    mydrill=addPadLong(x, y, dx, dy, perc, tp, 0)
    Part.show(mydrill)
    FreeCAD.ActiveDocument.ActiveObject.Label="mydrill"
    drill_name=FreeCAD.ActiveDocument.ActiveObject.Name
    FreeCAD.ActiveDocument.addObject("Part::Extrusion","Extrude_d")
    FreeCAD.ActiveDocument.Extrude_d.Base = FreeCAD.ActiveDocument.getObject(drill_name)
    FreeCAD.ActiveDocument.Extrude_d.Dir = (0,0,-1.6)
    FreeCAD.ActiveDocument.Extrude_d.Solid = (True)
    FreeCAD.ActiveDocument.Extrude_d.TaperAngle = (0)
    FreeCADGui.ActiveDocument.getObject(drill_name).Visibility = False
    FreeCAD.ActiveDocument.Extrude_d.Label = 'mydrill_hole'
    extrude_hole_name=FreeCAD.ActiveDocument.ActiveObject.Name
    FreeCAD.ActiveDocument.recompute()

    hole_name="hole"
    FreeCAD.ActiveDocument.addObject('Part::Feature',hole_name).Shape=FreeCAD.ActiveDocument.getObject(extrude_hole_name).Shape
    FreeCADGui.ActiveDocument.ActiveObject.ShapeColor = (0.67,1.00,0.50)
    FreeCADGui.ActiveDocument.ActiveObject.Transparency = 70
    myObj=FreeCADGui.ActiveDocument.ActiveObject
    FreeCAD.ActiveDocument.removeObject(drill_name)
    FreeCAD.ActiveDocument.removeObject(extrude_hole_name)
    FreeCAD.ActiveDocument.recompute()

    return myObj

###
def createHole2(x,y,dx,dy,type):
    if type=="oval":
        perc=100
        tp=0
    else:
        perc=0
        tp=0
    #mydrill=addPadLong(x, y, dx, dy, perc, tp, -0.01)
    mydrill=addPadLong(x, y, dx, dy, perc, tp, .01)
    #Part.show(mydrill)
    #hole = mydrill.extrude(FreeCAD.Base.Vector(0, 0, -1.58))
    hole = mydrill.extrude(FreeCAD.Base.Vector(0, 0, -1.61))
    holeModel=[]
    holeModel.append(hole)
    holeModel = Part.makeCompound(holeModel)
    #say("hereHole")
    #FreeCAD.ActiveDocument.recompute()
    return holeModel

###
def createHole3(x,y,dx,dy,type,height):
    if type=="oval":
        perc=100
        tp=0
    else:
        perc=0
        tp=0
    #mydrill=addPadLong(x, y, dx, dy, perc, tp, -0.01)
    mydrill=addPadLong(x, y, dx, dy, perc, tp, 0.1)
    #Part.show(mydrill)
    #hole = mydrill.extrude(FreeCAD.Base.Vector(0, 0, -1.58))
    hole = mydrill.extrude(FreeCAD.Base.Vector(0, 0, -(height+0.2)))
    holeModel=[]
    holeModel.append(hole)
    holeModel = Part.makeCompound(holeModel)
    #say("hereHole")
    #FreeCAD.ActiveDocument.recompute()

    return holeModel

###
###
def createHole4(x,y,dx,dy,type):
    if type=="oval":
        perc=100
        tp=0
    else:
        perc=0
        tp=0
    #mydrill=addPadLong(x, y, dx, dy, perc, tp, -0.01)
    #mydrill=addPadLong(x, y, dx, dy, perc, tp, .01)
    mydrill=addPadLong2(x, y, dx, dy, perc, tp, 0)
    holeModel=[]
    #holeModel.append(hole)
    holeModel.append(mydrill)
    ##holeModel = Part.makeCompound(holeModel)
    holeModel = Part.Face(holeModel)
    #say("hereHole")
    #FreeCAD.ActiveDocument.recompute()
    return holeModel

###
def createTHPlate(x,y,dx,dy,type):
    if type=="oval":
        perc=100
        tp=0
    else:
        perc=0
        tp=0
    #mydrill=addPadLong(x, y, dx, dy, perc, tp, -0.01)
    mydrill=addPadLong2(x, y, dx, dy, perc, tp, -0.01)
    myannular=addPadLong2(x, y, dx+0.01, dy+0.01, perc, tp, -0.01)
    wire2 = [myannular,mydrill]
    face3 = Part.Face(wire2)
    THP = face3.extrude(FreeCAD.Vector(0,0,-1.58))
    #Part.show(extr3)
    #FreeCAD.ActiveDocument.ActiveObject.Label="annular"
    ##hole = mydrill.extrude(FreeCAD.Base.Vector(0, 0, -1.58))
    #THP = myannular.extrude(FreeCAD.Base.Vector(0, 0, -1.58))
    THPModel=[]
    THPModel.append(THP)
    THPModel = Part.makeCompound(THPModel)
    #say("hereHole")
    #FreeCAD.ActiveDocument.recompute()

    return THPModel

###
def routineDrawFootPrint(content,name):
    global rot_wrl
    #for item in content:
    #    say(item)

    #                      x1, y1, x2, y2, width
    say("FootPrint Loader "+name+"\n")
    footprint_name=getModName(content)
    rot_wrl=getwrlRot(content)
    posiz, scale, rot = getwrlData(content)
    #say(posiz);say(scale);say(rot);say('\n')
    error_mod=False
    if scale!=['1', '1', '1']:
        sayw('wrong scale!!! set scale to (1 1 1)\n')
        error_mod=True
    if posiz!=['0', '0', '0']:
        sayw('wrong xyx position!!! set xyz to (0 0 0)\n')
        error_mod=True
    if rot[0]!='0' or rot[1]!='0':
        sayw('wrong rotation!!! set rotate x and y to (0 0 z)\n')
        error_mod=True
    if error_mod:
        msg="""<b>Error in '.kicad_mod' footprint</b><br>"""
        msg+="<br>reset values to:<br>"
        msg+="<b>(at (xyz 0 0 0))<br>"
        msg+="(scale (xyz 1 1 1))<br>"
        msg+="(rotate (xyz 0 0 z))<br>"
        msg+="</b><br>Only z rotation is allowed!"
        reply = QtGui.QMessageBox.information(None,"info", msg)
        #stop
    #say(footprint_name+" wrl rotation:"+str(rot_wrl)+"\r\n")
    if FreeCAD.activeDocument():
        doc=FreeCAD.activeDocument()
    else:
        doc=FreeCAD.newDocument()
    for obj in FreeCAD.ActiveDocument.Objects:
        FreeCADGui.Selection.removeSelection(obj)

    TopPadList=[]
    BotPadList=[]
    HoleList=[]
    THPList=[]
    for pad in getPadsList(content):
        #say(pad)
        #say("\r\n")
        #   pads.append({'x': x, 'y': y, 'rot': rot, 'padType': pType, 'padShape': pShape, 'rx': drill_x, 'ry': drill_y, 'dx': dx, 'dy': dy, 'holeType': hType, 'xOF': xOF, 'yOF': yOF, 'layers': layers})
        pType = pad['padType']
        pShape = pad['padShape']
        xs = pad['x'] #+ X1
        ys = pad['y'] #+ Y1
        dx = pad['dx']
        dy = pad['dy']
        hType = pad['holeType']
        drill_x = pad['rx']
        drill_y = pad['ry']
        xOF = pad['xOF']
        yOF = pad['yOF']
        rot = pad['rot']
        rx=drill_x
        ry=drill_y
        numberOfLayers = pad['layers'].split(' ')
        #say(str(rx)+"\r\n")
        #say(numberOfLayers)
        #if pType=="thru_hole":
        #pad shape - circle/rec/oval/trapezoid
        perc=0
        if pShape=="circle" or pShape=="oval":
            pShape="oval"
            perc=100
            # pad type - SMD/thru_hole/connect
        #say(pType+"here\r\n")
        if dx>rx and dy>ry:
            #say(pType+"\r\n")
            #say(str(dx)+"+"+str(rx)+" dx,rx\r\n")
            #say(str(dy)+"+"+str(ry)+" dy,ry\r\n")
            #say(str(xOF)+"+"+str(yOF)+" xOF,yOF\r\n")
            #def addPadLong(x, y, dx, dy, perc, typ, z_off):
            x1=xs+xOF
            y1=ys-yOF #yoffset opposite
            #say(str(x1)+"+"+str(y1)+" x1,y1\r\n")
            top=False
            bot=False
            if 'F.Cu' in numberOfLayers:
                top=True
            if '*.Cu' in numberOfLayers:
                top=True
                bot=True
            if 'B.Cu' in numberOfLayers:
                bot=True
            if top==True:
                #mypad=addPadLong(x1, y1, dx, dy, perc, 0, 0)
                mypad=createPad3(x1, y1, dx, dy, xs,ys,rx,ry,pShape,'top')
                ##pad pos x,y; pad size x,y; drillcenter x,y; drill size x,y, layer
                obj=mypad
                if rot!=0:
                    rotateObj(obj, [xs, ys, rot])
                TopPadList.append(obj)
            if bot==True:
                #mypad=addPadLong(x1, y1, dx, dy, perc, 0, -1.6)
                mypad=createPad3(x1, y1, dx, dy, xs,ys,rx,ry,pShape,'bot')
                ##pad pos x,y; pad size x,y; drillcenter x,y; drill size x,y, layerobj=mypad
                obj=mypad
                if rot!=0:
                    rotateObj(obj, [xs, ys, -rot+180])
                BotPadList.append(obj)
        if rx!=0:
            obj=createHole2(xs,ys,rx,ry,"oval") #need to be separated instructions
            #say(HoleList)
            if rot!=0:
                rotateObj(obj, [xs, ys, rot])
            HoleList.append(obj)
            obj2=createTHPlate(xs,ys,rx,ry,"oval")
            THPList.append(obj2)
            if rot!=0:
                rotateObj(obj2, [xs, ys, rot])

        ### cmt- #da gestire: pad type trapez

    FrontSilk = []
    # line
    #getLine('F.SilkS', content, 'fp_line')
    for i in getLine('F.SilkS', content, 'fp_line'):
        #say("here3\r\n")
        x1 = i[0] #+ X1
        y1 = i[1] #+ Y1
        x2 = i[2] #+ X1
        y2 = i[3] #+ Y1
        obj = addLine_2(x1, y1, x2, y2, i[4])
        #layerNew.changeSide(obj, X1, Y1, warst)
        #layerNew.rotateObj(obj, [X1, Y1, ROT])
        #layerNew.addObject(obj)
        FrontSilk.append(addLine_2(x1, y1, x2, y2, i[4]))

    # circle
    for i in getCircle('F.SilkS', content, 'fp_circle'):
        #say(i)
        xs = i[0] #+ X1
        ys = i[1] #+ Y1
        FrontSilk.append(addCircle_2(xs, ys, i[2], i[3]))

    # arc
    for i in getArc('F.SilkS', content, 'fp_arc'):
        x1 = i[0] #+ X1
        y1 = i[1] #+ Y1
        x2 = i[2] #+ X1
        y2 = i[3] #+ Y1

        arc1=addArc_3([x1, y1], [x2, y2], i[4], i[5])
        #arc2=arc1.copy()
        #arc2.Placement=arc1.Placement;
        #FrontSilk.append(arc2)
        ##shape=arc1.copy()
        ##shape.Placement=arc1.Placement;
        #say(i[4])
        #say(arcMidPoint([x1, y1], [x2, y2],i[4]))
        #[xm,ym]=arcMidPoint([x1, y1], [x2, y2],i[4])
        xm=(x1+x2)/2
        ym=(y1+y2)/2
        ##shape.rotate((xm,ym,0),(0,0,1),180)
        #shape.translate(((x1-x2)/2,(y1-y2)/2,0))
        rotateObj(arc1, [xm, ym, 180])
        ##arc1.Placement=shape.Placement

        #arc1.Placement = FreeCAD.Placement(arc1.Placement.Base, FreeCAD.Rotation(0, 0, 180))
        #FrontSilk.append(addArc_3([x1, y1], [x2, y2], i[4], i[5]))
        FrontSilk.append(arc1)


    if len(FrontSilk)>0:
        FSilk_lines = Part.makeCompound(FrontSilk)
        Part.show(FSilk_lines)
        FreeCAD.ActiveDocument.ActiveObject.Label="FrontSilk"
        FSilk_name=FreeCAD.ActiveDocument.ActiveObject.Name
        FreeCADGui.ActiveDocument.ActiveObject.ShapeColor = (1.0000,1.0000,1.0000)
        FreeCADGui.ActiveDocument.ActiveObject.Transparency = 60
    #
    if len(TopPadList)>0:
        TopPads = Part.makeCompound(TopPadList)
        Part.show(TopPads)
        FreeCAD.ActiveDocument.ActiveObject.Label="TopPads"
        TopPads_name=FreeCAD.ActiveDocument.ActiveObject.Name
        FreeCADGui.ActiveDocument.ActiveObject.ShapeColor = (0.81,0.71,0.23) #(0.85,0.53,0.10)
        FreeCADGui.ActiveDocument.ActiveObject.Transparency = 60
    if len(BotPadList)>0:
        BotPads = Part.makeCompound(BotPadList)
        Part.show(BotPads)
        FreeCAD.ActiveDocument.ActiveObject.Label="BotPads"
        BotPads_name=FreeCAD.ActiveDocument.ActiveObject.Name
        FreeCADGui.ActiveDocument.ActiveObject.ShapeColor = (0.81,0.71,0.23) #(0.85,0.53,0.10)
        FreeCADGui.ActiveDocument.ActiveObject.Transparency = 60

    #
    if len(HoleList)>0:
        Holes = Part.makeCompound(HoleList)
        Holes = Part.makeSolid(Holes)
        Part.show(Holes)
        #say(FreeCAD.ActiveDocument.ActiveObject.Name)
        FreeCAD.ActiveDocument.ActiveObject.Label="Holes"
        Holes_name=FreeCAD.ActiveDocument.ActiveObject.Name
        #say(Holes_name)
        FreeCADGui.ActiveDocument.ActiveObject.ShapeColor = (0.67,1.00,0.50)
        FreeCADGui.ActiveDocument.ActiveObject.Transparency = 70
        THPs = Part.makeCompound(THPList)
        THPs = Part.makeSolid(THPs)
        Part.show(THPs)
        #say(FreeCAD.ActiveDocument.ActiveObject.Name)
        FreeCAD.ActiveDocument.ActiveObject.Label="PTHs"
        THPs_name=FreeCAD.ActiveDocument.ActiveObject.Name
        #say(Holes_name)
        FreeCADGui.ActiveDocument.ActiveObject.ShapeColor = (0.67,1.00,0.50)
        FreeCADGui.ActiveDocument.ActiveObject.Transparency = 70

    fp_group=FreeCAD.ActiveDocument.addObject("App::DocumentObjectGroup", footprint_name+'fp')
    say(fp_group.Label+'\n')
    list=[]
    if len(FrontSilk)>0:
        obj2 = FreeCAD.ActiveDocument.getObject(FSilk_name)
        list.append(FSilk_name)
        fp_group.addObject(obj2)


    if len(TopPadList)>0:
        obj3 = FreeCAD.ActiveDocument.getObject(TopPads_name)
        fp_group.addObject(obj3)
        list.append(TopPads_name)
    if len(BotPadList)>0:
        obj4 = FreeCAD.ActiveDocument.getObject(BotPads_name)
        fp_group.addObject(obj4)
        list.append(BotPads_name)

    if len(HoleList)>0:
        obj5 = FreeCAD.ActiveDocument.getObject(Holes_name)
        fp_group.addObject(obj5)
        list.append(Holes_name)
        obj6 = FreeCAD.ActiveDocument.getObject(THPs_name)
        fp_group.addObject(obj6)
        list.append(THPs_name)

    #objFp=Part.makeCompound(list)
    #Part.show(objFp)
    #say(list)
    doc=FreeCAD.ActiveDocument
    fp_objs=[]
    list1=[]
    for obj in fp_group.Group:
        #if (obj.Label==fp_group.Label):
        #FreeCADGui.Selection.addSelection(obj)
        shape=obj.Shape.copy()
        #shape_name=FreeCAD.ActiveDocument.ActiveObject.Name
        list1.append(shape)
        #Part.show(shape)
        fp_objs.append(obj)
        #say("added")
        #
    #fp_objs.copy
    #objFp=Part.makeCompound(shape)
    objFp=Part.makeCompound(list1)
    Part.show(objFp)

    obj = FreeCAD.ActiveDocument.ActiveObject
    #say("h")
    FreeCADGui.Selection.addSelection(obj)            # select the object
    createSolidBBox2(obj)
    bbox=FreeCAD.ActiveDocument.ActiveObject
    FreeCAD.ActiveDocument.ActiveObject.Label ="Pcb_solid"
    pcb_solid_name=FreeCAD.ActiveDocument.ActiveObject.Name
    FreeCAD.ActiveDocument.removeObject(obj.Name)

    #FreeCADGui.ActiveDocument.getObject(bbox.Name).BoundingBox = True
    FreeCADGui.ActiveDocument.ActiveObject.ShapeColor = (0.664,0.664,0.496)
    FreeCADGui.ActiveDocument.ActiveObject.Transparency = 80
    #obj6 = FreeCAD.ActiveDocument.getObject(bbox.Name)
    fp_group.addObject(bbox)

    if len(HoleList)>0:
        cut_base = FreeCAD.ActiveDocument.getObject(pcb_solid_name).Shape
        for drill in HoleList:
            #Holes = Part.makeCompound(HoleList)
            hole = Part.makeSolid(drill)
            #Part.show(hole)
            #hole_name=FreeCAD.ActiveDocument.ActiveObject.Name
            #cutter = FreeCAD.ActiveDocument.getObject(hole_name).Shape
            cut_base=cut_base.cut(hole)
        Part.show(cut_base) 
        pcb_name=FreeCAD.ActiveDocument.ActiveObject.Name
        FreeCAD.ActiveDocument.ActiveObject.Label ="Pcb"
        FreeCADGui.ActiveDocument.ActiveObject.ShapeColor = (0.664,0.664,0.496)
        FreeCADGui.ActiveDocument.ActiveObject.Transparency = 80
        #say("cutted")
        pcb=FreeCAD.ActiveDocument.ActiveObject
        fp_group.addObject(pcb)
        #say("added")
        #FreeCAD.activeDocument().recompute()
        FreeCAD.ActiveDocument.removeObject(pcb_solid_name)
        FreeCAD.ActiveDocument.removeObject(Holes_name)
       
    list2=[]
    list2_objs=[]
    for obj in fp_group.Group:
        # do what you want to automate
        #if (obj.Label==fp_group.Label):
        #FreeCADGui.Selection.addSelection(obj)
        shape=obj.Shape.copy()
        #shape_name=FreeCAD.ActiveDocument.ActiveObject.Name
        list2.append(shape)
        #Part.show(shape)
        list2_objs.append(obj)
        #say("added")
    #say(list2)
    #say('here1')

    #Draft.rotate(list2_objs,90.0,FreeCAD.Vector(0.0,0.0,0.0),axis=FreeCAD.Vector(-0.0,-0.0,1.0),copy=False)
    #say('here1')

    rot=[0,0,rot_wrl]
    rotateObjs(list2_objs, rot)

    for obj in fp_group.Group:
        FreeCADGui.Selection.removeSelection(obj)
    #say('here2')

    FreeCADGui.SendMsgToActiveView("ViewFit")
    #pads_found=getPadsList(content)

###

def routineDrawIDF(doc,filename):
    """process_emn(document, filename)-> adds emn geometry from emn file"""
    global start_time
    msg='IDF_ImporterVersion='+IDF_ImporterVersion+'\n'
    say(msg)
    emnfile=pythonopen(filename, "r")
    emn_unit=1.0 #presume milimeter like emn unit
    emn_version=2 #presume emn_version 2
    board_thickness=0 #presume 0 board height
    board_outline=[] #no outline
    drills=[] #no drills
    placement=[] #no placement
    place_item=[] #empty place item
    emnlines=emnfile.readlines()
    emnfile.close()   
    passed_sections=[]
    current_section=""
    section_counter=0
    ignore_hole_size=min_drill_size
    #say((emnlines))
    for emnline in emnlines:
        emnrecords=split_records(emnline)
        if len( emnrecords )==0 : continue
        if len( emnrecords[0] )>4 and emnrecords[0][0:4]==".END":
            passed_sections.append(current_section)
            current_section=""
        elif emnrecords[0][0]==".":
            current_section=emnrecords[0]
            section_counter=0
        section_counter+=1
        if current_section==".HEADER"  and section_counter==2:
            emn_version=int(float(emnrecords[1]))
            say("Emn version: "+emnrecords[1]+"\n")
        if current_section==".HEADER"  and section_counter==3 and emnrecords[1]=="THOU":
            emn_unit=0.0254
            say("UNIT THOU\n" )
        if current_section==".HEADER"  and section_counter==3 and emnrecords[1]=="TNM":
            emn_unit=0.000010
            say("TNM\n" )
        if current_section==".BOARD_OUTLINE"  and section_counter==2:
            board_thickness=emn_unit*float(emnrecords[0])
            say("Found board thickness "+emnrecords[0]+"\n")
        if current_section==".BOARD_OUTLINE"  and section_counter>2:
            board_outline.append([int(emnrecords[0]),float(emnrecords[1])*emn_unit,float(emnrecords[2])*emn_unit,float(emnrecords[3])])
        if current_section==".DRILLED_HOLES"  and section_counter>1 and float(emnrecords[0])*emn_unit>ignore_hole_size:
            drills.append([float(emnrecords[0])*emn_unit,float(emnrecords[1])*emn_unit,float(emnrecords[2])*emn_unit])
        if current_section==".PLACEMENT"  and section_counter>1 and fmod(section_counter,2)==0:
            place_item=[]
            place_item.append(emnrecords[2]) #Reference designator
            place_item.append(emnrecords[1]) #Component part number
            place_item.append(emnrecords[0]) #Package name
        if current_section==".PLACEMENT"  and section_counter>1 and fmod(section_counter,2)==1:
            place_item.append(float(emnrecords[0])*emn_unit) #X
            place_item.append(float(emnrecords[1])*emn_unit) #Y
            if emn_version==3:
                place_item.append(float(emnrecords[2])*emn_unit) #Z  maui
                #say("\nZ="+(str(float(emnrecords[2])))+"\n")   
            place_item.append(float(emnrecords[emn_version])) #Rotation
            place_item.append(emnrecords[emn_version+1]) #Side
            place_item.append(emnrecords[emn_version+2]) #Place Status
            say(str(place_item)+"\n")
            placement.append(place_item)
        
    say("\n".join(passed_sections)+"\n")
    #say(board_outline)
    say("Proceed "+str(Process_board_outline(doc,board_outline,drills,board_thickness))+" outlines\n")
    ## place_steps(doc,placement,board_thickness)
    
###
def Process_board_outline(doc,board_outline,drills,board_thickness):
    """Process_board_outline(doc,board_outline,drills,board_thickness)-> number proccesed loops
        adds emn geometry from emn file"""
    global start_time
    vertex_index=-1; #presume no vertex
    lines=-1 #presume no lines
    out_shape=[]
    out_face=[]
    for point in board_outline:
        vertex=Base.Vector(point[1],point[2],0) 
        vertex_index+=1
        if vertex_index==0:
            lines=point[0] 
        elif lines==point[0]:
            if point[3]!=0 and point[3]!=360:
                out_shape.append(Part.Arc(prev_vertex,mid_point(prev_vertex,vertex,point[3]),vertex))
                #say("mid point "+str(mid_point)+"\n")
            elif point[3]==360:
                per_point=Per_point(prev_vertex,vertex)
                out_shape.append(Part.Arc(per_point,mid_point(per_point,vertex,point[3]/2),vertex))
                out_shape.append(Part.Arc(per_point,mid_point(per_point,vertex,-point[3]/2),vertex))
            else:
                out_shape.append(Part.Line(prev_vertex,vertex))
        else:
            out_shape=Part.Shape(out_shape)
            out_shape=Part.Wire(out_shape.Edges)
            out_face.append(Part.Face(out_shape))
            out_shape=[]
            vertex_index=0 
            lines=point[0] 
        prev_vertex=vertex
    if lines!=-1:
        out_shape=Part.Shape(out_shape)
        out_shape=Part.Wire(out_shape.Edges)
        out_face.append(Part.Face(out_shape))
        outline=out_face[0]
        say("Added outline\n")
        if len(out_face)>1:
            say("Cutting shape inside outline\n")
            for otl_cut in out_face[1: ]:
                outline=outline.cut(otl_cut)
                #say("Cutting shape inside outline\n")
        if len(drills)>0:
            say("Cutting holes inside outline\n")
        for drill in drills:
            #say("Cutting hole inside outline\n")
            out_shape=Part.makeCircle(drill[0]/2, Base.Vector(drill[1],drill[2],0))
            out_shape=Part.Wire(out_shape.Edges)
            outline=outline.cut(Part.Face(out_shape))
        doc_outline=doc.addObject("Part::Feature","Pcb")
        doc_outline.Shape=outline 
        #FreeCADGui.Selection.addSelection(doc_outline)
        #FreeCADGui.runCommand("Draft_Upgrade")
        #outline=FreeCAD.ActiveDocument.getObject("Union").Shape
        #FreeCAD.ActiveDocument.removeObject("Union")
        #doc_outline=doc.addObject("Part::Feature","Board_outline")
        doc_outline.Shape=outline.extrude(Base.Vector(0,0,-board_thickness))
        grp=doc.addObject("App::DocumentObjectGroup", "Board_Geoms")
        grp.addObject(doc_outline)
        doc.Pcb.ViewObject.ShapeColor = (colr,colg,colb)
        say_time()
        #say(str(start_time));say('*'+str(end_milli_time)+'start-end')
        FreeCADGui.activeDocument().activeView().viewAxometric()
        FreeCADGui.SendMsgToActiveView("ViewFit")
        #doc.Pcb.ViewObject.ShapeColor=(0.0, 0.5, 0.0, 0.0)
    return lines+1


###
def split_records(line_record):
    """split_records(line_record)-> list of strings(records)
       
       standard separator list separator is space, records containting encapsulated by " """
    split_result=[]
    quote_pos=line_record.find('"')
    while quote_pos!=-1:
        if quote_pos>0:
            split_result.extend(line_record[ :quote_pos].split())
            line_record=line_record[quote_pos: ]
            quote_pos=line_record.find('"',1)
        else: 
            quote_pos=line_record.find('"',1)
        if quote_pos!=-1:
            split_result.append(line_record[ :quote_pos+1])
            line_record=line_record[quote_pos+1: ]
        else:
            split_result.append(line_record) 
            line_record=""
        quote_pos=line_record.find('"')
    split_result.extend(line_record.split())
    return split_result
###

#def routineDrawPCB(content,pcbThickness,board_elab):
def routineDrawPCB(pcbThickness,board_elab):
    global start_time
    #for item in content:
    #    say(item)
    #                      x1, y1, x2, y2, width
    say("PCB Loader \n")
    doc=FreeCAD.activeDocument()
    for obj in FreeCAD.ActiveDocument.Objects:
        FreeCADGui.Selection.removeSelection(obj)
    TopPadList=[]
    BotPadList=[]
    HoleList=[]
    THPList=[]

    EdgeCuts = []
    EdgeCuts_face = []
    EdgeCuts_shape = []
    PCB = []
    
    edges=[]
    PCBs = []
    totalHeight=pcbThickness
    
    # arc
    #for i in getArc('Edge.Cuts', content, 'gr_arc'):
    for i in getArc('Edge.Cuts', board_elab, 'gr_arc'):
        #say('arcs')
        x1 = i[0] #+ X1
        y1 = i[1] #+ Y1
        x2 = i[2] #+ X1
        y2 = i[3] #+ Y1
        arc1=Part.Edge(Part.Arc(Base.Vector(x2,y2,0),mid_point(Base.Vector(x2,y2,0),Base.Vector(x1,y1,0),i[4]),Base.Vector(x1,y1,0)))
        #arc1=Part.Edge(getCurvedLine(x2, y2,x1, y1, i[4]))
        #say(arc1.Curve.EndPoint) #to do maui
        edges.append(arc1)
        if show_border:
            Part.show(arc1)
        #FreeCAD.ActiveDocument.ActiveObject.supportedProperties()
        #say(FreeCAD.ActiveDocument.ActiveObject.Shape.Name)
        PCB.append(['Arc', i[0], i[1], i[2], i[3], i[4]])
        
    # circle
    #for i in getCircle('Edge.Cuts', content, 'gr_circle'):
    for i in getCircle('Edge.Cuts', board_elab, 'gr_circle'):
        #say(i)
        xs = i[0] #+ X1
        ys = i[1] #+ Y1
        r  = i[2]
        circle1=Part.Edge(Part.Circle(Base.Vector(xs, ys,0), Base.Vector(0, 0, 1), r))
        ##circle1=Part.makeCircle(Base.Vector(xs, ys,0), Base.Vector(0, 0, 1), r)
        ##circle1=circle1.Edge
        if show_border:
            Part.show(circle1)
        circle1=Part.Wire(circle1)
        circle1=Part.Face(circle1)
        if show_shapes:
            Part.show(circle1)
        #circle1.translate(Base.Vector(0,0,-totalHeight))
        PCBs.append(circle1)
        #say('circle\n')
        PCB.append(['Circle', i[0], i[1], i[2]])
    
    # line
    #getLine('F.SilkS', content, 'fp_line')
    #for i in getLine('Edge.Cuts', content, 'gr_line'):
    for i in getLine('Edge.Cuts', board_elab, 'gr_line'):
        #say("here3\r\n")
        x1 = i[0] #+ X1
        y1 = i[1] #+ Y1
        x2 = i[2] #+ X1
        y2 = i[3] #+ Y1
        line1=Part.makeLine((x1, y1,0), (x2,y2,0))
        edges.append(line1);
        if show_border:
            Part.show(line1)
        PCB.append(['Line', i[0], i[1], i[2], i[3]])
    
    #sort edges to form a single closed 2D shape
    loopcounter = 0
    if (not len(edges)>0):
        say ("no PCBs found")
    else:
        newEdges = [];
        newEdges.append(edges.pop(0))
        #say(newEdges[0])
        #print [newEdges[0].Vertexes[0].Point]
        #print [newEdges[0].Vertexes[-1].Point]
        #say(str(len(newEdges[0].Vertexes)))
        nextCoordinate = newEdges[0].Vertexes[0].Point
        firstCoordinate = newEdges[0].Vertexes[-1].Point
        #nextCoordinate = newEdges[0].Curve.EndPoint
        #firstCoordinate = newEdges[0].Curve.StartPoint
        while(len(edges)>0 and loopcounter < 2):
            loopcounter = loopcounter + 1
            #print "nextCoordinate: ", nextCoordinate
            #if len(newEdges[0].Vertexes) > 1: # not circle
            for j, edge in enumerate(edges):
                #print "compare to: ", edges[j].Curve.StartPoint, "/" , edges[j].Curve.EndPoint
                #if edges[j].Curve.StartPoint == nextCoordinate:
                if edges[j].Vertexes[-1].Point == nextCoordinate:
                    nextCoordinate = edges[j].Vertexes[0].Point
                    newEdges.append(edges.pop(j))
                    loopcounter = 0
                    break
                elif edges[j].Vertexes[0].Point == nextCoordinate:
                    nextCoordinate = edges[j].Vertexes[-1].Point
                    newEdges.append(edges.pop(j))
                    loopcounter = 0
                    break
            if nextCoordinate == firstCoordinate:
                say('2d closed path\n')
                try: # maui
                    #say('\ntrying wire & face\n')
                    #newEdges_old=newEdges
                    ## newEdges = Part.Wire(newEdges)
                    #say('trying face\n')
                    ## newEdges = Part.Face(newEdges)
                    newEdges = OpenSCAD2Dgeom.edgestofaces(newEdges)
                    #say('done\n')
                    #newEdges.translate(Base.Vector(0,0,-totalHeight))
                    if show_shapes:
                        Part.show(newEdges)
                    #newEdges = newEdges.extrude(Base.Vector(0,0,totalHeight))
                    PCBs.append(newEdges)
                    if (len(edges)>0):
                        newEdges = [];
                        newEdges.append(edges.pop(0))
                        nextCoordinate = newEdges[0].Vertexes[0].Point
                        firstCoordinate = newEdges[0].Vertexes[-1].Point
                except Part.OCCError: # Exception: #
                    say("error in creating PCB")
                    stop
                    
        if loopcounter == 2:
            say("*** omitting PCBs because there was a not closed loop in your edge lines ***\n")
            say("*** have a look at position x=" + str(nextCoordinate.x) + "mm, y=" + str(nextCoordinate.y) + "mm ***\n")
            say('pcb edge not closed\n')
            QtGui.qApp.restoreOverrideCursor()
            diag = QtGui.QMessageBox(QtGui.QMessageBox.Icon.Critical,
                                    'Error in creating Board Edge                                                                ."+"\r\n"',
                                    """Try Loading IDF(.emn) instead of .kicad_pcb or <br><b>pcb edge not closed<br>review your Board Edges in Kicad!<br>position x=""" + str(nextCoordinate.x) + 'mm, y=' + str(-nextCoordinate.y) + 'mm')
            diag.setWindowModality(QtCore.Qt.ApplicationModal)
            diag.exec_()
            stop #maui
        if disable_cutting:
            FreeCADGui.activeDocument().activeView().viewTop()
            FreeCADGui.SendMsgToActiveView("ViewFit")
            stop #maui
        maxLenght=0
        idx=0
        for extruded in PCBs:
            #search for orientation of each pcb in 3d space, save it (no transformation yet!)
            angle = 0;
            axis = Base.Vector(0,0,1)
            position = Base.Vector(0,0,0)
            if show_shapes:
                Part.show(extruded)
            #extrude_XLenght=FreeCAD.ActiveDocument.ActiveObject.Shape.BoundBox.XLength
            # extrude_XLenght=extruded.Length #perimeter
            extrude_XLenght=extruded.BoundBox.XLength
            #extrude_XLenght=FreeCAD.ActiveDocument.ActiveObject.Shape.Edges.Length
            if maxLenght < extrude_XLenght:
                maxLenght = extrude_XLenght
                external_idx=idx
            #say('XLenght='+str(extrude_XLenght)+'\n')
            idx=idx+1
        say('max Length='+str(maxLenght)+' index='+str(external_idx)+'\n')
        cut_base=PCBs[external_idx]
        i=0
        for i in range (len(PCBs)):
            if i!=external_idx:
                cutter=PCBs[i]
                cut_base=cut_base.cut(cutter)
        if test_extrude:
            cut_base = cut_base.extrude(Base.Vector(0,0,totalHeight))
        if show_shapes:
            Part.show(cut_base)
        #cut_base_name=FreeCAD.ActiveDocument.ActiveObject.Name
        #say('Alive1')
    if len(PCBs)==1:
        cut_base = PCBs[0]
        if test_extrude:
            cut_base = cut_base.extrude(Base.Vector(0,0,totalHeight))
        if show_shapes:
            Part.show(cut_base)
        if show_shapes:
            FreeCAD.activeDocument().removeObject("Shape")
        ###FreeCAD.ActiveDocument.recompute()
    
    if len(PCBs)==0:
        say('pcb edge not found\n')
        QtGui.qApp.restoreOverrideCursor()
        diag = QtGui.QMessageBox(QtGui.QMessageBox.Icon.Critical,
                                'Error in creating Board Edge                                                                ."+"\r\n"',
                                'Try Loading IDF(.emn) instead of .kicad_pcb or \nreview your Board Edges in Kicad!\n')
        diag.setWindowModality(QtCore.Qt.ApplicationModal)
        diag.exec_()
        stop #maui
    FreeCADGui.activeDocument().activeView().viewTop()
    FreeCADGui.SendMsgToActiveView("ViewFit")
    say_time()
    # stop #maui       
    
    say("start cutting\n")    
    if holes_solid:
        HoleList = getPads(board_elab,pcbThickness)
    else:
        HoleList = getPads_flat(board_elab)
    #say('alive-getting holes\n')
    ## stop
    if len(HoleList)>0:
        #cut_base = FreeCAD.ActiveDocument.getObject(cut_base_name).Shape
        #cut_base_name=FreeCAD.ActiveDocument.ActiveObject
        #cut_base_name=FreeCAD.ActiveDocument.ActiveObject.Name
        #say(cut_base)
        for drill in HoleList:
            #say("Cutting hole inside outline\n")
            #say(drill)
            if holes_solid:
                drill = Part.makeSolid(drill)
            if show_shapes:
                Part.show(drill)
            cut_base=cut_base.cut(drill)
    doc_outline=doc.addObject("Part::Feature","Pcb")
    doc_outline.Shape=cut_base 
    doc_outline.Shape=cut_base.extrude(Base.Vector(0,0,-pcbThickness))
    #cut_base=cut_base.extrude(Base.Vector(0,0,-pcbThickness))
    #Part.show(cut_base)
    pcb_name=FreeCAD.ActiveDocument.ActiveObject.Name
    pcb_board=FreeCAD.ActiveDocument.ActiveObject
    #FreeCAD.ActiveDocument.ActiveObject.Label ="Pcb"
    FreeCADGui.ActiveDocument.ActiveObject.ShapeColor = (colr,colg,colb)
    #FreeCADGui.ActiveDocument.ActiveObject.Transparency = 20
    
    #if remove_pcbPad==True:
    #    FreeCAD.activeDocument().removeObject(cut_base_name)
        #FreeCAD.activeDocument().removeObject(Holes_name)
    grp=doc.addObject("App::DocumentObjectGroup", "Board_Geoms")
    grp.addObject(pcb_board)
    #grp.addObject(doc_outline)      
        
    say_time()
    FreeCADGui.activeDocument().activeView().viewAxometric()
    FreeCADGui.SendMsgToActiveView("ViewFit")
    #FreeCADGui.SendMsgToActiveView("ViewFit")
    #pads_found=getPadsList(content)
    
###

###
#cmd open option
args=sys.argv
#say(args)
if len(args) == 3:
#    #filename="./psu-fc-1.wrl"
    #path, fname = os.path.split(args[2])
    #export_board_2step=True
    sys.argv=""
    ext = os.path.splitext(os.path.basename(args[2]))[1]
    fullfname=args[2]
    fname=os.path.splitext(os.path.basename(args[2]))[0]
    #say(filePath+' ');say(fname+' ');say(ext);say('\n')
    fullFileName=fullfname+".kicad_pcb"
    fileName=fname+".kicad_pcb"
    #filePath = os.path.dirname(os.path.abspath(__file__))
    filePath = os.path.dirname(os.path.abspath(fullFileName))
    #filePath = os.path.split(os.path.realpath(__file__))[0]
    say ('arg file path '+filePath+'\n')
    if filePath == "":
        filePath = "."
    last_pcb_path = filePath
    #say(fullFileName+'\n')
    if os.path.exists(fullFileName):
        #say("opening "+ fullFileName+'\n')
        cfgParsWrite(configFilePath)
        onLoadBoard(fullFileName)
    else:
        fullfilePath=filePath+os.sep+fname+".kicad_pcb"
        #say(fullfilePath+'\n')
        if os.path.exists(fullfilePath):
            #say("opening "+ fullfilePath+'\n')
            cfgParsWrite(configFilePath)
            onLoadBoard(fullfilePath)
        else:
            sayw("missing "+ fullfilePath+'\n')
            sayw("missing "+ fullFileName+'\n')
            #say("error missing "+ fullfilePath+'\r\n')
            QtGui.qApp.restoreOverrideCursor()
            reply = QtGui.QMessageBox.information(None,"Error ...","... missing \r\n"+ fullfilePath+"\r\n... missing \r\n"+ fullFileName)
        #

###

QtGui.QDesktopServices.openUrl(QtCore.QUrl("t"))


# code ***********************************************************************************

form = RotateXYZGuiClass()

#
#Word size: 64-bit
#Version: 0.15.4671 (Git)
#Branch: releases/FreeCAD-0-15
#Python version: 2.7.5
#Qt version: 4.8.6
#Coin version: 3.1.3
#SoQt version: 1.5.0
#OCC version: 6.7.0
#

"""Create SERA Worksets"""
from pyrevit import revit, DB, UI

def create_worksets(d, names):
    for name in names:
        DB.Workset.Create(d, name)

workset_names = ["UNITS", "X_A_SITE_RVT", "X_M_MECHANICAL_RVT", "X_S_STRUCTURAL_RVT"]

# enable worksharing if not already workshared
if not revit.doc.IsWorkshared:
    # EnableWorksharing arguments required for shared levels, grids and main workset
    revit.doc.EnableWorksharing("DATUM ELEMENTS", "MAIN MODEL")

    # start a transcation to modify the active document
    t = DB.Transaction(revit.doc, "Create Worksets")
    t.Start()
    # make your model changes here
    create_worksets(revit.doc, workset_names)
    t.Commit()
    
    # create a taskdialog to report next steps and offer help
    message = UI.TaskDialog("Worksets Added")
    message.MainInstruction = "SERA standard worksets have been added to this file. Next Steps:\n\n1. Save file to project folder\n2. Select Collaborate > Relinquish All Mine\n3. Select File > Close\n\nOnce these steps are taken, you and your team can create new locals from this central model."
    message.Show()
       
else:
    message = UI.TaskDialog("No Worksets Added")
    message.MainInstruction = "The active file is already workshared. This command is for non-workshared files only."
    message.Show()

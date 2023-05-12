"""Create SERA Worksets"""
from pyrevit import revit, DB, UI, forms

def create_worksets(d, names):
    for name in names:
        DB.Workset.Create(d, name)

building_workset_names = ["UNITS", "X_A_SITE_RVT", "X_M_MECHANICAL_RVT", "X_S_STRUCTURAL_RVT"]
site_workset_names = ["X_A_BUILDING_RVT", "X_C_SURVEY_DWG"]
# landscape_workset_names= []

# each .rte file has a value for Project Information > Organization Description that includes a template text value (Building Template, Site Template, etc.)
# this value is used to determine which standard worksets to add to the document
templateType = revit.doc.ProjectInformation.get_Parameter(DB.BuiltInParameter.PROJECT_ORGANIZATION_DESCRIPTION).AsString()

# enable worksharing if not already workshared
if not revit.doc.IsWorkshared:
    # EnableWorksharing arguments required for shared levels, grids and main workset
    revit.doc.EnableWorksharing("DATUM ELEMENTS", "MAIN MODEL")

    # start a transcation to modify the active document
    t = DB.Transaction(revit.doc, "Create Worksets")
    t.Start()
    # make your model changes here
    if templateType == "Site Template":
        create_worksets(revit.doc, site_workset_names)
    # elif templateType == "Landscape Template":
    #     create_worksets(revit.doc, landscape_workset_names)
    else:
        create_worksets(revit.doc, building_workset_names)
    t.Commit()
    
    # create a taskdialog to report next steps and offer help
    forms.alert("SERA standard worksets have been added to this file. Next Steps:\n\n1. Save file to project folder\n2. Select Collaborate > Relinquish All Mine\n3. Select File > Close\n\nOnce these steps are taken, you and your team can create new locals from this central model.","Worksets Added", warn_icon=False)
       
else:
    forms.alert("The active file is already workshared. This command is for non-workshared files only.","No Worksets Added", warn_icon=False)
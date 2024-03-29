from pyrevit import forms
# forms.alert(message, title, body1, body2, footer)
from pyrevit import EXEC_PARAMS
from Autodesk.Revit.DB import ModelPathUtils

title = "Central Model Warning"
message = "You've opened the central model. OMG!"
body = "No worries. Simply click OK, do not save, and close out of the file. Try creating a new local instead."

if EXEC_PARAMS.event_args.Document.IsWorkshared:

    modelPath = EXEC_PARAMS.event_args.Document.GetWorksharingCentralModelPath()
    centralPath = ModelPathUtils.ConvertModelPathToUserVisiblePath(modelPath)
    currentDocPath = EXEC_PARAMS.event_args.Document.PathName

    modifiedCentralPath = centralPath.replace("\\\\local.serapdx.com\\library\\Projects\\","P:\\")

    try:
        # Autodesk Docs is in path name for Revit 2023 cloud projects, BIM 360 is in path name for Revit 2021 cloud projects
        if  currentDocPath == modifiedCentralPath and not "Autodesk Docs" in currentDocPath and not "BIM 360" in currentDocPath:
            forms.alert(message,title,body)
    except Exception as e:
        pass
    
else:
    pass
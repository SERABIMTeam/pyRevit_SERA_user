import clr

clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
uiapp = DocumentManager.Instance.CurrentUIApplication
uiDoc = uiapp.ActiveUIDocument
app = uiapp.Application

ids = uiDoc.Selection.GetElementIds();

for v in ids:
	uiDoc.RequestViewChange(doc.GetElement(v))

TransactionManager.Instance.ForceCloseTransaction()
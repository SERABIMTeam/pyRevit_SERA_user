from pyrevit import revit

ids = revit.uidoc.Selection.GetElementIds();

for v in ids:
	revit.uidoc.RequestViewChange(revit.doc.GetElement(v))
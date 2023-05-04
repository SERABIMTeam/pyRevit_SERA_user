:: clone latest version of pyRevit on GitHub to local repository
:: 'core' is the deployment type, see list of types in the pyRevitFile
:: 'core' installs pyRevit dependencies but not the pyRevit Revit addin
pyrevit clone pyRevit_core core --dest="%ProgramData%\Autodesk\pyRevit"

:: attach pyRevit to specified installed versions of Revit (adds manifest file to ProgramData)
:: BIM is currently not supporting Revit 2020 or earlier versions
pyrevit attach pyRevit_core default 2021 --allusers
pyrevit attach pyRevit_core default 2022 --allusers
pyrevit attach pyRevit_core default 2023 --allusers
pyrevit attach pyRevit_core default 2024 --allusers

pyrevit extend ui SERA_user https://github.com/SERABIMTeam/pyRevit_SERA_user.git --dest="%ProgramData%\Autodesk\pyRevit\extensions"
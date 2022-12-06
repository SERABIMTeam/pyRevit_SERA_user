# """Reload pyRevit into new session."""
# # -*- coding=utf-8 -*-
# #pylint: disable=import-error,invalid-name,broad-except
# from pyrevit import EXEC_PARAMS
# from pyrevit import script
import pyrevit
from pyrevit import forms
# from pyrevit.loader import sessionmgr
# from pyrevit.loader import sessioninfo

import subprocess
subprocess.call([r'\\local.serapdx.com\data\Support\ProgramData\AutoDesk\Dynamo\Revit\Deploy\Dynamo_Package Update.bat'])

pyrevit.forms.alert("Beep boop beep... \n\nDynamo now has everything it needs to run smoothly.", "Result")


# res = True

# if res:
#     logger = script.get_logger()
#     results = script.get_results()

#     # re-load pyrevit session.
#     logger.info('Reloading....')
#     sessionmgr.reload_pyrevit()

#     results.newsession = sessioninfo.get_session_uuid()

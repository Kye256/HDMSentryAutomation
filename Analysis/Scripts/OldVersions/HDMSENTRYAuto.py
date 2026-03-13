import pywinauto
import time

app = pywinauto.application.Application().start('"C:\Program Files (x86)\HDM-Sentry\HDMSentry.exe"')
dlg = app.top_window_()
dlg.MoveWindow(0,0)
dlg.TypeKeys('{TAB}')
dlg.TypeKeys('{TAB}')
dlg.TypeKeys('{TAB}')
dlg.TypeKeys('{ENTER}')

# Analysis Setup
dlg.TypeKeys('{TAB}')
dlg.TypeKeys('{TAB}')
dlg.TypeKeys('Test2')
time.sleep(5)
dlg.TypeKeys('{TAB}')
dlg.TypeKeys('{TAB}')
dlg.TypeKeys('{TAB}')
dlg.TypeKeys('{DOWN}')
time.sleep(1)
dlg.TypeKeys('{TAB}')
dlg.TypeKeys('{TAB}')
dlg.TypeKeys('{ENTER}')

#Traffic And Environment Page
dlg.TypeKeys('{TAB}')
dlg.TypeKeys('{TAB}')
dlg.TypeKeys('{DOWN}')
dlg.TypeKeys('{TAB}')
#Choose the Climate Zone (Humid Tropical is 7th)
dlg.TypeKeys('{DOWN}')
dlg.TypeKeys('{DOWN}')
dlg.TypeKeys('{DOWN}')
dlg.TypeKeys('{DOWN}')
dlg.TypeKeys('{DOWN}')
dlg.TypeKeys('{DOWN}')
dlg.TypeKeys('{DOWN}')

#Choose the Traffic Growth
dlg.TypeKeys('{TAB}')
dlg.TypeKeys('{DOWN}')
dlg.TypeKeys('{DOWN}')
dlg.TypeKeys('{TAB}')
dlg.TypeKeys('{TAB}')
dlg.TypeKeys('{ENTER}')

#Road Section Page
dlg.TypeKeys('{TAB}')
dlg.TypeKeys('{TAB}')
dlg.TypeKeys('TrialSection')
#Choose Traffic Volume
dlg.TypeKeys('{TAB}')
dlg.TypeKeys('{DOWN}')
dlg.TypeKeys('{DOWN}')
dlg.TypeKeys('{TAB}')
dlg.TypeKeys('{TAB}')
dlg.TypeKeys('{TAB}')
#Choose Surface Class
dlg.TypeKeys('{DOWN}')
dlg.TypeKeys('{DOWN}')
dlg.TypeKeys('{TAB}')
#Choose condition
dlg.TypeKeys('{DOWN}')
dlg.TypeKeys('{DOWN}')
dlg.TypeKeys('{TAB}')
dlg.TypeKeys('30')  # Enter Length
dlg.TypeKeys('{TAB}')
dlg.TypeKeys('{TAB}')
dlg.TypeKeys('{ENTER}')
# Maintenance Alternatives Page
dlg.TypeKeys('{TAB}')
dlg.TypeKeys('{TAB}')
dlg.TypeKeys('{TAB}')
dlg.TypeKeys('{TAB}')
dlg.TypeKeys('{TAB}')
dlg.TypeKeys('{DOWN}')  # Choose Alternative 1
dlg.TypeKeys('{DOWN}')
dlg.TypeKeys('{TAB}')
dlg.TypeKeys('{DOWN}')  # Choose Alternative 2
dlg.TypeKeys('{DOWN}')
dlg.TypeKeys('{DOWN}')
dlg.TypeKeys('{TAB}')
dlg.TypeKeys('{TAB}')
dlg.TypeKeys('{TAB}')
dlg.TypeKeys('{ENTER}')
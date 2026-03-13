import pywinauto
import time

app = pywinauto.application.Application().start('"C:\Program Files (x86)\HDM-Sentry\HDMSentry.exe"')
dlg = app.top_window_()
dlg.MoveWindow(0,0)

def move_cursor(cur_moves):
    moves = cur_moves
    while cur_moves != 0:
        dlg.TypeKeys('{TAB}')
        cur_moves -= 1

def click_element(clicks):
    num_clicks = clicks
    while num_clicks != 0:
        dlg.TypeKeys('{ENTER}')
        num_clicks -= 1		

def chng_dropdown(item_pos):
    num_clicks = item_pos
    while num_clicks !=0:
        dlg.TypeKeys('{DOWN}')
        num_clicks -= 1

def fill_text(text):
    dlg.TypeKeys(text)
    		
move_cursor(3)
click_element(1)
move_cursor(2)
fill_text('test04') # Run name
move_cursor(3)
chng_dropdown(1)
time.sleep(1)
move_cursor(2)
click_element(1)
move_cursor(2)
click_element(1)
move_cursor(2)
chng_dropdown(1) # Changing vehicle fleet
move_cursor(1)
chng_dropdown(7) # Changing climate zoner
move_cursor(1)   
chng_dropdown(2) # Changing Traffic Growth
move_cursor(3)
click_element(1)
move_cursor(2)
fill_text('Trial') # Section name
move_cursor(1)
chng_dropdown(2)  # Changing Traffic Volume
move_cursor(3)
chng_dropdown(2)  # Changing Surface Class
move_cursor(1)    
chng_dropdown(2)  # Changing condition
move_cursor(1)
fill_text('30')
move_cursor(2)
click_element(1)
move_cursor(5)
chng_dropdown(2)  # Changing Alternative 1
move_cursor(1)
chng_dropdown(3)  # Changing Alternative 2
move_cursor(3)
click_element(1)
'''

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
dlg.TypeKeys('{ENTER}')'''
import pywinauto
import time
import fileinput

# Reads input parameters from input2.txt and creates HDMSENTY analysis. Does not use the GE Parameter
# Logical error in analysis_run not yet sorted out
# Unsed to generate trial2 results in .\results folder

global dlg, app
#app = pywinauto.application.Application().start('"C:\Program Files (x86)\HDM-Sentry\HDMSentry.exe"')
#dlg = app.top_window_()
#dlg.MoveWindow(0,0)

def move_cursor(cur_moves):
    global dlg
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
    		
def analysis_run(name, traffic_growth, condition, traffic_volume, geometry):
    global app, dlg
    app = pywinauto.application.Application().start('"C:\Program Files (x86)\HDM-Sentry\HDMSentry.exe"')
    time.sleep(10)
    dlg = app.top_window_()
    dlg.MoveWindow(0,0)
    move_cursor(3)
    click_element(1)
    move_cursor(2)
    fill_text(str(name)) # Run name
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
    chng_dropdown(7) # Changing climate zone
    move_cursor(1)   
    chng_dropdown(int(traffic_growth)) # Changing Traffic Growth
    move_cursor(3)
    click_element(1)
    move_cursor(2)
    fill_text('Trial') # Section name
    move_cursor(1)
    chng_dropdown(int(traffic_volume))  # Changing Traffic Volume
    move_cursor(3)
    chng_dropdown(2)  # Changing Surface Class
    move_cursor(1)    
    chng_dropdown(int(condition))  # Changing condition
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

for line in fileinput.input('../data/input2.txt'):
    srt = line
    params = line.split(',')
    analysis_run(params[0],int(params[1]),int(params[2]),int(params[3]),int(params[4]))
    print '%s' %(params[0]) + "Done"
    time.sleep(30)
    dlg.TypeKeys('%{F4}')
    time.sleep(10)
    

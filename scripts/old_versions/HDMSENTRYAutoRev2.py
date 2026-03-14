import pywinauto
import time
import fileinput

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
    		
def analysis_run(name, climate_zone, traffic_growth, traffic_volume, surface_class, condition):
    global app, dlg
    app = pywinauto.application.Application().start('"C:\Program Files (x86)\HDM-Sentry\HDMSentry.exe"')
    dlg = app.top_window_()
    dlg.MoveWindow(0,0)
    move_cursor(3)
    click_element(1)
    move_cursor(2)
    fill_text(name) # Run name
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

for line in fileinput.input('../data/input.txt'):
    srt = line
    params = line.split(',')
    analysis_run(params[0],int(params[1]),int(params[2]),int(params[3]),int(params[4]),int(params[5]))
    print 'Waiting for analysis'
    time.sleep(30)
    dlg.TypeKeys('%{F4}')
    

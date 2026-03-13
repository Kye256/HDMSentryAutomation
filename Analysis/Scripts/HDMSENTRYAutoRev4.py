import pywinauto
import time
import fileinput

# Reads input parameters from input2.txt and creates HDMSENTY analysis. 

global dlg, app

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
        #time.sleep(1)

def fill_text(text):
    dlg.TypeKeys(text)
    		
def analysis_run(name, traffic_growth, condition, traffic_volume, geometry):
    global app, dlg
    app = pywinauto.application.Application().start('"C:\Program Files (x86)\HDM-Sentry\HDMSentry.exe"')
    #time.sleep(10)
    dlg = app.top_window_()
    dlg.MoveWindow(0,0)  # Moves the window to top left hand corner so that in case we need to use the mouse we know where the window is
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
    #move_cursor(2)
    chng_dropdown(1) # Setting vehicle fleet
    move_cursor(1)
    chng_dropdown(7) # Setting climate zone
    move_cursor(1)   
    chng_dropdown(int(traffic_growth)) # Setting Traffic Growth
    move_cursor(2)
    click_element(1)
    move_cursor(2)
    fill_text('Trial') # Section name
    move_cursor(1)
    chng_dropdown(int(traffic_volume))  # Setting Traffic Volume
    move_cursor(2)
    chng_dropdown(int(geometry)) # Setting the geometry
    move_cursor(1)
    chng_dropdown(2)  # Setting Surface Class (0: Surface dressing 1: Asphaltic concrete  2: gravel 3: earth)
    move_cursor(1)    
    chng_dropdown(int(condition))  # Setting condition
    move_cursor(1)
    fill_text('30')
    move_cursor(2)
    click_element(1)
    move_cursor(5)
    chng_dropdown(1)  # Setting Alternative 1 
    move_cursor(1)
    chng_dropdown(2)  # Setting Alternative 2 (For Unpaved surface: 1: Regravelling 2: Upgrading) (For Bituminous: 1: Reseal 2: Overlay 3: Reconstruction 4: Minimum maintenance)
    move_cursor(3)
    click_element(1)

input_file = 'C:\Users\Kyeyune.PKAZIBWE-LAP\Documents\Msc. RoadMgtAndEng\Academics\IndividualProject\Analysis\Scripts\\input3rerun2.txt'
print " Using: %s as input file" % input_file  
for line in fileinput.input(input_file):
    srt = line
    params = line.split(',')
    analysis_run(params[0],int(params[1]),int(params[2]),int(params[3]),int(params[4]))
    print '%s' %(params[0]) + "Done"
    time.sleep(30)
    dlg.TypeKeys('%{F4}')
    time.sleep(5)  

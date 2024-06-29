import PySimpleGUI as pg
import joblib

volts = 0.0
height = 0.0
soil_type = 0
#model
model = joblib.load('D:\\Projects\\mine detecter proj\\mine_model.joblib')
#theme
pg.theme("DarkBrown4")
#layout
layout = [
    [pg.Push(),pg.Text("AI FLC sensor based Mine detector"),pg.Push()],
    [pg.Text("Voltage:",tooltip="float value between 0v and 1v given by FLC sensor")],
    [pg.InputText()],
    [pg.Text("Height of Sensor:",tooltip="float value between 0m and 1m")],
    [pg.InputText()],
    [pg.Text("Soil Type:",tooltip="""
             1= Dry and Sandy
             2= Dry and Humus
             3= Dry and Limy
             4= Humid and Sandy
             5= Humid and Humus
             6= Humid and Limy
             """)],
    [pg.InputText()],
    [pg.Push(),pg.Button("Detect"),pg.Push()],
    [pg.Push(),pg.Text("Press Detect to get Value",key='out',),pg.Push()]
]
#window
window = pg.Window("AI based Mine detector",layout)

#loop
while True:
    event, values=window.read()
    if event == pg.WIN_CLOSED:
        break
    volts = values[0]
    height = values[1]
    soil_type = values[2]
    answer = model.predict([[volts,height,soil_type]])
    if answer == 0:
        print("There is no mine in the area!")
        window['out'].update("No Mine Detected")

    elif answer == 1:
        print("There is a mine in the area!")
        window['out'].update("Mine Detected")


#end
window.close()
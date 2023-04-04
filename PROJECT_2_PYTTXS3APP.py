import PySimpleGUI as sg
import pyttsx3

engine = pyttsx3.init()
VOICE_TYPES = engine.getProperty('voices')



layout = [    [sg.Text('Select the type of voice:',text_color='black',background_color='red'),
               sg.Radio('Male Voice', 'RADIO1', default=True, key='male',background_color='blue'),
               sg.Radio('Female Voice', 'RADIO1', key='female',background_color='pink')],
              [sg.Text('Enter text to speak:',text_color='black',background_color='gold',)],
              [sg.Text('Volume:'),
              sg.Slider(range=(0, 150), default_value=50, orientation='h', key='-VOLUME-')],
              [sg.Text('Rate:'),
             sg.Slider(range=(0, 200), default_value=100, orientation='h', key='-RATE-')],     
             [sg.InputText(key='input'),sg.Button('Speak',button_color='green')],
   
]

window = sg.Window('TEXT TO SPEECH CONVETOR', layout,background_color='grey')

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Speak':
        text = values['input']
        volume = values['-VOLUME-']
        rate = values['-RATE-']
        if values['male']:
            engine.setProperty('voice', VOICE_TYPES[0].id)
        elif values['female']:
           engine.setProperty('voice', VOICE_TYPES[1].id) 
           engine.setProperty('volume', volume/150)
           engine.setProperty('rate', rate)
           engine.say(text)
           engine.runAndWait()

window.close()
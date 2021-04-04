import PySimpleGUI as sg

class Layout:

    def __init__(self):
        # Define the window's contents.
        self.layout = [[sg.Text("Tecla alfanumérica 1"), sg.Input(enable_events=True, key='key1', size=[5, 5])],
                  [sg.Text("Duração (seg):"), sg.Input(default_text=5, enable_events=True, key='duration1', size=[8,5]),
                   sg.Text("Delay (seg):"), sg.Input(default_text=0, enable_events=True, key='delay1', size=[5,5])],

                  [sg.Text('')],

                  [sg.Text("Tecla alfanumérica 2"), sg.Input(enable_events=True, key='key2', size=[5, 5])],

                  [sg.Text('')],

                  [sg.Text("Mouse"), sg.Combo(['nenhum', 'left', 'right'], default_value='nenhum', key='mouseButton')],
                  [sg.Text("Duração (seg):"), sg.Input(default_text=5, enable_events=True, key='duration3', size=[8, 5]),
                   sg.Text("Delay (seg):"), sg.Input(default_text=0, enable_events=True, key='delay3', size=[5, 5])],

                  [sg.Text('')],

                  [sg.Text("Atalho para iniciar o macro:")],
                  [sg.Text("Tecla 1:"), sg.Input(default_text='h', enable_events=True, key='keyInit1', size=[5, 5])],

                  [sg.Text('')],

                  [sg.Text("Delay para iniciar o macro:")],
                  [sg.Text("Delay (seg):"), sg.Input(default_text=0, enable_events=True, key='delayInit', size=[5, 5])],

                  [sg.Text('')],

                  [sg.Button('Aceitar definições', key='startMacro'), sg.Button('Fechar macro', key='closeMacro')]]

        # Create the window
        self.window = sg.Window('simpleMacro', self.layout, size=[400, 400])
        self.event, self.values = self.window.read()

    def run(self):
        # Display and interact with the Window using an Event Loop
        while True:
            event, values = self.window.read()

            if event == sg.WINDOW_CLOSED or event == 'closeMacro':
                break

            if len(values['key1']) > 1:
                self.window['key1'].Update(values['key1'][:-1])
            if len(values['key2']) > 1:
                self.window['key2'].Update(values['key2'][:-1])

            if len(values['keyInit1']) > 1:
                self.window['keyInit1'].Update(values['keyInit1'][:-1])

            if values['duration1'] == "":
                values['duration1'] = 1
                self.window['duration1'].Update(values['duration1'])

            if values['delay1'] == "":
                values['delay1'] = 0
                self.window['delay1'].Update(values['delay1'])

            if values['duration3'] == "":
                values['duration3'] = 1
                self.window['duration3'].Update(values['duration3'])
            if values['delay3'] == "":
                values['delay3'] = 0
                self.window['delay3'].Update(values['delay3'])

            if event == 'startMacro':
                try:
                    if (values['key1'] != "" or values['key2'] != "" or values['mouseButton'] != 'nenhum') and values['keyInit1'] != '':
                        break
                except:
                    pass

        self.event, self.values = self.window.read()

        # Finish up by removing from the screen
        self.window.close()

from macro import Macro
from pynput.keyboard import Key, Listener
import time
from interface import Layout


class Main:

    def __init__(self):
        self.macro = Macro()
        self.layout = Layout()
        self.timer = 0

    def startLayout(self):
        self.layout.run()

    def run(self):
        time.sleep(int(self.layout.values['delayInit']))
        while self.macro.macroAtivo:
            try:
                if self.layout.values['key2'] == "":
                    self.macro.press_key(int(self.layout.values['duration1']), self.layout.values['key1'],
                                         int(self.layout.values['delay1']))
                elif self.layout.values['key1'] == "":
                    self.macro.press_key(int(self.layout.values['duration1']), self.layout.values['key2'],
                                         int(self.layout.values['delay1']))
                else:
                    self.macro.press_two_keys(int(self.layout.values['duration1']), self.layout.values['key1'],
                                         self.layout.values['key2'], int(self.layout.values['delay1']))

                if self.layout.values['mouseButton'] != 'nenhum':
                    self.macro.click_mouse(int(self.layout.values['duration3']), self.layout.values['mouseButton'],
                                           int(self.layout.values['delay3']))

                break

            except:
                pass


main = Main()
main.startLayout()


def on_press(key):
    if 'char' in dir(key):  # check if char method exists,
        if key.char == main.layout.values['keyInit1']:
            main.macro.macroAtivo = True
            return False


def on_release(key):
    pass


with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

main.run()





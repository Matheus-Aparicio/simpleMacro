import easygui
from macro import Macro
from pynput.keyboard import Key, Listener
import pyautogui


class Main:

    def __init__(self):
        self.macro = Macro()

    def start(self):
        easygui.msgbox("Aperte H para ativar ou desativar o macro.\n"
                       "O macro será ativado após 5 segundos.", title="Instruções")

    def end(self):
        while self.macro.macroAtivo:
            self.macro.holdW(self.macro.tempo)
            pyautogui.press('enter')


main = Main()
main.start()


def on_press(key):
    if 'char' in dir(key):  # check if char method exists,
        if key.char == 'h':  # check if it is 'q' key
            main.macro.macroAtivo = True
            return False


def on_release(key):
    pass


with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

main.end()





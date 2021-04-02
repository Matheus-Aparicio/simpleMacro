import pyautogui
import time


class Macro:

    def __init__(self):
        self.__macroAtivo = False
        self.__tempo = 20
        self.__contador = 0
        self.__delay = 0

    @property
    def macroAtivo(self):
        return self.__macroAtivo

    @property
    def tempo(self):
        return self.__tempo

    @property
    def contador(self):
        return self.__contador

    @property
    def delay(self):
        return self.__delay

    @macroAtivo.setter
    def macroAtivo(self, ativo: bool):
        self.__macroAtivo = ativo

    @tempo.setter
    def tempo(self, tempo: float):
        self.__tempo = tempo

    @contador.setter
    def contador(self, contador: float):
        self.__contador = contador

    @delay.setter
    def delay(self, delay: float):
        self.__delay = delay

    def holdW(self, holdTime: int):
        start = time.time()
        while time.time() - start < holdTime:
            pyautogui.press('w')

    def holdRB(self, holdTime: int):
        start = time.time()
        while time.time() - start < holdTime:
            pyautogui.click(button='right')

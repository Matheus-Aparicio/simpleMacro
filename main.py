import pyautogui
import time
import easygui
from pynput.keyboard import Key, Listener

class Macro:

    def __init__(self):
        self.__macroAtivo = False
        self.__tempoPequeno = 5
        self.__tempoMedio = 10
        self.__tempoGrande = 15
        self.__tempoAndar = 20

        self.__contadorPequeno = 0
        self.__contadorMedio = 0
        self.__contadorGrande = 0

    @property
    def macroAtivo(self):
        return self.__macroAtivo

    @macroAtivo.setter
    def macroAtivo(self, ativo: bool):
        self.__macroAtivo = ativo

    @property
    def tempoPequeno(self):
        return self.__tempoPequeno

    @property
    def tempoMedio(self):
        return self.__tempoMedio

    @property
    def tempoGrande(self):
        return self.__tempoGrande

    @property
    def tempoAndar(self):
        return self.__tempoAndar

    @property
    def contadorPequeno(self):
        return self.__contadorPequeno

    @contadorPequeno.setter
    def contadorPequeno(self, numero: int):
        self.__contadorPequeno = numero

    @property
    def contadorMedio(self):
        return self.__contadorMedio

    @contadorMedio.setter
    def contadorMedio(self, numero: int):
        self.__contadorMedio = numero

    @property
    def contadorGrande(self):
        return self.__contadorGrande

    @contadorGrande.setter
    def contadorGrande(self, numero: int):
        self.__contadorGrande = numero


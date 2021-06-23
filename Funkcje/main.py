import Wprowadzenie.Funkcje._01_Podstawy as p
import Wprowadzenie.Funkcje._02_argumenty as a
import Wprowadzenie.Funkcje._03_Zaawansowane as z
import Wprowadzenie.Funkcje._06_generatory as gen
from Wprowadzenie.Funkcje._06_generatory import *


def podstawy_test():
    #p.przyklad_funkcji()
    #p.zakres_globalny()
    #p.pokaz_x()
    #p.f_fabryczne_test()
    #p.zakresy_zagniezdzone_lambda_test()
    #p.zmienne_nonlocal_test()
    p.nonlocal_inna_wersja_test()

def argumenty_test():
    #a.argumenty_modyfikowalne_test()
    #a.zwracanie_kilku_argumentow_test()
    #a.slowa_kluczowe_test()
    #a.dowolna_liczba_argumentow_test()
    a.dowolna_liczba_argumentow_test_2()

def zaawansowane_test():
    #z.rekurencja_test()
    #z.posrednie_wywolanie_funkcji_test()
    z.lambda_test()

def generatory_test():
    #gen.przyklad_generatora_test()
    #gen.wyrazenie_generatora()
    #gen.implementacja_zip_map()
    #gen.implementacja_zip_map_2()
    implementacja_zip_map_2()

if __name__ == '__main__':
    #podstawy_test()
    argumenty_test()
    #zaawansowane_test()
    #generatory_test()
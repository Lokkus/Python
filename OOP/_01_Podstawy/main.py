import Wprowadzenie.OOP._01_Podstawy._01_Podstawy as p
import Wprowadzenie.OOP._01_Podstawy._02_Realistyczny_przyklad as rp
import Wprowadzenie.OOP._01_Podstawy._03_Szczegoly as sz
import Wprowadzenie.OOP._01_Podstawy._04_Przeciazanie_operatorow as po
import Wprowadzenie.OOP._01_Podstawy._05_Projektowanie_z_uzyciem_klas as uk
import Wprowadzenie.OOP._01_Podstawy._06_temp as t


def podstawy_test():
    #p.first_class_test()
    #p.second_class_test()
    p.third_class_test()

def realistyczny_przyklad_test():
    #rp.realistyczny_przyklad_test()
    rp.realistyczny_przyklad_test_2()

def szczegoly_test():
    #sz.wywolywanie_danych_z_klasy()
    #sz.wywolywanie_konstruktorow_z_klasy_nadrzednej()
    sz.klasy_abstrakcyjne_test()

def przeladowanie_operatorow_test():
    #po.przeladowany_operator_sub()
    #po.test_getitem()
    #po.test_getitem_slice()
    #po.test_squares()
    #po.test_iters()
    #po.emulowanie_prywatnosci_test()
    po.callee_test()

def projektowanie_z_uzyciem_klas_test():
    #uk.projektowanie_z_uzyciem_klas()
    #uk.zwiazek_jest_test()
    #uk.atrybuty_pseudoprywatne_test()
    #uk.metody_zwiazane_test()
    uk.wypisywanie_atrybutow_test()

if __name__ == '__main__':
    #podstawy_test()
    #realistyczny_przyklad_test()
    #szczegoly_test()
    #przeladowanie_operatorow_test()
    #projektowanie_z_uzyciem_klas_test()
    t.temp_test()
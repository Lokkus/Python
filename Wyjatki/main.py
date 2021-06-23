import Wprowadzenie.Wyjatki._01_wyjatki_podstawy as wp
import Wprowadzenie.Wyjatki._02_szczegolowe_informacje as si


def podstawy_test():
    wp.fetcher_test()
    #wp.f_wykorzystujaca_klase_wyjatkow_test()

def szczegolowe_informacje_test():
    #si.dzielenie_przez_zero_test()
    si.dodawanie_roznych_typow_test()

if __name__ == "__main__":
    #podstawy_test()
    szczegolowe_informacje_test()
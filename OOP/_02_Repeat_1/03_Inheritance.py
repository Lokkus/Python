class Uart:
    def __init__(self, gpio, pin_tx, pin_rx):
        self.gpio = gpio
        self.pin_tx = pin_tx
        self.pin_rx = pin_rx

    def send_data(self, string):
        print(string)

    def __str__(self):
        return f'Uart: GPIO: {self.gpio}, RX: {self.pin_tx}, TX: {self.pin_rx}'


class Logger(Uart):
    # ponizej, jak mozna pprzedefiniowac __init__ w klasie pochodnej
    # def __init__(self):
    #     super(Logger, self).__init__('GPIOD', 'PIN_6', 'PIN_77')

    def send_data(self, string):
        print(f'Przekazane parametry: GPIO: {self.gpio}, TX: {self.pin_tx}, RX: {self.pin_rx}')
        #Uart.send_data(self, string)
        super(Logger, self).send_data(string)

def test_logger():
    lista_logger = [Uart('GPIOD', 'PIN_11', 'PIN_12'), Logger('GPIOA', 'PIN_1', 'PIN_2'),
                    Logger('GPIOB', 'PIN_3', 'PIN_4'), Logger('GPIOC', 'PIN_5', 'PIN_6')]

    for x in lista_logger:
        x.send_data('Jakis string dla testow')
        print('\n')


# inny przyklad
class Person:
    def __init__(self, name, surname, position, salary=0):
        self.name = name
        self.surname = surname
        self.position = position
        self.salary = salary

    def gainSalary(self, percent):
        self.salary = int(self.salary + (percent/100*self.salary))

    def __str__(self):
        return (f'Person: Name: {self.name}, Surname: {self.surname}, Position: {self.position}, Salary: {self.salary}')

class Manager(Person):
    def __init__(self, name, surname, salary):
        super(Manager, self).__init__(name, surname, 'Manager', salary)

    def gainSalary(self, percent, bonus=10):
        super(Manager, self).gainSalary(percent+bonus)


def test_person():
    anna = Person('Anna', 'Iksinska', 'Programmer', 100)
    bob = Person('Bob', 'Ygrek', 'Boss', 300)
    adam = Manager('Adam', 'Novak', 200)
    print(anna)
    print(bob)
    print(adam)

    print('--after changes--')
    list_of_person = [anna, bob, adam]
    for x in list_of_person:
        x.gainSalary(10)
        print(x)





if __name__ == '__main__':
    test_person()







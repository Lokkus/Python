class Rec: pass


def rec_class_test():
    Rec.name = 'Name'
    Rec.surname = 'Surname'
    Rec.phone = 123456789
    Rec.mail = 'name.surname@rec.com'
    return Rec


if __name__ == '__main__':
    r = rec_class_test()
    print(r.name)           #Name
    print(Rec.mail)         #123456789
    print(Rec.phone)        #name.surname@rec.com
    print(Rec.__dict__.keys())
    print(Rec.__bases__)
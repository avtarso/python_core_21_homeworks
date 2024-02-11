from collections import UserDict
from datetime import date, datetime


class Field:
    def __init__(self, value):
        self.value = value


    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Birthday(Field):
    def __init__(self, value):
        self.__value = None
        self.value = value        
    
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        try:
            self.__value = datetime.strptime(value, "%d/%m/%Y")
        except ValueError:
            print('Waiting format of date - DD/MM/YYYY. Reinput, please')

    def __str__(self):
        return self.value.strftime('%d/%m/%Y')


class Phone(Field):
    def __init__(self, value):
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if len(value) != 10 or not value.isdigit():
            raise ValueError('Incorrect number format. Please enter a 10-digit number.')
        self.__value = value  


class Record:
    def __init__(self, name):
       self.name = Name(name)
       self.phones = []
       self.birthday = ""

    def __str__(self):
        phones_str = '; '.join(p.value for p in self.phones)
        birthday_str = f", birthday: {self.birthday.value.strftime('%d/%m/%Y')}" if self.birthday else ""
        return f"Contact name: {self.name.value}, phones: {phones_str}{birthday_str}"

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        for i in self.phones:
            if phone == i.value:
                self.phones.remove(i)
                return True
        raise ValueError('Incorrect number. Reinput, please')

    def edit_phone(self, old_phone, edited_phone):
        cash_phones = []
        for i in self.phones:
            cash_phones.append(i.value)
        if old_phone in cash_phones:
            new_phones = []
            for i in self.phones:
                if i.value == old_phone:
                    new_phones.append(Phone(edited_phone))
                else:
                    new_phones.append(Phone(i.value))
            self.phones = new_phones
            return True
        else: 
            raise ValueError('Incorrect number. Reinput, please')

    def find_phone(self, phone):
        cash_phones = []
        for i in self.phones:
            cash_phones.append(i.value)
        if phone in cash_phones:
            for i in self.phones:
                if phone == i.value:
                    return i
        else:
            return None

    def add_birthday(self, birthday):
        if not self.birthday:
            self.birthday = Birthday(birthday)
        else:
            print(f'Record {self.name} yet have field birthday - {self.birthday.value.strftime("%d/%m/%Y")}')

    def edit_birthday(self, new_birthday): #в завданні відсутній, але потрібний для консистентності
        pass 

    def delete_birthday(self): #в завданні відсутній, але потрібний для консистентності
        pass 

    def days_to_birthday(self):
        if not self.birthday:
            return f"Record {self.name} saved without birthday"
        today_date = date.today()
        birthday_date = date(today_date.year, self.birthday.value.month, self.birthday.value.day)
        if birthday_date < today_date:
            birthday_date = birthday_date.replace(year=today_date.year + 1)
        delta = birthday_date - today_date
        return delta.days


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        if name in self:
            for i in self:
                if i == name:
                    return self.data[i]
        else:
            return None

    def delete(self, name):
        if name in self:
            for i in self:
                if i == name:
                    self.data.pop(name)
                    return True
        else:
            return None

    def iterator_simple(self):
        PAG = 3
        st_list, obj_len = [], len(self.data)

        for i, (name, record) in enumerate(self.data.items(), 1):
            st_list.append(str(record))
            if i % PAG == 0:
                print('\n'.join(st_list))
                st_list.clear()
                if i != obj_len and input(f"-->You can ^^see^^ {i} records from {obj_len}\n-->press any key to continue or 'q' to exit --> ").lower() == "q":
                    break
        if st_list:
            print('\n'.join(st_list))
        print(f"-->You can ^^see^^ {i} records from {obj_len}\n")

    def iterator(self):
        PAG = 3
        obj_len = len(self.data)
        i = 0

        def generate_records():
            for name, record in self.data.items():
                yield str(record)

        record_generator = generate_records()
        while True:
            portion = [next(record_generator, None) for _ in range(PAG)]
            portion = [item for item in portion if item is not None]  # Исключить None (когда записи закончились)
            i += len(portion)
            print('\n'.join(portion))
            if not portion or i == obj_len:
                print(f"-->You can ^^see^^ {i} records from {obj_len}\n")
                break
            if input(f"-->You can ^^see^^ {i} records from {obj_len}\n-->press any key to continue or 'q' to exit --> ").lower() == "q":
                break


    


book = AddressBook()

john_record1 = Record("John1")
john_record1.add_phone("1234567890")
book.add_record(john_record1)

jane_record1 = Record("Jane1")
jane_record1.add_phone("9876543210")
book.add_record(jane_record1)

john_record2 = Record("John2")
john_record2.add_phone("1234567890")
john_record2.add_birthday("01/01/2024")
print("\n>>>Second add record birthday\n")
john_record2.add_birthday("01/01/2024")
book.add_record(john_record2)

jane_record2 = Record("Jane2")
jane_record2.add_phone("9876543210")
jane_record2.add_birthday("01/06/2024")
book.add_record(jane_record2)

john_record3 = Record("John3")
john_record3.add_phone("1234567890")
book.add_record(john_record3)

jane_record3 = Record("Jane3")
jane_record3.add_phone("9876543210")
book.add_record(jane_record3)


print("\n>>>work days_to_birthday()\n")
print(john_record2.days_to_birthday())
print(jane_record2.days_to_birthday())
print(jane_record3.days_to_birthday())

print("\n>>>start pagination version 1\n")
book.iterator()
print("\n>>>end pagination version 1\n")

print("\n>>>start pagination version 2\n")
book.iterator_simple()
print("\n>>>end pagination version 2\n")
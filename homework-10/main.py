from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value


    def __str__(self):
        return str(self.value)
    

class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if len(value) > 10 or len(value) < 10:
            raise ValueError('Incorrect number of digits. Reinput, please')
        elif not value.isdigit():
            raise ValueError('Incorrect sumbols in number. Reinput, please')
        else:
            self.value = value


class Record:

    def __init__(self, name):
       self.name = Name(name)
       self.phones = []


    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    
    
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

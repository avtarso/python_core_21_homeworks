from settings import path_data_base


wellcome_message = f"Please enter your command:  "
hello_message = "How can I help you?"
good_bye_message = "Good bye!"
bad_command = "Incorrect command!"
help_string = """For working with me, please, input one of next command:
"hello" - I print "How can I help you?"
"add [Name] [Phone number]" - I record [Name] and [Phone number]
"change [Name] [Phone number]" - I change [Phone number] for record [Name]
"phone [Name]" - I print phone number for record [Name]
"show all" - I print all recorded phone numbers
"good bye", "close" or "exit" - I stop working
"help" - I print this text"""


def line():
    return "-".center(33, "-")
def header():
    return line() + "\n" + "|{:>15}|{:<15}|".format("Name", "Phone number") + "\n" + line()
def body_card(name, phone):
    return "|{:>15}|{:<15}|".format(name, phone)


def get_database(path):
    with open(path, "r") as fh:
        dict = {}
        one_string = fh.read().split("\n")
        for i in one_string:
            if len(i) > 0:
                record = i.split(",")
                dict[record[0]] = record[1]
        return dict


def save_database(path, dict_database):
    with open(path, "w") as fh:
        string_database = ""
        for i in dict_database:
            if string_database:
                string_database += "\n"
            string_database = string_database + i + "," + dict_database[i]
        fh.write(string_database)
        return True
    
dict_data_base = get_database(path_data_base)


def show_all(dict_data_base):  
    output_string = header() + "\n"
    for i in dict_data_base:
        output_string = output_string + body_card(i, dict_data_base[i]) + "\n"
    output_string = output_string + line()
    return output_string


def input_error(func):
    def inner(string):
        command_sting = string.split()
        if command_sting[0].lower() == "phone":
            if len(command_sting) == 1:
                return "Please, retry request - phone [name] with [name]"
            try:
                result = func(command_sting[1])
            except KeyError:
                return f"There is no entry with a name '{command_sting[1]}'. Please, retry the request with a different name - phone [name]"
            return result
        
        if command_sting[0].lower() == "add":
            if len(command_sting) == 1:
                return "Please, retry request - add [name] [phone number] with [name] and [phone number]"
            if command_sting[1] in dict_data_base:
                return f"""An entry with the name '{command_sting[1]}' is among existing entries.
You can edit it with a special command - change [name] [phone]
""" + show_phone(command_sting[1])
            result = func(command_sting[1], command_sting[2]) + "\n" + f"Entry with name '{command_sting[1]}' has been created\n" + show_phone(command_sting[1])
            return result
                
        if command_sting[0].lower() == "change":
            if len(command_sting) == 1 or len(command_sting) == 2:
                return "Please, retry request - change [name] [phone number] with [name] and [phone number]"
            if command_sting[1] in dict_data_base:
                result = func(command_sting[1], command_sting[2]) + "\n" + f"Entry with name '{command_sting[1]}' has been changed\n" + show_phone(command_sting[1])
                return result
            else:
                return f"""An entry with the name '{command_sting[1]}' is not among existing entries.
You can add it with a special command - add [name] [phone number]"""

    return inner


def show_phone(name):
    output_string = header() + "\n"
    output_string = output_string + body_card(name, dict_data_base[name]) + "\n"
    output_string = output_string + line()
    return output_string

get_phone = input_error(show_phone)


def write_contact(name, phone):
    dict_data_base[name] = phone
    save_database(path_data_base, dict_data_base)
    return "Successfully completed!"
new_phone = input_error(write_contact)
edit_phone = input_error(write_contact)


def main():

    while True:
        user_input = input(wellcome_message)
        user_command = user_input.lower()
 
        if user_command == "help": 
            print(help_string)
        elif user_command == "hello":
            print(hello_message)
        elif user_command == "show all":
            print(show_all(dict_data_base))
        elif user_command.startswith("phone"):
            print(get_phone(user_input))
        elif user_command.startswith("add"):
            print(new_phone(user_input))
        elif user_command.startswith("change"):
            print(edit_phone(user_input))
        elif user_command in ["good bye", "close", "exit"]:
            print(good_bye_message)
            break

        else: print(bad_command + "\n" + help_string)

if __name__ == '__main__':
    main()
def screen():
    print("*" * 50)
    print("Welcome to Business card management system V1.0")
    print("\n1.Create new care")
    print("2.Show all")
    print("3.Inquire information")
    print("\n0.Exit")
    print("*" * 50)
    action = input("Please choose one function：")
    print("You want to：", action)
    return action


card_list = []


def function1():
    print("-" * 50)
    print("Function: Create new card\n")
    name_str = input("Name：")
    phone_str = input("Phone Number：")
    qq_str = input("Email：")
    card_dict = {"name": name_str,
                 "phone": phone_str,
                 "qq": qq_str}
    card_list.append(card_dict)
    print(name_str, "now is in the system！")


def function2():
    print("-" * 50)
    print("Function: Show all\n")
    if len(card_list) == 0:
        print("No data. Please add some cards")
        return
    #表头
    print("Name\t\tPhone\t\tEmail\t\t")
    print("-" * 50)
    for info in card_list:
        print("%s\t\t%s\t\t%s\t\t"% (info["name"], info["phone"], info["qq"]))


def deal_card(temp_dict):
    action = input("You want to:"
                   " [1] Modify [2] Delete [0] Back")
    if action == "1":
        temp_dict["name"] = input_info(temp_dict["name"], "new name: ")
        temp_dict["phone"] = input_info(temp_dict["phone"], "new phone number: ")
        temp_dict["qq"] = input_info(temp_dict["qq"], "new email: ")
        print("Modified.")
    elif action == "2":
        card_list.remove(temp_dict)
        print("Deleted.")


def input_info(dict_value, new_massage):
    result = input(new_massage)
    if len(result) > 0:
        return result
    else:
        return dict_value

def function3():
    print("-" * 50)
    print("Function: Inquire information")
    find_name = input("you want to find who：")
    for card_dict in card_list:
        if card_dict["name"] == find_name:
            print("got it!")
            print("Name\t\t\tPhone\t\t\tEmail\t\t\t")
            print("%s\t\t\t%s\t\t\t%s\t\t\t" % (card_dict["name"], card_dict["phone"], card_dict["qq"]))
            deal_card(card_dict)
            break
    else:
        print("sorry we cannot find.QAQ")


def function0():
    print("Thanks! Welcome next time!")



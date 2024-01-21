import Transaction

print("Budget-Bear - Version 0.0.1")

list = []

print("Main Menu\n"
      "[1] Add\n"
      "[2] Edit\n"
      "[3] Delete\n")

print("Selection :")
inp = input()
if inp == "1":
    date = input("Enter date : ")
    amount = input("Enter amount : ")
    type = input("Enter type : ")
    company = input("Enter company : ")
    description = input("Enter description : ")
    category = input("Enter category : ")
    list.append(Transaction.Transaction(date, amount, type, company, description, category))

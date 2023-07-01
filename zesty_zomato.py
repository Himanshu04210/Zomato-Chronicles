import os
import json

def addDish():
    dishId = int(input("Enter dish Id: "))
    dishName = input("Enter dish name: ")
    dishPrice = int(input("Enter dish price: "))
    dishAvailability = input("Enter dish availability (Yes/No): ").lower()
    file_path = "zomato.txt"

    try:
        with open(file_path, "r") as file:
            lines = file.readlines()

            for line in lines:
                dish_data = json.loads(line)
                if dish_data["dishId"] == dishId:
                    return "Dish already exists"

    except FileNotFoundError:
        string =  "File does not exist."

    dish = {
        "dishId": dishId,
        "dishName": dishName,
        "dishPrice": dishPrice,
        "dishAvailability": dishAvailability
    }
    if not os.path.exists(file_path):
        with open(file_path, "w"):
            pass
    with open(file_path, "a") as sold_file:
        sold_file.write(json.dumps(dish) + "\n")

    return "Dish added successfully"


def seeTheMenu():
    file_path = "zomato.txt"

    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            print("Details of dishes")
            print("----------")
            for line in lines:
                dish_data = json.loads(line)
                dishId = dish_data["dishId"]
                dishName = dish_data["dishName"]
                dishPrice = dish_data["dishPrice"]
                dishAvailability = dish_data["dishAvailability"]

                print(f"Dish:- Dish Id- {dishId},")
                print(f"Dish name- {dishName},")
                print(f"Dish price- {dishPrice},")
                print(f"Dish Availability- {dishAvailability}\n")
                print("+++++++++")
            print("-----------")

    except FileNotFoundError:
        print("File does not exist.");


def updateDishAvailability():
   
    dishId  = int(input("Enter dish id : "))
    file_path = "zomato.txt"
    updated_lines = []

    try:
        with open(file_path, "r") as file:
            lines = file.readlines()

            for line in lines:
                dish_data = json.loads(line)
                if dish_data["dishId"] == dishId:
                    dishAvailability = input("Enter new availability (Yes/No): ").lower()
                    dish_data["dishAvailability"] = dishAvailability

                updated_lines.append(json.dumps(dish_data) + "\n")

        with open(file_path, "w") as file:
            file.writelines(updated_lines)

        return "Dish availability updated successfully"

    except FileNotFoundError:
        return "File does not exist."

def removeDish():
    dishId = int(input("Enter dish ID to remove: "))
    file_path = "zomato.txt"

    try:
        with open(file_path, "r") as file:
            lines = file.readlines()

        with open(file_path, "w") as file:
            dish_removed = False

            for line in lines:
                dish_data = json.loads(line)
                if dish_data["dishId"] == dishId:
                    dish_removed = True
                    continue

                file.write(json.dumps(dish_data) + "\n")

        if dish_removed:
            return "Dish removed successfully"
        else:
            return "Dish with the provided ID does not exist"

    except FileNotFoundError:
        return "File does not exist."

def buyDish():
    dishId = int(input("Enter dish ID to buy: "))
    file_path = "zomato.txt"
    sold_file_path = "soldDishes.txt"

    try:
        with open(file_path, "r") as file:
            dishes = file.readlines()

        for line in dishes:
            dish = json.loads(line)
            if dish["dishId"] == dishId:
                if dish["dishAvailability"] == "yes":
                    print("Dish price is " + str(dish["dishPrice"]))
                    money = int(input("Pay the money: "))
                    if dish["dishPrice"] <= money:
                        if not os.path.exists(sold_file_path):
                            with open(sold_file_path, "w"):
                                pass

                        with open(sold_file_path, "a") as sold_file:
                            sold_file.write(json.dumps(dish) + "\n")
                        return "Order placed successfully"
                    else:
                        return "Money is not sufficient"
                else:
                    return "Dish is not available for purchase"

        return "Dish with the provided ID does not exist"

    except FileNotFoundError:
        return "File does not exist."


def seeAllTheSoldDishes():
    file_path = "soldDishes.txt"

    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            print("----------")
            for line in lines:
                dish_data = json.loads(line)
                dishId = dish_data["dishId"]
                dishName = dish_data["dishName"]
                dishPrice = dish_data["dishPrice"]
                dishAvailability = dish_data["dishAvailability"]

                print(f"Dish:- Dish Id- {dishId},")
                print(f"Dish name- {dishName},")
                print(f"Dish price- {dishPrice},")
                print(f"Dish Availability- {dishAvailability}\n")
                print("+++++++++")
            print("-----------")

    except FileNotFoundError:
        print("File does not exist.");
        
 

def startProgram() :
    
    while True:
        
        role = str(input("Provide your role (costumer/Staff/Exit) : ")).lower()
        
        if(role == "exit") : 
            return
        
        if(role == "staff") :
            staffRole()
        else :
            customerRole();
            


def customerRole() :
    
    while True :
        print("select your choice")
        print("1. See the menu") 
        print("2. Buy a dish")
        print("3. exit")
        
        choice = int(input("Enter your choice : "))
        if choice == 1 :
            seeTheMenu();
        elif choice == 2 :
            print(buyDish());
        elif choice == 3 :
            return;
        else :
            print("Invalid Choice, Try again ")
    
def staffRole() :
    password = input("Enter the common password for Staff : ").lower()
    if(password != "admin") :
        return; 
    while True :
        print("1. See the menu")
        print("2. Add the dish")
        print("3. update the availability")
        print("4. removed a dish")
        print("5. See All the sold dished")
        print("6. Exit")
        choice = int(input("Enter yuor choice : "))
        if choice == 1 :
            seeTheMenu();
        elif choice == 2 :
            print(addDish());
        elif choice == 3 :
            print(updateDishAvailability());
        elif choice == 4 :
            print(removeDish())
        elif choice == 5 :
            seeAllTheSoldDishes();
        elif choice == 6 :
            return;
        else :
            print("Invalid Choice, Try again ")
        
        
        
startProgram()
import datetime
import difflib


def main():
    time = datetime.datetime.now()
    print("""     
                   _______
                  //  ||\ \\
            _____//___||_\ \___
            )  _          _    \\
            |_/ \________/ \___|
           ___\_/________\_/______
       """)

    print("\n\tWELCOME TO CAR RENTAL SHOP!\n")
    print(f"\tCurrent date and time: {time}")

    while True:
        print("""
        ******** Car Rental Shop ********
        1. Add a New Vehicle
        2. Remove a Vehicle
        3. Assign a Job(hire)
        4. Release from assigned job
        5. Available Vehicles
        6. Exit the Program
        """)

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a number!")
            continue

        if choice == 1:
            add_a_new_vehicle()

        elif choice == 2:
            remove_a_vehicle()

        elif choice == 3:
            assign_a_job()

        elif choice == 4:
            release_job()

        elif choice == 5:
            available_vehicles()

        elif choice == 6:
            break

        else:
            print("Please enter a choice between 1-5 only!")


def add_a_new_vehicle():
    while True:
        print("""
        ******** Add a New Vehicle ********
        1. Cars
        2. Vans
        3. 3 Wheelers
        4. Lorries
        5. Trucks
        6. Return to Main Manu
        """)

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a number!")
            continue
        if choice == 1:
            add_car()
        elif choice == 2:
            add_vans()
        elif choice == 3:
            add_3_wheelers()
        elif choice == 4:
            add_lorries()
        elif choice == 5:
            add_trucks()
        elif choice == 6:
            break
        else:
            print("Please enter a valid choice")


def remove_a_vehicle():
    while True:
        print("""
        ******** Delete a Vehicle ********
        1. Cars
        2. Vans
        3. 3 Wheelers
        4. Lorries
        5. Trucks
        6. Return to Main Manu
        """)

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a number!")
            continue
        if choice == 1:
            remove_car()
        elif choice == 2:
            remove_vans()
        elif choice == 3:
            remove_3_wheelers()
        elif choice == 4:
            remove_lorries()
        elif choice == 5:
            remove_trucks()
        elif choice == 6:
            break
        else:
            print("Please enter a valid choice")


def assign_a_job():
    while True:
        print("""
            ******** Assign a job ********
            1. Car
            2. Van
            3. 3 Wheeler
            4. Lorry
            5. Truck
            6. Exit the Program
            """)

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a number!")
            continue

        if choice == 1:
            display_car()
            book_car()

        elif choice == 2:
            display_van()
            book_van()

        elif choice == 3:
            display_wheel()
            book_wheel()

        elif choice == 4:
            display_lorry()
            book_lorry()

        elif choice == 5:
            display_truck()
            book_truck()

        elif choice == 6:
            break

        else:
            print("Please enter a Valid number")


def release_job():
    display_rent_car()
    a_file = open("rent_vehicle.txt", "r")
    lines = a_file.readlines()
    a_file.close()

    del lines[int(input("please enter line number wish to delete")) - 1]
    print("your data deleted Successfully..!")

    new_file = open("rent_vehicle.txt", "w+")
    for line in lines:
        new_file.write(line)
    new_file.close()


def available_vehicles():
    while True:
        print("""
            ******** Available Vehicle for hire ********
            1. Cars
            2. Vans
            3. 3 Wheelers
            4. Lorries
            5. Trucks
            6. Return to Main Manu
            """)
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a number!")
            continue
        if choice == 1:
            view_car()
        elif choice == 2:
            view_vans()
        elif choice == 3:
            view_wheelers()
        elif choice == 4:
            view_lorries()
        elif choice == 5:
            view_trucks()
        elif choice == 6:
            break
        else:
            print("Please enter a valid choice")


# adding new vehicles


def add_car():
    with open("car_details.txt", "a") as text:
        v_type = "Car"
        no_of_passenger = input("Maximum Number of Passenger (3 or 4):")
        air_condition = input("AC / Non AC: ").upper()
        text.write("\n%s:%s:%s" % (v_type, no_of_passenger, air_condition))


def add_vans():
    with open("van_details.txt", "a") as text:
        v_type = "Van"
        no_of_passenger = input("Maximum Number of Passenger (6 or 8):")
        air_condition = input("AC / Non AC: ").upper()
        text.write("\n%s:%s:%s" % (v_type, no_of_passenger, air_condition))


def add_3_wheelers():
    with open("wheeler_details.txt", "a") as text:
        v_type = "3wheeler"
        no_of_passenger = 3
        text.write("\n%s:%s" % (v_type, no_of_passenger))


def add_lorries():
    with open("lorry_details.txt", "a") as text:
        v_type = "Lorrie"
        size = input("Max load (2500kg or 3500kg):")
        text.write("\n%s:%s" % (v_type, size))


def add_trucks():
    with open("truck_details.txt", "a") as text:
        v_type = "Truck"
        size = input("Size of the Truck (7ft or 12ft):")
        text.write("\n%s:%s" % (v_type, size))


# remove vehicle


def remove_car():
    display_car()
    a_file = open("car_details.txt", "r")
    lines = a_file.readlines()
    a_file.close()

    del lines[int(input("please enter line number wish to delete")) - 1]
    print("your data deleted Successfully..!")

    new_file = open("car_details.txt", "w+")
    for line in lines:
        new_file.write(line)
    new_file.close()


def remove_vans():
    display_van()
    a_file = open("van_details.txt", "r")
    lines = a_file.readlines()
    a_file.close()

    del lines[int(input("please enter line number wish to delete")) - 1]
    print("your data deleted Successfully..!")

    new_file = open("van_details.txt", "w+")
    for line in lines:
        new_file.write(line)
    new_file.close()


def remove_3_wheelers():
    display_van()
    a_file = open("van_details.txt", "r")
    lines = a_file.readlines()
    a_file.close()

    del lines[int(input("please enter line number wish to delete")) - 1]
    print("your data deleted Successfully..!")

    new_file = open("van_details.txt", "w+")
    for line in lines:
        new_file.write(line)
    new_file.close()


def remove_lorries():
    display_van()
    a_file = open("lorry_details.txt", "r")
    lines = a_file.readlines()
    a_file.close()

    del lines[int(input("please enter line number wish to delete")) - 1]
    print("your data deleted Successfully..!")

    new_file = open("lorry_details.txt", "w+")
    for line in lines:
        new_file.write(line)
    new_file.close()


def remove_trucks():
    display_van()
    a_file = open("truck_details.txt", "r")
    lines = a_file.readlines()
    a_file.close()

    del lines[int(input("please enter line number wish to delete")) - 1]
    print("your data deleted Successfully..!")

    new_file = open("truck_details.txt", "w+")
    for line in lines:
        new_file.write(line)
    new_file.close()

# Display vehicle info


def display_car():
    with open("car_details.txt", "r") as text:
        lines = text.readlines()
        index = 1
        for line in lines:
            splitter = line.rstrip().split(":")
            v_type = splitter[0]
            no_of_passenger = splitter[1]
            air_condition = splitter[2]
            print("%d. Type: %s No of Passenger: %s AC: %s" % (index, v_type, no_of_passenger, air_condition))
            index += 1


def display_van():
    with open("van_details.txt", "r") as text:
        lines = text.readlines()
        index = 1
        for line in lines:
            splitter = line.rstrip().split(":")
            v_type = splitter[0]
            no_of_passenger = splitter[1]
            air_condition = splitter[2]
            print("%d. Type: %s No of Passenger: %s AC: %s" % (index, v_type, no_of_passenger, air_condition))
            index += 1


def display_wheel():
    with open("wheeler_details.txt", "r") as text:
        lines = text.readlines()
        index = 1
        for line in lines:
            splitter = line.rstrip().split(":")
            v_type = splitter[0]
            no_of_passenger = splitter[1]
            print("%d. Type: %s No of Passenger: %s" % (index, v_type, no_of_passenger))
            index += 1


def display_lorry():
    with open("lorry_details.txt", "r") as text:
        lines = text.readlines()
        index = 1
        for line in lines:
            splitter = line.rstrip().split(":")
            v_type = splitter[0]
            weight = splitter[1]
            print("%d. Type: %s Weight: %s" % (index, v_type, weight))
            index += 1


def display_truck():
    with open("truck_details.txt", "r") as text:
        lines = text.readlines()
        index = 1
        for line in lines:
            splitter = line.rstrip().split(":")
            v_type = splitter[0]
            size = splitter[1]
            print("%d. Type: %s Size: %s" % (index, v_type, size))
            index += 1


def display_rent_car():
    with open("rent_vehicle.txt") as text:
        line = text.readline()
        cnt = 1
        while line:
            line = line.strip()
            print("{}: {}".format(cnt, line.strip()))
            line = text.readline()
            cnt += 1


def book_car():
    read_file = "car_details.txt"
    write_file = "rent_vehicle.txt"
    file = open(read_file, "r")
    data = file.readlines()
    select_vehicle = data[int(input("Please select a Car"))-1]
    file.close()

    with open(write_file, "a+") as text:
        text.write(select_vehicle)
        text.write('\n')


def book_van():
    read_file = "car_details.txt"
    write_file = "rent_vehicle.txt"
    file = open(read_file, "r")
    data = file.readlines()
    select_vehicle = data[int(input("Please select a Car"))-1]
    file.close()

    with open(write_file, "a") as text:
        text.write(select_vehicle)
        text.write('\n')


def book_wheel():
    read_file = "wheeler_details.txt"
    write_file = "rent_vehicle.txt"
    file = open(read_file, "r")
    data = file.readlines()
    select_vehicle = data[int(input("Please select a Car"))-1]
    file.close()

    with open(write_file, "a") as text:
        # text.seek(0)
        text.write(select_vehicle)
        text.write('\n')


def book_lorry():
    read_file = "lorry_details.txt"
    write_file = "rent_vehicle.txt"
    file = open(read_file, "r")
    data = file.readlines()
    select_vehicle = data[int(input("Please select a Car"))-1]
    file.close()

    with open(write_file, "a") as text:
        text.write(select_vehicle)
        text.write('\n')



def book_truck():
    read_file = "truck_details.txt"
    write_file = "rent_vehicle.txt"
    file = open(read_file, "r")
    data = file.readlines()
    select_vehicle = data[int(input("Please select a Car"))-1]
    file.close()

    with open(write_file, "a") as text:
        text.write(select_vehicle)
        text.write('\n')


def view_car():
    car_file = "car_details.txt"
    rent_file = "rent_vehicle.txt"

    with open(car_file) as file_1:
        file_1_text = file_1.readlines()

    with open(rent_file) as file_2:
        file_2_text = file_2.readlines()

    # Find and print the diff:
    for line in difflib.unified_diff(
            file_1_text, file_2_text, fromfile='file1.txt',
            tofile='file2.txt', lineterm=''):
        print(line)


if __name__ == "__main__":
    main()

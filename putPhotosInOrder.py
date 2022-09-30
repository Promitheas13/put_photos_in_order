import os
import shutil
import sys

current_path = os.getcwd()
os_separator = os.path.sep

folder_put_into = "photos"
path = current_path + os_separator + folder_put_into

year_start, year_end = 4, 8
month_start, month_end = 8, 10
# year_start, year_end = 0, 4
# month_start, month_end = 4, 6
months = [[], [], [], [], [], [], [], [], [], [], [], []]
months_names = ["01.January", "02.February", "03.March", "04.April", "05.May", "06.June", "07.July", "08.August",
                "09.September", "10.October", "11.November", "12.December"]
used_months = []
jan, feb, mar, apr, may, jun, jul, aug, sep, octo, nov, dec = [], [], [], [], [], [], [], [], [], [], [], []


def check_folder():
    if os.path.isdir(path):
        return
    else:
        os.mkdir(path)
        print("Directory photos has been created...\n" +
              "Insert all photos / videos inside that directory\n" +
              "When you are done restart the app")
        wait = input("Hit enter to exit.")
        sys.exit().sys.exit()


def create_lists(files, input_year):
    # Create list of files
    global months
    months = [[], [], [], [], [], [], [], [], [], [], [], []]
    for file in files:
        if file[year_start:year_end] == input_year:
            if len(file) > 9:
                get_month = int(file[month_start:month_end])
                months[get_month-1].append(file)

    # Create list of used months
    a = 0
    used_months.clear()
    while a < len(months):
        if len(months[a]) > 0:
            used_months.append(months_names[a])
        a += 1


def create_folders(input_year):
    # Create the year folder first
    temp_path = path + os_separator + input_year
    if os.path.isdir(temp_path):
        return
    else:
        os.mkdir(temp_path)
    # End of the year directory creation

    # Now proceed to the creation of the month directories
    for i in used_months:
        temp_path = path + os_separator + input_year + os_separator + i
        if os.path.isdir(temp_path):
            continue
        else:
            os.mkdir(temp_path)


def copy_files(number, input_year):
    start_path = path + os_separator

    a = 0
    used_months_index = 0
    while a < len(months):          # Run through the entire array
        if len(months[a]) > 0:      # If the array is not empty then enter
            b = 0
            # print("Index point: ", a)
            # print("Month: ", months_names[a])

            while b < len(months[a]):   # Run through the index of the array were is not empty
                number += 1
                from_ = start_path + months[a][b]
                to_ = start_path + input_year + os_separator + used_months[used_months_index] + os_separator
                # print("Move file: ", from_, " to ", to_)
                shutil.move(from_, to_)
                b += 1
            used_months_index += 1
        a += 1

    return number


def create_options(files):
    years = []      # Create the array of options

    for year in files:
        if len(year) > 9:
            years.append(year[year_start:year_end])     # Fill the array with options depending on the existing files

    years = list(dict.fromkeys(years))      # Remove duplicates
    years.sort()    # Sort the array with ascending order

    return years


def menu(options):
    results = []

    works = False
    while not works:
        print("//////////////////////////\n" +
              "// 1. Choose year\n" +
              "// 2. Arrange everything\n" +
              "// 3. Exit\n" +
              "//////////////////////////")

        choice = input("Select: ")
        results.append(choice)

        # You need to select the correct year. Includes checks to specify that the option was correct
        if choice == "1":                           # START of
            check = False                           # 1st Choice
            while not check:                        # /// Start printing list of years
                print("Available options...")       #
                print("//////////")                 #
                for i in options:                   #
                    print("// ", i)                 #
                print("//////////")                 # /// Printing COMPLETE
                select = input("Select year: ")     # /// Enter a specific Year
                valid = False                       # /// Check if the option was correct START
                for a in options:                   # ///
                    if a == select:                 # ///
                        valid = True                # ///
                    else:                           # ///
                        continue                    # /// END of check
                if valid:                           #
                    check = True                    #
                    works = True                    #
                    results.append(select)
                else:                               #
                    print("Wrong choice please try again...")   # END of 1st Choice
        # Automatically should arrange everything inside the specified directory
        elif choice == "2":                         # 2nd Choice
            works = True                            #
        elif choice == "3":                         # 3rd Choice EXIT
            sys.exit().sys.exit()                   #
        else:                                       #
            print("Wrong choice please try again...")

    return results


def main():
    files_transferred = 0

    check_folder()  # if directory doesn't exist create it
    files_path = os.listdir(path)  # get the directory path

    list_options = create_options(files_path)
    if not list_options:
        print("The directory", folder_put_into, "is empty...")
        wait = input("Hit enter to exit.")
        sys.exit().sys.exit()

    results = menu(list_options)
    if len(results) == 2:
        create_lists(files_path, results[1])  # fill up the list with all the files of the specified year
        create_folders(results[1])  # prepare/create the directories needed

        # start the transfer and keep record of the number of files transferred
        files_transferred = copy_files(files_transferred, results[1])

    elif results[0] == "2":
        counter = 0
        while counter < len(list_options):
            create_lists(files_path, list_options[counter])  # fill up the list with all the files of the specified year
            create_folders(list_options[counter])  # prepare/create the directories needed
            # start the transfer and keep record of the number of files transferred
            files_transferred = copy_files(files_transferred, list_options[counter])
            counter += 1

    print("Done!")
    print(files_transferred, " files have transferred")

    wait = input("Hit enter to exit.")


if __name__ == '__main__':

    main()

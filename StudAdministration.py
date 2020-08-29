import csv


def to_csv_file(myl):
    with open("studentAdm.csv", "a+",newline="") as csv_file:
        w = csv.writer(csv_file)
        if csv_file.tell() == 0:
            w.writerow(["Name", "Age", "Contact no.", "E-Mail ID"])

        w.writerow(myl)


choice = True
stud_num=1
while choice:
    info = input(f"Enter the student #{stud_num} information(Name Age ContactNo EmailId): ")
    mylist = info.split()
    print(
        f"The entered information is:\n Name: {mylist[0]} \n Age: {mylist[1]} \n Contact no.: {mylist[2]} \n"
        f" Email Id: {mylist[3]}")
    confirm = input("Enter (yes/no) if you have printed the correct information: ")
    if confirm == "yes":
        to_csv_file(mylist)

    elif confirm == "no":
        print("Enter the correct information again")
    else:
        print("Incorrect response.This entry won't be considered")
    option = input("Do you want to continue(yes/no): ")
    if option == "yes":
        choice = True
        stud_num+=1
    else:
        choice = False

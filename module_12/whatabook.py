#  Title: whatabook.py
#  Author: John Wall
#  Date: 12 August 2022
#  Description: WhatABook program to access information from a database 
#  and view contents in a User interface and alter the database

import mysql.connector
from mysql.connector import errorcode

# Configuration to connect to local database 
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

# method to display the Main Menu
def show_menu():
    print("\n                    Welcome to WhatABook")
    print("\n                         -- Menu --")
    print("\n      View Books     View Store Locations     My Account     Exit")
    print("          1                    2                3              4 ")

# Method to retrieve the book table and display all items
def show_books(cursor):
    cursor.execute("SELECT book_id, book_name, author, details from book;")
    books = cursor.fetchall()
    print("\n -- Displaying All Books -- \n")
    for book in books:
        print(" Book ID: {}\n Title: {}\n Author: {}\n Details: {}\n".format(book[0], book[1], book[2], book[3]))
    
    print("Select New Menu Option (2 - View Locations, 3 - My Account, 4 - Exit): ")

# Method to retrieve the store table and display all items
def show_locations(cursor):
    cursor.execute("SELECT store_id, locale from store;")
    stores = cursor.fetchall()
    print("\n -- Displaying Locations -- \n")
    for store in stores:
        print(" Store ID: {}\n Location: {}\n".format(store[0], store[1]))
    
    print("Select New Menu Option (1 - View Books, 3 - My Account, 4 - Exit): ")

# Method to validate user
def validate_user():
    cursor.execute("SELECT user_id from user;")
    users = cursor.fetchall()
    valid = False
    selected_user = int(float(input("Please Enter a User ID: ")))
    
    # Loop to iterate through all users and compare against the input to validate
    for user in users:
        
        # Statement to extract tuple from within the list
        if selected_user == user[0]:
            print(("Welcome User: ") + str(selected_user))
            valid = True
            break
    return selected_user, valid # Used to hold the selected user and validation to prevent constant login
    
# Method to show the Account Menu    
def show_account_menu():
    print("\n                    Account Menu ")
    print("\n      Wishlist     Add Book     Main Menu")
    print("          1            2            3")

# Method to retrieve the wishlist for the specified userid 
def show_wishlist(cursor, userid):
    cursor.execute(("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author, book.details FROM wishlist")  
        + (" INNER JOIN user ON wishlist.user_id = user.user_id")
        + (" INNER JOIN book ON wishlist.book_id = book.book_id WHERE user.user_id = ") + str(userid) + (";"))

    wishlists = cursor.fetchall()

    print("\n  -- DISPLAYING User Wishlist -- \n")
    
    # Loop to iterate through the wishlist table and extract each tuple within the wishlists list
    for wishlist in wishlists:
        for i in range(len(wishlists)):
            result = wishlists[i]
            print("User ID: {}\n First Name: {}\n Last Name: {}\n Book ID: {}\n Title: {}\n Author: {}\n Details: {}\n".format(*result))
        break

# Method to display all books specified userid does not have in their wishlist
def show_books_to_add(cursor, userid):
    cursor.execute(("SELECT book_id, book_name, author, details FROM book WHERE book_id NOT IN ") +
    ("(SELECT book_id FROM wishlist WHERE user_id = ") + str(userid) + (");"))

    available_books = cursor.fetchall()
    print("\n -- Available Books to Add to Wishlist -- \n")
    
    # Loop to iterate through the book table and extract each tuple within the available_books list
    for book in available_books:
        for i in range(len(available_books)):
            result = available_books[i]
            print("Book ID: {}\n Title: {}\n Author: {}\n Details: {}\n".format(*result))
        break

# Method to add a specified book into the current user's wishlist
def add_book_to_wishlist(cursor, userid, bookid):
    cursor.execute(("INSERT INTO wishlist(user_id, book_id) VALUES (") + str(userid) +(", ") + str(bookid) + (");"))
    db.commit()
    print(("\nBook: ") + str(bookid) + (" added to Wishlist \n"))
try:
    # Verify the connection to the user
    db = mysql.connector.connect(**config) 
    print("\n  Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    program = True # Used to establish the start of the program loop

    # Program Menu displays and prompts user for option
    show_menu()
    menu_choice = int(input("Enter Choice: "))

    # Loop to keep program running unless request to exit
    while program == True:
        
        cursor = db.cursor()
        
        # View all books menu option
        if menu_choice == 1:
            show_books(cursor)
            menu_choice = int(input())

        # View all locations menu option
        elif menu_choice == 2:
            show_locations(cursor)
            menu_choice = int(input())

        # Access My Account Menu option
        elif menu_choice == 3:
            # Validate user
            selected_account, validation = validate_user()

            # While user is valid access account menu
            while validation == True:
                show_account_menu()
                account_choice = int(input("Menu Selection: "))
                # User must enter a valid menu option
                if (account_choice < 1 or account_choice > 3):
                    print("Invalid Menu Selection Try again")
                # Functions if user decides option 2 - add book
                # Go back to account menu when complete
                elif account_choice == 2:
                    show_books_to_add(cursor, selected_account)
                    book_to_add = int(input("Enter the Book ID to add to Wishlist: "))
                    add_book_to_wishlist(cursor, selected_account, book_to_add)
                    continue
                # Function if user decides option 1 - view wishlist
                # Go back to account menu when complete
                elif account_choice == 1:
                    show_wishlist(cursor, selected_account)
                    continue   
                # If user decides option 3 return to main menu and exit loop
                elif account_choice == 3:
                    show_menu()
                    menu_choice = int(input("Enter Choice: "))
                    break
                else:
                    break
            # If invalid user id is entered, try again till correct        
            else:
                print("You must enter a valid User ID")
                break                    
        # Exit program Menu option
        elif menu_choice == 4:
            program = False
        # User must enter a valid menu option prompt with message until correct
        else:
            print("Invalid Menu Option")
            menu_choice = int(input("Enter Choice Again: "))
    # Press any key to fully close program
    else:
        input("\n\n  Press any key to close...")

# Error messages
except mysql.connector.Error as err:

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)
# Close file
finally:

    db.close()
    
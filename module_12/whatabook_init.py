#
#
#
#
#
#

import mysql.connector
from mysql.connector import errorcode


config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}


def show_menu():
    print("\n                    Welcome to WhatABook")
    print("\n                         -- Menu --")
    print("\n      View Books     View Store Locations     My Account     Exit")
    print("          1                    2                3              4 ")


def show_books(cursor):
    cursor.execute("SELECT book_id, book_name, author, details from book;")
    books = cursor.fetchall()
    print("\n -- Displaying All Books -- \n")
    for book in books:
        print(" Book ID: {}\n Title: {}\n Author: {}\n Details: {}\n".format(book[0], book[1], book[2], book[3]))
    
    print("Select New Menu Option (2 - View Locations, 3 - My Account, 4 - Exit): ")


def show_locations(cursor):
    cursor.execute("SELECT store_id, locale from store;")
    stores = cursor.fetchall()
    print("\n -- Displaying Locations -- \n")
    for store in stores:
        print(" Store ID: {}\n Location: {}\n".format(store[0], store[1]))
    
    print("Select New Menu Option (1 - View Books, 3 - My Account, 4 - Exit): ")


def validate_user():
    cursor.execute("SELECT user_id from user;")
    users = cursor.fetchall()
    valid = False
    selected_user = int(float(input("Please Enter a User ID: ")))
    for user in users:
        
        if selected_user == user[0]:
            print(("Welcome User: ") + str(selected_user))
            valid = True
            break
    return selected_user, valid
    
    
def show_account_menu():
    print("\n                    Account Menu ")
    print("\n      Wishlist     Add Book     Main Menu")
    print("          1            2            3")

def show_wishlist(cursor, userid):
    cursor.execute(("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author, book.details FROM wishlist")  
        + (" INNER JOIN user ON wishlist.user_id = user.user_id")
        + (" INNER JOIN book ON wishlist.book_id = book.book_id WHERE user.user_id = ") + str(userid) + (";"))

    wishlists = cursor.fetchall()

    print("\n  -- DISPLAYING User Wishlist -- \n")
    
    for wishlist in wishlists:
        for i in range(len(wishlists)):
            result = wishlists[i]
            print("User ID: {}\n First Name: {}\n Last Name: {}\n Book ID: {}\n Title: {}\n Author: {}\n Details: {}\n".format(*result))
        break

def show_books_to_add(cursor, userid):
    cursor.execute(("SELECT book_id, book_name, author, details FROM book WHERE book_id NOT IN ") +
    ("(SELECT book_id FROM wishlist WHERE user_id = ") + str(userid) + (");"))

    available_books = cursor.fetchall()
    print("\n -- Available Books to Add to Wishlist -- \n")
    for book in available_books:
        for i in range(len(available_books)):
            result = available_books[i]
            print("Book ID: {}\n Title: {}\n Author: {}\n Details: {}\n".format(*result))
        break


def add_book_to_wishlist(cursor, userid, bookid):
    cursor.execute(("INSERT INTO wishlist(user_id, book_id) VALUES (") + str(userid) +(", ") + str(bookid) + (");"))
    db.commit()

try:
    # Verify the connection to the user
    db = mysql.connector.connect(**config) 
    print("\n  Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    program = True # Used to establish the start of the program loop


    show_menu()
    menu_choice = int(input("Enter Choice: "))

    while program == True:
        
        cursor = db.cursor()
        
        if menu_choice == 1:
            show_books(cursor)
            menu_choice = int(input())

        elif menu_choice == 2:
            show_locations(cursor)
            menu_choice = int(input())


        elif menu_choice == 3:
            selected_account, validation = validate_user()

            while validation == True:
                show_account_menu()
                account_choice = int(input("Menu Selection: "))
                if (account_choice < 1 or account_choice > 3):
                    print("Invalid Menu Selection Try again")
                elif account_choice == 2:
                    show_books_to_add(cursor, selected_account)
                    book_to_add = int(input("Enter the Book ID to add to Wishlist: "))
                    add_book_to_wishlist(cursor, selected_account, book_to_add)
                    continue
                elif account_choice == 1:
                    show_wishlist(cursor, selected_account)
                    continue   
                elif account_choice == 3:
                    show_menu()
                    menu_choice = int(input("Enter Choice: "))
                    break
                else:
                    break
                    
            else:
                print("You must enter a valid User ID")
                break                    
        elif menu_choice == 4:
            program = False
        else:
            print("Invalid Menu Option")
            menu_choice = int(input("Enter Choice Again: "))
    else:
        input("\n\n  Press any key to close...")

except mysql.connector.Error as err:

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:

    db.close()
    
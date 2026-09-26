"""
Midterm Practical Exam — Movie Collection Manager
Student: Macapinlac, Jeremiah S.
"""
import add

def display_menu():
    # print the menu
    # return the user's choice
     print("Menu")
     print("1. Add Movie")
     print("2. View all movies")
     print("3. Count watched vs unwatched")
     print("4. Find a movie")
     print("5. Remove a movie")
     print("6. Exit")

def main():
     while True:
          display_menu()
          choice = int(input("choice an option(1-5):"))

     if choice == 1:
      a = add.add_movie
      print(a) 

               
     main()

    


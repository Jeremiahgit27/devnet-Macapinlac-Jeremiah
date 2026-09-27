"""
Module 2 — Activity: File Sorting with os and shutil
Student: Macapinlac, Jeremiah S.
Date: 09/26/26

============================================
WHAT DID YOU BUILD? (explain in your own words)
============================================
[Paste your working script below first, then come back and explain
it here: what does your script do, and what rule did you use to
sort the files? e.g. by extension, by name, by date, etc.]

 my code only ask the folder path and check if it exist, if the folder exist it create a new folder for each extention to sort the file with
that extention, if the file has no extention it will go to the other folder and print "Files have been sorted successfully", if it doesn't 
exist it print "path doesn't exist", I use list, for loop and if else.
============================================
KEY VOCABULARY
============================================
- os module:
- shutil module:
- file path:
- directory:
(add more as needed)


============================================
YOUR SCRIPT
============================================
Paste the code you already wrote for this activity below.
"""
import os
import shutil

folder_path = str(input("give folder path: "))

if os.path.exists(folder_path):

    list_of_file = os.listdir(folder_path)

    for file in list_of_file:

        file_path = os.path.join(folder_path, file)

        if os.path.isfile(file_path):

            file_extension = os.path.splitext(file)[1].lower()

            if file_extension:
                folder_name = file_extension[1:] + "_files"
            else:
                folder_name = "other_files"

            selected_folder = os.path.join(folder_path, folder_name)

            if not os.path.exists(selected_folder):
                os.mkdir(selected_folder)

            shutil.move(file_path, os.path.join(selected_folder, file))

    print("Files have been sorted successfully.")

else:

    print("path doesn't exist")


# --- paste your existing code here ---


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[what tripped you up while building this? e.g. a path that didn't
exist, a file that got overwritten, something that didn't work the
way you expected at first]

I got problem in sorting it made an error and won't sort the files.

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional: how is this similar to what real automation scripts do?
think about your own gradebook/attendance workflow — could something
like this save you time there?]

I think in other office work they use this to sort there file because in that line of work there's a lot of file needed and it will confuse them
when the files are not sorted.
"""

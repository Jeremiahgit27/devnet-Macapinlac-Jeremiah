"""
Module 2 — Lesson 2: Control Flow (if / elif / else)
Student: Macapinlac, Jeremiah S. 
Date: 09/26/26

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================

Control flow is where you make python makes the decision by adding decision making, repetition and branching logic.

============================================
KEY VOCABULARY
============================================
- condition:
- if / elif / else:
- comparison operator:
- boolean expression:
(add more as needed)


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

# --- your code example goes here ---
x = int(input("how much?" ))

if x >= 500:
 print("it\'s expensive")

elif x >= 100:
 print("fair price")

elif x <= 99:
 print("it\'s so cheap")

else:
  print("invalid")

"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[what's something confusing or easy to get wrong
about this topic?]

when i put the (it's) it did not work because i need to put (it\'s) to python read it.

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
it can be help in grading system to analyze who passed and who failed.
"""

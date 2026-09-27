"""
Module 2 — Lesson 4: Functions
Student: Macapinlac, Jeremiah S.
Date: 09/26/26

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
 The topic is Function, function is very useful for programmers because instead of writting the code multiple times the programmers can reuse the code.


============================================
KEY VOCABULARY
============================================
- function: block of reusable code that performs
  a specific task.

- parameter: variable listed inside a function definition that receives a value.

- argument: when it is called, the actual value given to a function.

- return value: the result that a function sends back to the code that called it.

- def: the keyword used to create a function.

- call: using the function to make it run.

- return: sends a value back from a function.


============================================
MY OWN EXAMPLE(S)
============================================
"""


def calculate_total(price, quantity):
    total = price * quantity
    return total


item_price = 50
item_quantity = 3

total_price = calculate_total(item_price, item_quantity)

print("Item price:", item_price)
print("Quantity:", item_quantity)
print("Total price:", total_price)


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
A mistake i made is i forgot to use return when I need the function to give a result back.


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================

It's a big help for programmers because they can reuse the code.
"""
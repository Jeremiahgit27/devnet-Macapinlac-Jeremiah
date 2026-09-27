"""
Module 2 — Lesson 3: Loops & Lists
Student: Macapinlac, Jeremiah S.
Date: 09/26/26

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
[write your own explanation here]
List is like a cart that stores a collection of data. Loops read it and run it repeatedly

============================================
KEY VOCABULARY
============================================
- list: it stored a collection of data.
- for loop: it repeat each item in the list.
- while loop: while the condition is true it repeat the code it only break when the condition is false.
- index: tells the position of the item on the list.
- iteration: one repitition of a loop.



============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""
# --- your code example goes here ---
# list and for loop
cellphone = ["Vivo", "Oppo", "Iphone", "Tecno"]

for cellphones in cellphone:
  print(cellphones)

# while loop
x = 1

while x < 5:
  print(x)
  x += 1

  # index
  cellphones = ['Iphone', 'Tecno', 'Vivo']

x = cellphone.index("VIvo")

print(x)

# itiration
x = "programming"
x = iter(x)

print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[what's something confusing or easy to get wrong
about this topic?]
i just get confuse how the index work but i manage to understand it.
============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
this helps a programmer in creating website, instead of using a lot of print it only needed 1.
"""

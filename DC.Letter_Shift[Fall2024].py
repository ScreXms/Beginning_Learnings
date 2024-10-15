import random

name = {
    "Derek": 2,
    "Fred": 4,
    "Kora": 10,
    "Cherp": 8,
    "Fredreka": 1
}

place = {
    "Ya Ya Tea": 15,
    "Top Bread": 1,
    "Shabu Shabu": 30,
    "Cast Iron Grill": 50, 
    "Pop Eyes": 25
}

meals = {
    "breakfast": 6,
    "lunch": 7,
    "dinner": 10,
    "dessert": 12,
    "snacks": 15
}

food = {
    "sandwhiches": 20,
    "pasta": 50,
    "steaks": 3,
    "ice cream": 35,
    "cookies": 10
}

date = {
    "Oct.10": 16,
    "Oct.15": 22,
    "Oct.20": 25,
    "Oct.31": 7,
}

socialmedia = {
    "Instagram":(1, 4),
    "Tik Tok": (6, 10),
    "Snapchat": (5, 26),
    "X": (13, 1),
    "Facebook": (9, 3)
}

username = {
    "daddy1": 8,
    "cheesehead": 9,
    "dinobear": 14,
    "chadbod": 78,
    "bob123": 6
}

def shift_letters(text, shift):
    shifted_text = ''
    for char in text:
        if char.isalpha(): # checking letters 
            shift_base = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            shifted_text += shifted_char
        else:
            shifted_text += char # keeps non letters from changing
    return shifted_text

Note = f''' Hi {random.choice(list(name.keys()))}
I have seen you around, would you like to go to {random.choice(list(place.keys()))}. I know
they have the best {random.choice(list(meals.keys()))} {random.choice(list(food.keys()))}. I have some aviability on {random.choice(list(date.keys()))} if 
you would like to go. My {random.choice(list(socialmedia.keys()))} is {random.choice(list(username.keys()))}, we could connect there. 
You can send me a message when you get a chance. I would love to spoil you.
Love {random.choice(list(name.keys()))} 
'''
print("original Note:")
print(Note)

shift_value = int(input("enter value:"))

shifted_note = shift_letters(Note, shift_value)

# print("\nShifted Note:")
print(shifted_note)
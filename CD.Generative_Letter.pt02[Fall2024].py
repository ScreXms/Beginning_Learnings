import random

propernouns = {
    "Derek": 2,
    "Fred": 4,
    "Kora": 10,
    "Cherp": 8,
    "Fredreka": 1,
    "Ya Ya Tea": 15,
    "Top Bread": 1,
    "Shabu Shabu": 30,
    "Cast Iron Grill": 50, 
    "Pop Eyes": 25
}

nouns = {
    "sandwhiches": 20,
    "pasta": 50,
    "steaks": 3,
    "ice cream": 35,
    "cookies": 10,
    "daddy1": 8,
    "cheesehead": 9,
    "dinobear": 14,
    "chadbod": 78,
    "bob123": 6,
    "Instagram":(1, 4),
    "Tik Tok": (6, 10),
    "Snapchat": (5, 26),
    "X": (13, 1),
    "Facebook": (9, 3),
    "breakfast": 6,
    "lunch": 7,
    "dinner": 10,
    "dessert": 12,
    "snacks": 15
}

dates = {
    "Oct.10": 16,
    "Oct.15": 22,
    "Oct.20": 25,
    "Oct.31": 7,
}


categories = { 
    "nouns": nouns,
    "propernouns": propernouns,
    "dates": dates,
    "random": {**nouns, **dates, **propernouns}
}

random_nouns = random.choice(list(nouns.keys()))
random_propernouns = random.choice(list(propernouns.keys()))
random_dates = random.choice(list(dates.keys()))
random_random = random.choice(list(categories["random"].keys())) 


user_input = input("hi (nouns, propernouns, dates, random): ").strip().lower()
if user_input in categories:
    random_choice = random.choice(list(categories[user_input].keys()))
    print({random_choice})
else:
    print(f"The category '{user_input}' is not found.")

user_input = input("I have seen you around, would you like to go to (nouns, propernouns, dates, random): ").strip().lower()
if user_input in categories:
    random_choice = random.choice(list(categories[user_input].keys()))
    print({random_choice})
else:
    print(f"The category '{user_input}' is not found.")

user_input = input("I know they have the best (nouns, propernouns, dates, random): ").strip().lower()
if user_input in categories:
    random_choice = random.choice(list(categories[user_input].keys()))
    print({random_choice})
else:
    print(f"The category '{user_input}' is not found.")

user_input = input("I have some availability on (nouns, propernouns, dates, random) if you would like to go: ").strip().lower()
if user_input in categories:
    random_choice = random.choice(list(categories[user_input].keys()))
    print({random_choice})
else:
    print(f"The category '{user_input}' is not found.")

user_input = input("My (nouns, propernouns, dates, random) is: ").strip().lower()
if user_input in categories:
    random_choice = random.choice(list(categories[user_input].keys()))
    print({random_choice})
else:
    print(f"The category '{user_input}' is not found.")

user_input = input("(nouns, propernouns, dates, random), we could connect there. You can send me a message when you get a chance.: ").strip().lower()
if user_input in categories:
    random_choice = random.choice(list(categories[user_input].keys()))
    print({random_choice})
else:
    print(f"The category '{user_input}' is not found.")

user_input = input("I would love to spoil you. Love(nouns, propernouns, dates, random): ").strip().lower()
if user_input in categories:
    random_choice = random.choice(list(categories[user_input].keys()))
    print({random_choice})
else:
    print(f"The category '{user_input}' is not found.")
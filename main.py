
import random
import requests

pokemon_list = [
    "pikachu", "bulbasaur", "charmander",
    "squirtle", "eevee", "gastly"
]

def get_pokemon(name):
    try:
        url = f"https://pokeapi.co/api/v2/pokemon/{name}"
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            print("Invalid Pokémon or API error:", response.status_code)
            return None

        return response.json()

    except (requests.exceptions.RequestException, ValueError) as error:
        print("Network or data error:", error)
        return None


while True:
    pokemon = get_pokemon(random.choice(pokemon_list))

    if pokemon:
        print("\n=== Guess the Pokémon! ===")
        print("Height:", pokemon["height"], "dm")
        print("Weight:", pokemon["weight"], "hg")

        for key in ["types", "abilities", "moves"]:
            items = pokemon[key][:5] if key == "moves" else pokemon[key]
            names = [
                item[{"types": "type", "abilities": "ability", "moves": "move"}[key]]["name"]
                for item in items
            ]
            print(key.title() + ":", ", ".join(names))

        for attempt in range(3):
            guess = input(f"\nGuess {attempt + 1}/3: ").strip().lower()

            if guess == pokemon["name"]:
                print("Congratulations! You guessed correctly!")
                break

            print("Wrong guess!")
        else:
            print("Game over! The Pokémon was", pokemon["name"].title())

    if input("\nPlay again? (yes/no): ").strip().lower() not in ["yes", "y"]:
        print("Thanks for playing!")
        break

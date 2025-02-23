# # Superhero Dictionary: Enter a Superhero Name & Get Its Urdu Meaning!

words = {
    "batman": "chamkaadarAdmi",
    "spiderman": "makriAdmi",
    "antman": "chootiAdmi",
    "black panther": "kalaBagh",
    "wolverine": "bhediya",
    "hawkman": "baazAdmi",
    "beast": "darinda",
    "catwoman": "billiAurat",
    "tigerman": "sherAdmi",
    "rhino": "genda",
    "scorpion": "bichu",
}

word = input("Enter a word you want meaning of: ").lower()  # Convert input to lowercase
meaning = words.get(word, "Sorry, this word is not in the dictionary.")  # Handle unknown words

print(meaning)


# Create a module

from random import choice as cs

capital = "New Delhi"
national_animal = "Tiger"
continent = "Asia"

fun_facts_about_india = [
    "India is the world's largest democracy.",
    "The Himalayas, the world's highest mountain range, form India's northern border.",
    "The Taj Mahal, one of the Seven Wonders of the World, is located in Agra, India.",
    "India is home to the world's largest film industry, Bollywood.",
    "India has the most number of languages spoken in the world.",
    "Yoga originated in India thousands of years ago.",
    "India is the birthplace of cricket.",
    "The Indian flag is saffron, white, and green, with a blue wheel in the center.",
    "India has the world's largest postal network.",
    "The Indian cuisine is one of the most diverse in the world, with regional variations.",
    "India is home to the world's largest tiger population.",
    "The Indian elephant is the national animal of India.",
    "India is the birthplace of Buddhism and Hinduism.",
    "India has the world's largest number of vegetarians.",
    "The Indian rupee is the world's oldest currency in continuous use.",
]


def run_fun_facts():
    print(cs(fun_facts_about_india))


if __name__ == "__main__":
    run_fun_facts()

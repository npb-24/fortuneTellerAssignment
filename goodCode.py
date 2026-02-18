# four requirements - Clean Code, Seperation of Concerns, KISS, DRY Code
import random

# sets up a dictionary 
# Clean Code - all functions and defined variables have clear meaning
tarotCards = {
    "The Fool" : "New beginnings",
    "The Magician" : "Resourcefulness",
    "The High Priestess" : "Intuition",
    "The Empress" : "Abundance",
    "The Emperor" : "Leadership",
    "The Hierophant" : "Tradition",
    "The Lovers" : "Love",
    "The Chariot" : "Success",
    "The Strength" : "Courage",
    "The Hermit" : "Wisdom",
    "The Wheel of Fortune" : "Luck",
    "The Justice" : "Truth",
    "The Hanged Man" : "Letting go",
    "The Death" : "Transformation",
    "The Temperance" : "Balance",
    "The Devil" : "Temptation",
    "The Tower" : "Sudden change",
    "The Star" : "Hope",
    "The Moon" : "Mystery",
    "The Sun" : "Joy",
    "The Judgement" : "Self-reflection",
    "The World" : "Success"
}

# SOC - function that only handles conversational input
def conversation(current_line):
    match current_line:
        case 1:
            first_question = input('You enter a tent and see an old woman bent over a small table.\n"Hello dearie" she says with a grin "Sit down and tell me of your troubles."\n > ')
            return first_question
        case 2:
            second_question = input('"Oh ho ho! Now THAT was interesting!"\nshe begins quickly shuffling the deck\n"Now sweetie tell me of your greatest ambition"\n > ')
            return second_question
        case 3:
            final_question = input('"Hmmm..."\n"I now possess a greater understanding."\n"Finally! tell me what it is you fear most"\n > ')
            return final_question

# SOC - function that only handles card selection
# KISS - returns a clean string
# DRY - accesses the dictionary only once
def drawACard(user_input):
    selected_card = random.choice(tarotCards.keys())
    meaning = tarotCards[selected_card]
    return f'\n"Ahh", "{user_input}", "and your card is...\n" {selected_card} which can only mean a {meaning}\n'

# SOC - function that only handles the continuation of the game
def continuedFortune():
    want_to_continue = input("This is the end...\n or is it?\nWould you like to reassess your fortune? (y/n):\n >").lower
    return want_to_continue == "y"

def main():
    # Clean Code - uses a simple for loop to navigate the dialogue
    for i in range(1,4):
        user_response = conversation(i)
        print(drawACard(user_response))

    if continuedFortune:
        main()
    else:
        print("Suddenly the old woman arises and with a cackle her and the tent vanish.")


if __name__ == '__main__':
    main()
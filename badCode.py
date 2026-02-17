import random
import asyncio

myDict = {
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

global num
num=0

async def shuffle():
    while(True):
        global num
        num = int((num+random.randint(0,4)) % len(myDict))
        await asyncio.sleep(0.1)
    


async def story():
    #introduction
    print("You enter a tent and see an old women bent over a small table.")
    await asyncio.sleep(0.5)
    print('"Hello, and welcome to my humble tarot reading."')
    await asyncio.sleep(0.5)
    print("She starts to shuffle the deck of cards in front of her.")
    await asyncio.sleep(0.5)
    print('"Say the word whenever you want me to stop dearie"')
    await asyncio.sleep(0.5)
    x = input(" > ")
    await asyncio.sleep(0.5)
    print("hmmm, interesting")
    await asyncio.sleep(0.5)
    print("AGAAGA: " + str(num))
    print(f"you drew {list(myDict)[num]} card. This card represents {myDict[list(myDict)[num]]}")

    #ask question 1
    #draw a card
    #ask question 2
    #draw a card
    #ask question 3
    #draw a card

async def main():
    await asyncio.gather(shuffle(), story())

asyncio.run(main())
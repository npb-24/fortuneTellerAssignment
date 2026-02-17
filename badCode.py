import random
import asyncio

#setsup a dictionary 
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

global usuallyTrue
usuallyTrue = True

#updates num
async def myFunction():
    while(usuallyTrue):
        global num

        #adds a random number to num and finds the modulus of the dictionary's length
        num = int((num+random.randint(1,4)) % len(myDict))
        await asyncio.sleep(0.1)

#Draws a card
def drewCard(number):

    #chooses a random number
    i = random.randint(1,3)

    match i:
        case 1:
            print('"Hmm, interesting"')
        case 2:
            print('"Intriguing"')
        case _:
            print('"Oh my"')

    #prints a message
    print(f"you drew {list(myDict)[number]} card. This card represents '{myDict[list(myDict)[number]]}'")

async def story():
    global usuallyTrue

    #the introduction to the story
    print("You enter a tent and see an old women bent over a small table.")
    await asyncio.sleep(0.5)
    print('"Hello, and welcome to my humble tarot reading."')
    await asyncio.sleep(0.5)
    print("She starts to shuffle the deck of cards in front of her.")
    await asyncio.sleep(0.5)
    print('"Say the word whenever you want me to stop dearie"')
    await asyncio.sleep(0.5)
    
    #waits for the users input
    input(" > ")
    await asyncio.sleep(0.5)
    
    a=num
    drewCard(a)
    await asyncio.sleep(0.5)
    
    
    print("The lady start shuffling again")
    await asyncio.sleep(0.5)
    input(" > ")
    b=num
    await asyncio.sleep(0.5)
    while(a==b):
        b=num
        await asyncio.sleep(0.2)
    drewCard(b)
    await asyncio.sleep(0.5)

    print("The lady start shuffling again")
    await asyncio.sleep(0.5)
    input(" > ")
    c=num
    await asyncio.sleep(0.5)
    while(c==a or c==b):
        c=num
        await asyncio.sleep(0.2)
    drewCard(c)
    await asyncio.sleep(0.5)

    print("I hope you have found this fortune insightful, and that good things shall come to pass.")
    
    #sets "usuallyTrue" to false
    usuallyTrue=False


async def main():
    await asyncio.gather(myFunction(), story())

#runs main
asyncio.run(main())
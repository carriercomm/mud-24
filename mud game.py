#Attempting to make a mud like game
#Author: Brad Riley

import random
import time
import monsters

#Player name
playName = input('What is your name? ')

#Skills
playHealth = random.randint(10,100)
playMana = random.randint(10,50)
playStrength = random.randint(1,10)
playMagic = random.randint(1,10)
playMarksman = random.randint(1,10)

print('Your skills are: ')
print('Your Health is: ' + str(playHealth))
print('Your Mana is: ' + str(playMana))
print('Your Strength skill level is: ' + str(playStrength))
print('Your Magic skill level is: ' + str(playMagic))
print('Your Marksman skill level is: ' + str(playMarksman))


#Reroll skills

skillChange = input('Would you like to re roll these skills? (yes/no): ')
skillChange = skillChange.lower()
while skillChange == 'yes' :
    playHealth = random.randint(30,100)
    playMana = random.randint(10,50)
    playStrength = random.randint(1,10)
    playMagic = random.randint(1,10)
    playMarksman = random.randint(1,10)
    print('Your skills are: ')
    print('Your Health is: ' + str(playHealth))
    print('Your Mana is: ' + str(playMana))
    print('Your Strength skill level is: ' + str(playStrength))
    print('Your Magic skill level is: ' + str(playMagic))
    print('Your Marksman skill level is: ' + str(playMarksman))
    skillChange = input('Would you like to re roll these skills? (yes/no): ')
    skillChange = skillChange.lower()

#Map Logic

genSurr = random.randint(1,4)
if genSurr == 1:
    genSurr = 'a door: '
elif genSurr == 2:
    genSurr = 'it bends left: '
elif genSurr == 3:
    genSurr = 'it bends right: '
else:
    genSurr = 'the way goes straight: '


# Monster Logic

monChan = 1
if monChan == 1:
    monChan = '...the way is clear...'
else:
    monChan = 'Oh no theres a goblin! You cant run!'


#Goblin
staticGoblinHp = 7
goblinAtk = random.randint(5, 15)
goblinChan = random.randint(1,19)
goblinHp = 7
#Goblin Skills
#health = random.randint(5,40)
#mana = random.randint(10,50)
#strength = random.randint(1,10)
#magic = random.randint(1,10)
#marksman = random.randint(1,10)

#start

maxHealth = playHealth
maxMana = playMana
currentLevel = 1
xp = 0

#Introduction
start = input('You see a dungeion entrace... do you enter? ')
if start == 'No':
    print('You fall off a cliff.')
    playHealth -= maxHealth

#While in dungeon
while playHealth > 0:
    go = input('You look ahead, ' + genSurr)
    if go == 'Continue':
        monChan = random.randint(1,2)
        if monChan == 2:
            print('Oh no! there is a Goblin! You cannot run!')
            while goblinHp > 0:
                playac = input("What will you attack with? (magic, strength, or marksman? )")
                if playac == 'magic':
                    chanHit = random.randint(1,10+playMagic)
                    if chanHit > 11:
                        playDamage = random.randint(1,playMagic)
                        print('You casted a magic missle hitting the golin, for ' + str(playDamage) + '!')
                        goblinHp -= playDamage
                    elif chanHit < 11:
                        print('YOU MISSED!')
                    chanHit = random.randint(1,10+playMagic)
                if playac == 'strength':
                    chanHit = random.randint(1,10+playStrength)
                    if chanHit > 11:
                        playDamage = random.randint(1,playStrength)
                        print('You swung your sword at the goblin hitting the golin, for ' + str(playDamage) + '!')
                        goblinHp -= playDamage
                    elif chanHit < 11:
                        print('YOU MISSED!')
                    chanHit = random.randint(1,10+playStrength)
                if playac == 'marksman':
                    chanHit = random.randint(1,10+playMarksman)
                    if chanHit > 11:
                        playDamage = random.randint(1,playMarksman)
                        print('You shot an arrow at the goblin, for ' + str(playDamage) + '!')
                        goblinHp -= playDamage
                    elif chanHit < 11:
                        print('YOU MISSED!')
                    chanHit = random.randint(1,10+playMarksman)
                if goblinChan > 11:
                    print('The goblin wounded you with its spear, dealing ' + str(goblinAtk) + '.')
                    playHealth -= goblinAtk
                    print('Careful! You have ' + str(playHealth) + ' health left')
                if goblinChan < 11:
                    print('THE GOBLIN MISSED!')
                goblinAtk = random.randint(5, 15)
                goblinChan = random.randint(1,19)
                if playHealth < 0:
                    break
        goblinHp = staticGoblinHp
        xp += 5
        if xp == 20:
            print('Congragulations you leveled up!')
            currentLevel += 1
            #skillup = input('Enter a skill to level up! ')
        if monChan == 1:
            print('The way is clear....for now...')
            ############Where I am at
        
        







#On Death

print('Oh no you died! You were level ' + str(currentLevel))

#DnD charactor calculator
#this is declaring what the classes and races
import random
strength = random.randint(1,20)
dex = random.randint(1,20)
con = random.randint(1,20)
intel = random.randint(1,20)
wis = random.randint(1,20)
char = random.randint(1,20)
print('These are your stats I rolled them for you so you do not have to worry about it.')
print('Strength ',strength)
print('Dexterity',dex)
print('Constitution',con)
print('Intelligence',intel)
print('Wisdom',wis)
print('Charisma',char)
print('Please choose your class.')
classes = 'Barbarian' #', ' 'Bard' #the classes are Barbarian, Warlock, Bard, Wizard, Rogue, Monk, Sorcerer, Fighter, Cleric, Paladin, Druid, and Ranger.
print(classes)
usrclass = input()
if usrclass == "barbarian" or usrclass == "Barbarian":
    print('You have chosen Barbarian. This means that you have Rage, and Unarmored defense.')
    print()
    print('Rage is an ability that you must activate as a bonus action. '
          'It gives you advantage on strength checks and strength saving throws.')
    print('It also gives you a bonus to strength attacks, at first level it is a +2 to the attack roll and it increses when you level up.')
    print()
    print('Unarmored Defense is a passive skill for barbarians. ')
    print('It changes your armor class while not wearing armor to 10 + your dex modifier + your Constiusion modifier.')
    races = ['Gnome'] #the races are Dragonborn, Dwarf, Elf, Gnome, Half-Elf, Halfling, Half-Orc, Human, and Tiefling.
    print('Now please pick the race of your character.')
    print(races)
    usrace = input()
    if usrace == "gnome" or usrace == "Gnome":
        intel = intel + 2

else:
    print('Please pick your class, and be sure that it is spelled correctly.')

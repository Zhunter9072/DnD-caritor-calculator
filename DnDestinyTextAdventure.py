#DnD charactor calculator
#this is declaring what the classes and races
strength = 10 #remember that this is for debugging
dex = 10
con = 10
intel = 10
wis = 10
carisma = 10
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

else:
    print('Please pick your class, and be sure that it is spelled correctly.')

races = ['Gnome'] #the races are Dragonborn, Dwarf, Elf, Gnome, Half-Elf, Halfling, Half-Orc, Human, and Tiefling.

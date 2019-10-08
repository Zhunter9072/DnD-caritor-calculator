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
def gnome():
        print('You have chosen to be a Gnome. This means that you have Darkvision and Gnomish cunnung')
        print('Gnome\'s energy and enthusiasm for living shines through every inch of her or his tiny body. Gnomes average slightly over 3 feet tall and weigh 40 to 45 pounds. Their tan or brown faces are usually adorned with broad smiles (beneath their prodigious noses), and their bright eyes shine with excitement. Their fair hair has a tendency to stick out in every direction, as if expressing the gnome’s insatiable interest in everything around.')
        print('Darkvision: Accustomed to life underground, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can’t discern color in darkness, only shades of gray.')
        print('Gnomish cunning You have advantage on all Intelligence, Wisdom, and Charisma saving throws against magic.')

def dwarf():
    print('You have chosen Dwarf.')
    print()

def barbarian():
    print('You have chosen Barbarian. This means that you have Rage, and Unarmored defense.')
    print()
    print('Rage is an ability that you must activate as a bonus action. '
          'It gives you advantage on strength checks and strength saving throws.')
    print('It also gives you a bonus to strength attacks, at first level it is a +2 to the attack roll and it increses when you level up.')
    print()
    print('Unarmored Defense is a passive skill for barbarians. ')
    print('It changes your armor class while not wearing armor to 10 + your dex modifier + your Constiusion modifier.')
def cla():
    races = "Gnome, " "Dwarf"  #the races are Dragonborn, Dwarf, Elf, Gnome, Half-Elf, Halfling, Half-Orc, Human, and Tiefling.
    print('Now please pick the race of your character.')
    print(races)

classes = 'Barbarian'  #', ' 'Bard' #the classes are Barbarian, Warlock, Bard, Wizard, Rogue, Monk, Sorcerer, Fighter, Cleric, Paladin, Druid, and Ranger.
print(classes)
usrclass = input()
if usrclass == "barbarian" or usrclass == "Barbarian":
    barbarian()
    cla()
    usrace = input()
    if usrace == "gnome" or usrace == "Gnome":
        intel = intel + 2
        gnome()
    elif usrace == "dwarf" or "Dwarf":
        dwarf()

else:
    print('Please pick your class, and be sure that it is spelled correctly.')

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
    print('You have chosen Dwarf. This means that you have Darkvision, Dwarven resilience, Dwarven combat training, and Stone cutting')
    print()
    print('Darkvision is \"Accustomed to life underground, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can’t discern color in darkness, only shades of gray.\"')
    print('Dwarven Resilience is \"You have advantage on saving throws against poison,/ and you have resistance against poison damage (explained in the \“Combat\” section).\"')
    print('Dwarven combat training \"You have proficiency with the battleaxe, handaxe, light hammer, and warhammer.\"')
    print('Stonecutting is \"Whenever you make an Intelligence (History) check related to the origin of stonework, you are considered proficient in the History skill and add double your proficiency bonus to the check, instead of your normal proficiency bonus.\"')
    print('Please choose one of these three artisan\'s tools. Smiths tools, Brewer\'s tools, or Mason\'s tools.')
    art = input()
    if art == "smith\'s tools" or art == "Smith\'s tools" or art == "smiths tools" or art == "Smiths tools":
        print('You have proficancy with Smith\'s tools.')
    elif art == "brewer\'s tools" or art == "Brewer\'s tools" or art == "brewers tools" or art == "Brewers tools":
        print('You have proficancy with Brewer\'s tools.')
    elif art == "mason\'s tools" or art == "Mason\'s tools" or art == "masons tools" or art == "Masons tools":
        print('You have proficancy with Mason\'s tools.')
    else:
        print('You may have spelled your answer incorrectly.')



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
        con = con + 2
        dwarf()

else:
    print('Please pick your class, and be sure that it is spelled correctly.')

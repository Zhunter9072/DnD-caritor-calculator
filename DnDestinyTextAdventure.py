# DnD charactor calculator
# this is declaring what the classes and races
import random
strength = random.randint(1, 20)
dex = random.randint(1, 20)
con = random.randint(1, 20)
intel = random.randint(1, 20)
wis = random.randint(1, 20)
char = random.randint(1, 20)
acro = dex
animlhand = wis
arcana = intel
athletics = strength
deception = char
history = intel
insite = wis
intimidation = char
investigat = intel
medican = wis
nature = intel
perception = wis
performance = char
perswasion = char
religion = intel
sloh = dex
stealth = dex
survival = wis
print('These are your stats I rolled them for you so you do not have to worry about it.')
print('Strength ', strength)
print('Dexterity', dex)
print('Constitution', con)
print('Intelligence', intel)
print('Wisdom', wis)
print('Charisma', char)
print('Please choose your class.')
lang = "Abyssal, " "Celestial, " "Deep Speech, " "Draconic, " "Dwarvish, " "Elvish, " "Giant, " "Gith, " "Gnomish, " "Goblin, " "Halfling, " "Infernal, " "Kraul, " "Loxodon, " "Minotaur, " "Orc, " "Primordial, " "Sylvan, " "Undercommon."


def darkvision():
    print("Darkvision is a trait of your race which enables you to see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can’t discern color in darkness, only shades of gray.")


def gnome():
    print('You have chosen to be a Gnome. This means that you have Darkvision and Gnomish cunning')
    print('Gnome\'s energy and enthusiasm for living shines through every inch of her or his tiny body. Gnomes average slightly over 3 feet tall and weigh 40 to 45 pounds. Their tan or brown faces are usually adorned with broad smiles (beneath their prodigious noses), and their bright eyes shine with excitement. Their fair hair has a tendency to stick out in every direction, as if expressing the gnome’s insatiable interest in everything around.')
    darkvision()
    print('Gnomish cunning You have advantage on all Intelligence, Wisdom, and Charisma saving throws against magic.')
    print('You also can speak read and write Common, and Gnomish')


def dwarf():
    print('You have chosen Dwarf. This means that you have Darkvision, Dwarven resilience, Dwarven combat training, and Stone cutting')
    print()
    darkvision()
    print('Dwarven Resilience is an ability that gives you advantage on saving throws against poison, and you have resistance against poison damage.')
    print('Dwarven combat training gives you proficiency with weapons such as the battleaxe, handaxe, light hammer, and warhammer.')
    print('Stonecutting is a trait that activates whenever you make an Intelligence (History) check related to the origin of stonework, you are considered proficient in the History skill and add double your proficiency bonus to the check, instead of your normal proficiency bonus.')
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


def human():
    print('You have chosen Human. This means that you get a +1 to all stats and you can choose another language to speak other than common.')
    print('Here is a list of all the other languages.')
    print(lang)
    usrlang = input()
    if usrlang == "abyssal" or usrlang == "Abyssal" or usrlang == "celestial" or usrlang == "Celestial" or usrlang == "deep speech" or usrlang == "Deep speech" or usrlang == "Deep Speech" or usrlang == "Draconic" or usrlang == "draconic" or usrlang == "dwarvish" or usrlang == "Dwarvish" or usrlang == "elvish" or usrlang == "Elvish" or usrlang == "giant" or usrlang == "Giant" or usrlang == "gith" or usrlang == "Gith" or usrlang == "gnomish" or usrlang == "Gnomish" or usrlang == "goblin" or usrlang == "Goblin" or usrlang == "halfling" or usrlang == "Halfling" or usrlang == "infernal" or usrlang == "Infernal" or usrlang == "kraul" or usrlang == "Kraul" or usrlang == "loxodon" or usrlang == "Loxodon" or usrlang == "minotaur" or usrlang == "Minotaur" or usrlang == "orc" or usrlang == "Orc" or usrlang == "primordial" or usrlang == "Primordial" or usrlang == "sylvan" or usrlang == "Sylvan" or usrlang == "undercommon" or usrlang == "Undercommon":
        print("You can speak read and write common and", usrlang)


def halfling():
    print("You have chosen Halfling. This means that you have a +2 to dexterity, as well as the skills Lucky, Brave, and Halfling nimbleness. Halflings are able to speak, read, and write common, and Halfling, also they are considered small creatures.")
    print()
    print("Lucky is a skill that activates when you roll a 1 on the d20 for an attack roll, ability check, or saving throw, it lets you reroll the die however you must take the new roll as your roll.")
    print("Brave is a skill that gives you have advantage on saving throws against being frightened.")
    print("And last but not least there is Halfling nimbleness which is an ablility that allows you to move through the space of any creature that is of a size larger than yours.")


def tefling():
    print("You have chosen Tiefling. This means that you have a +1 in intelligence, a +2 in charisma, you also have Darkvision, Hellish Resistance, Infernal Legacy, You can also speak, read, and write common and infernal.")
    print()
    darkvision()
    print("Hellish Resistance is a trait that gives you resistance to fire damage (meaning that you take half damage from fire attacks).")
    print("Infernal Legacy is a trait that gives you the thaumaturgy cantrip. When you reach 3rd level, you can cast the hellish rebuke spell as a 2nd-level spell once with this trait and regain the ability to do so when you finish a long rest. When you reach 5th level, you can cast the darkness spell once with this trait and regain the ability to do so when you finish a long rest. Charisma is your spellcasting ability for these spells.")


def dragonborn():
    ancestor = "Black, " "Blue, " "Brass, " "Bronze, " "Copper, " "Gold, " "Green, " "Red, " "Silver, " "White."
    print("You have chosen Dragonborn. This means that you have a +2 in strength, a +1 in charisma, you also have Draconic ancestry, a breath weapon, and a damage resistance")
    print("Please choose your Draconic ancestry.")
    print(ancestor)
    usrinput = input()
    if usrinput == "black" or usrinput == "Black":
        print("You have chosen to have Black Dragon ancestry this means that you're breath weapon does acid damage and hits in a 5 by 30ft line and does 2d6 acid damage if the target creature fails the save DC(the way you calculate the DC for this is 8+ your constitution modifier + your proficiency bonus), this also means that you have a resistance to acid damage.")
    elif usrinput == "blue" or usrinput == "Blue":
        print("You have chosen to have Blue Dragon ancestry this means that you're breath weapon does lightning damage and hits in a 5 by 30ft line and does 2d6 lightning damage if the target creature fails the save DC(the way you calculate the DC for this is 8+ your constitution modifier + your proficiency bonus), this also means that you have a resistance to lightning damage.")
    elif usrinput == "brass" or usrinput == "Brass":
        print("You have chosen to have Brass Dragon ancestry this means that you're breath weapon does fire damage and hits in a 5 by 30ft line and does 2d6 fire damage if the target creature fails the save DC(the way you calculate the DC for this is 8+ your constitution modifier + your proficiency bonus), this also means that you have a resistance to fire damage.")
    elif usrinput == "bronze" or usrinput == "Bronze":
        print("You have chosen to have Bronze Dragon ancestry this means that you're breath weapon does lightning damage and hits in a 5 by 30ft line and does 2d6 lightning damage if the target creature fails the save DC(the way you calculate the DC for this is 8+ your constitution modifier + your proficiency bonus), this also means that you have a resistance to lightning damage.")
    elif usrinput == "copper" or usrinput == "Copper":
        print("You have chosen to have Copper Dragon ancestry this means that you're breath weapon does acid damage and hits in a 5 by 30ft line and does 2d6 acid damage if the target creature fails the save DC(the way you calculate the DC for this is 8+ your constitution modifier + your proficiency bonus), this also means that you have a resistance to acid damage.")
    elif usrinput == "gold" or usrinput == "Gold":
        print("You have chosen to have Gold Dragon ancestry this means that you're breath weapon does fire damage and hits in a 15ft cone and does 2d6 fire damage if the target creature fails the save DC(the way you calculate the DC for this is 8+ your constitution modifier + your proficiency bonus), this also means that you have a resistance to fire damage.")
    elif usrinput == "green" or usrinput == "Green":
        print("You have chosen to have Green Dragon ancestry this means that you're breath weapon does poison damage and hits in a 15ft cone and does 2d6 poison damage if the target creature fails the save DC(the way you calculate the DC for this is 8+ your constitution modifier + your proficiency bonus), this also means that you have a resistance to poison damage.")
    elif usrinput == "red" or usrinput == "Red":
        print("You have chosen to have Red Dragon ancestry this means that you're breath weapon does fire damage and hits in a 15ft cone and does 2d6 fire damage if the target creature fails the save DC(the way you calculate the DC for this is 8+ your constitution modifier + your proficiency bonus), this also means that you have a resistance to fire damage.")
    elif usrinput == "silver" or usrinput == "Silver":
        print("You have chosen to have Silver Dragon ancestry this means that you're breath weapon does cold damage and hits in a 15ft cone and does 2d6 cold damage if the target creature fails the save DC(the way you calculate the DC for this is 8+ your constitution modifier + your proficiency bonus), this also means that you have a resistance to cold damage.")
    elif usrinput == "white" or usrinput == "White":
        print("You have chosen to have White Dragon ancestry this means that you're breath weapon does cold damage and hits in a 15ft cone and does 2d6 cold damage if the target creature fails the save DC(the way you calculate the DC for this is 8+ your constitution modifier + your proficiency bonus), this also means that you have a resistance to cold damage.")
    else:
        print("You may have spelled something wrong. Please restart the program.")


def elf():
    print("You have chosen Elf this means that you gain a +2 to dexterity, darkvision, keen senses, fey ancestry, and trance.")
    print()
    darkvision()
    print("Keen Senses is a trait that gives you proficiency in the perception skill.")
    print("Fey Ancestry is a trait that gives you advantage on saving throws against being charmed, also you cannot be put to sleep by magical means.")
    print("Trance is a trait for Elves which means that Elves do not actually sleep instead they go in to a deep meditation for 4 hours.")
    print("In addition to this you can speak read and write in common and elvish.")


def halfork():
    print("You have chosen Half-Orc. This means that you have a + 2 in strength a + 1 in constitution, Darkvision, Menacing, Relentless endurance, and Savage attacks.")
    print()
    darkvision()
    print("Menacing is a skill that gives proficiency in the intimidation skill.")
    print("Relentless endurance is a skill that gives you the ability that if you were to be reduced to 0 hitpoints you instead get reduced to 1 HP however this can only be used once for every long rest.")
    print("Savage attacks is a skill that when you score a critical hit with a melee weapon attack, you can roll one of the weapon’s damage dice one additional time and add it to the extra damage of the critical hit.")
    print("You can also speak read and write common and orc.")


def halfelf():
    print("This also means that you also get Darkvision, Fey Ancestry, and Skill Versatility.")
    print()
    darkvision()
    print("Fey Ancestry is a trait that gives you advantage on saving throws against being charmed, also you cannot be put to sleep by magical means.")
    print("Skill Versatility is a trait that gives you proficiency with 2 skills of your choice.")


def barbarian():
    print('You have chosen Barbarian. This means that you have Rage, and Unarmored defense.')
    print()
    print('Rage is an ability that you must activate as a bonus action. '
          'It gives you advantage on strength checks and strength saving throws.')
    print('It also gives you a bonus to strength attacks, at first level it is a +2 to the attack roll and it increses when you level up.')
    print()
    print('Unarmored Defense is a passive skill for barbarians. ')
    print('It changes your armor class while not wearing armor to 10 + your dex modifier + your Constiusion modifier.')


def rouge():
    print("You have chosen to be a rouge this means that you have ")


def cla():  # the remaining races are half-elf and half-orc
    races = "Gnome, " "Dwarf, " "Human, " "Halfling, " "Tiefling, " "Dragonborn, " "Elf, " "Half-Orc, " "Half-Elf."  # the races are Dragonborn Dwarf, Elf, Gnome, Half-Elf, Halfling, Half-Orc, Human, and Tiefling.
    print('Now please pick the race of your character.')
    print(races)


classes = 'Barbarian, ' 'Rouge'  # 'Bard' #the classes are Barbarian, Warlock, Bard, Wizard, Rogue, Monk, Sorcerer, Fighter, Cleric, Paladin, Druid, and Ranger.
print(classes)
usrclass = input()
if usrclass == "barbarian" or usrclass == "Barbarian":
    barbarian()
    print("Please choose two(2) proficiencies")
    print("Animal Handling, Athletics, Intimidation, Nature, Perception, or Survival.")
    usrpro = input()
    usrpro1 = input()
    if usrpro == "Animal Handling" or usrpro == "Animal handling" or usrpro == "animal Handling" or usrpro == "animal handling" and usrpro1 == "Intimidation" or usrpro1 == "intimidation":
        animlhand = animlhand + 2
        intimidation = intimidation + 2
        print("You now have a +2 in", usrpro, "and", usrpro1)
    elif usrpro == "Animal Handling" or usrpro == "Animal handling" or usrpro == "animal Handling" or usrpro == "animal handling" and usrpro1 == "Athletics" or usrpro1 == "athletics":
        animlhand = animlhand + 2
        athletics = athletics + 2
        print("You now have a +2 in", usrpro, "and", usrpro1)
    elif usrpro == "Animal Handling" or usrpro == "Animal handling" or usrpro == "animal Handling" or usrpro == "animal handling" and usrpro1 == "Nature" or usrpro1 == "nature":
        animlhand = animlhand + 2
        nature = nature + 2
        print("You now have a +2 in", usrpro, "and", usrpro1)
    elif usrpro == "Animal Handling" or usrpro == "Animal handling" or usrpro == "animal Handling" or usrpro == "animal handling" and usrpro1 == "Perception" or usrpro1 == "perception":
        animlhand = animlhand + 2
        perception = perception + 2
        print("You now have a +2 in", usrpro, "and", usrpro1)
    elif usrpro == "Animal Handling" or usrpro == "Animal handling" or usrpro == "animal Handling" or usrpro == "animal handling" and usrpro1 == "Survival" or usrpro1 == "survival":
        animlhand = animlhand + 2
        survival = survival + 2
        print("You now have a +2 in", usrpro, "and", usrpro1)
    elif usrpro == "Athletics" or usrpro == "athletics" and usrpro1 == "Animal Handling" or usrpro1 == "Animal handling" or usrpro1 == "animal Handling" or usrpro1 == "animal handling":
        athletics = athletics + 2
        animlhand = animlhand + 2
        print("You now have a +2 in", usrpro, "and", usrpro1)
    elif usrpro == "Athletics" or usrpro == "athletics" and usrpro1 == "Intimidation" or usrpro1 == "intimidation":
        athletics = athletics + 2
        intimidation = intimidation + 2
        print("You now have a +2 in", usrpro, "and", usrpro1)
    elif usrpro == "Athletics" or usrpro == "athletics" and usrpro1 == "Nature" or usrpro1 == "nature":
        athletics = athletics + 2
        nature = nature + 2
        print("You now have a +2 in", usrpro, "and", usrpro1)
    elif usrpro == "Athletics" or usrpro == "athletics" and usrpro1 == "Perception" or usrpro1 == "perception":
        athletics = athletics + 2
        perception = perception + 2
        print("You now have a +2 in", usrpro, "and", usrpro1)
    elif usrpro == "Athletics" or usrpro == "athletics" and usrpro1 == "Survival" or usrpro1 == "survival":
        athletics = athletics + 2
        survival = survival + 2
        print("You now have a +2 in", usrpro, "and", usrpro1)
    elif usrpro == "Intimidation" or usrpro == "intimidation" and usrpro1 == "Athletics" or usrpro1 == "athletics":
        intimidation = intimidation + 2
        athletics = athletics + 2
        print("You now have a +2 in", usrpro, "and", usrpro1)
    elif usrpro == "Intimidation" or usrpro == "intimidation" and usrpro1 == "Animal Handling" or usrpro1 == "Animal handling" or usrpro1 == "animal Handling" or usrpro1 == "animal handling":
        intimidation = intimidation + 2
        animlhand = animlhand + 2
        print("You now have a +2 in", usrpro, "and", usrpro1)
    elif usrpro == "Intimidation" or usrpro == "intimidation" and usrpro1 == "Nature" or usrpro1 == "nature":
        intimidation = intimidation + 2
        nature = nature + 2
        print("You now have a +2 in", usrpro, "and", usrpro1)
    elif usrpro == "Intimidation" or usrpro == "intimidation" and usrpro1 == "Perception" or usrpro1 == "perception":
        intimidation = intimidation + 2
        perception = perception + 2
        print("You now have a +2 in", usrpro, "and", usrpro1)
    elif usrpro == "Intimidation" or usrpro == "intimidation" and usrpro1 == "Survival" or usrpro1 == "survival":
        intimidation = intimidation + 2
        survival = survival + 2
        print("You now have a +2 in", usrpro, "and", usrpro1)
    elif usrpro == "Nature" or usrpro == "nature" and usrpro1 == "Animal Handling" or usrpro1 == "Animal handling" or usrpro1 == "animal Handling" or usrpro1 == "animal handling":
        nature = nature + 2
        animlhand = animlhand + 2
        print("You now have a +2 in", usrpro, "and", usrpro1)
    elif usrpro == "Nature" or usrpro == "nature" and usrpro1 == "Athletics" or usrpro1 == "athletics":
        nature = nature + 2
        athletics = athletics + 2
        print("You now have a +2 in", usrpro, "and", usrpro1)
    elif usrpro == "Nature" or usrpro == "nature" and usrpro1 == "Intimidation" or usrpro1 == "intimidation":
        nature = nature + 2
        intimidation = intimidation +  2
        print("You now have a +2 in", usrpro, "and", usrpro1)
    elif usrpro == "Nature" or usrpro == "nature" and usrpro1 == "Perception" or usrpro1 == "perception":
        nature = nature + 2
        perception = perception + 2
        print("You now have a +2 in", usrpro, "and", usrpro1)
    elif usrpro == "Nature" or usrpro == "nature" and usrpro1 == "Survival" or usrpro1 == "survival":
        nature = nature + 2
        survival = survival + 2
        print("You now have a +2 in", usrpro, "and", usrpro1)
    elif usrpro == "Perception" or usrpro == "perception" and usrpro1 == "Animal Handling" or usrpro1 == "Animal handling" or usrpro1 == "animal Handling" or usrpro1 == "animal handling":
        perception = perception + 2
        animlhand = animlhand + 2
        print("You now have a +2 in", usrpro, "and", usrpro1)
    elif usrpro == "Perception" or usrpro == "perception" and usrpro1 == "Athletics" or usrpro1 == "athletics":
        perception = perception + 2
        athletics = athletics + 2
        print("You now have a +2 in", usrpro, "and", usrpro1)
    elif usrpro == "Perception" or usrpro == "perception" and usrpro1 == "Intimidation" or usrpro1 == "intimidation":
        perception = perception + 2
        intimidation = intimidation + 2
        print("You now have a +2 in", usrpro, "and", usrpro1)
    elif usrpro == "Perception" or usrpro == "perception" and usrpro1 == "Nature" or usrpro1 == "nature":
        perception = perception + 2
        nature = nature + 2
        print("You now have a +2 in", usrpro, "and", usrpro1)
    elif usrpro == "Perception" or usrpro == "perception" and usrpro1 == "Survival" or usrpro1 == "survival":
        perception = perception + 2
        survival = survival + 2
        print("You now have a +2 in", usrpro, "and", usrpro1)
    elif usrpro == "Survival" or usrpro == "survival" and usrpro1 == "Animal Handling" or usrpro1 == "Animal handling" or usrpro1 == "animal Handling" or usrpro1 == "animal handling":
        survival = survival + 2
        animlhand = animlhand + 2
        print("You now have a +2 in", usrpro, "and", usrpro1)
    elif usrpro == "Survival" or usrpro == "survival" and usrpro1 == "Athletics" or usrpro1 == "athletics":
        survival = survival + 2
        athletics = athletics + 2
        print("You now have a +2 in", usrpro, "and", usrpro1)
    elif usrpro == "Survival" or usrpro == "survival" and usrpro1 == "Intimidation" or usrpro1 == "intimidation":
        survival = survival + 2
        intimidation = intimidation + 2
        print("You now have a +2 in", usrpro, "and", usrpro1)
    elif usrpro == "Survival" or usrpro == "survival" and usrpro1 == "Nature" or usrpro1 == "nature":
        survival = survival + 2
        nature = nature + 2
        print("You now have a +2 in", usrpro, "and", usrpro1)
    elif usrpro == "Survival" or usrpro == "survival" and usrpro1 == "Perception" or usrpro1 == "perception":
        survival = survival + 2
        perception = perception + 2
        print("You now have a +2 in", usrpro, "and", usrpro1)
    else:
        print("You may have inputted something wrong please restart the program")

    cla()
    usrace = input()
    if usrace == "gnome" or usrace == "Gnome":
        intel = intel + 2
        gnome()
    elif usrace == "dwarf" or usrace == "Dwarf":
        con = con + 2
        dwarf()
    elif usrace == "human" or usrace == "Human":
        strength = strength + 1
        dex = dex + 1
        con = con + 1
        intel = intel + 1
        wis = wis + 1
        char = char + 1
        human()
    elif usrace == "halfling" or usrace == "Halfling":
        dex = dex + 2
        halfling()
    elif usrace == "tiefling" or usrace == "Tiefling":
        intel = intel + 1
        char = char + 2
        tefling()
    elif usrace == "dragonborn" or usrace == "Dragonborn":
        strength = strength + 2
        char = char + 1
        dragonborn()
        print("You can speak read and write Draconic and common.")
    elif usrace == "elf" or usrace == "Elf":
        dex = dex + 2
        elf()
    elif usrace == "half orc" or usrace == "Half orc" or usrace == "Half Orc" or usrace == "halforc" or usrace == "Halforc" or usrace == "Half-Orc" or usrace == "Half-orc":
        strength = strength + 2
        con = con + 1
        halfork()
    elif usrace == "half elf" or usrace == "Half elf" or usrace == "Half Elf" or usrace == "halfelf" or usrace == "Halfelf" or usrace == "Half-Elf" or usrace == "Half-Elf":
        char = char + 2
        print("You have chosen Half-Elf. This means that you get a +2 to Charisma and a + 1 to 2 other abilities of your choice please choose 2.")
        print("Strength, Dexterity, Constitution, Intelligence, and Wisdom.")
        stat1 = input()
        stat2 = input()
        if stat1 == "Strength" or stat1 == "strength" and stat2 == "Dexterity" or stat2 == "dexterity":
            strength = strength + 1
            dex = dex + 1
            print("You now have a + 1 in strength and dexterity.")
        elif stat1 == "Strength" or stat1 == "strength" and stat2 == "Constitution" or stat2 == "constitution":
            strength = strength + 1
            con = con + 1
            print("You now have a + 1 in strength and constitution.")
        elif stat1 == "Strength" or stat1 == "strength" and stat2 == "Intelligence" or stat2 == "intelligence":
            strength = strength + 1
            intel = intel + 1
            print("You now have a + 1 in strength and intelligence.")
        elif stat1 == "Strength" or stat1 == "strength" and stat2 == "Wisdom" or stat2 == "wisdom":
            strength = strength + 1
            wis = wis + 1
            print("You now have a + 1 in strength and wisdom.") # continue this today
        elif stat1 == "Dexterity" or stat1 == "dexterity" and stat2 == "Strength" or stat2 == "strength":
            dex = dex + 1
            strength = strength + 1
            print("You now have a + 1 in dexterity and strength.")
        elif stat1 == "Dexterity" or stat1 == "dexterity" and stat2 == "Constitution" or stat2 == "constitution":
            dex = dex + 1
            con = con + 1
            print("You now have a + 1 in dexterity and constitution.")
        elif stat1 == "Dexterity" or stat1 == "dexterity" and stat2 == "Intelligence" or stat2 == "intelligence":
            dex = dex + 1
            intel = intel + 1
            print("You now have a + 1 in dexterity and intelligence.")
        elif stat1 == "Dexterity" or stat1 == "dexterity" and stat2 == "Wisdom" or stat2 == "wisdom":
            dex = dex + 1
            wis = wis + 1
            print("You now have a + 1 dexterity and wisdom.")
        elif stat1 == "Constitution" or stat1 == "constitution" and stat2 == "Strength" or stat2 == "stremgth":
            con = con + 1
            strength = strength + 1
            print("You now have a + 1 in constitution and strength.")
        elif stat1 == "Constitution" or stat1 == "constitution" and stat2 == "Dexterity" or stat2 == "dexterity":
            con = con + 1
            dex = dex + 1
            print("You now have a + 1 in constitution and dexterity.")
        elif stat1 == "Constitution" or stat1 == "constitution" and stat2 == "Intelligence" or stat2 == "intelligence":
            con = con + 1
            intel = intel + 1
            print("You now have a + 1 in constitution and intelligence.")
        elif stat1 == "Constitution" or stat1 == "constitution" and stat2 == "Wisdom" or stat2 == "wisdom":
            con = con + 1
            wis = wis + 1
            print("You now have a + 1 in constitution and wisdom.")
        elif stat1 == "Intelligence" or stat1 == "intelligence" and stat2 == "Strength" or stat2 == "strength":
            intel = intel + 1
            strength = strength + 1
            print("You now have a + 1 in intelligence and strength.")
        elif stat1 == "Intelligence" or stat1 == "intelligence" and stat2 == "Dexterity" or stat2 == "dexterity":
            intel = intel + 1
            dex = dex + 1
            print("You now have a + 1 in intelligence and dexterity.")
        elif stat1 == "Intelligence" or stat1 == "intelligence" and stat2 == "Constitution" or stat2 == "constitution":
            intel = intel + 1
            con = con + 1
            print("You now have a + 1 in intelligence and constitution.")
        elif stat1 == "Intelligence" or stat1 == "intelligence" and stat2 == "Wisdom" or stat2 == "wisdom":
            intel = intel + 1
            wis = wis + 1
            print("You now have a + 1 in intelligence and wisdom.")
        elif stat1 == "Wisdom" or stat1 == "wisdom" and stat2 == "Strength" or stat2 == "strength":
            wis = wis + 1
            strength = strength + 1
            print("You now have a + 1 in wisdom and strength.")
        elif stat1 == "Wisdom" or stat1 == "wisdom" and stat2 == "Dexterity" or stat2 == "dexterity":
            wis = wis + 1
            dex = dex + 1
            print("You now have a + 1 in wisdom and dexterity.")
        elif stat1 == "Wisdom" or stat1 == "wisdom" and stat2 == "Constitution" or stat2 == "constitution":
            wis = wis + 1
            con = con + 1
            print("You now have a + 1 in wisdom and constitution.")
        elif stat1 == "Wisdom" or stat1 == "wisdom" and stat2 == "Intelligence" or stat2 == "intelligence":
            wis = wis + 1
            intel = intel + 1
            print("You now have a + 1 in wisdom and intelligence.")
        else:
            print("You may have spelled something incorrectly please try again.")
        halfelf()
elif usrclass == "rouge" or usrclass == "Rouge":
    rouge()
    cla()
    usrace = input()
    if usrace == "gnome" or usrace == "Gnome":
        intel = intel + 2
        gnome()
    elif usrace == "dwarf" or usrace == "Dwarf":
        con = con + 2
        dwarf()
    elif usrace == "human" or usrace == "Human":
        strength = strength + 1
        dex = dex + 1
        con = con + 1
        intel = intel + 1
        wis = wis + 1
        char = char + 1
        human()
    elif usrace == "halfling" or usrace == "Halfling":
        dex = dex + 2
        halfling()
    elif usrace == "tiefling" or usrace == "Tiefling":
        intel = intel + 1
        char = char + 2
        tefling()
    elif usrace == "dragonborn" or usrace == "Dragonborn":
        strength = strength + 2
        char = char + 1
        dragonborn()
        print("You can speak read and write Draconic and common.")
    elif usrace == "elf" or usrace == "Elf":
        dex = dex + 2
        perception = perception + 2
        elf()
    elif usrace == "half orc" or usrace == "Half orc" or usrace == "Half Orc" or usrace == "halforc" or usrace == "Halforc" or usrace == "Half-Orc" or usrace == "Half-orc":
        strength = strength + 2
        con = con + 1
        intimidation = intimidation + 2
        halfork()
    elif usrace == "half elf" or usrace == "Half elf" or usrace == "Half Elf" or usrace == "halfelf" or usrace == "Halfelf" or usrace == "Half-Elf" or usrace == "Half-Elf":
        char = char + 2
        print("You have chosen Half-Elf. This means that you get a +2 to Charisma and a + 1 to 2 other abilities of your choice please choose 2.")
        print("Strength, Dexterity, Constitution, Intelligence, and Wisdom.")
        stat1 = input()
        stat2 = input()
        if stat1 == "Strength" or stat1 == "strength" and stat2 == "Dexterity" or stat2 == "dexterity":
            strength = strength + 1
            dex = dex + 1
            print("You now have a + 1 in strength and dexterity.")
        elif stat1 == "Strength" or stat1 == "strength" and stat2 == "Constitution" or stat2 == "constitution":
            strength = strength + 1
            con = con + 1
            print("You now have a + 1 in strength and constitution.")
        elif stat1 == "Strength" or stat1 == "strength" and stat2 == "Intelligence" or stat2 == "intelligence":
            strength = strength + 1
            intel = intel + 1
            print("You now have a + 1 in strength and intelligence.")
        elif stat1 == "Strength" or stat1 == "strength" and stat2 == "Wisdom" or stat2 == "wisdom":
            strength = strength + 1
            intel = intel + 1
            print("You now have a + 1 in strength and wisdom.") # continue this today
        elif stat1 == "Dexterity" or stat1 == "dexterity" and stat2 == "Strength" or stat2 == "strength":
            dex = dex + 1
            strength = strength + 1
            print("You now have a + 1 in dexterity and strength.")
        elif stat1 == "Dexterity" or stat1 == "dexterity" and stat2 == "Constitution" or stat2 == "constitution":
            dex = dex + 1
            con = con + 1
            print("You now have a + 1 in dexterity and constitution.")
        elif stat1 == "Dexterity" or stat1 == "dexterity" and stat2 == "Intelligence" or stat2 == "intelligence":
            dex = dex + 1
            intel = intel + 1
            print("You now have a + 1 in dexterity and intelligence.")
        elif stat1 == "Dexterity" or stat1 == "dexterity" and stat2 == "Wisdom" or stat2 == "wisdom":
            dex = dex + 1
            wis = wis + 1
            print("You now have a + 1 dexterity and wisdom.")
        elif stat1 == "Constitution" or stat1 == "constitution" and stat2 == "Strength" or stat2 == "stremgth":
            con = con + 1
            strength = strength + 1
            print("You now have a + 1 in constitution and strength.")
        elif stat1 == "Constitution" or stat1 == "constitution" and stat2 == "Dexterity" or stat2 == "dexterity":
            con = con + 1
            dex = dex + 1
            print("You now have a + 1 in constitution and dexterity.")
        elif stat1 == "Constitution" or stat1 == "constitution" and stat2 == "Intelligence" or stat2 == "intelligence":
            con = con + 1
            intel = intel + 1
            print("You now have a + 1 in constitution and intelligence.")
        elif stat1 == "Constitution" or stat1 == "constitution" and stat2 == "Wisdom" or stat2 == "wisdom":
            con = con + 1
            wis = wis + 1
            print("You now have a + 1 in constitution and wisdom.")
        elif stat1 == "Intelligence" or stat1 == "intelligence" and stat2 == "Strength" or stat2 == "strength":
            intel = intel + 1
            strength = strength + 1
            print("You now have a + 1 in intelligence and strength.")
        elif stat1 == "Intelligence" or stat1 == "intelligence" and stat2 == "Dexterity" or stat2 == "dexterity":
            intel = intel + 1
            dex = dex + 1
            print("You now have a + 1 in intelligence and dexterity.")
        elif stat1 == "Intelligence" or stat1 == "intelligence" and stat2 == "Constitution" or stat2 == "constitution":
            intel = intel + 1
            con = con + 1
            print("You now have a + 1 in intelligence and constitution.")
        elif stat1 == "Intelligence" or stat1 == "intelligence" and stat2 == "Wisdom" or stat2 == "wisdom":
            intel = intel + 1
            wis = wis + 1
            print("You now have a + 1 in intelligence and wisdom.")
        elif stat1 == "Wisdom" or stat1 == "wisdom" and stat2 == "Strength" or stat2 == "strength":
            wis = wis + 1
            strength = strength + 1
            print("You now have a + 1 in wisdom and strength.")
        elif stat1 == "Wisdom" or stat1 == "wisdom" and stat2 == "Dexterity" or stat2 == "dexterity":
            wis = wis + 1
            dex = dex + 1
            print("You now have a + 1 in wisdom and dexterity.")
        elif stat1 == "Wisdom" or stat1 == "wisdom" and stat2 == "Constitution" or stat2 == "constitution":
            wis = wis + 1
            con = con + 1
            print("You now have a + 1 in wisdom and constitution.")
        elif stat1 == "Wisdom" or stat1 == "wisdom" and stat2 == "Intelligence" or stat2 == "intelligence":
            wis = wis + 1
            intel = intel + 1
            print("You now have a + 1 in wisdom and intelligence.")
        else:
            print("You may have spelled something incorrectly please try again.")
        halfelf()


else:
    print('Please restart the program, and be sure that you spell your answers how they are shown.')

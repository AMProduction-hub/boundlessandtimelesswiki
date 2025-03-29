---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/6
- ttrpg-cli/monster/environment/grassland
- ttrpg-cli/monster/environment/mountain
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/dragon
statblock: inline
aliases: ["Young Wind Dragon"]
---
# [Young Wind Dragon](03 - Player Log & Handouts\Mechanics\CLI\bestiary\dragon/young-wind-dragon-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 135*  

*Howling wind encircles the dragon, filling and pushing its wings without the need for them to beat.*Wind dragons view anywhere touched by air as their property, and mortals point to them as the epitome of arrogance. Their narcissism is not without reason, for awe‑inspiring power supports their claims of rightful control. To the dragons of the shifting gales, strength is the ultimate arbiter.

## Braggarts and Bullies

Wind dragons number among the greatest bullies and worst tyrants of mortal creatures. The sometimes-foolhardy creatures take offense at any perceived challenge and pleasure in humiliating rivals. They claim great swathes of territory but care little for its governance—they perceive mortals in that territory as possessions. Vassals receive only dubious protection in exchange for their loyalty. A wind dragon might seek bloody vengeance for the murder of a follower, but it's unlikely to go to any length to prevent the loss of that life in the first place.

## Lords of the Far Horizons

Some believe that the dragons of the winds claim much more than they are capable of controlling or patrolling. Because they so love altitude, they prefer to rule and meet with earth-bound supplicants at the highest point available: the summit of a great mountain or atop a towering monument erected by fearful slaves. But these dragons are also driven by wanderlust and roam far from their thrones. They return eventually, ready to subjugate new generations and press a tyrannical claw on the neck of anyone who questions their right to rule.

## Perpetual Infighting

These wandering tyrants are even more territorial among their own kind than they are among groundlings. Simple trespass by one wind dragon into the territory of another can lead to a battle to the death. Thus, their numbers never grow large, and the weakest among them are frequently culled.

## Portable Hoards

Wind dragons' hoards typically consist of only a few truly valuable relics. Other dragons might sleep on a bed of coins, but common things bore wind dragons. While all true dragons desire and display great wealth, wind dragons concentrate their riches in a small number of notable trophies or unique historic items—often quite portable.

```statblock
"name": "Young Wind Dragon (ToB1-2023)"
"size": "Large"
"type": "dragon"
"alignment": "Chaotic Neutral"
"ac": !!int "16"
"ac_class": "natural armor"
"hp": !!int "123"
"hit_dice": "13d10 + 52"
"stats":
- !!int "20"
- !!int "16"
- !!int "18"
- !!int "14"
- !!int "13"
- !!int "16"
"speed": "30 ft., fly 90 ft. (hover)"
"saves":
  "Charisma": !!int "6"
  "Dexterity": !!int "6"
  "Wisdom": !!int "4"
  "Constitution": !!int "7"
"skillsaves":
  "Intimidation": !!int "6"
  "Stealth": !!int "6"
  "Perception": !!int "7"
  "Acrobatics": !!int "9"
"damage_resistances": "cold"
"damage_immunities": "lightning"
"senses": "blindsight 30 ft., darkvision 120 ft., passive Perception 17"
"languages": "Common, Draconic, Primordial"
"cr": "6"
"traits":
- "desc": "The dragon has advantage on ability checks and saving throws made to avoid\
    \ or escape an effect that would reduce its speed or grapple or restrain it."
  "name": "Elusive"
- "desc": "The dragon can see through areas obscured by fog, mist, clouds, or precipitation."
  "name": "Storm Sight"
"actions":
- "desc": "The dragon makes one Bite attack and two Claw attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +8 to hit, reach 10 ft., one target. Hit: 16\
    \ (2d10 + 5) piercing damage."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 12\
    \ (2d6 + 5) slashing damage."
  "name": "Claw"
- "desc": "The dragon exhales a blast of stormy wind in a 30-foot cone. Each creature\
    \ in that area must make a DC 15 Strength saving throw. On a failure, a creature\
    \ takes 27 (6d8) bludgeoning damage and is pushed up to 15 feet away from the\
    \ dragon and knocked [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone).\
    \ On a success, a creature takes half the damage and isn't pushed or knocked [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone).\
    \ Unprotected flames, such as torches, in the area are extinguished, and protected\
    \ flames, such as those in lanterns, have a 50 percent chance of being extinguished."
  "name": "Tempest Breath (Recharge 5-6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/dragon/token/young-wind-dragon-tob1-2023.webp"
```
^statblock

## Environment

grassland, mountain
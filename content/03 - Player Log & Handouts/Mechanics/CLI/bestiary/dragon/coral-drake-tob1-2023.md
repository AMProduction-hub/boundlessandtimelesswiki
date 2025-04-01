---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/7
- ttrpg-cli/monster/environment/coastal
- ttrpg-cli/monster/environment/underwater
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/dragon
statblock: inline
aliases: ["Coral Drake"]
---
# [Coral Drake](03 - Player Log & Handouts\Mechanics\CLI\bestiary\dragon/coral-drake-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 140*  

*Swimming upright, this creature peels itself from the vibrant seascape and strikes with spined fins, shredding teeth, and a wickedly curved stinger.*

## Camouflaged Hunter

Like a piece of moving coral, this drake's coloration and scale patterns change to match nearby anemones, corals, seaweed, and sea urchins. This adaptation allows the creature considerable stealth in its natural habitat. It avoids combat if it can, preferring to hide and protect its young. Long serrated spines stretch from the coral drake's body, waving in brilliant colors against a blue sea.

## All Spikes and Needles

An array of spikes and slender protrusions form a jagged crown above the creature's narrow face, while a long snout stretches out in front. Inside its mouth, serrated teeth form multiple ringed ridges where its young feed on leftover scraps of food and small parasites. Needle-thin talons spring from finned appendages, and a stinger frilled with tiny barbs curves at the end of its slender tail.

A coral drake measures seven feet from the tip of its snout to its barbed tail. Thin and agile, the beast weighs less than 100 pounds. Both male and female coral drakes gestate their delicate eggs inside sacks within their mouths and throats. This oral incubation protects the vulnerable eggs, but only a handful ever reach maturity, as the parents use their ravenous spawn for defense.

## Poisonous Lairs

Coral drakes live in warm waters near great coral reefs. They hollow out small lairs and protect their meager hoards with the aid of the area's natural inhabitants. Because they are immune to poison, coral drakes often choose lairs nestled in forests of poisonous sea urchins, stinging anemones, and toxic corals. Aside from humankind, the coral drake harbors a great rivalry with dragon turtles. These beasts prize the same hunting grounds and nests and fight for supremacy in the richest reefs.

```statblock
"name": "Coral Drake (ToB1-2023)"
"size": "Medium"
"type": "dragon"
"alignment": "Neutral Evil"
"ac": !!int "16"
"ac_class": "natural armor"
"hp": !!int "127"
"hit_dice": "15d8 + 60"
"stats":
- !!int "19"
- !!int "17"
- !!int "18"
- !!int "10"
- !!int "13"
- !!int "10"
"speed": "15 ft., swim 60 ft."
"saves":
  "Dexterity": !!int "6"
"skillsaves":
  "Stealth": !!int "6"
  "Perception": !!int "7"
  "Acrobatics": !!int "6"
"damage_resistances": "cold"
"damage_immunities": "poison"
"condition_immunities": "[poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 120 ft., passive Perception 17"
"languages": "Draconic"
"cr": "7"
"traits":
- "desc": "The coral drake has advantage on Dexterity ([Stealth](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Stealth))\
    \ checks made while underwater."
  "name": "Underwater Camouflage"
- "desc": "The coral drake can breathe only underwater."
  "name": "Water Breathing"
"actions":
- "desc": "The coral drake makes one Bite attack and two Spined Fin attacks. It can\
    \ replace its Bite attack with a Stinger attack."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 15\
    \ (2d10 + 4) piercing damage."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 13\
    \ (2d8 + 4) piercing damage."
  "name": "Spined Fin"
- "desc": "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 11\
    \ (2d6 + 4) piercing damage, and the target must succeed on a DC 15 Constitution\
    \ saving throw or be [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ for 1 minute. While [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned),\
    \ the target takes 5 (2d4) poison damage at the start of each of its turns.\
    \ The target can repeat the saving throw at the end of each of its turns, ending\
    \ the effect on itself on a success."
  "name": "Stinger"
- "desc": "The coral drake pressurizes the throat sacs that contain its growing young\
    \ and spews tiny, ravenous hatchling drakes in a 15-foot cone. Each creature in\
    \ the area must make a DC 15 Dexterity saving throw. On a failure, a creature\
    \ takes 21 (6d6) piercing damage and is [blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded)\
    \ for 1 minute. On a success, a creature takes half the damage and isn't [blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded).\
    \ A [blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded)\
    \ creature can repeat the saving throw at the end of each of its turns, ending\
    \ the effect on itself on a success."
  "name": "Biting Breath (Recharge 5-6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/dragon/token/coral-drake-tob1-2023.webp"
```
^statblock

## Environment

coastal, underwater
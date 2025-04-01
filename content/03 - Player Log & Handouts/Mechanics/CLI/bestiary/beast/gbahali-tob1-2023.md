---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/6
- ttrpg-cli/monster/environment/grassland
- ttrpg-cli/monster/size/huge
- ttrpg-cli/monster/type/beast
statblock: inline
aliases: ["Gbahali"]
---
# [Gbahali](03 - Player Log & Handouts\Mechanics\CLI\bestiary\beast/gbahali-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 195*  

*This large reptile has dagger-like teeth and a scaly hide of shifting colors.*

## Chameleon Crocodiles

While distantly related to crocodiles, gbahali have adapted to life away from the water. To make up for the lack of cover, gbahali developed hides that shift to match their environments. Gbahali hide changes color to match its surroundings so perfectly that it becomes nearly invisible. Any lonely rock on the grassland might be a gbahali waiting along a trail, caravan route, or watering hole. Their thick hide can be made into hide or leather armor, and with the proper alchemical techniques it retains some of its color-shifting properties.

## Strong Hunters

Gbahalis are powerful predators, challenged only by rivals too large for a gbahali to take down or by predators that hunt in packs and prides, such as lions and gnolls. Gbahalis live solitary lives except during the fall, when males seek out females in their territory. Females lay eggs in the spring and guard the nest until the eggs hatch, but the young gbahali are abandoned to their own devices. Killing an adult gbahali is a sign of bravery and skill for many plains hunters.

## Sentries and Stragglers

In combat, a gbahali relies on its camouflaging hide to ambush prey. It may wait quietly for hours, but its speed and stealth mean it strikes quickly, especially against weak or solitary prey. Its onslaught is strong enough to scatter a herd and leave behind the slowest for the gbahali to bring down.

```statblock
"name": "Gbahali (ToB1-2023)"
"size": "Huge"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "126"
"hit_dice": "12d12 + 48"
"stats":
- !!int "19"
- !!int "14"
- !!int "19"
- !!int "2"
- !!int "13"
- !!int "7"
"speed": "50 ft."
"skillsaves":
  "Stealth": !!int "8"
  "Perception": !!int "4"
"senses": "passive Perception 14"
"languages": ""
"cr": "6"
"traits":
- "desc": "The gbahali's hide adapts to its current surroundings. The gbahali has\
    \ advantage on Dexterity ([Stealth](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Stealth))\
    \ checks made to hide in nonmagical, natural terrain."
  "name": "Shifting Camouflage"
"actions":
- "desc": "The gbahali makes one Bite attack and two Claw attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +7 to hit, reach 10 ft., one target. Hit: 15\
    \ (2d10 + 4) piercing damage. If the target is a Medium or smaller creature,\
    \ it is [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ (escape DC 15). Until this grapple ends, the target is [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained),\
    \ and the gbahali can't Bite another target."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 13\
    \ (2d8 + 4) slashing damage."
  "name": "Claw"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/beast/token/gbahali-tob1-2023.webp"
```
^statblock

## Environment

grassland
---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/6
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/grassland
- ttrpg-cli/monster/size/huge
- ttrpg-cli/monster/type/monstrosity
statblock: inline
aliases: ["Loxoda"]
---
# [Loxoda](03 - Player Log & Handouts\Mechanics\CLI\bestiary\monstrosity/loxoda-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 259*  

*This massive creature combines the torso of an ogre and the body of an elephant as it lumbers through the open plains.*

## Nomadic Families

Loxodas live in small herds of two to three extended families. Several of these communities will usually cluster together, allowing members to move between groups as they get older. They have no permanent settlements, and instead loxoda families travel to new areas when they deplete the available food. Voracious omnivores, a family of loxodas will quickly strip trees bare of leaves, or hunt and cook an entire elephant.

## Often Underestimated

Many people assume that loxodas are as dull witted as the ogres they resemble. This is often a fatal mistake, as the loxoda are quite intelligent. Their simple equipment and straightforward living come not from a lack of skill or knowledge, but their own isolationism and xenophobia. Their immense size and quadruped body make it difficult for them to mine metal ore, and they violently reject communications and trade with other people. The little metal they can gather is either taken from the bodies of their prey or stolen in raids on dwarven, human, or gnoll settlements.

## Vestigial Tusks

All loxodas have curved tusks. While they are too small for use in even ritual combat, they are often decorated with intricate carvings or inlays or are dyed in a pattern developed by their family. Each individual also adapts the patterns with their own individual marks, often inspired by important events in their lives. Some loxodas put golden rings or jeweled bracelets stolen from humanoids onto their tusks as trophies. A loxoda matriarch may have long, dangling chains of such ornaments, indicating her high status and long life.

```statblock
"name": "Loxoda (ToB1-2023)"
"size": "Huge"
"type": "monstrosity"
"alignment": "Neutral Evil"
"ac": !!int "13"
"ac_class": "natural armor"
"hp": !!int "147"
"hit_dice": "14d12 + 56"
"stats":
- !!int "19"
- !!int "12"
- !!int "19"
- !!int "12"
- !!int "14"
- !!int "10"
"speed": "40 ft."
"skillsaves":
  "Athletics": !!int "7"
  "Survival": !!int "5"
"senses": "passive Perception 12"
"languages": "Loxodan"
"cr": "6"
"traits":
- "desc": "If the loxoda moves at least 20 feet straight toward a creature and then\
    \ hits it with a Slam attack on the same turn, that target must succeed on a DC\
    \ 15 Strength saving throw or be knocked [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone).\
    \ If the target is [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone),\
    \ the loxoda can make one Stomp attack against it as a bonus action."
  "name": "Trampling Charge"
"actions":
- "desc": "The loxoda makes one Slam attack and one Spear attack."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +7 to hit, reach 10 ft., one target. Hit: 22\
    \ (4d8 + 4) bludgeoning damage."
  "name": "Slam"
- "desc": "Melee or Ranged Weapon Attack: +7 to hit, reach 5 ft. or range 20/60\
    \ ft., one target. Hit: 14 (3d6 + 4) piercing damage, or 17 (3d8 + 4) piercing\
    \ damage if used with two hands to make a melee attack."
  "name": "Spear"
- "desc": "Melee Weapon Attack: +7 to hit, reach 5 ft., one [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)\
    \ creature. Hit: 20 (3d10 + 4) bludgeoning damage."
  "name": "Stomp"
- "desc": "The loxoda rears up and lands heavily, rattling the land and creatures\
    \ around it. Each creature in contact with the ground within 20 feet of the loxoda\
    \ must make a DC 15 Dexterity saving throw. On a failure, a creature takes 36\
    \ (8d8) bludgeoning damage and takes an extra 10 (3d6) thunder damage at the\
    \ end of its next turn as the shockwaves from the Tooth-Rattling Pound continue\
    \ up through its body. On a success, a creature takes half the damage and doesn't\
    \ take extra thunder damage from shockwaves."
  "name": "Tooth-Rattling Pound (Recharge 5-6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/monstrosity/token/loxoda-tob1-2023.webp"
```
^statblock

## Environment

forest, grassland
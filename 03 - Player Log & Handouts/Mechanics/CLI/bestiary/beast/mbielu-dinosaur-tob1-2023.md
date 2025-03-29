---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/3
- ttrpg-cli/monster/environment/grassland
- ttrpg-cli/monster/environment/underwater
- ttrpg-cli/monster/size/huge
- ttrpg-cli/monster/type/beast
statblock: inline
aliases: ["Mbielu Dinosaur"]
---
# [Mbielu Dinosaur](03 - Player Log & Handouts\Mechanics\CLI\bestiary\beast/mbielu-dinosaur-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 101*  

*This lumbering saurian quadruped has large, oblong plates of bone covered in greenish slime protruding from its back and its thick, club-like tail.*

## Large Plates

People describe this reptilian herbivore as "the animal with planks growing out of its back." The mbielu is a large dinosaur akin to a stegosaurus, with square dorsal plates that support symbiotic colonies of toxic, green algae. The plates themselves are as large as shields.

## Aquatic Herbivore

An mbielu spends most of its life underwater, feeding on aquatic plants and avoiding the withering glare of the harsh sun, but it comes onto land frequently to sun itself for a few hours before immersing itself once again.

## Toxic Alchemy

Its dorsal plate algae undergo an alchemical reaction in the continual transition between water and sky, especially during mbielu migrations to new watery dens. The algae produce a hallucinogenic poison that clouds the minds of most creatures. Mbielus themselves are immune to the toxin.

```statblock
"name": "Mbielu Dinosaur (ToB1-2023)"
"size": "Huge"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "76"
"hit_dice": "8d12 + 24"
"stats":
- !!int "19"
- !!int "14"
- !!int "16"
- !!int "2"
- !!int "12"
- !!int "6"
"speed": "30 ft., swim 20 ft."
"skillsaves":
  "Perception": !!int "3"
"damage_immunities": "poison"
"condition_immunities": "[poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "passive Perception 13"
"languages": ""
"cr": "3"
"traits":
- "desc": "The mbielu can hold its breath for 30 minutes."
  "name": "Hold Breath"
- "desc": "A creature that touches the mbielu or hits it with a melee attack while\
    \ within 5 feet of it takes 2 (1d4) poison damage and must succeed on a DC 13\
    \ Constitution saving throw or be [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ for 1 minute. While [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ in this way, a creature has disadvantage on Intelligence, Wisdom, and Charisma\
    \ saving throws as it experiences mild hallucinations. The [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ creature can repeat the saving throw at the end of each of its turns, ending\
    \ the effect on itself on a success."
  "name": "Toxic Skin"
"actions":
- "desc": "Melee Weapon Attack: +6 to hit, reach 10 ft., one target. Hit: 20\
    \ (3d10 + 4) bludgeoning damage plus 2 (1d4) poison damage. If the target\
    \ is a Large or smaller creature, it must succeed on a DC 13 Strength saving throw\
    \ or be knocked [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)."
  "name": "Tail"
- "desc": "The mbielu releases a deep bellow that vibrates within the bodies of those\
    \ nearby. Each creature within 15 feet of the mbielu must make a DC 13 Constitution\
    \ saving throw, taking 18 (4d8) thunder damage on a failed save, or half as\
    \ much damage on a successful one. If a creature [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ by the mbielu's Toxic Skin fails this saving throw, it is also [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated)\
    \ until the end of its next turn as the combined vibrations and hallucinations\
    \ disorient it."
  "name": "Rumbling Bellow (Recharge 5-6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/beast/token/mbielu-dinosaur-tob1-2023.webp"
```
^statblock

## Environment

grassland, underwater
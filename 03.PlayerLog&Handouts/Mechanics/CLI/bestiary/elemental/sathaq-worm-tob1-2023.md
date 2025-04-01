---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/10
- ttrpg-cli/monster/environment/desert
- ttrpg-cli/monster/environment/hill
- ttrpg-cli/monster/environment/mountain
- ttrpg-cli/monster/environment/underdark
- ttrpg-cli/monster/size/huge
- ttrpg-cli/monster/type/elemental
statblock: inline
aliases: ["Sathaq Worm"]
---
# [Sathaq Worm](03 - Player Log & Handouts\Mechanics\CLI\bestiary\elemental/sathaq-worm-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 317*  

*This titanic worm's rocky hide is rough and hard as stone. Its yawning gullet writhes with miniature worms like itself.*

## Elemental Predators

Sathaq worms are nightmarish predators from the Plane of Elemental Earth with rugged brown hide embedded with stones. They devour stone and flesh with equal ease.

## Guts Filled with Larvae

Sathaq worms are solitary; they approach each other only to mate. Their young incubate inside the worms' gullets. Creatures they swallow are simultaneously digested by the parent worm and devoured by the larvae.

## Painful Presence

Ultrasonic noise and magical ripples that tear at flesh and bone make the very presence of a sathaq worm extremely uncomfortable for creatures of the Material Plane.

```statblock
"name": "Sathaq Worm (ToB1-2023)"
"size": "Huge"
"type": "elemental"
"alignment": "Neutral Evil"
"ac": !!int "16"
"ac_class": "natural armor"
"hp": !!int "149"
"hit_dice": "13d12 + 65"
"stats":
- !!int "22"
- !!int "6"
- !!int "20"
- !!int "5"
- !!int "12"
- !!int "9"
"speed": "20 ft., burrow 40 ft."
"skillsaves":
  "Stealth": !!int "2"
  "Perception": !!int "5"
"damage_resistances": "bludgeoning, piercing, slashing from nonmagical attacks"
"damage_immunities": "acid, poison"
"condition_immunities": "[exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [petrified](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Petrified),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "tremorsense 60 ft., passive Perception 15"
"languages": "understands Deep Speech and Terran but can't speak"
"cr": "10"
"traits":
- "desc": "The sathaq worm emits ultrasonic noise and minor vibrations that cause\
    \ pain and subtly disrupt the functions of most creatures. A creature that starts\
    \ its turn within 15 feet of the sathaq worm must succeed on a DC 17 Constitution\
    \ saving throw or have disadvantage on attack rolls until the start of its next\
    \ turn. Creatures with resistance or immunity to thunder damage automatically\
    \ succeed on the saving throw."
  "name": "Agonizing Aura"
- "desc": "The sathaq worm can burrow through nonmagical, unworked earth and stone.\
    \ While doing so, the worm doesn't disturb the material it moves through."
  "name": "Earth Glide"
- "desc": "The sathaq worm has advantage on Dexterity ([Stealth](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Stealth))\
    \ checks made to hide in sandy, muddy, or rocky terrain."
  "name": "Earthen Camouflage"
- "desc": "The sathaq worm deals double damage to objects and structures."
  "name": "Siege Monster"
"actions":
- "desc": "The sathaq worm makes one Bite attack and two Slam attacks, or it makes\
    \ three Slam attacks. It can replace its Bite attack with a use of Swallow."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +10 to hit, reach 10 ft., one target. Hit: 24\
    \ (4d8 + 6) piercing damage, and the target is [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ (escape DC 17). Until this grapple ends, the target is [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained),\
    \ and the sathaq worm can't Bite another target."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +10 to hit, reach 10 ft., one target. Hit: 19\
    \ (3d8 + 6) bludgeoning damage."
  "name": "Slam"
- "desc": "The sathaq worm makes one Bite attack against a Large or smaller creature\
    \ it is grappling. If the attack hits, the target is also swallowed, and the grapple\
    \ ends. While swallowed, the target is [blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded)\
    \ and [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained),\
    \ it has total cover against attacks and other effects outside the worm (including\
    \ the worm's Agonizing Aura), and takes 10 (3d6) piercing damage and 10 (3d6)\
    \ acid damage at the start of each of the sathaq worm's turns. The sathaq worm\
    \ can have only one creature swallowed at a time.\n\nIf the sathaq worm takes\
    \ 30 damage or more on a single turn from the swallowed creature, the sathaq worm\
    \ must succeed on a DC 15 Constitution saving throw at the end of that turn or\
    \ regurgitate the creature, which falls [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)\
    \ in a space within 5 feet of the sathaq worm. If the sathaq worm dies, a swallowed\
    \ creature is no longer [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ by it and can escape from the corpse by using 10 feet of movement, exiting [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)."
  "name": "Swallow"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/elemental/token/sathaq-worm-tob1-2023.webp"
```
^statblock

## Environment

desert, hill, mountain, underdark
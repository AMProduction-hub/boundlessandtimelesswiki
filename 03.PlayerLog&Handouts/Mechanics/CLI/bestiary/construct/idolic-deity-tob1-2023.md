---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/8
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/small
- ttrpg-cli/monster/type/construct
statblock: inline
aliases: ["Idolic Deity"]
---
# [Idolic Deity](03 - Player Log & Handouts\Mechanics\CLI\bestiary\construct/idolic-deity-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 239*  

*This small demonic idol emits a palpable malice.*

## Relics of Dark Gods

Idolic deities are found in ancient temples and deserted tombs. They are relics of an elder age and all that remain of the favored children of a deceiving dark god—mighty lordlings like Akoman the Evil Thought, Nanghant the Discontented, and Sarvar the Oppressor. Sent to consume the souls of those worshiping gods of light, these beings of shadow and sand labor slowly through corruption of the soul rather than outright war.

## Imprisoned Corruption

The first idolic deities were created when corrupted ancient tribes and their priests began worshiping idols as gods, forsaking their masters' purposes to revel in their pride and vanity. Their deities struck them down for their treachery and imprisoned their corrupted souls in the idols they worshiped.

```statblock
"name": "Idolic Deity (ToB1-2023)"
"size": "Small"
"type": "construct"
"alignment": "Neutral Evil"
"ac": !!int "17"
"ac_class": "natural armor"
"hp": !!int "105"
"hit_dice": "14d6 + 56"
"stats":
- !!int "14"
- !!int "20"
- !!int "18"
- !!int "10"
- !!int "11"
- !!int "20"
"speed": "0 ft., fly 30 ft. (hover)"
"saves":
  "Wisdom": !!int "3"
"skillsaves":
  "Deception": !!int "8"
  "Stealth": !!int "8"
"damage_resistances": "bludgeoning, piercing, slashing from nonmagical attacks"
"damage_immunities": "poison, psychic"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [petrified](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Petrified),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned),\
  \ [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)"
"senses": "darkvision 60 ft., passive Perception 10"
"languages": "Abyssal, Common, Infernal, telepathy 60 ft."
"cr": "8"
"traits":
- "desc": "The idolic deity's presence causes devout followers to doubt their faith.\
    \ When a creature attempts to use divine or celestial power, such as a cleric\
    \ casting a spell or a paladin using Divine Smite, it must make a DC 16 Wisdom\
    \ saving throw. On a failure, the spell, class feature, or other divine or celestial\
    \ power is expended, but it has no effect."
  "name": "Apostasy Aura"
- "desc": "The idolic deity doesn't require air, food, drink, or sleep."
  "name": "Construct Nature"
- "desc": "While the idolic deity remains motionless, it is indistinguishable from\
    \ a normal statue."
  "name": "False Appearance"
- "desc": "The idolic deity can move through other creatures and objects as if they\
    \ were difficult terrain. It takes 5 (1d10) force damage if it ends its turn\
    \ inside an object."
  "name": "Incorporeal Movement"
"actions":
- "desc": "The idolic deity can use its Seduce the Righteous. It then makes two Slam\
    \ attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 8 (1d6\
    \ + 5) bludgeoning damage plus 18 (4d8) psychic damage."
  "name": "Slam"
- "desc": "The idolic deity corrupts one creature it can see within 30 feet of it.\
    \ The target must succeed on a DC 16 Wisdom saving throw or have disadvantage\
    \ on attack rolls, ability checks, or saving throws (the idolic deity's choice)\
    \ until the end of its next turn. Creatures that wield divine or celestial power,\
    \ such as clerics, paladins, or aasimars, have disadvantage on the saving throw."
  "name": "Seduce the Righteous"
"bonus_actions":
- "desc": "While in dim light or darkness, the idolic deity takes the Hide action."
  "name": "Shadow Stealth"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/construct/token/idolic-deity-tob1-2023.webp"
```
^statblock

## Environment

urban
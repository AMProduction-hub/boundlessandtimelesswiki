---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/6
- ttrpg-cli/monster/environment/underdark
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/fiend/devil
statblock: inline
aliases: ["Crystalline Devil"]
---
# [Crystalline Devil](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fiend/crystalline-devil-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 94*  

*This gem-encrusted devil grins with jagged teeth and bares claws as sharp as glass.*

## Gem-Coated

Crystalline devils resemble gem-coated humanoids with cruel, twisted faces, jagged teeth, and terrible talons like shards of broken glass. Their feet, however, are soft and bare, allowing them to pad along in silence as they seek a favorable spot to assume gem form.

## Winking Jewels

In its treasure form, a crystalline devil resembles a sparkling jewel, glowing with a warm inner light. It seeks to catch the eye of an unwary creature whose mind it might corrupt to greed and murder. If its identity is discovered in gem form, it reassumes its normal form and attacks.

## Passed Along

After insinuating themselves into groups, crystalline devils encourage betrayal and murder, then persuade a host to pass on their treasure as atonement for their crimes.

```statblock
"name": "Crystalline Devil (ToB1-2023)"
"size": "Medium"
"type": "fiend"
"subtype": "devil"
"alignment": "Lawful Evil"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "102"
"hit_dice": "12d8 + 48"
"stats":
- !!int "18"
- !!int "12"
- !!int "18"
- !!int "14"
- !!int "13"
- !!int "15"
"speed": "30 ft."
"saves":
  "Charisma": !!int "5"
  "Wisdom": !!int "4"
"skillsaves":
  "Deception": !!int "8"
  "Stealth": !!int "7"
  "Insight": !!int "4"
"damage_resistances": "acid; cold; bludgeoning, piercing, slashing from nonmagical\
  \ attacks that aren't silvered"
"damage_immunities": "fire, poison"
"condition_immunities": "[poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 120 ft., passive Perception 11"
"languages": "Celestial, Common, Infernal, telepathy 120 ft."
"cr": "6"
"traits":
- "desc": "Magical darkness doesn't impede the crystalline devil's darkvision."
  "name": "Devil's Sight"
- "desc": "While the devil remains motionless, it is indistinguishable from an ordinary\
    \ gemstone."
  "name": "False Appearance (Gemstone Form Only)"
- "desc": "The devil sheds dim light in a 5-foot radius. Each creature that starts\
    \ its turn within 30 feet of the devil and that can see it must succeed on a DC\
    \ 15 Wisdom saving throw or be [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed)\
    \ for 1 minute. While [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
    \ a creature is [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated)\
    \ and must move on its turn toward the devil by the safest route, trying to get\
    \ within 5 feet of the devil to hold it. The [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed)\
    \ creature can repeat the saving throw at the end of each of its turns, ending\
    \ the effect on itself on a success. On a success, a creature is also immune to\
    \ this devil's Glittering Temptation for the next 24 hours. A creature [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed)\
    \ by the devil has disadvantage on the saving throw against Crystalline Spray."
  "name": "Glittering Temptation (Gemstone Form Only)"
- "desc": "The crystalline devil has advantage on saving throws against spells and\
    \ other magical effects."
  "name": "Magic Resistance"
"actions":
- "desc": "The devil makes three Claw attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 13\
    \ (2d8 + 4) slashing damage."
  "name": "Shard Claw (Fiend Form Only)"
- "desc": "The crystalline devil sprays a burst of crystal shards. Each creature within\
    \ 15 feet of the devil must make a DC 15 Dexterity saving throw, taking 27 (6d8)\
    \ piercing damage on a failed save, or half as much damage on a successful one."
  "name": "Crystalline Spray (Recharge 5-6)"
"bonus_actions":
- "desc": "The crystalline devil magically transforms into a Small or smaller gemstone\
    \ or back into its true form, which is a Fiend. Its statistics, other than its\
    \ size, are the same in each form, except it can't move or speak when in its gemstone\
    \ form. Any equipment it is wearing or carrying transforms with it. It reverts\
    \ to its true from if it dies."
  "name": "Betraying Carbuncle"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fiend/token/crystalline-devil-tob1-2023.webp"
```
^statblock

## Environment

underdark, urban
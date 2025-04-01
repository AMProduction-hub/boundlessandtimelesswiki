---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/7
- ttrpg-cli/monster/environment/any
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/fiend
statblock: inline
aliases: ["Herald of Darkness"]
---
# [Herald of Darkness](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fiend/herald-of-darkness-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 233*  

*A tall and beautiful fiend, this creature resembles a dark-haired fey wearing a cloak and armor glittering with dark light.*

Heralds of darkness speak in fluid tones and sing with the voices of angels, but their hearts are foul and treacherous.

## Vision of Evil

Heralds of darkness can take on another appearance entirely, disappearing into insubstantial shadows and unveiling an evil majestic form that leaves those who see it shaken and weak—and often blind. Speaking of this form is difficult, but poets and bards trying to describe it have said it resembles an apocalyptic horror built of chained souls and the slow death of innocents carried along in a glacial river, rushing to an inevitable doom.

## Sword and Cloak

The black sword and star-scattered cloak of a herald of darkness are part of its magical substance and cannot be parted from it. Some believe the cloak and blade are true visions of its body, and that the smiling face and pleasing form are entirely illusory.

## Corruptors of the Fey

Heralds of darkness are companions and sometimes masters to the shadow fey. They seek to draw many others into their orbit with wild promises of great power, debauchery, and other delights. They are rivals to the heralds of blood and bitter foes to all angels of light.

```statblock
"name": "Herald of Darkness (ToB1-2023)"
"size": "Large"
"type": "fiend"
"alignment": "Neutral Evil"
"ac": !!int "15"
"ac_class": "[chain shirt](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/items/chain-shirt.md)"
"hp": !!int "105"
"hit_dice": "10d10 + 50"
"stats":
- !!int "20"
- !!int "14"
- !!int "20"
- !!int "12"
- !!int "15"
- !!int "19"
"speed": "30 ft., fly 50 ft., swim 30 ft."
"saves":
  "Charisma": !!int "7"
  "Strength": !!int "8"
  "Constitution": !!int "8"
"skillsaves":
  "Athletics": !!int "8"
  "Deception": !!int "7"
  "Stealth": !!int "5"
  "Perception": !!int "5"
"damage_resistances": "bludgeoning, cold, lightning"
"damage_immunities": "necrotic, poison"
"condition_immunities": "[exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [petrified](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Petrified),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 240 ft., passive Perception 15"
"languages": "Common, Elvish, Goblin, Infernal, Sylvan"
"cr": "7"
"traits":
- "desc": "The herald of darkness has resistance to bludgeoning, piercing, and slashing\
    \ damage and can enter a hostile creature's space and stop there. In addition,\
    \ it can move through a space as narrow as 1 inch wide without squeezing."
  "name": "Made of Shadows (Shadow Form Only)"
- "desc": "Magical darkness doesn't impede the herald's darkvision."
  "name": "Shadow's Sight"
"actions":
- "desc": "The herald of darkness makes two Embrace Darkness or Shadow Sword attacks."
  "name": "Multiattack"
- "desc": "Melee Spell Attack: +7 to hit, reach 0 ft., one creature in the herald's\
    \ space. Hit: 18 (3d8 + 5) necrotic damage, and the target must succeed on\
    \ a DC 15 Constitution saving throw or be [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed)\
    \ until the end of its next turn."
  "name": "Embrace Darkness (Shadow Form Only)"
- "desc": "Melee Weapon Attack: +8 to hit, reach 10 ft., one target. Hit: 14\
    \ (2d8 + 5) slashing damage plus 9 (2d8) necrotic damage."
  "name": "Shadow Sword (Fiend Form Only)"
- "desc": "The herald of darkness emits a sinister burst of infernal power. Each creature\
    \ within 15 feet of the herald and that can see it must make a DC 15 Constitution\
    \ saving throw. On a failure, a creature takes 27 (6d8) necrotic damage and\
    \ is [blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded)\
    \ for 1 minute. On a success, a creature takes half the damage and isn't [blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded).\
    \ A creature that fails the saving throw by 5 or more is also [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed)\
    \ until the end of its next turn. A [blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded)\
    \ creature can repeat the saving throw at the end of each of its turns, ending\
    \ the effect on itself on a success."
  "name": "Majesty of the Abyss (Recharge 5-6)"
"bonus_actions":
- "desc": "The herald magically transforms into a Large shadow or back into its true\
    \ form, which is a Fiend. Its statistics are the same in each form. Any equipment\
    \ it is wearing or carrying transforms with it. It reverts to its true form if\
    \ it dies."
  "name": "Shadow Shape"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fiend/token/herald-of-darkness-tob1-2023.webp"
```
^statblock

## Environment

any
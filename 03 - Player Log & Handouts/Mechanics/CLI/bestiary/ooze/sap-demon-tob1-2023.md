---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/4
- ttrpg-cli/monster/environment/farmland
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/size/small
- ttrpg-cli/monster/type/ooze
statblock: inline
aliases: ["Sap Demon"]
---
# [Sap Demon](03 - Player Log & Handouts\Mechanics\CLI\bestiary\ooze/sap-demon-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 315*  

*The axe mark in the tree oozes with viscous sap that forms into a small, vaguely humanoid shape at the tree's roots. It half walks and half flows forward.*

## Tree Oozes

Despite the name, sap demons aren't true demons. They are sentient oozes that form when an enchanted tree is cut or injured. A few hours after the injury, they pool into a shape that vaguely resembles their tree's attacker; if the tree cutter had a beard, the sap demon's human-like head drips in the vague shape of a beard. After dispatching the tree's attacker, most sap demons return to the tree, though some remain curious or malevolent enough to continue exploring the world.

## Reckless Possessors

A sap demon earns its name from its ability to possess another creature by oozing down its throat. Once inside, the sap demon makes the host bleed as the tree bled and is reckless with the body. However, no matter how the body is bandaged or cured, the host perpetually bleeds.

```statblock
"name": "Sap Demon (ToB1-2023)"
"size": "Small"
"type": "ooze"
"alignment": "Chaotic Evil"
"ac": !!int "13"
"ac_class": "natural armor"
"hp": !!int "81"
"hit_dice": "18d6 + 18"
"stats":
- !!int "14"
- !!int "6"
- !!int "12"
- !!int "7"
- !!int "14"
- !!int "7"
"speed": "20 ft., climb 20 ft."
"damage_resistances": "bludgeoning"
"damage_immunities": "acid"
"condition_immunities": "[blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded),\
  \ [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [deafened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Deafened),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)"
"senses": "blindsight 90 ft. (blind beyond this radius), passive Perception 12"
"languages": ""
"cr": "4"
"traits":
- "desc": "The sap demon can move through a space as narrow as 1 inch wide without\
    \ squeezing."
  "name": "Amorphous"
- "desc": "The sap demon doesn't require sleep."
  "name": "Ooze Nature"
- "desc": "If the sap demon takes fire damage, its speed is increased by 10 feet until\
    \ the end of its next turn. If it takes cold damage, its speed is reduced by 10\
    \ feet until the end of its next turn."
  "name": "Season's Change"
"actions":
- "desc": "The sap demon makes two Slam or Lob Sap attacks. If both Slam attacks hit\
    \ a Medium or smaller creature, the creature is [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ (escape DC 12)."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 7 (2d4\
    \ + 2) bludgeoning damage plus 7 (2d6) acid damage."
  "name": "Slam"
- "desc": "Ranged Weapon Attack: +4 to hit, range 20/60 ft., one target. Hit:\
    \ 12 (3d6 + 2) bludgeoning damage, and the target's speed is reduced by 10 feet\
    \ until the end of its next turn."
  "name": "Lob Sap"
- "desc": "One humanoid the sap demon is grappling or that is [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated)\
    \ within 5 feet of the sap demon must succeed on a DC 12 Constitution saving throw\
    \ or be possessed by the sap demon. The sap demon then disappears, and the target\
    \ is [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated)\
    \ and loses control of its body. The sap demon now controls the body but doesn't\
    \ deprive the target of awareness. The ooze can't be targeted by any attack, spell,\
    \ or other effect, except ones that restore a creature's hp maximum. The ooze\
    \ retains its Intelligence, Wisdom, and Charisma and condition immunities. It\
    \ otherwise uses the possessed target's statistics, but doesn't gain access to\
    \ the target's knowledge, class features, or proficiencies.\n\nWhile possessed,\
    \ the target's body seeps blood out of its ears, nose, and eyes, and the target\
    \ takes 2 (1d4) acid damage at the end of each hour. Its hp maximum is also\
    \ reduced by that amount. This reduction lasts until the target finishes a long\
    \ rest after the possession ends. The possession lasts until the body drops to\
    \ 0 hp, the ooze ends it as a bonus action, or the ooze is forced out by an effect\
    \ like the [greater restoration](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/greater-restoration.md)\
    \ spell. When the possession ends, the ooze reappears in an unoccupied space within\
    \ 5 feet of the body. The target is immune to this sap demon's Soul Sap for 24\
    \ hours after succeeding on the saving throw or after the possession ends."
  "name": "Soul Sap (Recharge 6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/ooze/token/sap-demon-tob1-2023.webp"
```
^statblock

## Environment

farmland, forest
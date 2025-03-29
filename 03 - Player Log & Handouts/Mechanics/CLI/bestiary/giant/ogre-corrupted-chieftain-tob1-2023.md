---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/7
- ttrpg-cli/monster/environment/badlands
- ttrpg-cli/monster/environment/farmland
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/giant
statblock: inline
aliases: ["Ogre Corrupted Chieftain"]
---
# [Ogre Corrupted Chieftain](03 - Player Log & Handouts\Mechanics\CLI\bestiary\giant/ogre-corrupted-chieftain-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 289*  

*Spikes adorn the green skin of this large ogre, and it brandishes a nail-studded club.*

Twisted by wild magic, fiendish power, or arcane disease, the corrupted chieftain has turned its mutation into an advantage. The corruption within makes this chieftain stronger and more savage than the ogres it bullies and commands.

## Changed Form

The power that changed the corrupted chieftain's body caused its skin to toughen and produce dozens of bony spikes. It also caused the chieftain to become stronger, hardier, and more imposing than its ogre kin, solidifying its position as a clan's chieftain.

## Powerful Leader

Though the corrupted chieftain remains as tactical as it was before coming into contact with the force that changed it, the power coursing through its veins gives it uncanny sway over other ogres. The chieftain can belt out orders without receiving grumbles and can even imbue a measure of its power into its underlings.

```statblock
"name": "Ogre Corrupted Chieftain (ToB1-2023)"
"size": "Large"
"type": "giant"
"alignment": "Chaotic Evil"
"ac": !!int "17"
"ac_class": "natural armor"
"hp": !!int "133"
"hit_dice": "14d10 + 56"
"stats":
- !!int "23"
- !!int "8"
- !!int "18"
- !!int "5"
- !!int "7"
- !!int "12"
"speed": "40 ft."
"saves":
  "Charisma": !!int "4"
  "Constitution": !!int "7"
"senses": "darkvision 60 ft., passive Perception 8"
"languages": "Common, Giant"
"cr": "7"
"traits":
- "desc": "The power coursing through the corrupted chieftain's veins flows into its\
    \ weapons. The chieftain's weapon attacks are magical. When the chieftain hits\
    \ with any weapon, the weapon deals an extra 2d8 force damage (included in the\
    \ attack)."
  "name": "Magic-Infused Weapons"
- "desc": "A creature that touches the ogre or hits it with a melee attack while within\
    \ 5 feet of it takes 5 (2d4) piercing damage."
  "name": "Spiked Hide"
"actions":
- "desc": "The corrupted ogre can use its Chieftain's Command or Chieftain's Might.\
    \ It then makes two Greatclub or Javelin attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 15\
    \ (2d8 + 6) bludgeoning damage plus 9 (2d8) force damage."
  "name": "Greatclub"
- "desc": "Melee or Ranged Weapon Attack: +9 to hit, reach 5 ft. or range 30/120\
    \ ft., one target. Hit: 13 (2d6 + 6) piercing damage plus 9 (2d8) force\
    \ damage."
  "name": "Javelin"
- "desc": "The corrupted chieftain barks an order to one Giant it can see within 30\
    \ feet of it, sharing a measure of its power with the target. The target has advantage\
    \ on the next attack roll it makes before the start of the chieftain's next turn.\
    \ In addition, the next attack roll against the target before the start of the\
    \ chieftain's next turn has disadvantage."
  "name": "Chieftain's Command"
- "desc": "The corrupted chieftain causes its eyes to glow, its muscles to swell,\
    \ and the ground beneath its feet to rumble. Each creature within 15 feet of the\
    \ chieftain must succeed on a DC 15 Wisdom saving throw or be [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)\
    \ until the end of its next turn."
  "name": "Chieftain's Might"
"bonus_actions":
- "desc": "The corrupted chieftain moves up to its speed toward a hostile creature\
    \ it can see."
  "name": "Aggressive"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/giant/token/ogre-corrupted-chieftain-tob1-2023.webp"
```
^statblock

## Environment

badlands, farmland, forest
---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/5
- ttrpg-cli/monster/environment/farmland
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/grassland
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/aberration
statblock: inline
aliases: ["Rift Swine"]
---
# [Rift Swine](03 - Player Log & Handouts\Mechanics\CLI\bestiary\aberration/rift-swine-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 307*  

*This enormous pig is as large as an ox, and its mouth bristles with mismatched tusks. Its body is a lopsided mass of tumorous flesh that gives way to eyes and vestigial mouths, while long tentacles trail from its sides.*

From time to time, a breach forms in the fabric of the multiverse, and the Material Plane is bathed in the energy of alien dimensions. Living creatures exposed to this incursion can undergo horrible mutations, turning into monstrous mockeries of their former shapes. One example of this phenomenon is the rift swine: once-ordinary pigs transformed into slavering horrors after being bathed in eldritch light.

## Destructive Herds

Rift swine travel in small herds. Their effect on an area can be catastrophic—they eat nearly anything, possess a fiendish cunning, and delight in the destruction they cause. A rift swine has difficulty perceiving anything smaller than itself as a threat, leading it to attack most other creatures on sight and fighting until it is destroyed.

## Abyssal Meat

Rumors of vast herds of hundreds of rift swine on strongly chaos-aligned planes, cultivated by the lords of those places as a food source, are thankfully unconfirmed.

```statblock
"name": "Rift Swine (ToB1-2023)"
"size": "Large"
"type": "aberration"
"alignment": "Neutral"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "127"
"hit_dice": "15d10 + 45"
"stats":
- !!int "18"
- !!int "10"
- !!int "17"
- !!int "4"
- !!int "12"
- !!int "5"
"speed": "40 ft."
"damage_resistances": "force, poison"
"senses": "darkvision 60 ft., passive Perception 11"
"languages": ""
"cr": "5"
"traits":
- "desc": "At the start of each of its turns, the rift swine's body experiences a\
    \ mutation. Choose an option or roll a d6 to determine the type of mutation.\
    \ The mutation lasts until the start of the rift swine's next turn."
  "name": "Chaos Mutations"
- "desc": "The next creature that hits the rift swine with a melee attack while within\
    \ 5 feet of the rift swine takes 3 (1d6) acid damage."
  "name": "1 Acid Boils"
- "desc": "The next melee attack the rift swine makes that hits a creature deals an\
    \ extra 3 (1d6) acid damage to the creature."
  "name": "2 Acid Saliva"
- "desc": "The rift swine has advantage on the next attack roll it makes."
  "name": "3 Extra Eyes"
- "desc": "The rift swine's speed increases by 10 feet, and the rift swine doesn't\
    \ provoke opportunity attacks when it moves out of an enemy's reach."
  "name": "4 Extra Hooves"
- "desc": "The rift swine gains 10 3d6 temporary hp."
  "name": "5 Second Heart"
- "desc": "The rift swine has resistance to bludgeoning, piercing, or slashing damage\
    \ (the rift swine's choice)."
  "name": "6 Toughened Hide"
- "desc": "The rift swine has advantage on Wisdom ([Perception](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Perception))\
    \ checks that rely on sight and on saving throws against being [blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded).\
    \ In addition, if the rift swine isn't [blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded),\
    \ creatures attacking it can't benefit from traits and features that rely on a\
    \ creature's allies distracting or surrounding the rift swine, such as the Pack\
    \ Tactics trait or Sneak Attack class feature."
  "name": "Dozens of Eyes"
"actions":
- "desc": "The rift swine makes one Tusk attack and two Tentacle attacks, or it makes\
    \ three Warping Bolt attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 13\
    \ (2d8 + 4) slashing damage."
  "name": "Tusk"
- "desc": "Melee Weapon Attack: +7 to hit, reach 10 ft., one target. Hit: 11\
    \ (2d6 + 4) bludgeoning damage. If the target is a Medium or smaller creature,\
    \ it is [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ (escape DC 14). Until this grapple ends, the target is [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained).\
    \ The rift swine has two tentacles, each of which can grapple only one target."
  "name": "Tentacle"
- "desc": "Ranged Spell Attack: +4 to hit, range 60 ft., one target. Hit: 11\
    \ (3d6 + 1) force damage, and the target must succeed on a DC 14 Constitution\
    \ saving throw or have disadvantage on attack rolls as reality-warping energies\
    \ temporarily distort its body."
  "name": "Warping Bolt"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/aberration/token/rift-swine-tob1-2023.webp"
```
^statblock

## Environment

farmland, forest, grassland
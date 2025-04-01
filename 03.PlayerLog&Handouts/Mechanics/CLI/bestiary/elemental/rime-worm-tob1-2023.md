---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/6
- ttrpg-cli/monster/environment/arctic
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/elemental
statblock: inline
aliases: ["Rime Worm"]
---
# [Rime Worm](03 - Player Log & Handouts\Mechanics\CLI\bestiary\elemental/rime-worm-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 308*  

*The long, crusty slug sparkles like ice, and long tendrils dangle from its gaping mouth.*

## Ice Burrowers

The rime worm's tendrils help it burrow through ice and snow as well as absorb sustenance from prey. Their pale, almost translucent, skin is coated with ice crystals, making them difficult to spot in their snowy habitat.

## Spray Black Ice

The worms are fierce hunters, and their abilities to spray skewers of ice and freeze their prey make them extremely dangerous.

```statblock
"name": "Rime Worm (ToB1-2023)"
"size": "Large"
"type": "elemental"
"alignment": "Unaligned"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "114"
"hit_dice": "12d10 + 48"
"stats":
- !!int "20"
- !!int "14"
- !!int "19"
- !!int "6"
- !!int "14"
- !!int "3"
"speed": "30 ft., burrow 30 ft., swim 30 ft."
"skillsaves":
  "Stealth": !!int "5"
"damage_immunities": "cold"
"senses": "darkvision 120 ft., passive Perception 12"
"languages": ""
"cr": "6"
"traits":
- "desc": "The rime worm can breathe air and water."
  "name": "Amphibious"
- "desc": "A creature that touches the rime worm or hits it with a melee attack while\
    \ within 5 feet of it takes 4 (1d8) cold damage."
  "name": "Icy Body"
- "desc": "The rime worm has advantage on Dexterity ([Stealth](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Stealth))\
    \ checks made to hide in snowy terrain."
  "name": "Snow Camouflage"
- "desc": "The rime worm can burrow through nonmagical snow and ice in addition to\
    \ sand, earth, and mud. In addition, difficult terrain composed of snow or ice\
    \ doesn't cost it extra movement."
  "name": "Snow Stride"
"actions":
- "desc": "The rime worm makes two Rime Tendril attacks. It can replace one attack\
    \ with a use of Freeze Prey."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +8 to hit, reach 10 ft., one target. Hit: 12\
    \ (2d6 + 5) bludgeoning damage plus 9 (2d8) cold damage. The target is [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ (escape DC 15) if it is a Medium or smaller creature and the rime worm doesn't\
    \ have another creature [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)."
  "name": "Rime Tendril"
- "desc": "One creature [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ by the rime worm must succeed on a DC 15 Constitution saving throw or be [petrified](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Petrified)\
    \ in ice for 1 minute. The target can repeat the saving throw at the end of each\
    \ of its turns, ending the effect on itself on a success. A [petrified](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Petrified)\
    \ creature that takes fire damage has advantage on the saving throw."
  "name": "Freeze Prey"
- "desc": "The rime worm sprays slivers of ice in a 30-foot cone. Each creature in\
    \ the area must make a DC 15 Constitution saving throw, taking 36 (8d8) cold\
    \ damage on a failed save, or half as much damage on a successful one. The area\
    \ then becomes icy, difficult terrain for 1 minute."
  "name": "Black Ice Spray (Recharge 5-6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/elemental/token/rime-worm-tob1-2023.webp"
```
^statblock

## Environment

arctic
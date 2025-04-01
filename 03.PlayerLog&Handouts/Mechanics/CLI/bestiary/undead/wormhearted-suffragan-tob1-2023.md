---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/5
- ttrpg-cli/monster/environment/any
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/undead
statblock: inline
aliases: ["Wormhearted Suffragan"]
---
# [Wormhearted Suffragan](03 - Player Log & Handouts\Mechanics\CLI\bestiary\undead/wormhearted-suffragan-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 398*  

*Robes cover the rotting flesh and lifeless gray hair of this humanoid. Fine, arm-length worms wriggle through abscesses in its flesh and its empty eye-sockets, and it moves with a stooped, shuffling gait.*

Wormhearted suffragans are devoted followers of Qorgeth, Demon Lord of Worms, who they believe is the servant and forerunner of a dark goddess of worms and decay.

## Dark Worm Hearts

Formerly, the suffragans were priests or holy officers of other faiths, but their hearts were corrupted by their fear and loathing. Once pledged to the service of the devouring worm, Qorgeth replaced their hearts with a bulbous, writhing conglomeration of worms, which permits them to carry on with an undead mockery of life.

## Prey on the Wounded

Suffragans frequently follow armies, visiting battlefields shortly after the fighting is over. In the guise of gravediggers, nurses, or chirurgeons, they select their targets from among the dead and dying for as long as they can remain undetected, spreading their worms to create new servants for their demon lord.

## Fear Light and Radiance

Wormhearted suffragans are especially susceptible to the flesh-searing power of light. For this reason, they avoid priests of the sun god or gods of light. At night, however, they are a walking contagion, infesting enemies with parasitic worms that devour victims from within.

```statblock
"name": "Wormhearted Suffragan (ToB1-2023)"
"size": "Medium"
"type": "undead"
"alignment": "Chaotic Evil"
"ac": !!int "13"
"hp": !!int "120"
"hit_dice": "16d8 + 48"
"stats":
- !!int "10"
- !!int "17"
- !!int "16"
- !!int "11"
- !!int "16"
- !!int "8"
"speed": "30 ft."
"skillsaves":
  "Medicine": !!int "6"
  "Religion": !!int "3"
"damage_vulnerabilities": "radiant"
"damage_immunities": "necrotic, poison"
"condition_immunities": "[poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 60 ft., passive Perception 13"
"languages": "the languages it knew in life"
"cr": "5"
"traits":
- "desc": "The wormhearted suffragan has advantage on saving throws against spells\
    \ and other magical effects."
  "name": "Magic Resistance"
- "desc": "A Humanoid killed by the wormhearted suffragan's disease rises 1d4 hours\
    \ later as a skeleton or zombie (the suffragan's choice), unless the Humanoid\
    \ is restored to life or its body is destroyed. Between its disease and its Animating\
    \ Worms, the suffragan can have no more than fifteen total skeletons and zombies\
    \ under its control at one time."
  "name": "Master of Undeath"
- "desc": "The wormhearted suffragan doesn't require air, food, drink, or sleep."
  "name": "Undead Nature"
"actions":
- "desc": "The wormhearted suffragan makes two Worm-Coated Fist or Paralyzing Bolt\
    \ attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 10\
    \ (2d6 + 3) bludgeoning damage plus 7 (2d6) necrotic damage, and the target\
    \ must succeed on a DC 14 Constitution saving throw or contract a disease. Until\
    \ the disease is cured, the target can't regain hp, and its hp maximum decreases\
    \ by 7 (2d6) every 24 hours. This reduction lasts until the target finishes\
    \ a long rest after the disease is cured. The target dies if this effect reduces\
    \ its hp maximum to 0."
  "name": "Worm-Coated Fist"
- "desc": "Ranged Spell Attack: +6 to hit, range 60 ft., one target. Hit: 17\
    \ (4d6 + 3) necrotic damage, and the target must succeed on a DC 14 Constitution\
    \ saving throw or be [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed)\
    \ until the end of its next turn."
  "name": "Paralyzing Bolt"
- "desc": "The wormhearted suffragan touches the body of a dead Humanoid, passing\
    \ on some of the suffragan's worms. The worms fill the target, animating it as\
    \ a skeleton or zombie (the suffragan's choice) under the suffragan's control."
  "name": "Animating Worms (3/Day)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/undead/token/wormhearted-suffragan-tob1-2023.webp"
```
^statblock

## Environment

any
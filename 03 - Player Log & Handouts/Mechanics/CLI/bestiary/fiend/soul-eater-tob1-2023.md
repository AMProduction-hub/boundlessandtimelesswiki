---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/7
- ttrpg-cli/monster/environment/any
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/fiend
statblock: inline
aliases: ["Soul Eater"]
---
# [Soul Eater](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fiend/soul-eater-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 336*  

*The creature walks on crab-like legs, carrying a fleshy, ectoplasm-filled mass on its back.*

## Merchants from the Lower Planes

Soul eaters are soul-collecting fiends from the Lower Planes where they freely barter for prey. When a soul eater dies, the souls it carried are released and returned to their bodies or to their appropriate final destinations. Regardless, a dead soul eater has no souls for the demons and devils who value souls as currency. This gives soul eaters a measure of safety and power in the Lower Planes, and many of them operate as neutral merchants among other fiends.

## Hatred of the Sun God

Soul eaters bear a particular antipathy for followers of the deities of the sun. They go to great lengths to kill any such deity's clergy, even defying the wishes of their fiendish superiors on occasion.

```statblock
"name": "Soul Eater (ToB1-2023)"
"size": "Medium"
"type": "fiend"
"alignment": "Neutral Evil"
"ac": !!int "16"
"hp": !!int "105"
"hit_dice": "14d8 + 42"
"stats":
- !!int "13"
- !!int "22"
- !!int "17"
- !!int "12"
- !!int "11"
- !!int "11"
"speed": "30 ft., fly 60 ft. (hover)"
"saves":
  "Charisma": !!int "3"
  "Dexterity": !!int "9"
  "Constitution": !!int "6"
"skillsaves":
  "Intimidation": !!int "3"
  "Stealth": !!int "9"
  "Perception": !!int "3"
"damage_resistances": "cold; fire; lightning; bludgeoning, piercing, slashing from\
  \ nonmagical attacks"
"damage_immunities": "poison"
"condition_immunities": "[paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned),\
  \ [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone),\
  \ [stunned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Stunned),\
  \ [unconscious](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Unconscious)"
"senses": "darkvision 60 ft., passive Perception 13"
"languages": "Abyssal, Infernal, telepathy 60 ft."
"cr": "7"
"traits":
- "desc": "The soul eater has advantage on saving throws against spells and other\
    \ magical effects."
  "name": "Magic Resistance"
- "desc": "The soul eater can pinpoint the location of creatures that have souls within\
    \ 60 feet of it and can sense the general direction of such creatures within 1\
    \ mile of it."
  "name": "Soul Sense"
"actions":
- "desc": "The soul eater makes two Claw attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 13\
    \ (2d6 + 6) slashing damage plus 10 (3d6) psychic damage."
  "name": "Claw"
- "desc": "The soul eater emits a wave of psychic energy to hasten the demise of nearby\
    \ creatures, bringing them one step closer to having their souls consumed. Each\
    \ creature within 20 feet of the soul eater must make a DC 14 Charisma saving\
    \ throw, taking 31 (9d6) psychic damage on a failed save, or half as much damage\
    \ on a successful one. A creature reduced to below half its hp maximum by this\
    \ effect has disadvantage on the saving throw against the soul eater's Soul Drain\
    \ for 1 minute."
  "name": "Hasten Consumption (Recharge 5-6)"
"reactions":
- "desc": "When the soul eater reduces a target to 0 hp, the soul eater consumes that\
    \ creature's soul. The victim must succeed on a DC 14 Constitution saving throw\
    \ or immediately die as the soul eater consumes its soul. A creature killed in\
    \ this way can be restored to life only by means of a true resurrection or a [wish](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/wish.md)\
    \ spell. If the soul eater is killed within 120 feet of the body of a soul it\
    \ consumed and the victim has been dead for no longer than 1 minute, the victim's\
    \ soul returns to the body and returns to life, [unconscious](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Unconscious)\
    \ and stable with 0 hp."
  "name": "Soul Drain"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fiend/token/soul-eater-tob1-2023.webp"
```
^statblock

## Environment

any, planar
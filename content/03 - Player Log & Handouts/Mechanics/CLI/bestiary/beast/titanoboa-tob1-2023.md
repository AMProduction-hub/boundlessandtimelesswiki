---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/12
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/size/gargantuan
- ttrpg-cli/monster/type/beast
statblock: inline
aliases: ["Titanoboa"]
---
# [Titanoboa](03 - Player Log & Handouts\Mechanics\CLI\bestiary\beast/titanoboa-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 363*  

*This titanic green serpent raises its enormous head high, its body extending in seemingly endless coils.*

## Territorial and Aggressive

Territorial and voracious, the rare titanoboa devours all trespassers in its domain. Stronger and faster than the giant anaconda, the true king of the rainforest is also more stubborn, fighting off entire groups of hunters and poachers. When stalking prey, these great serpents strike from ambush, swallowing even some dinosaurs in one bite.

## Blinding Scales

Against groups of foes, titanoboas trust in their ability to dazzle their enemies with the light reflected from their scales, using this distraction to entwine the stunned foes in crushing coils.

## Slow to Mate

Titanoboas mate rarely. They live for hundreds of years and never stop growing, which makes the need for propagation less urgent. When two titanoboas nest, the result is a brood of a half-dozen smaller snakes. An adult titanoboa is at least 80 feet long and weighs 6,000 pounds or more.

```statblock
"name": "Titanoboa (ToB1-2023)"
"size": "Gargantuan"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "14"
"ac_class": "natural armor"
"hp": !!int "232"
"hit_dice": "15d20 + 75"
"stats":
- !!int "26"
- !!int "10"
- !!int "20"
- !!int "3"
- !!int "10"
- !!int "3"
"speed": "40 ft., climb 40 ft., swim 40 ft."
"saves":
  "Dexterity": !!int "4"
  "Wisdom": !!int "4"
"skillsaves":
  "Perception": !!int "4"
"senses": "blindsight 10 ft., passive Perception 14"
"languages": ""
"cr": "12"
"traits":
- "desc": "If the titanoboa hasn't eaten a Huge creature in the last 24 hours, it\
    \ can easily move through any open large enough for a Large creature, and it can\
    \ squeeze through any opening large enough for a Medium creature. The titanoboa's\
    \ destination must still have suitable room to accommodate its volume."
  "name": "Slither"
- "desc": "When a creature that can see the titanoboa starts its turn within 30 feet\
    \ of the titanoboa and the titanoboa is in bright light, isn't [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated),\
    \ and can see the creature, the titanoboa can force the creature to make a DC\
    \ 17 Wisdom saving throw. On a failed save, the creature is [stunned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Stunned)\
    \ until the start of its next turn.\n\nUnless surprised, a creature can avert\
    \ its eyes to avoid the saving throw at the start of its turn. If the creature\
    \ does so, it can't see the titanoboa until the start of its next turn, when it\
    \ can avert its eyes again. If the creature looks at the titanoboa in the meantime,\
    \ it must immediately make the save."
  "name": "Sparkling Scales"
"actions":
- "desc": "The titanoboa makes two Bite attacks or one Bite attack and one Constrict\
    \ attack. It can replace one Bite attack with a use of Swallow."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +12 to hit, reach 10 ft., one target. Hit: 30\
    \ (5d8 + 8) piercing damage."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +12 to hit, reach 15 ft., one target. Hit: 30\
    \ (4d10 + 8) bludgeoning damage, and the target is [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ (escape DC 18) if it is a Huge or smaller creature. Until this grapple ends,\
    \ the target is [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained),\
    \ and the titanoboa can't Constrict another target."
  "name": "Constrict"
- "desc": "The titanoboa makes one Bite attack against a Huge or smaller target it\
    \ is grappling. If the attack hits, the target is also swallowed, and the grapple\
    \ ends. While swallowed, the target is [blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded)\
    \ and [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained),\
    \ it has total cover against attacks and other effects outside the titanoboa,\
    \ and it takes 21 (6d6) acid damage at the start of each of the titanoboa's\
    \ turns. If the titanoboa takes 30 damage or more on a single turn from a swallowed\
    \ creature, the titanoboa must succeed on a DC 15 Constitution saving throw at\
    \ the end of that turn or regurgitate all swallowed creatures, which fall [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)\
    \ in a space within 10 feet of the titanoboa. If the titanoboa dies, a swallowed\
    \ creature is no longer [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ by it and can escape from the corpse by using 20 feet of movement, exiting [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)."
  "name": "Swallow"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/beast/token/titanoboa-tob1-2023.webp"
```
^statblock

## Environment

forest
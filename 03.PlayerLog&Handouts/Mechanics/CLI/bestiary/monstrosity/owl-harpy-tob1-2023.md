---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/5
- ttrpg-cli/monster/environment/desert
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/hill
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/monstrosity
statblock: inline
aliases: ["Owl Harpy"]
---
# [Owl Harpy](03 - Player Log & Handouts\Mechanics\CLI\bestiary\monstrosity/owl-harpy-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 230*  

*This winged woman's face is wreathed in a headdress of feathers; her luminous eyes and aquiline nose lend beauty to her feral demeanor. Her sharp, taloned feet seem even more inhuman by comparison.*

## Harpy Queens

An owl harpy is a queen among her kind, possessing superior grace and intelligence and an owl's predatory instinct and savage appetite. Owl harpies never grow hair, only feathers, which often wreathe their faces and crown their heads like a headdress. Their taloned feet are strong and razor sharp. They are much stronger fliers than lesser harpies; they swoop and hover in mid-air with ease to tear their prey apart. They are found in temperate climates as well as in deserts and jungles.

## Nocturnal Magic

Owl harpies practice a rare, potent magic associated with darkness and the night. They can counter most light sources easily. So refined is their hearing that neither darkness nor invisibility detracts from their ability to hunt their quarry. Their acute hearing also means that thunderous noises distress them.

## Servants of Darkness

Owl harpies are natural bards thanks to their sharp wits, and most are zealous followers of deities and demon lords of darkness and night. Less common but not unheard of are owl harpy oracles, scholars, and collectors. These savants are known to exchange their knowledge and insights for companionship or for unusual gifts and treasures.

```statblock
"name": "Owl Harpy (ToB1-2023)"
"size": "Medium"
"type": "monstrosity"
"alignment": "Neutral Evil"
"ac": !!int "14"
"ac_class": "natural armor"
"hp": !!int "112"
"hit_dice": "15d8 + 45"
"stats":
- !!int "12"
- !!int "17"
- !!int "16"
- !!int "11"
- !!int "14"
- !!int "18"
"speed": "20 ft., fly 80 ft. (hover)"
"skillsaves":
  "Stealth": !!int "9"
  "Performance": !!int "7"
"damage_vulnerabilities": "thunder"
"senses": "blindsight 60 ft., darkvision 120 ft., passive Perception 12"
"languages": "Abyssal, Common, Giant"
"cr": "5"
"traits":
- "desc": "The owl harpy has advantage on Wisdom ([Perception](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Perception))\
    \ checks that rely on hearing, and it can't use its blindsight while [deafened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Deafened)."
  "name": "Hypersensitive Hearing"
- "desc": "The owl harpy has advantage on Dexterity ([Stealth](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Stealth))\
    \ checks made to hide while flying."
  "name": "Quiet Wings"
"actions":
- "desc": "The owl harpy makes two Claw attacks and two Talon attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 8 (2d4\
    \ + 3) slashing damage."
  "name": "Claw"
- "desc": "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 10\
    \ (2d6 + 3) slashing damage."
  "name": "Talon"
- "desc": "The owl harpy sings a magical melody. Every Humanoid and Giant within 300\
    \ feet of the harpy that can hear the song must succeed on a DC 15 Wisdom saving\
    \ throw or fall [unconscious](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Unconscious)\
    \ until the song ends. The harpy must take a bonus action on its subsequent turns\
    \ to continue singing. It can stop singing at any time. The song ends if the harpy\
    \ is [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated).\
    \ An [unconscious](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Unconscious)\
    \ target wakes if it takes damage or if another creature uses an action to wake\
    \ it. A target that successfully saves is immune to this harpy's song for the\
    \ next 24 hours."
  "name": "Sleeping Song"
- "desc": "While flying, the owl harpy shakes a fine, magical dander from her wings,\
    \ and a 15-foot radius of magical darkness extends out from her, moves with her,\
    \ and spreads around corners. The darkness lasts as long as the owl harpy flies\
    \ and maintains [concentration](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Concentration),\
    \ up to 10 minutes (as if [concentrating](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Concentration)\
    \ on a spell). Darkvision can't penetrate this darkness, and no natural light\
    \ can illuminate it. If any of the darkness overlaps with an area of light created\
    \ by a spell of 2nd level or lower, the spell creating the light is dispelled."
  "name": "Hovering Darkness (3/Day)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/monstrosity/token/owl-harpy-tob1-2023.webp"
```
^statblock

## Environment

desert, forest, hill
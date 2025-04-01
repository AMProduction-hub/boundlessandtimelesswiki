---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/4
- ttrpg-cli/monster/environment/any
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/fiend
statblock: inline
aliases: ["Volguloth"]
---
# [Volguloth](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fiend/volguloth-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 391*  

*What at first appears to be a humanoid wearing voluminous robes is a thin, fiendish figure whose skin drapes about its form like a wet shroud.*

These minor fiends are often found in the service of more powerful fiends or, occasionally, powerful mortals. Volguloths are quiet, efficient killers and often act as assassins. They are sadistic and cruel, reveling in the deaths they cause, and are loathe to turn their stealthy skills to less violent tasks, such as theft or reconnaissance.

## Skin Shroud

A volguloth's skin behaves more like a sinuous sheet of muscle, contracting and expanding as the volguloth requires. Typically, it drapes the fiend's form like a robe. However, the volguloth can tighten it to a rumpled but close-fitting hide or extend it into long sheets. This allows it to glide short distances or enwrap and smother victims, engulfing them in the folds of its skin and squeezing them until they run out of air.

```statblock
"name": "Volguloth (ToB1-2023)"
"size": "Medium"
"type": "fiend"
"alignment": "Neutral Evil"
"ac": !!int "14"
"ac_class": "natural armor"
"hp": !!int "78"
"hit_dice": "12d8 + 24"
"stats":
- !!int "16"
- !!int "15"
- !!int "14"
- !!int "12"
- !!int "13"
- !!int "11"
"speed": "30 ft., climb 30 ft."
"skillsaves":
  "Stealth": !!int "6"
  "Perception": !!int "3"
"damage_resistances": "cold; fire; lightning; bludgeoning, piercing, slashing from\
  \ nonmagical attacks"
"damage_immunities": "acid, poison"
"condition_immunities": "[poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "blindsight 30 ft., darkvision 60 ft., passive Perception 13"
"languages": "Abyssal, Infernal, telepathy 60 ft."
"cr": "4"
"traits":
- "desc": "The volguloth has draping skin that it can expand while falling to slow\
    \ its rate of descent to 60 feet per round, landing on its feet and taking no\
    \ falling damage. It can move up to 5 feet horizontally for every 1 foot it falls.\
    \ The volguloth can't gain height with its expanded skin alone. If subjected to\
    \ a strong wind or lift of any kind, it can use the updraft to glide farther."
  "name": "Glide"
- "desc": "The volguloth has advantage on saving throws against spells and other magical\
    \ effects."
  "name": "Magic Resistance"
- "desc": "The volguloth's weapons are coated with a magical poison. When the volguloth\
    \ hits with any weapon, the weapon deals an extra 2d6 poison damage (included\
    \ in the attack)."
  "name": "Poisoned Weapons"
"actions":
- "desc": "The volguloth makes two Claw attacks. If both Claw attacks hit a Medium\
    \ or smaller target, the target is [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ (escape DC 13), and the volguloth uses its Enshroud on the target."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 8 (2d4\
    \ + 3) slashing damage plus 7 (2d6) poison damage."
  "name": "Claw"
- "desc": "The volguloth enshrouds a Medium or smaller target [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ by it. The enshrouded target is [blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded),\
    \ [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained),\
    \ and unable to breathe or speak until the grapple ends. If the volguloth moves,\
    \ the enshrouded target moves with it. The volguloth can have only one creature\
    \ enshrouded at a time, and it can't use its Glide trait while enshrouding a creature."
  "name": "Enshroud"
"bonus_actions":
- "desc": "A creature enshrouded by the volguloth must succeed on a DC 13 Strength\
    \ saving throw or take 10 (3d6) bludgeoning damage and begin suffocating, as\
    \ the air is squeezed from its lungs."
  "name": "Strangle"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fiend/token/volguloth-tob1-2023.webp"
```
^statblock

## Environment

any, planar
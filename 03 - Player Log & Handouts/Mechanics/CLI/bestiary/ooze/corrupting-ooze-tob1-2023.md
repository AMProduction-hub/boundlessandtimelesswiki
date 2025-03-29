---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/5
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/swamp
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/ooze
statblock: inline
aliases: ["Corrupting Ooze"]
---
# [Corrupting Ooze](03 - Player Log & Handouts\Mechanics\CLI\bestiary\ooze/corrupting-ooze-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 291*  

*The ooze boils and bubbles with rank marsh gas and the fetid stench of the sewer. It leaves a stinking trail of acidic slime wherever it goes.*

## Swim and Walk

A corrupting ooze is a festering slime that can slither and even swim like a gigantic sea slug, or it can assume a roughly humanoid form and shamble through the streets. Its stench and its lack of speech, however, make it unlikely that anyone might mistake it for a person. They are frequently soldiers and servants to heralds of blood and heralds of darkness.

## Dissolve Bones

A corrupting ooze can absorb an entire large animal or small person, simply dissolving everything in a matter of minutes. This function makes them an important element of certain dark rituals.

## Strong Swimmer

A corrupting ooze naturally floats on the surface of water. It swims with a pulsating motion that propels it.

```statblock
"name": "Corrupting Ooze (ToB1-2023)"
"size": "Large"
"type": "ooze"
"alignment": "Neutral Evil"
"ac": !!int "12"
"ac_class": "natural armor"
"hp": !!int "115"
"hit_dice": "10d10 + 60"
"stats":
- !!int "16"
- !!int "10"
- !!int "22"
- !!int "4"
- !!int "2"
- !!int "1"
"speed": "20 ft., swim 30 ft."
"skillsaves":
  "Stealth": !!int "3"
"damage_resistances": "bludgeoning, slashing"
"damage_immunities": "poison"
"condition_immunities": "[blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded),\
  \ [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [deafened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Deafened),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned),\
  \ [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)"
"senses": "blindsight 60 ft. (blind beyond this radius), passive Perception 6"
"languages": ""
"cr": "5"
"traits":
- "desc": "The ooze doesn't require sleep."
  "name": "Ooze Nature"
- "desc": "A creature that starts its turn within 5 feet of the corrupting ooze must\
    \ succeed on a DC 14 Constitution saving throw or take 3 (1d6) poison damage\
    \ and be [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ until the start of its next turn."
  "name": "Putrid Stench"
"actions":
- "desc": "The corrupting ooze makes two Slam attacks. If both attacks hit one creature,\
    \ the target must succeed on a DC 14 Dexterity saving throw or one nonmagical\
    \ leather, metal, or wooden item the creature is wearing or carrying is destroyed.\
    \ This effect can't destroy armor or weapons."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 12\
    \ (2d8 + 3) bludgeoning damage plus 7 (2d6) poison damage."
  "name": "Slam"
"bonus_actions":
- "desc": "The corrupting ooze can reshape its mass into a vaguely Humanoid shape\
    \ or back into its amorphous shape. It reverts to its amorphous shape if it dies.\
    \ While in a Humanoid shape, it can take any action that requires hands, except\
    \ it can't wield weapons or a shield or don armor."
  "name": "Reshape Body"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/ooze/token/corrupting-ooze-tob1-2023.webp"
```
^statblock

## Environment

forest, swamp, urban
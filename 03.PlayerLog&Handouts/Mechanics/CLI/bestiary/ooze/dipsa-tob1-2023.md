---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/1-4
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/size/tiny
- ttrpg-cli/monster/type/ooze
statblock: inline
aliases: ["Dipsa"]
---
# [Dipsa](03 - Player Log & Handouts\Mechanics\CLI\bestiary\ooze/dipsa-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 105*  

*Except for a pair of tiny fangs, the entire body of this yellowishgreen worm looks like a ropy tangle of slime-covered tubes and puddles of mucus.*

## Anesthetic Ooze

Many jungle clans believe the dipsa is an eyeless snake, but it is a tubular ooze with a lethal, poisonous bite. The dipsa's venom has an anesthetic quality that allows the ooze to cling to creatures and slowly turn their innards to jelly without being noticed until the victim falls down dead. Once the poison's numbing property wears off, however, victims report an agonizing sense of burning from the inside out.

## Tiny Fangs

A dipsa's undulating movement evokes that of a snake as much as its serpentine form, but close examination reveals that it has neither bones nor internal organs, only tiny fangs of the same color and substance as the rest of its body. A dipsa never exceeds 1 foot in length. Its coloration oscillates between sickly hues of yellow or green.

## Gelatinous Eggs

Dipsas are hermaphroditic. When two dipsas breed, they leave behind a hundred gelatinous eggs in a small puddle of highly acidic milt. A dozen become fertilized and survive long enough to hatch, after which they immediately devour the others.

```statblock
"name": "Dipsa (ToB1-2023)"
"size": "Tiny"
"type": "ooze"
"alignment": "Unaligned"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "27"
"hit_dice": "6d4 + 12"
"stats":
- !!int "3"
- !!int "17"
- !!int "14"
- !!int "1"
- !!int "6"
- !!int "1"
"speed": "20 ft., climb 20 ft., swim 20 ft."
"skillsaves":
  "Stealth": !!int "5"
"damage_resistances": "acid"
"condition_immunities": "[blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded),\
  \ [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [deafened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Deafened),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)"
"senses": "blindsight 60 ft. (blind beyond this radius), passive Perception 8"
"languages": ""
"cr": "1/4"
"traits":
- "desc": "The dipsa can move through a space as narrow as 1 inch wide without squeezing."
  "name": "Amorphous"
- "desc": "The bite of a dipsa is barely perceptible and the wound is quickly anesthetized.\
    \ When the dipsa hits with a Bite attack, the target must succeed on a DC 15 Wisdom\
    \ ([Perception](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Perception))\
    \ check to notice the dipsa and its attack. Each time the creature takes acid\
    \ damage from an attached dipsa, it can repeat this check, noticing the dipsa\
    \ on a success. A creature that takes acid damage from the dipsa while below half\
    \ its hp maximum automatically succeeds on this check."
  "name": "Discreet Bite"
- "desc": "The dipsa doesn't require sleep."
  "name": "Ooze Nature"
- "desc": "The dipsa has advantage on Dexterity ([Stealth](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Stealth))\
    \ checks made to hide in swampy terrain."
  "name": "Swamp Camouflage"
"actions":
- "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one creature. Hit: 1\
    \ piercing damage, and the dipsa attaches to the target. While attached, the dipsa\
    \ can't attack, and at the start of each of the dipsa's turns, the target takes\
    \ 3 (1d6) acid damage and must succeed on a DC 12 Constitution saving throw\
    \ or have its hp maximum reduced by an amount equal to the damage taken. This\
    \ reduction lasts until the target finishes a long rest. The target dies if this\
    \ effect reduces its hp maximum to 0.\n\nThe attached dipsa moves with the target\
    \ whenever the target moves, requiring none of the dipsa's movement. It can detach\
    \ itself by spending 5 feet of its movement on its turn. A creature, including\
    \ the target, can use its action to detach the dipsa."
  "name": "Bite"
"bonus_actions":
- "desc": "The dipsa takes the Hide action."
  "name": "Translucent"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/ooze/token/dipsa-tob1-2023.webp"
```
^statblock

## Environment

forest
---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/4
- ttrpg-cli/monster/environment/mountain
- ttrpg-cli/monster/size/tiny
- ttrpg-cli/monster/type/fey
statblock: inline
aliases: ["Bereginyas"]
---
# [Bereginyas](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fey/bereginyas-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 36*  

*These small, winged faeries appear to be made of gray mist, and they can conceal themselves completely in the fogbanks and clouds enshrouding their mountainous lairs.*

## Mist Dancers

These evil, cunning faeries (whose name means "mist dancers" in Old Elvish) overcome their victims by seeping into the creature's lungs to choke it on the bereginyas's foul essence.

## Mountain Spirits

They are most commonly found in the highest mountain ranges, often above the tree line, but they can be encountered in any foggy or misty mountainous region. Shepherds and goatherds often leave bits of milk or cheese to placate them, particularly during the spring lambing season.

```statblock
"name": "Bereginyas (ToB1-2023)"
"size": "Tiny"
"type": "fey"
"alignment": "Neutral Evil"
"ac": !!int "14"
"hp": !!int "81"
"hit_dice": "18d4 + 36"
"stats":
- !!int "14"
- !!int "19"
- !!int "14"
- !!int "13"
- !!int "12"
- !!int "11"
"speed": "20 ft., fly 60 ft."
"saves":
  "Dexterity": !!int "6"
"skillsaves":
  "Stealth": !!int "8"
  "Perception": !!int "5"
"damage_immunities": "bludgeoning"
"senses": "darkvision 60 ft., passive Perception 15"
"languages": "Common, Elvish, Sylvan"
"cr": "4"
"traits":
- "desc": "The bereginyas's semi-solid form emits poisonous gases. Any creature that\
    \ starts its turn within 5 feet of the bereginyas must succeed on a DC 14 Constitution\
    \ saving throw or be [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned).\
    \ A creature that succeeds on this saving throw by 5 or more is immune to the\
    \ bereginyas's Foul Form for the next 24 hours."
  "name": "Foul Form"
"actions":
- "desc": "The bereginyas makes two Claw attacks. If both attacks hit the same target,\
    \ the bereginyas attaches to the target. While attached, the bereginyas can use\
    \ only the Smother action, and it moves with the target whenever the target moves,\
    \ requiring none of the bereginyas's movement. The bereginyas can detach itself\
    \ by spending 5 feet of its movement. A creature, including the target, can take\
    \ its action to detach the bereginyas by succeeding on a DC 14 Strength check."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 8 (1d8\
    \ + 4) slashing damage plus 4 (1d8) poison damage."
  "name": "Claw"
- "desc": "While attached to a creature that isn't a Construct or Undead, the bereginyas\
    \ extends a tendril of poisonous gas down the creature's throat. The creature\
    \ must make a DC 14 Constitution saving throw. On a failure, it takes 22 (5d8)\
    \ poison damage, immediately runs out of breath, and begins suffocating. On a\
    \ success, it takes half the damage, doesn't run out of breath, and isn't suffocating.\
    \ Suffocation ends if the creature dies, if the bereginyas is removed from the\
    \ creature, or if the bereginyas is killed. A suffocating creature that fails\
    \ this saving throw reduces its remaining rounds of breath by 1."
  "name": "Smother"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fey/token/bereginyas-tob1-2023.webp"
```
^statblock

## Environment

mountain
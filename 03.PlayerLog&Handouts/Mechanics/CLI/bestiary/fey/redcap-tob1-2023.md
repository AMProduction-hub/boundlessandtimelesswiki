---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/6
- ttrpg-cli/monster/environment/farmland
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/fey
statblock: inline
aliases: ["Redcap"]
---
# [Redcap](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fey/redcap-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 306*  

*This grizzled, weather-beaten creature looks like a sour old man, complete with scraggly beard. It carries a great pike and wears a blood-soaked hat and heavy boots shod with iron. It grins with massive yellow teeth*.

## Blood-Soaked Caps

Redcaps are exceedingly dangerous creatures who wear the mark of their cruelty and evil quite literally. The caps from which they take their name define their very existence—these caps must constantly be revived with fresh blood.

## Compelled to Kill

Redcaps aren't cruel and murderous by choice, but by necessity. A redcap must frequently bathe its cap in fresh, humanoid blood to sustain itself. If it fails to do so every three days, the creature withers and dies quickly. A redcap whose hat is nearly dry is a desperate, violent force of nature that prefers to die in battle rather than waste away to nothing.

## Bandits and Mercenaries

Most long-lived redcaps are drawn to serve in marauding armies or make a living through constant banditry.

```statblock
"name": "Redcap (ToB1-2023)"
"size": "Medium"
"type": "fey"
"alignment": "Neutral Evil"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "120"
"hit_dice": "16d8 + 48"
"stats":
- !!int "20"
- !!int "10"
- !!int "17"
- !!int "11"
- !!int "13"
- !!int "8"
"speed": "40 ft."
"saves":
  "Constitution": !!int "6"
"skillsaves":
  "Intimidation": !!int "5"
  "Athletics": !!int "8"
"damage_resistances": "bludgeoning, piercing, slashing from nonmagical attacks"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)"
"senses": "darkvision 60 ft., passive Perception 11"
"languages": "Common, Sylvan, Undercommon"
"cr": "6"
"traits":
- "desc": "The redcap must soak its cap in the blood of a Humanoid that has been dead\
    \ for no more than 1 hour at least once every 3 days. Every 24 hours past the\
    \ third day that it goes without soaking its cap in blood in this way, it suffers\
    \ one level of [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion).\
    \ This [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion)\
    \ can be reduced only when the redcap finishes a long rest after soaking its cap\
    \ in fresh Humanoid blood, which reduces its [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion)\
    \ level to 0. If the redcap dies as a result of this [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
    \ it crumbles to dust."
  "name": "Red Cap"
"actions":
- "desc": "The redcap makes one Bleeding Bite attack and two Pike attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 14\
    \ (2d8 + 5) piercing damage. If the target is a creature other than a Construct\
    \ or Undead, it must succeed on a DC 15 Constitution saving throw or lose 7 2d6\
    \ hp at the start of each of its turns due to a bleeding wound. The creature can\
    \ repeat the saving throw at the end of each of its turns, ending the effect on\
    \ itself on a success. Any creature can take an action to stanch the wound with\
    \ a successful DC 13 Wisdom ([Medicine](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Medicine))\
    \ check. The wound also closes if the target receives magical healing."
  "name": "Bleeding Bite"
- "desc": "Melee Weapon Attack: +8 to hit, reach 10 ft., one target. Hit: 10\
    \ (1d10 + 5) piercing damage."
  "name": "Pike"
"bonus_actions":
- "desc": "The redcap kicks a Medium or smaller creature within 5 feet of it. The\
    \ target must succeed on a DC 15 Strength saving throw or be knocked [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)."
  "name": "Solid Kick"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fey/token/redcap-tob1-2023.webp"
```
^statblock

## Environment

farmland, forest
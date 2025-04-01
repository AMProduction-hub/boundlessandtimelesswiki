---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/5
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/fiend
statblock: inline
aliases: ["Dream Eater"]
---
# [Dream Eater](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fiend/dream-eater-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 148*  

*This tattered skeletal humanoid resembles a monster from a nightmare with vestigial skeletal wings with a few feathers, small horns, sharp teeth, and cloven hooves.*

## Drawn to Sin

Dream eaters are dedicated to lust, gluttony, and greed. They make their lairs in casinos, brothels, thieves' dens, and other locations where gambling, food, and other pleasures are readily available. Sometimes dream eaters work together to create such a place, especially near large towns or cities. Some band together to create traveling shows, offering all the oddities, whimsies, and flights of fantasy customary for such entertainers.

## Devouring Hopes

Dream eaters lure people into their lairs, enticing them with promises of pleasure or wealth. Of course, they make sure the odds are stacked in their favor. Eventually, their victims are left with nothing. Worse than the loss of physical treasures, dream eaters leave their victims stripped of hopes and aspirations. Dream eaters feed on emotions, leaving helpless thralls willing to sell their souls for their vices.

```statblock
"name": "Dream Eater (ToB1-2023)"
"size": "Medium"
"type": "fiend"
"alignment": "Lawful Evil"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "75"
"hit_dice": "10d8 + 30"
"stats":
- !!int "15"
- !!int "18"
- !!int "17"
- !!int "16"
- !!int "13"
- !!int "20"
"speed": "30 ft., fly 20 ft."
"skillsaves":
  "Deception": !!int "8"
  "Insight": !!int "4"
  "Persuasion": !!int "8"
"damage_resistances": "cold; fire; lightning; bludgeoning, piercing, slashing from\
  \ nonmagical attacks"
"damage_immunities": "poison"
"condition_immunities": "[poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 60 ft., passive Perception 11"
"languages": "Abyssal, Celestial, Common, Infernal, telepathy 120 ft."
"cr": "5"
"traits":
- "desc": "A creature that starts its turn [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ by the dream eater must succeed on a DC 14 Charisma saving throw or take 5 (2d4)\
    \ psychic damage. The dream eater gains temporary hp equal to the psychic damage\
    \ dealt."
  "name": "Dream Eater's Caress"
"actions":
- "desc": "The dream eater uses its Lotus Scent. It then makes one Bite attack and\
    \ one Claw attack."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 15\
    \ (2d10 + 4) piercing damage."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 13\
    \ (2d8 + 4) slashing damage, and the target is [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ (escape DC 14) if it is a Large or smaller creature. Until this grapple ends,\
    \ the creature is [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained).\
    \ The dream eater has two claws, each of which can grapple only one target."
  "name": "Claw"
- "desc": "The dream eater secretes an oily chemical that most creatures find intoxicating.\
    \ Each creature that isn't a Construct or Undead within 15 feet of the dream eater\
    \ must succeed on a DC 14 Constitution saving throw or be [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ for 1 minute. While [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned),\
    \ the creature is [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed)\
    \ by the fiend. A [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ creature can repeat the saving throw at the end of each of its turns, ending\
    \ the effect on itself on a success. If a creature's saving throw is successful\
    \ or the effect ends for it, the creature is immune to the dream eater's Lotus\
    \ Scent for the next 24 hours."
  "name": "Lotus Scent"
- "desc": "Each creature within 20 feet of the dream eater must make a DC 14 Charisma\
    \ saving throw. On a failure, a creature takes 21 (6d6) psychic damage and is\
    \ [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated)\
    \ for 1 minute. When it moves, an [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated)\
    \ creature moves in a random direction. On a success, a creature takes half the\
    \ damage and isn't [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated).\
    \ A creature can repeat the saving throw at the end of each of its turns, ending\
    \ the effect on itself on a success."
  "name": "Waking Dreams (Recharge 5-6)"
"bonus_actions":
- "desc": "The dream eater magically transforms into a Small or Medium humanoid it\
    \ has seen, or back into its true form, which is a Fiend. Its statistics, other\
    \ than its size, are the same in each form. Any equipment it is wearing or carrying\
    \ transforms with it. It reverts to its true form if it dies."
  "name": "Change Shape"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fiend/token/dream-eater-tob1-2023.webp"
```
^statblock

## Environment

urban
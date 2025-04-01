---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/1
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/humanoid/human
statblock: inline
aliases: ["Eonic Drifter"]
---
# [Eonic Drifter](03 - Player Log & Handouts\Mechanics\CLI\bestiary\humanoid/eonic-drifter-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 165*  

*The air crackles and lights flicker in the ruins. In a whirl of colorful robes, a gaunt human materializes from the maelstroms of time. His eyes scan the hall in panic, witnessing an event only he can see*.

## Adrift in Time

Not much is known about the time-traveling eonic drifters other than that they were humans who left a dying civilization to look for help not available in their own age. To their misfortune, returning to their own time proved much more difficult than leaving it, and the eonic drifters found themselves adrift in the river of time. As the decades passed, their chance of returning home withered, along with much of their vitality. They have become gaunt and semi-mummified by the passing of ages.

## Crystal Belts

A drifter carries an odd assembly of gear gathered in countless centuries. It barters with these goods when necessary. The more eclectic the collection, the more jumps it has performed on its odyssey. Belts of crystals around its body store the energy that fuels a drifter's travels. After each large jump through time, the reservoirs are exhausted for awhile, allowing only short jumps.

## Jittery and Paranoid

Visiting countless eras in which mankind has all but forgotten their once-great civilization has robbed most eonic drifters of their hope. Their greatest fear is being robbed of their crystal belts, which are their only remaining links to the people they once were. They plead or fight to the death for the belts.

## Ruins Dwellers

Drifters can appear at any time or place, but they often frequent the sites of their people's past (or future) cities. There they are comforted by knowing that they're at least in the right place, if not the right time.

```statblock
"name": "Eonic Drifter (ToB1-2023)"
"size": "Medium"
"type": "humanoid"
"subtype": "human"
"alignment": "Chaotic Neutral"
"ac": !!int "13"
"ac_class": "[leather armor](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/items/leather-armor.md)"
"hp": !!int "65"
"hit_dice": "10d8 + 20"
"stats":
- !!int "9"
- !!int "14"
- !!int "14"
- !!int "18"
- !!int "11"
- !!int "13"
"speed": "30 ft."
"skillsaves":
  "History": !!int "6"
  "Arcana": !!int "6"
"senses": "passive Perception 10"
"languages": "Common, Eonic, Giant, Sylvan"
"cr": "1"
"actions":
- "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6\
    \ + 2) bludgeoning damage plus 3 (1d6) force damage."
  "name": "Time-Warping Staff"
- "desc": "The drifter chooses one creature it can see within 5 feet of its future\
    \ self. The target must make a DC 13 Wisdom saving throw. On a failure, the target\
    \ takes 7 (2d6) psychic damage and is pulled forward in time. On a success,\
    \ the target takes half the damage and isn't pulled forward in time. A target\
    \ pulled forward in time disappears, along with the drifter's future self, as\
    \ the future self pulls the target with it. At the end of the drifter's next turn,\
    \ the target and the drifter's future self reappear in the spaces they previously\
    \ occupied, or the nearest unoccupied spaces. When the target reappears, it has\
    \ disadvantage on attack rolls until the end of its next turn as it recovers from\
    \ the disorienting experience."
  "name": "Drift Forward (Recharge 5-6)"
"bonus_actions":
- "desc": "The eonic drifter calls to a future version of itself, which appears in\
    \ an unoccupied space the drifter can see within 30 feet of it. The drifter's\
    \ future self acts on the drifter's turn, and each turn it makes one Time-Warping\
    \ Staff attack against a creature of the drifter's choice or uses the Help action\
    \ to aid the drifter. The future self can be attacked and destroyed (AC 13; hp\
    \ 30; resistance to bludgeoning, piercing, and slashing damage; immunity to poison\
    \ and psychic damage), otherwise it remains until the drifter dismisses it as\
    \ a bonus action or the drifter finishes a long rest. If the drifter's future\
    \ self is destroyed, the drifter must succeed on a DC 13 Wisdom saving throw or\
    \ be [stunned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Stunned)\
    \ until the end of its next turn."
  "name": "Call to the Future (1/Day)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/humanoid/token/eonic-drifter-tob1-2023.webp"
```
^statblock

## Environment

planar
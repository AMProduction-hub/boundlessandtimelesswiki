---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/1-2
- ttrpg-cli/monster/environment/coastal
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/tiny
- ttrpg-cli/monster/type/fey
statblock: inline
aliases: ["Rum Gremlin"]
---
# [Rum Gremlin](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fey/rum-gremlin-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 223*  

*Found on docks and ships, these small, pot-bellied creatures have bright green hair, orange eyes, and a drunken stare. They reveal mouths filled with razor-sharp teeth behind lopsided grins.*

## Drunken Aura

Rum gremlins make their homes near the docks of seaside towns and some are known to stow away on ships. Each rum gremlin radiates a magic aura that causes those nearby to experience the effects of being drunk. Those affected find it difficult to stay on their feet and may become sick if exposed to rum gremlins for too long.

## Sailor Victims

The little horrors often create distracting sounds and small traps. Rum gremlins prey on sailors and dockworkers, working in groups to swarm affected victims who they drag into their lairs below docks or in the holds of ships. They also take great delight in the collateral damage their magic can wreak, frequently sparking accusations and quarrels in places they inhabit before picking off isolated victims.

## Rat Friends

Rum gremlins are often found with rat swarms or doppelrats they have trained to help protect their nests. The sound of bells drives rum gremlins into a rage, and they will go to great lengths to destroy the source of their torment.

> [!note] Rum Gremlins in Midgard
> 
> Legends say the rum gremlins originated when Loki bet Ninkash she couldn't craft a brew potent enough to knock him out in a drinking contest. Ninkash won the contest, but a band of mites watching the contest made off with the remaining beer and transformed into the first rum gremlins.
^rum-gremlins-in-midgard

```statblock
"name": "Rum Gremlin (ToB1-2023)"
"size": "Tiny"
"type": "fey"
"alignment": "Chaotic Evil"
"ac": !!int "13"
"hp": !!int "27"
"hit_dice": "6d4 + 12"
"stats":
- !!int "10"
- !!int "16"
- !!int "14"
- !!int "12"
- !!int "9"
- !!int "12"
"speed": "20 ft., climb 10 ft., swim 10 ft."
"skillsaves":
  "Stealth": !!int "5"
"condition_immunities": "[poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 120 ft., passive Perception 10"
"languages": "Common, Sylvan"
"cr": "1/2"
"traits":
- "desc": "The gremlin casts one of the following spells, requiring no material components\
    \ and using Charisma as the spellcasting ability (spell save DC 11):\n\nAt will:\
    \ [prestidigitation](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/prestidigitation.md)\n\
    \n3/day: [command](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/command.md)"
  "name": "Spellcasting"
- "desc": "The rum gremlin radiates an aura of drunkenness to a radius of 20 feet.\
    \ Each creature that starts its turn in the aura must succeed on a DC 12 Constitution\
    \ saving throw or be [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ for 1 hour. A creature that has consumed alcohol within the past hour has disadvantage\
    \ on the saving throw. While [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned),\
    \ a creature falls [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)\
    \ if it tries to move more than half its speed during a turn. A creature that\
    \ succeeds on the saving throw is immune to the rum gremlin's Aura of Drunkenness\
    \ for 24 hours."
  "name": "Aura of Drunkenness"
- "desc": "The rum gremlin has advantage on saving throws against spells and other\
    \ magical effects."
  "name": "Magic Resistance"
"actions":
- "desc": "Melee Weapon Attack: +5 to hit, range 5 ft., one target. Hit: 5 (1d4\
    \ + 3) piercing damage."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +5 to hit, range 5 ft., one target. Hit: 6 (1d6\
    \ + 3) slashing damage."
  "name": "Claws"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fey/token/rum-gremlin-tob1-2023.webp"
```
^statblock

## Environment

coastal, urban
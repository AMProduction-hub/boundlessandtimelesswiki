---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/3
- ttrpg-cli/monster/environment/desert
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/fey
statblock: inline
aliases: ["Mirager"]
---
# [Mirager](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fey/mirager-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 271*  

*Diaphanous veils cover a graceful woman, flowing like water across her as she dances through the dust.*

## Humanoid Sand

Cursed with crumbling, sandy bodies by a long-since-forgotten fey lord, miragers rely on blood and moisture from mortal creatures to replenish and sustain their forms. With such sustenance hard to acquire in their desert homes, miragers don't gather in groups and can be particularly vicious when starved. Some miragers might make bargains or forge friendships with mortal creatures, but the mirager's everpresent need for blood and moisture means such alliances rarely survive the dry season.

## Enticing Illusion

A mirager can take on the guise of a lovely man or woman with luminous eyes, delicate features, and seductive garments. Whatever its form, a mirager dresses in veils and flowing robes that accentuate its enticing beauty.

```statblock
"name": "Mirager (ToB1-2023)"
"size": "Medium"
"type": "fey"
"alignment": "Neutral Evil"
"ac": !!int "13"
"hp": !!int "78"
"hit_dice": "12d8 + 24"
"stats":
- !!int "12"
- !!int "16"
- !!int "14"
- !!int "10"
- !!int "14"
- !!int "19"
"speed": "30 ft."
"skillsaves":
  "Deception": !!int "6"
  "Perception": !!int "4"
  "Performance": !!int "8"
"senses": "darkvision 60 ft., passive Perception 14"
"languages": "Common, Sylvan"
"cr": "3"
"traits":
- "desc": "The mirager casts one of the following spells, requiring no material components\
    \ and using Charisma as the spellcasting ability (spell save DC 14):\n\n1/day\
    \ each: [hallucinatory terrain](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/hallucinatory-terrain.md)\
    \ (as an action), [suggestion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/suggestion.md)\n\
    \n3/day: [charm person](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/charm-person.md)"
  "name": "Spellcasting"
- "desc": "The mirager moves with a flowing grace that Humanoids find appealing. If\
    \ the mirager moves at least 10 feet on its turn, each Humanoid within 30 feet\
    \ of it that can see it must succeed on a DC 14 Charisma saving throw or be [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed)\
    \ until the end of its next turn."
  "name": "Sensuous Grace"
"actions":
- "desc": "The mirager makes two Slam attacks. If both Slam attacks hit a Medium or\
    \ smaller creature, the target is also [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ (escape DC 13). The mirager can grapple only one creature at a time."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 10\
    \ (2d6 + 3) bludgeoning damage."
  "name": "Slam"
- "desc": "Melee Spell Attack: +6 to hit, reach 5 ft., one willing creature, or\
    \ a creature that is [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ by the mirager, [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated),\
    \ or [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained).\
    \ Hit: 22 (4d8 + 4) necrotic damage, and the mirager gains temporary hp equal\
    \ to half that amount."
  "name": "Thirsting Kiss"
- "desc": "The mirager blows a kiss at a creature [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed)\
    \ by it. The target must make a DC 14 Charisma saving throw. On a failure, a creature\
    \ takes 17 (5d6) psychic damage and is [stunned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Stunned)\
    \ until the end of its next turn. On a success, a creature takes half the damage\
    \ and the [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed)\
    \ condition immediately ends on it."
  "name": "Blow Kiss"
- "desc": "The mirager covers itself and anything it is wearing or carrying with a\
    \ magical illusion that makes it look like another creature of its general size\
    \ and Humanoid shape. The illusion ends if the mirager takes a bonus action to\
    \ end it or if the mirager dies.\n\nThe changes wrought by this effect fail to\
    \ hold up to physical inspection. For example, the mirager could appear to have\
    \ smooth skin, but someone touching it would feel its rough, sand-like skin. Otherwise,\
    \ a creature must take an action to visually inspect the illusion and succeed\
    \ on a DC 20 Intelligence ([Investigation](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Investigation))\
    \ check to discern that the mirager is disguised."
  "name": "Illusory Appearance"
"bonus_actions":
- "desc": "While in sandy terrain, the mirager takes the Dash or Disengage action."
  "name": "Sand Dancer"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fey/token/mirager-tob1-2023.webp"
```
^statblock

## Environment

desert
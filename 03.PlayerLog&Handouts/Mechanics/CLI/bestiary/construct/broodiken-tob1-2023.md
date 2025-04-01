---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/1
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/tiny
- ttrpg-cli/monster/type/construct
statblock: inline
aliases: ["Broodiken"]
---
# [Broodiken](03 - Player Log & Handouts\Mechanics\CLI\bestiary\construct/broodiken-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 43*  

*Tiny and built like a caricature of a person, this creature's enlarged head is filled with pointed teeth.*

## Bodily Children

Broodikens are crude servants created by humanoid spellcasters willing to grow the creatures within their own bodies. Broodikens resemble their creators in the most obvious ways, with the same number of limbs and basic features, but all broodikens stand one foot tall with overly large heads and heavily fanged mouths. Those born to humanoids with wings or horns have ineffective, decorative versions that do not help the creature fly or fight.

## Emotional Echoes

Broodikens have little personality of their own and respond to their creators' emotions, growling when their creators feel anger and babbling happily when their creators feel joy. When their creators are more than 100 feet away, they cry loudly with a sound that resembles children of the creator's own species. If discovered crying by anyone other than their creator, they attack. When their creators focus their anger on specific individuals, the broodikens attack as a group, using stealth to get close and overwhelm single opponents.

## Born With Daggers

Broodikens are created by eating the heart of a dead broodiken. Once this "seed" is consumed, `2d4` broodikens grow inside of the "mother" or creator. Nurturing the growing brood requires consuming specific muds, ashes, and plants, which cost 50 gp per day for each incubating broodiken. The incubation period requires one month and takes a toll on the creator's health. During this time, the creator becomes fatigued after four hours without eight hours' rest. If the creator is not a spellcaster, a spellcaster must supervise the incubation and birth. Most spellcasters birth the broodiken using a dagger before the broodiken tears its way out. A "mother" can control only one brood of broodiken at a time. Incubating a second brood makes the first brood furiously jealous, and they turn on their own creator.

```statblock
"name": "Broodiken (ToB1-2023)"
"size": "Tiny"
"type": "construct"
"alignment": "Unaligned"
"ac": !!int "13"
"ac_class": "natural armor"
"hp": !!int "44"
"hit_dice": "8d4 + 24"
"stats":
- !!int "8"
- !!int "14"
- !!int "16"
- !!int "2"
- !!int "10"
- !!int "6"
"speed": "20 ft., climb 20 ft."
"skillsaves":
  "Stealth": !!int "6"
  "Perception": !!int "4"
"damage_resistances": "bludgeoning, piercing, slashing from nonmagical attacks"
"damage_immunities": "poison, psychic"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [petrified](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Petrified),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 60 ft., passive Perception 14"
"languages": ""
"cr": "1"
"traits":
- "desc": "The broodiken doesn't require air, food, drink, or sleep."
  "name": "Construct Nature"
- "desc": "The broodiken is immune to any spell or effect that would alter its form."
  "name": "Immutable Form"
- "desc": "The broodiken has advantage on saving throws against spells and other magical\
    \ effects."
  "name": "Magic Resistance"
- "desc": "The broodiken can't speak with its creator telepathically, but it can magically\
    \ receive simple ideas, emotions, and images telepathically from its creator while\
    \ within 100 feet of its creator. The creator can send the broodiken an image\
    \ of a creature and emotion or simple idea tied to it, such as anger or retrieval,\
    \ and the broodiken will seek the creature to carry out the emotion or desire.\
    \ As long as the broodiken is following such an order, it can be more than 100\
    \ feet away from its master without wailing."
  "name": "Shared Rage"
"actions":
- "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 9 (2d6\
    \ + 2) piercing damage, and the broodiken attaches to the target. While attached,\
    \ the broodiken can't attack, and at the start of each of the broodiken's turns,\
    \ the target takes 9 (2d6 + 2) piercing damage.\n\nThe attached broodiken moves\
    \ with the target whenever the target moves, requiring none of the broodiken's\
    \ movement. It can detach itself by spending 5 feet of its movement on its turn.\
    \ A creature, including the target, can use its action to detach the broodiken\
    \ by succeeding on a DC 9 Strength check."
  "name": "Bite"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/construct/token/broodiken-tob1-2023.webp"
```
^statblock

## Environment

urban
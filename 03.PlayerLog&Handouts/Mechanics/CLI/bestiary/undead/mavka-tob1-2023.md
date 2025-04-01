---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/12
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/undead
statblock: inline
aliases: ["Mavka"]
---
# [Mavka](03 - Player Log & Handouts\Mechanics\CLI\bestiary\undead/mavka-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 265*  

*With burnt and blackened skin, burnt twigs for hair, and clawed hands and feet that resemble burnt and twisted roots, this creature appears scorched and even frail. Pupilless red eyes gleam in its sockets with a hellish green flame.*

Mavkas are twisted dryads created by undead warlocks and vampiric experiments.

## Death Riders

Mavkas ride nightmares and are fearsome raiders, snatching victims up into the saddle, never to be seen again. They despise and trample foot soldiers as peasants unworthy of attention.

## Hag Killers

Mavkas are the mortal enemies of red hags, who call these undead horrors "greenbanes." When red hag covens discover vampires and other undead turning local dryads into mavkas, they go on a rampage, destroying all undead they encounter.

> [!note] Mavkas in Midgard
> 
> There were once three dryad sisters named Mica, Anthelia, and Saramantha. After his conquest of Morgau, the Black Prince Lucan had the dryads and their trees killed and then raised them as powerful undead—mavkas. His warlocks bonded the new undead with nightmares instead of trees to complete their corruption.
> 
> These three sisters have since spawned many more such undead fey. Some serve the Black Prince as generals or concubines, while others pursue their own ends, destroying vampires, laying waste to villages, and seeking power in the Shadow Realm.
^mavkas-in-midgard

```statblock
"name": "Mavka (ToB1-2023)"
"size": "Medium"
"type": "undead"
"alignment": "Chaotic Evil"
"ac": !!int "17"
"ac_class": "natural armor"
"hp": !!int "170"
"hit_dice": "20d8 + 80"
"stats":
- !!int "20"
- !!int "15"
- !!int "18"
- !!int "13"
- !!int "13"
- !!int "18"
"speed": "30 ft."
"saves":
  "Charisma": !!int "8"
  "Dexterity": !!int "6"
  "Strength": !!int "9"
  "Constitution": !!int "8"
"skillsaves":
  "Nature": !!int "5"
  "Athletics": !!int "9"
  "Perception": !!int "5"
"damage_resistances": "fire; bludgeoning, piercing, slashing from nonmagical attacks"
"damage_immunities": "necrotic, poison"
"condition_immunities": "[poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 90 ft., passive Perception 15"
"languages": "Abyssal, Common, Infernal, Sylvan"
"cr": "12"
"traits":
- "desc": "The mavka casts one of the following spells, requiring no material components\
    \ and using Charisma as the spellcasting ability (spell save DC 16):\n\nAt will:\
    \ [create or destroy water](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/create-or-destroy-water.md),\
    \ [dancing lights](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/dancing-lights.md)\n\
    \n1/day each: [bestow curse](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/bestow-curse.md),\
    \ [dispel magic](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/dispel-magic.md)\n\
    \n3/day each: [darkness](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/darkness.md),\
    \ [hold person](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/hold-person.md),\
    \ [silence](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/silence.md)"
  "name": "Spellcasting"
- "desc": "While the mavka is mounted, her mount can't be [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed)\
    \ or [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)."
  "name": "Mounted Warrior"
- "desc": "The mavka has formed a bond with a nightmare. The nightmare acts as a controlled\
    \ mount while carrying the mavka, obeying the mavka's spoken commands. Mounting\
    \ and dismounting the nightmare costs the mavka only 5 feet of movement."
  "name": "Nightmare Mount"
- "desc": "The mavka takes 20 radiant damage when she starts her turn in sunlight.\
    \ While in sunlight, she has disadvantage on attack rolls and ability checks."
  "name": "Sunlight Hypersensitivity"
- "desc": "The mavka doesn't require air, food, drink, or sleep."
  "name": "Undead Nature"
"actions":
- "desc": "The mavka makes two Enervating Slam attacks or three Necrotic Bolt attacks.\
    \ If she is riding a nightmare, the nightmare can then make one Hooves attack.\
    \ If both Enervating Slam attacks hit one creature, the mavka regains hp equal\
    \ to the total necrotic damage dealt by both attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 23\
    \ (4d8 + 5) bludgeoning damage plus 16 (3d10) necrotic damage."
  "name": "Enervating Slam"
- "desc": "Ranged Spell Attack: +8 to hit, range 60 ft., one target. Hit: 26\
    \ (4d10 + 4) necrotic damage."
  "name": "Necrotic Bolt"
- "desc": "While riding a nightmare, the mavka channels her power into her mount,\
    \ causing its fiery light to burn those nearby. Each creature within 20 feet of\
    \ the mavka must make a DC 16 Dexterity saving throw, taking 54 (12d8) fire\
    \ damage on a failed save, or half as much damage on a successful one."
  "name": "Flame Burst (Recharge 5-6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/undead/token/mavka-tob1-2023.webp"
```
^statblock

## Environment

forest
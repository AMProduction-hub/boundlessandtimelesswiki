---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/3
- ttrpg-cli/monster/environment/badlands
- ttrpg-cli/monster/environment/coastal
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/tiny
- ttrpg-cli/monster/type/fey
statblock: inline
aliases: ["Spire Walker"]
---
# [Spire Walker](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fey/spire-walker-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 347*  

*This miniscule creature kicks up a ghostly, sparkling fire when it jostles and jigs. Lightning sparks fly between it and its perch.*

## Storm Dancers

When storm clouds gather over cities, harbors, and twisted badlands, electrical energy fills the air. During these times, miniscule fey dance on church steeples, desolate peaks, and ships' masts. Also called corposanti by scholars, spire walkers are nature spirits that delight in grandiose displays of thunderbolts. They can be found frolicking in a thunderstorm or keeping company with blue dragons or storm giants—though these larger creatures often chase them off for being a nuisance.

## Small and Metallic

Spire walkers stand no more than a foot tall, with dusky blue-gray skin and shocks of silvery, slate, or pale blue hair. Spire walkers prefer clothing in metallic hues with many buttons, and they always carry a handful of tiny copper darts that they hurl at each other during their incomprehensible games. When excited, they emit a sparking glow from the tips of their noses, eyebrows, ears, and pointy shoes. They play rough-and-tumble games among themselves and enjoy pranking bystanders with frightening but mostly harmless electric shocks. If a spire walker perishes during the fun, the others pause just long enough to say "awww, we'll miss you" and go through their comrade's pockets before continuing with the game.

## Love Copper and Amber

Spire walkers like gold but they love copper. They prefer it over all other metals, and they keep the copper pieces in their pockets brilliantly polished. They also value amber gems. Among a group of spire walkers, the leader is not the cleverest or most ruthless, but the one displaying the most ostentatious amber jewel.

```statblock
"name": "Spire Walker (ToB1-2023)"
"size": "Tiny"
"type": "fey"
"alignment": "Chaotic Neutral"
"ac": !!int "16"
"ac_class": "natural armor"
"hp": !!int "49"
"hit_dice": "11d4 + 22"
"stats":
- !!int "3"
- !!int "18"
- !!int "14"
- !!int "11"
- !!int "10"
- !!int "16"
"speed": "20 ft."
"saves":
  "Dexterity": !!int "6"
"skillsaves":
  "Acrobatics": !!int "6"
"damage_resistances": "piercing from nonmagical attacks"
"damage_immunities": "lightning, thunder"
"senses": "passive Perception 10"
"languages": "Common, Sylvan"
"cr": "3"
"traits":
- "desc": "A creature wearing metal or wielding a metal weapon that touches the spire\
    \ walker or hits it with a melee attack while within 5 feet of it takes 3 (1d6)\
    \ lightning damage."
  "name": "Energized Body"
"actions":
- "desc": "Melee or Ranged Spell Attack: +5 to hit, reach 5 ft. or range 60 ft.,\
    \ one target. Hit: 17 (4d6 + 3) lightning damage, and each creature, other\
    \ than the target, within 10 feet of the target must make a DC 13 Dexterity saving\
    \ throw, taking 7 (2d6) lightning damage on a failed save, or half as much damage\
    \ on a successful one."
  "name": "Lightning Burst"
- "desc": "The spire walker magically turns [invisible](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Invisible)\
    \ until it attacks or until its [concentration](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Concentration)\
    \ ends (as if [concentrating](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Concentration)\
    \ on a spell). Any equipment the spire walker wears or carries is [invisible](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Invisible)\
    \ with it."
  "name": "Invisibility"
"bonus_actions":
- "desc": "The spire walker teleports, along with any equipment it is wearing or carrying,\
    \ up to 30 feet to an unoccupied space it can see. The destination must be on\
    \ the steeple of a building, mast of a ship, corner of a rooftop, or similar narrow\
    \ point or feature."
  "name": "Steeple Step"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fey/token/spire-walker-tob1-2023.webp"
```
^statblock

## Environment

badlands, coastal, urban
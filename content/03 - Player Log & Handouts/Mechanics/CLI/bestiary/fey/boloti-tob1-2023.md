---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/1
- ttrpg-cli/monster/environment/swamp
- ttrpg-cli/monster/size/tiny
- ttrpg-cli/monster/type/fey
statblock: inline
aliases: ["Boloti"]
---
# [Boloti](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fey/boloti-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 38*  

*This small, leering water spirit resembles a cross between a gray frog and a damp scarecrow, with small tendrils sprouting from all its extremities. It has water wings seemingly made out of jellyfish flesh.*

## Swamp Robbers

Known as uriska in Draconic, the bolotis are small, swamp-dwelling water spirits which delight in drowning unsuspecting victims in shallow pools and springs, then robbing the corpses of whatever shiny objects they find. Bolotis use their magical vortex abilities to immobilize their victims and drag them to a watery death. They delight in storing up larders of victims under winter ice or under logs.

## Fond of Allies

Bolotis sometimes team up with miremals and will-o'-wisps to create cunning ambushes. They are happy with a single kill at a time.

```statblock
"name": "Boloti (ToB1-2023)"
"size": "Tiny"
"type": "fey"
"alignment": "Neutral Evil"
"ac": !!int "15"
"hp": !!int "45"
"hit_dice": "10d4 + 20"
"stats":
- !!int "12"
- !!int "20"
- !!int "14"
- !!int "13"
- !!int "12"
- !!int "11"
"speed": "20 ft., swim 40 ft. (0 ft. swim 60 ft. in vortex form)"
"skillsaves":
  "Stealth": !!int "7"
  "Perception": !!int "3"
"senses": "darkvision 60 ft., passive Perception 13"
"languages": "Common, Primordial, Sylvan"
"cr": "1"
"traits":
- "desc": "The boloti casts one of the following spells, requiring no material components\
    \ and using Intelligence as the spellcasting ability (spell save DC 11):\n\nAt\
    \ will: [water breathing](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/water-breathing.md),\
    \ [water walk](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/water-walk.md)\n\
    \n1/day: [control water](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/control-water.md)\n\
    \n3/day each: [create or destroy water](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/create-or-destroy-water.md),\
    \ [fog cloud](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/fog-cloud.md),\
    \ [sleep](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/sleep.md)"
  "name": "Spellcasting (True Form Only)"
- "desc": "The boloti can breathe air and water."
  "name": "Amphibious"
- "desc": "The boloti has advantage on Dexterity ([Stealth](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Stealth))\
    \ checks made to hide while at least half of its body is submerged in water."
  "name": "Water Camouflage"
- "desc": "A boloti has advantage on attack rolls if both it and its target are touching\
    \ the same body of water. If the target and the boloti are both on dry ground,\
    \ the boloti has disadvantage on attack rolls."
  "name": "Water Mastery"
- "desc": "The boloti can enter a hostile creature's space and stop there. It can\
    \ move through a space as narrow as 1 inch wide without squeezing. A creature\
    \ that starts its turn in the boloti's space must succeed on a DC 12 Strength\
    \ saving throw or take 4 (1d8) bludgeoning damage as it is buffeted by the swirl\
    \ of water."
  "name": "Watery Body (Vortex Form Only)"
"actions":
- "desc": "Melee or Ranged Weapon Attack: +7 to hit, reach 5 ft. or range 20/60\
    \ ft., one target. Hit: 7 (1d4 + 5) piercing damage."
  "name": "Dagger (True Form Only)"
- "desc": "One creature in the boloti's space must make a DC 12 Strength saving throw.\
    \ On a failure, the target takes 9 (2d8) bludgeoning damage, and if it is Medium\
    \ or smaller, it is [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ (escape DC 12). Until this grapple ends, the target is [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ and unable to breathe unless it can breathe water. If the saving throw is successful,\
    \ the target takes half the damage and is pushed out of the boloti's space."
  "name": "Whirlpool (Vortex Form Only)"
"bonus_actions":
- "desc": "The boloti magically transforms into a Small vortex of swirling, churning\
    \ water or back into its true form, which is Fey. The boloti can transform into\
    \ its vortex form only while at least half of its body is submerged in water,\
    \ and any creature it is grappling with Whirlpool is freed if the boloti transforms\
    \ back to its true form. Its statistics are the same in each form. Any equipment\
    \ it is wearing or carrying transforms with it. It reverts to its true form if\
    \ it dies."
  "name": "Vortex Form"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fey/token/boloti-tob1-2023.webp"
```
^statblock

## Environment

swamp
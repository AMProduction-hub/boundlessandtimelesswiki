---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/2
- ttrpg-cli/monster/environment/underdark
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/small
- ttrpg-cli/monster/type/humanoid/kobold
statblock: inline
aliases: ["Kobold Alchemist"]
---
# [Kobold Alchemist](03 - Player Log & Handouts\Mechanics\CLI\bestiary\humanoid/kobold-alchemist-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 244*  

*This slight, reptilian humanoid is bedecked with ceramic flasks and glass vials. An acrid reek follows in its wake.*

Kobold alchemists are usually smelled before they are seen, thanks to the apothecary's store of chemicals and poisons they carry. Alchemists often sport mottled and discolored scales and skin, caused by the caustic nature of their obsessions. They raid alchemy shops and magical laboratories to gather more material to fuel their alchemical experiments.

## Dangerous Assets

Alchemists can be a great boon to their clan, but at a cost. Not only do the alchemists require rare, expensive, and often dangerous substances to ply their trade, they tend to be a little unhinged. Their experiments yield powerful weapons and defensive concoctions that can save many kobold lives, but the destruction caused by an experiment gone awry can be devastating for the alchemist's neighbors.

```statblock
"name": "Kobold Alchemist (ToB1-2023)"
"size": "Small"
"type": "humanoid"
"subtype": "kobold"
"alignment": "Lawful Neutral"
"ac": !!int "15"
"ac_class": "[studded leather](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/items/studded-leather-armor.md)"
"hp": !!int "44"
"hit_dice": "8d6 + 16"
"stats":
- !!int "7"
- !!int "16"
- !!int "15"
- !!int "16"
- !!int "9"
- !!int "8"
"speed": "30 ft."
"saves":
  "Dexterity": !!int "5"
"skillsaves":
  "Medicine": !!int "3"
  "Arcana": !!int "5"
"damage_immunities": "poison"
"condition_immunities": "[poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 60 ft., passive Perception 9"
"languages": "Common, Draconic"
"cr": "2"
"traits":
- "desc": "At the start of each of the kobold alchemist's turns, the alchemist chooses\
    \ one of the following damage types: acid, cold, fire, lightning, or poison. The\
    \ alchemist has resistance to that damage type until the start of its next turn."
  "name": "Apothecary"
- "desc": "The kobold has advantage on attack rolls against a creature if at least\
    \ one of the kobold's allies is within 5 feet of the creature and the ally isn't\
    \ [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated)."
  "name": "Pack Tactics"
- "desc": "While in sunlight, the kobold has disadvantage on attack rolls, as well\
    \ as on Wisdom ([Perception](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Perception))\
    \ checks that rely on sight."
  "name": "Sunlight Sensitivity"
"actions":
- "desc": "The kobold makes two Alchemical Dagger or Alchemical Bolt attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 5 1d4\
    \ + 3 piercing damage plus 3 (1d6) damage of the type determined by Apothecary."
  "name": "Alchemical Dagger"
- "desc": "Ranged Spell Attack: +5 to hit, range 60 ft., one target. Hit: 10\
    \ (2d6 + 3) damage of the type determined by Apothecary."
  "name": "Alchemical Bolt"
- "desc": "The kobold alchemist releases alchemical vapors pleasing to draconic senses\
    \ and unpleasant to all others. Each creature that isn't a dragonborn or kobold\
    \ within 15 feet of the alchemist must make a DC 13 Constitution saving throw,\
    \ taking 17 (5d6) poison damage on a failed save, or half as much damage on\
    \ a successful one. Each dragonborn and kobold within 15 feet of the alchemist\
    \ has resistance to damage of the type determined by Apothecary for 1 minute."
  "name": "Alchemical Vapors (Recharge 6)"
- "desc": "The kobold alchemist throws a flask of volatile substances at a point it\
    \ can see within 30 feet of it. The flask explodes, and each creature within 15\
    \ feet of that point must make a DC 13 Dexterity saving throw. On a failure, a\
    \ creature takes 14 4d6 damage of the type determined by Apothecary and is [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ for 1 minute. On a success, a creature takes half the damage and isn't [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned).\
    \ A [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ creature can repeat the saving throw at the end of each of its turns, ending\
    \ the effect on itself on a success."
  "name": "Explosive Flask (Recharge 5-6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/humanoid/token/kobold-alchemist-tob1-2023.webp"
```
^statblock

## Environment

underdark, urban
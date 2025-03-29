---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/2
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/underwater
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/fey
statblock: inline
aliases: ["Eel Hound"]
---
# [Eel Hound](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fey/eel-hound-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 155*  

*The grotesque beast has the muscular tail, bulbous head, and rubbery, slime-covered flesh of an eel. Its torso and webbed paws resemble those of a misshapen canine, while needle-sharp teeth fill its menacing jaws.*

## Hounds of the River Fey

Ferocious aquatic fey, these amphibious menaces often serve lake trolls, lorelei, green hags, and other watery fey and giants. Predatory beasts as dangerous on land as they are in the water, the have a capricious cruelty. Few creatures beyond the fey appreciate eel hounds' lithe power and cruel grace, instead noting only their grotesque form and unnerving savagery.

## Slippery Ambushers

Eel hounds are ambush predators, hiding among the muck and algae of riverbanks, bursting out as a pack. Possessed of a low cunning, they prepare ambushes by vomiting their slippery spittle where land animals come to drink or along game trails. Then they surge from the water to snatch the off-balance prey. They surround targets, latching on with their powerful jaws, and then drag non-aquatic prey into the depths to drown or force aquatic prey onto land to suffocate.

## Fey Water Hounds

Eel hounds understand Sylvan, and those dwelling near humans or other races pick up a few words in other tongues.

```statblock
"name": "Eel Hound (ToB1-2023)"
"size": "Medium"
"type": "fey"
"alignment": "Neutral"
"ac": !!int "14"
"ac_class": "natural armor"
"hp": !!int "77"
"hit_dice": "14d8 + 14"
"stats":
- !!int "19"
- !!int "16"
- !!int "13"
- !!int "6"
- !!int "13"
- !!int "16"
"speed": "30 ft., swim 40 ft."
"skillsaves":
  "Stealth": !!int "5"
  "Perception": !!int "3"
"senses": "darkvision 60 ft., passive Perception 13"
"languages": "understands Sylvan but can't speak"
"cr": "2"
"traits":
- "desc": "The eel hound can breathe air and water."
  "name": "Amphibious"
- "desc": "The eel hound has advantage on attack rolls against a creature if at least\
    \ one of the hound's allies is within 5 feet of the creature and the ally isn't\
    \ [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated)."
  "name": "Pack Tactics"
"actions":
- "desc": "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 11\
    \ (2d6 + 4) piercing damage, and the target is [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ (escape DC 14). Until this grapple ends, the creature is [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained),\
    \ and the hound can't Bite another target."
  "name": "Bite"
- "desc": "The eel hound covers the ground in a 5-foot square centered on a point\
    \ it can see within 10 feet of it with its slippery spittle. Each creature standing\
    \ in that area must succeed on a DC 13 Dexterity saving throw or fall [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone).\
    \ A creature that enters the area or ends its turn there must also succeed on\
    \ a DC 13 Dexterity saving throw or fall [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone).\
    \ The spittle remains on the ground for 1 minute."
  "name": "Slick Spittle"
"bonus_actions":
- "desc": "The eel hound teleports, along with any equipment it is wearing or carrying,\
    \ up to 30 feet to an unoccupied space it can see. The origin and destination\
    \ spaces must contain enough water to partially submerge the hound."
  "name": "Water Step"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fey/token/eel-hound-tob1-2023.webp"
```
^statblock

## Environment

forest, underwater
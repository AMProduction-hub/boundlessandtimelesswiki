---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/2
- ttrpg-cli/monster/environment/mountain
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/size/small
- ttrpg-cli/monster/type/monstrosity
statblock: inline
aliases: ["Eala"]
---
# [Eala](03 - Player Log & Handouts\Mechanics\CLI\bestiary\monstrosity/eala-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 152*  

*This swanlike creature's feathers are made of shining metal. When it inhales, the feathers on its chest glow red hot.*

Eala are beautiful but deadly creatures native to the Plane of Shadow. They grow feathers like their Material Plane counterparts, but their feathers are made of gleaming, razor-sharp metal.

## Metallic Diet

Eala plumage displays a stunning mixture of metallic colors, which vary depending on their diet. An eala uses its fire breath to melt metals with low melting points such as gold, silver, lead, copper, and bronze. The eala consumes the molten metal, some of which migrates into the creature's deadly feathers. Eala that display primarily or entirely a single color are highly prized among some nobility.

> [!note] Eala in Midgard
> 
> Eala are favorites of Sarastra, the Queen of Night and Magic and a ruler of the shadow fey. She is partial to jet black eala, and all such specimens are brought to her flock at the Winter Palace. Those who bring her such birds are rewarded with a magical dagger and the title and status of "Honored Eala Catcher," or "Lord or Lady of Black Feathers" for those who bring her several.
^eala-in-midgard

```statblock
"name": "Eala (ToB1-2023)"
"size": "Small"
"type": "monstrosity"
"alignment": "Unaligned"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "40"
"hit_dice": "9d6 + 9"
"stats":
- !!int "10"
- !!int "16"
- !!int "12"
- !!int "2"
- !!int "12"
- !!int "16"
"speed": "10 ft., fly 60 ft."
"saves":
  "Dexterity": !!int "5"
"damage_immunities": "fire"
"senses": "darkvision 60 ft., passive Perception 11"
"languages": ""
"cr": "2"
"actions":
- "desc": "The eala makes two Wing Blades attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 7 (1d8\
    \ + 3) slashing damage."
  "name": "Wing Blades"
- "desc": "The eala breathes fire in a 15-foot cone. Each creature in the area must\
    \ make a DC 13 Dexterity saving throw, taking 10 (3d6) fire damage on a failed\
    \ save, or half as much damage on a successful one. The eala's fire breath ignites\
    \ flammable objects and melts soft metals, such as gold and lead, in the area\
    \ that aren't being worn or carried."
  "name": "Fire Breath (Recharge 5-6)"
"reactions":
- "desc": "When the eala is reduced to 0 hp, it can use its last breath to sing a\
    \ plaintive and beautiful melody. Each creature within 20 feet of it that can\
    \ hear the eala must succeed on a DC 13 Charisma saving throw or be [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated)\
    \ until the end of its next turn. While [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated),\
    \ the creature's speed is reduced to 0."
  "name": "Swan Song"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/monstrosity/token/eala-tob1-2023.webp"
```
^statblock

## Environment

mountain, planar
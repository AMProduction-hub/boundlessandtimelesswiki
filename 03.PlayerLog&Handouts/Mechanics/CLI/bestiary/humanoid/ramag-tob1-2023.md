---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/1-4
- ttrpg-cli/monster/environment/desert
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/humanoid
statblock: inline
aliases: ["Ramag"]
---
# [Ramag](03 - Player Log & Handouts\Mechanics\CLI\bestiary\humanoid/ramag-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 299*  

*The especially lanky man with long limbs and thick locks of hair traced magical symbols with delicate fingers, opening a small portal.*

The ramag were a powerful tribe of dimensional sorcerers allied with a great society of titans, and they were indeed human in ages past. Over time, strange practices warped them into their current state, and they are clearly no longer purely human. They have angular features, and their limbs grow long in proportion to their bodies, giving them a stooped posture. A ramag's hair is impossibly thick, each strand being the width of a human finger, which they wear tied back with decorative clasps.

## Portal Network

The ramag used their innate magical gifts and affinity for portals to maintain powerful magical conduits. This mastery of the arcane allowed instantaneous travel to the farthest-flung outpost. The ramag still maintain a network of magical monoliths that connect the scattered districts of their home, but this network is frayed and fading.

## Studious and Powerful

Although physically weak, the ramag are sharp-witted, studious, and naturally infused with magic. Lifetimes of exposure to the warping effect of their runaway magical energy have given them innate control over magic as well as sharp resistance to it. They are acutely aware of their responsibility for keeping magic in check and fully know the danger of uncontrolled magical energies. Even the lowliest ramag has a keen intellect and a natural understanding of magic. Many ramag take up the study of wizardry. Few become wandering adventurers, but well-equipped expeditions sometimes leave their homeland to inspect the surrounding countryside.

> [!note] Ramag in Midgard
> 
> The ramag all live within the twelve scattered districts of their home city, Ramagani (home, in their dialect), with eleven districts in the Abandoned Lands of the Southlands and one on an island off the coast. Though the districts are far apart, the ramag consider them all part of one great metropolis. The inhabited districts are guarded by powerful ramag spellcasters and by the Stormwatch—a garrison of arcane warriors who operate enchanted lightning ballistae in defense of the city. A lightning ballista functions identically to a standard ballista but does an additional `1d10` lightning damage with each hit.
^ramag-in-midgard

```statblock
"name": "Ramag (ToB1-2023)"
"size": "Medium"
"type": "humanoid"
"alignment": "Neutral"
"ac": !!int "13"
"ac_class": "[leather armor](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/items/leather-armor.md)"
"hp": !!int "27"
"hit_dice": "6d8"
"stats":
- !!int "9"
- !!int "14"
- !!int "10"
- !!int "16"
- !!int "12"
- !!int "11"
"speed": "30 ft."
"skillsaves":
  "Investigation": !!int "5"
  "Arcana": !!int "5"
"senses": "passive Perception 11"
"languages": "Common"
"cr": "1/4"
"traits":
- "desc": "The ramag has advantage on saving throws against spells or other magical\
    \ effects."
  "name": "Magic Resistance"
- "desc": "The ramag can pinpoint the location of planar portals within 100 feet of\
    \ it and can sense the general direction of planar portals within 1 mile of it.\
    \ In addition, if the ramag spends 10 minutes studying a portal, it can determine\
    \ the portal's destination and any requirements to use or activate it."
  "name": "Portal Sense"
"actions":
- "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6\
    \ + 2) slashing damage."
  "name": "Scimitar"
- "desc": "Ranged Weapon Attack: +4 to hit, range 80/320 ft., one target. Hit:\
    \ 5 (1d6 + 2) piercing damage."
  "name": "Shortbow"
"bonus_actions":
- "desc": "The ramag creates and steps into a small portal and out of an identical\
    \ portal in a space it can see within 60 feet of it. If a creature is in the destination\
    \ space, the creature must make a DC 13 Intelligence saving throw. On a failure,\
    \ the ramag trades spaces with the creature. On a success, the ramag fails to\
    \ teleport. Whatever the result, the portal disappears."
  "name": "Portal Traveler (Recharge 5-6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/humanoid/token/ramag-tob1-2023.webp"
```
^statblock

## Environment

desert, urban
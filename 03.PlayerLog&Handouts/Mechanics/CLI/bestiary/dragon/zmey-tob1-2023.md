---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/15
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/swamp
- ttrpg-cli/monster/size/huge
- ttrpg-cli/monster/type/dragon
statblock: inline
aliases: ["Zmey"]
---
# [Zmey](03 - Player Log & Handouts\Mechanics\CLI\bestiary\dragon/zmey-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 403*  

*Crashing through the forest, this three-headed dragon stands upright, its long tail thrashing from side to side as it walks.*

Hunting beneath the canopy of the forest, lurking below the surfaces of lakes, and guarding caves concealing great treasure and mystery, the zmey has two roles—vicious terror and nature's protector.

## Claws of the Forest

Single-mindedly destructive, the zmey keeps the heart of the forest free from interlopers. Rumors suggest the heart of an ancient forest itself can control the actions of these lesser dragons, while others believe zmeys have pacts with certain druid circles.

## Voracious Headlings

A zmey's head doesn't die when severed from its body. Within days, it becomes a miniature zmey, developing into a full-grown zmey after two months. Voracious appetite fuels this growth. Coating the head or headling in the first month of life prevents this growth.

## A Zmey's Lair

Zmeys make their lairs in the deepest parts of the forest. They plant and grow trees into "caves" with satellite "rooms" within their lair.

```statblock
"name": "Zmey (ToB1-2023)"
"size": "Huge"
"type": "dragon"
"alignment": "Chaotic Evil"
"ac": !!int "18"
"ac_class": "natural armor"
"hp": !!int "189"
"hit_dice": "18d12 + 72"
"stats":
- !!int "22"
- !!int "13"
- !!int "19"
- !!int "16"
- !!int "16"
- !!int "12"
"speed": "30 ft., fly 50 ft., swim 30 ft."
"saves":
  "Charisma": !!int "6"
  "Wisdom": !!int "8"
  "Constitution": !!int "9"
"skillsaves":
  "Perception": !!int "8"
"damage_resistances": "cold, fire"
"condition_immunities": "[paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [unconscious](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Unconscious)"
"senses": "blindsight 60 ft., darkvision 90 ft., passive Perception 18"
"languages": "Common, Draconic, Elvish, Sylvan"
"cr": "15"
"traits":
- "desc": "The zmey can breathe air and water."
  "name": "Amphibious"
- "desc": "If the zmey fails a saving throw, it can choose to succeed instead."
  "name": "Legendary Resistance (3/Day)"
- "desc": "The zmey regains 15 hp at the start of its turn. If the zmey takes acid\
    \ or fire damage, this trait doesn't function at the start of the zmey's next\
    \ turn. The zmey dies if it starts its turn with 0 hp and doesn't regenerate."
  "name": "Regeneration"
- "desc": "The zmey has three heads. While it has more than one head, the zmey has\
    \ advantage on saving throws against being [blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded),\
    \ [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
    \ [deafened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Deafened),\
    \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
    \ [stunned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Stunned),\
    \ and knocked [unconscious](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Unconscious).\
    \ Whenever the zmey takes 40 damage or more in a single turn, one of its heads\
    \ is severed. If it has only one head remaining, dealing 40 damage or more to\
    \ it doesn't sever the final head. It regrows any severed heads when it finishes\
    \ a long rest.\n\nThe zmey's severed head grows into a zmey headling in 1d4\
    \ rounds. The headling isn't under the zmey's control, but it takes the zmey's\
    \ requests or actions in the most favorable way it can."
  "name": "Three Heads"
"actions":
- "desc": "The zmey makes two Claw attacks and as many Bite attacks as it has heads."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +11 to hit, reach 10 ft., one target. Hit: 19\
    \ (2d12 + 6) piercing damage."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +11 to hit, reach 5 ft., one target. Hit: 20\
    \ (4d6 + 6) slashing damage."
  "name": "Claw"
- "desc": "The zmey exhales fire in a 30-foot cone out of each of its heads. Each\
    \ creature in a cone must make a DC 17 Dexterity saving throw, taking 49 (14d6)\
    \ fire damage on a failed save, or half as much damage on a successful one. If\
    \ the cones overlap, each creature in the overlapping cones must make one saving\
    \ throw with disadvantage against only one of the cones rather than one saving\
    \ throw for each cone. The zmey can choose for this breath to not harm plants\
    \ or Plant creatures."
  "name": "Fire Breath (Recharge 5-6)"
"legendary_actions":
- "desc": "The zmey moves up to its speed, or flies up to half its flying speed, without\
    \ provoking opportunity attacks."
  "name": "Move"
- "desc": "The zmey whips its tail around it. Each creature within 15 feet of the\
    \ zmey must succeed on a DC 17 Dexterity saving throw or be knocked [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)."
  "name": "Tail Whip"
- "desc": "The zmey's heads exhale a three‑part roar, one a deafening shriek, one\
    \ a frightful screech, and one a stunning bellow, in a 30-foot cone. Each creature\
    \ in that area must succeed on a DC 17 Wisdom saving throw or suffer the effects\
    \ of the roars until the end of its next turn. The effects depend upon the number\
    \ of heads the zmey has remaining: [deafened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Deafened)\
    \ for only one head, [deafened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Deafened)\
    \ and [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)\
    \ for two heads, or [stunned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Stunned)\
    \ for three heads."
  "name": "Tripartite Roar (Costs 2 Actions)"
"lair_actions":
- "desc": "On initiative count 20 (losing initiative ties), the zmey takes a lair\
    \ action to cause one of the following effects; it can't use the same effect two\
    \ rounds in a row:"
  "name": ""
- "desc": "- Hinder Movement. One hostile creature the zmey can see within 120\
    \ feet of it has its speed halved until initiative count 20 on the next round,\
    \ as roots trip up walking and hanging branches and vines dangle in the way of\
    \ flight.  \n- Invigorate Headlings. One severed zmey head the zmey can see\
    \ within 120 feet of it immediately grows into a zmey headling, or one slain zmey\
    \ headling the zmey can see within 120 feet of it regains 10 hp and becomes active\
    \ again. A severed head or zmey headling smeared in a pound of salt can't be affected\
    \ by this lair action.  \n- Spread Forest's Gloom. Light reduces in a 30-foot-radius\
    \ sphere centered on a point the zmey can see within 120 feet of it. Bright light\
    \ becomes dim light, dim light becomes darkness, and darkness becomes magical\
    \ darkness in the sphere. The sphere lasts until the zmey dismisses it as an action,\
    \ uses this lair action again, or dies.  "
  "name": ""
"regional_effects":
- "desc": "The region containing the zmey's lair is warped by the link between the\
    \ creature and its forest home, which creates one or more of the following effects:"
  "name": ""
- "desc": "- Fear and Rage. Creatures within 1 mile of the lair feel constantly\
    \ on the verge of an overwhelming fight-or-flight response, keeping them on edge\
    \ and making their sleep fitful.  \n- Unfriendly Forest. The forest within\
    \ 6 miles of the lair is as uninviting as possible to those not native to it:\
    \ unattended fires tend to go out mysteriously and new fires are hard to start,\
    \ flora and fauna slain or foraged spoil almost immediately, and similar.  \n\
    - Unnerving Presence. Creatures within 3 miles of the lair are unsettled by\
    \ the forest and frequently distracted by phantom chattering, tricks of the light,\
    \ and other sensations.  "
  "name": ""
- "desc": "If the zmey dies, these effects fade over the course of 1d10 days."
  "name": ""
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/dragon/token/zmey-tob1-2023.webp"
```
^statblock

## Environment

forest, swamp
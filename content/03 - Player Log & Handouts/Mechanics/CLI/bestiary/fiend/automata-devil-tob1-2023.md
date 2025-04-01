---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/10
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/fiend/devil
statblock: inline
aliases: ["Automata Devil"]
---
# [Automata Devil](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fiend/automata-devil-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 92*  

*A nightmare wrapped in chains and held together by cutting cogs and whirring gears, this fiend howls like a hurricane in battle.*

## Guards and Overseers

Sometimes called castigas, automata devils are made to monitor others. They are often put in charge of prisoners or infernal factories.

## Pierced by Chain and Wire

This slender creature's skin is pierced with barbs, sharp nails, and coils of wire, which have been threaded through its flesh. Chains are buried under blisters and scabs. This infernal horror's eyelids—both front and back pairs—are sewn back with wire, while six arms ending in large grasping hands erupt from its shoulders.

## Coiled Metal Whips

The creature's head is a dark mass ending in two large mandibles. By its side, it carries a huge coiled whip that squirms like a snake and is said to scent lies and treachery. The creature's stomach opens up like a second mouth, lined with tooth-like spines.

> [!note] Automata Devils in Midgard
> 
> One corner of the Eleven Hells is known simply as the Forge. Here, black chimneys rise a mile high from a dead land of choking air and red poison hills. The Machine, a greater devil who never sleeps and never lets his subjects know rest, rules this land. His overseers consist of thousands of imps who whip and punish the workers. The imps themselves are kept in check by hordes of chain devils, who in turn answer to the automata devils as overseers.
^automata-devils-in-midgard

```statblock
"name": "Automata Devil (ToB1-2023)"
"size": "Large"
"type": "fiend"
"subtype": "devil"
"alignment": "Lawful Evil"
"ac": !!int "17"
"ac_class": "natural armor"
"hp": !!int "168"
"hit_dice": "16d10 + 80"
"stats":
- !!int "24"
- !!int "17"
- !!int "20"
- !!int "11"
- !!int "14"
- !!int "19"
"speed": "40 ft."
"saves":
  "Charisma": !!int "8"
  "Dexterity": !!int "7"
  "Wisdom": !!int "6"
  "Strength": !!int "11"
"skillsaves":
  "Intimidation": !!int "8"
  "Athletics": !!int "11"
"damage_resistances": "cold; bludgeoning, piercing, slashing from nonmagical attacks\
  \ that aren't silvered"
"damage_immunities": "fire, poison"
"condition_immunities": "[poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 120 ft., passive Perception 12"
"languages": "Common, Infernal, telepathy 120 ft."
"cr": "10"
"traits":
- "desc": "Magical darkness doesn't impede the devil's darkvision."
  "name": "Devil's Sight"
- "desc": "A creature that starts its turn within 10 feet of the automata devil must\
    \ succeed on a DC 17 Wisdom saving throw or become [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)\
    \ until the start of its next turn. On a successful saving throw, the creature\
    \ is immune to the automata devil's Fear Aura for 24 hours."
  "name": "Fear Aura"
- "desc": "The automata devil has advantage on saving throws against spells and other\
    \ magical effects."
  "name": "Magic Resistance"
"actions":
- "desc": "The automata devil makes one Bite attack, one Whip attack, and two Claw\
    \ attacks. It can replace two Claw attacks with a use of Shredding Maw."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +11 to hit, reach 5 ft., one target. Hit: 18\
    \ (2d10 + 7) slashing damage."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +11 to hit, reach 5 ft., one target. Hit: 16\
    \ (2d8 + 7) slashing damage."
  "name": "Claw"
- "desc": "Melee Weapon Attack: +11 to hit, reach 15 ft., one target. Hit: 12\
    \ (2d4 + 7) slashing damage, and the target is [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ (escape DC 17). The automata devil has two whips, each of which can grapple\
    \ only one target."
  "name": "Whip"
- "desc": "One creature [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ by the automata devil is pulled up to 10 feet toward the devil's central maw,\
    \ which shreds the creature with churning gears, razor teeth, and whirling blades.\
    \ The target must make a DC 17 Strength saving throw, taking 36 (8d8) slashing\
    \ damage on a failed save, or half as much damage on a successful one."
  "name": "Shredding Maw"
- "desc": "The automata devil magically teleports, along with any equipment it is\
    \ wearing or carrying up to 120 feet to an unoccupied space it can see."
  "name": "Teleport"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fiend/token/automata-devil-tob1-2023.webp"
```
^statblock

## Environment

planar
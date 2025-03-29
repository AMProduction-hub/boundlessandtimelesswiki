---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/23
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/size/gargantuan
- ttrpg-cli/monster/type/fiend/demon
statblock: inline
aliases: ["Demon Lord Qorgeth"]
---
# [Demon Lord Qorgeth](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fiend/demon-lord-qorgeth-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 80*  

*This massive undulating worm-like creature crushes trees and cracks stone.*

Qorgeth, the Writhing Prince, Pale Maw, the Devourer, is the lord of worms and decay. Its presence seeps into the world of mortals via the trails of worms and maggots through rotting flesh. The demon lord views all things that live, or once lived, as its property in the making. Everything becomes its food eventually.

## Fiendish Worm

An impossibly massive, pale-fleshed worm, Qorgeth's segmented body is road-mapped with pale veins of pink and blue. When it opens its massive maw, it reveals a writhing mass of smaller worms, many of which are adorned with wailing or enraged humanoid heads.

## Qorgeth's Lair

Qorgeth's lair is a tangled labyrinth of tunnels in the heart of its dark realm. The tunnels seem to twist and burrow through space itself rather than just the rock and soil surrounding them.

```statblock
"name": "Demon Lord Qorgeth (ToB1-2023)"
"size": "Gargantuan"
"type": "fiend"
"subtype": "demon"
"alignment": "Chaotic Evil"
"ac": !!int "21"
"ac_class": "natural armor"
"hp": !!int "370"
"hit_dice": "20d20 + 160"
"stats":
- !!int "29"
- !!int "6"
- !!int "26"
- !!int "9"
- !!int "22"
- !!int "18"
"speed": "50 ft., burrow 50 ft., climb 30 ft."
"saves":
  "Charisma": !!int "11"
  "Dexterity": !!int "5"
  "Wisdom": !!int "13"
  "Constitution": !!int "15"
"skillsaves":
  "Perception": !!int "13"
"damage_resistances": "cold, fire, lightning"
"damage_immunities": "poison; bludgeoning, piercing, slashing from nonmagical attacks"
"condition_immunities": "[blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded),\
  \ [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "blindsight 120 ft., tremorsense 120 ft., passive Perception 23"
"languages": "all, telepathy 120 ft."
"cr": "23"
"traits":
- "desc": "Qorgeth casts one of the following spells, requiring no material or somatic\
    \ components and using Charisma as the spellcasting ability (spell save DC 19):\n\
    \nAt will: [Evard's black tentacles](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/evards-black-tentacles.md),\
    \ [detect magic](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/detect-magic.md)\n\
    \n1/day each: [earthquake](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/earthquake.md),\
    \ [teleport](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/teleport.md)\
    \ (self only)\n\n3/day each: [dispel magic](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/dispel-magic.md),\
    \ [insect plague](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/insect-plague.md)\
    \ (biting worms)"
  "name": "Spellcasting"
- "desc": "If Qorgeth fails a saving throw, it can choose to succeed instead."
  "name": "Legendary Resistance (3/Day)"
- "desc": "Qorgeth has advantage on saving throws against spells and other magical\
    \ effects."
  "name": "Magic Resistance"
- "desc": "Qorgeth's weapon attacks are magical."
  "name": "Magic Weapons"
- "desc": "Qorgeth can burrow through solid rock and leaves a 15-foot-diameter tunnel\
    \ in its wake."
  "name": "Tunneler"
"actions":
- "desc": "Qorgeth makes one Bite attack, two Crush attacks, and one Stinger attack."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +16 to hit, reach 10 ft., one target. Hit: 22\
    \ (2d12 + 9) piercing damage. If the target is a Large or smaller creature,\
    \ it must succeed on a DC 21 Dexterity saving throw or be swallowed by Qorgeth.\
    \ A swallowed creature is [blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded)\
    \ and [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained),\
    \ it has total cover against attacks and other effects outside the worm, and it\
    \ takes 16 (3d10) necrotic damage at the start of each of Qorgeth's turns.\n\
    \nIf Qorgeth takes 50 damage or more in a single turn from a creature inside it,\
    \ Qorgeth must succeed on a DC 25 Constitution saving throw at the end of that\
    \ turn or regurgitate all swallowed creatures, which fall [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)\
    \ in a space within 10 feet of Qorgeth. If Qorgeth dies, a swallowed creature\
    \ is no longer [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ by it and can escape the corpse by spending 30 feet of movement, exiting [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +16 to hit, reach 10 ft., one target. Hit: 20\
    \ (2d10 + 9) bludgeoning damage, and if the target is a Large or smaller creature,\
    \ it is [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ until Qorgeth moves. A creature, including the [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ creature, can use an action to free the [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ creature by succeeding on a DC 21 Strength check."
  "name": "Crush"
- "desc": "Melee Weapon Attack: +16 to hit, reach 15 ft., one target. Hit: 23\
    \ (4d6 + 9) piercing damage, and the target must make a DC 21 Constitution saving\
    \ throw. On a failure, the target takes 33 (6d10) poison damage and is [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ for 1 hour. On a success, the target takes half the damage and isn't [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned).\
    \ A creature that fails the saving throw by 10 or more is also [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed)\
    \ while [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ in this way."
  "name": "Stinger"
"legendary_actions":
- "desc": "Each creature within 60 feet of Qorgeth and that can hear the demon must\
    \ succeed on a DC 21 Wisdom saving throw or be [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)\
    \ for 1 minute. The creature can repeat the saving throw at the end of each of\
    \ its turns, ending the effect on itself on a success."
  "name": "Shriek"
- "desc": "Qorgeth moves up to half its speed straight toward a creature and makes\
    \ one Crush attack against the creature. Each object and structure between Qorgeth\
    \ and the target takes 33 (6d10) bludgeoning damage."
  "name": "Death Roll (Costs 2 Actions)"
- "desc": "Qorgeth makes one Bite attack."
  "name": "Devour (Costs 3 Actions)"
"lair_actions":
- "desc": "On initiative count 20 (losing initiative ties), Qorgeth takes a lair action\
    \ to cause one of the following effects; Qorgeth can't use the same effect two\
    \ rounds in a row:"
  "name": ""
- "desc": "- Collapse Passage. A section of ceiling in the lair collapses, raining\
    \ debris onto a point Qorgeth can see within 120 feet of it. Each creature within\
    \ 20 feet of that point must succeed on a DC 21 Dexterity saving throw or take\
    \ 18 (4d8) bludgeoning damage and be restrained by the debris. A creature, including\
    \ the restrained creature, can use an action to free the restrained creature by\
    \ succeeding on a DC 21 Strength check.  \n- Warp Reality. Until initiative\
    \ count 20 on the next round, Qorgeth twists space through the tunnels of its\
    \ lair. A creature that isn't a demon that tries to move must succeed on a DC\
    \ 21 Charisma saving throw or move half its speed in a random direction before\
    \ getting its bearings; it can then finish moving as it wants.  \n- Worm Infestation.\
    \ Thick tangles of demonic worms erupt from the floor, wall, or ceiling near up\
    \ to three creatures Qorgeth can see within 60 feet of it. Qorgeth commands the\
    \ tangles to make one melee attack roll (+11 to hit) against each target before\
    \ disappearing. On a hit, the target takes 14 (4d6) piercing damage.  "
  "name": ""
"regional_effects":
- "desc": "The region containing Qorgeth's lair is warped by the demon lord's magic,\
    \ which creates one or more of the following effects:"
  "name": ""
- "desc": "- Rapid Rot. Dead bodies within 1 mile of the lair decay quickly. Any\
    \ corpse is reduced to bones in 24 hours. Magic that prevents decay staves off\
    \ this decomposition normally. Anointing the body with holy water prevents decomposition\
    \ for 1 day but no longer.  \n- Spoiled Supplies. Within 1 mile of the lair,\
    \ food rots and spontaneously erupts with maggots. One day's worth of food carried\
    \ by creatures spoils every 24 hours the creature remains in the area. Creatures\
    \ can't forage for food in this area.  \n- Wormhome. Tunnels within 5 miles\
    \ of the lair attract all manner of worms and vermin, including purple worms.\
    \ These creatures are ravenous and violent.  "
  "name": ""
- "desc": "If Qorgeth dies, conditions in the area surrounding the lair return to\
    \ normal over the course of 1d10 days."
  "name": ""
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fiend/token/demon-lord-qorgeth-tob1-2023.webp"
```
^statblock

## Environment

planar
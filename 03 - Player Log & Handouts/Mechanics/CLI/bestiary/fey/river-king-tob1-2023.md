---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/16
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/fey
statblock: inline
aliases: ["River King"]
---
# [River King](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fey/river-king-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 182*  

*This powerfully muscled elf lord wears a cloak of foam-trimmed dark blue and a vest of woven green reeds and willow branches. His crown shines like the sun on a lake, and his flowing hair curls and moves even when there is no wind. An orb of blue light that ripples like water circles his hand*.

His Rippling Majesty, Ulorian the River King, also bears the titles Defender of the Pearl Tower and Master of the Deep Forest. A lean elf noble with whipcord muscles and flowing grace, the River King rules over the Rippling Court and ultimately all the river elves of the forest. His court resides just beyond the river's reflection, in a realm of fey glamour and silty water.

## A Fickle Friend

The River King is a stern ruler with a great love for his people and a quick temper for those who threaten his domain. As much a force of nature as he is a monarch, the River King is known to sometimes forget promises that were made in sincerity, and dealing with him can be perilous at the best of times. "The river may change its course when it wills" is the usual expression among his court when His Rippling Majesty has had a sudden change of heart.

## Fey Lords and Ladies

Fey are capricious, mischievous, and often dangerous beings. However, despite their chaotic reputations, they do follow a certain set of rules. These rules—widely misunderstood by outsiders—are codified and enforced by a cadre of lofty fey nobility. Befitting any courtly structure, the fey bow to lords and ladies: eldritch creatures of immense power who rule the courts.

### Heads of State

The fey lords and ladies are beings of high station and prodigious personal power. Each rules over at least a great city if not an entire nation. No matter the scope of a fey noble's domain, in his or her eyes, a fey ruler's word is law. Outsiders might not understand the edicts and interdicts of a fey noble, but that's no protection against the harsh penalties that await any who break them, knowingly or otherwise.

### Vacant Thrones

When a lord or lady of the fey dies, the court does not remain leaderless for long. Ambitious beings among the fey always hunger for more power and covet the stations of their superiors. After a traditional month or year of mourning, vicious power struggles winnow the weak and pave the way for the most cunning or the strongest to take the court's vacant throne.

## The River King's Lair

The Court of the River King is a pair of small islands in the middle of a wide, swift river that flows from the mortal realm through a dimension of fey magic. The western keep houses servants, and the eastern is built above the Great Rippling Hall. The Great Rippling Hall is a bubble whose walls and ceiling are the river itself. A driftwood throne dominates the main hall.

```statblock
"name": "River King (ToB1-2023)"
"size": "Medium"
"type": "fey"
"alignment": "Chaotic Neutral"
"ac": !!int "18"
"ac_class": "natural armor"
"hp": !!int "190"
"hit_dice": "20d8 + 100"
"stats":
- !!int "21"
- !!int "17"
- !!int "20"
- !!int "14"
- !!int "13"
- !!int "17"
"speed": "30 ft., swim 60 ft."
"saves":
  "Dexterity": !!int "8"
  "Wisdom": !!int "6"
  "Constitution": !!int "10"
"skillsaves":
  "Nature": !!int "7"
  "Intimidation": !!int "8"
  "Stealth": !!int "8"
  "Perception": !!int "6"
"damage_resistances": "bludgeoning, piercing, slashing, cold, fire, lightning, thunder\
  \ from nonmagical attacks not made with cold iron weapons"
"damage_immunities": "poison"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)"
"senses": "blindsight 10 ft., darkvision 120 ft., passive Perception 16"
"languages": "Common, Elvish, Giant, Primordial"
"cr": "16"
"traits":
- "desc": "The River King casts one of the following spells, requiring no material\
    \ components and using Charisma as the spellcasting ability (save DC 16):\n\n\
    At will: [create or destroy water](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/create-or-destroy-water.md),\
    \ [water breathing](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/water-breathing.md)\n\
    \n1/day: [control weather](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/control-weather.md)\
    \ (as an action)\n\n3/day each: [freedom of movement](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/freedom-of-movement.md),\
    \ [control water](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/control-water.md)"
  "name": "Spellcasting"
- "desc": "The River King can breathe air and water."
  "name": "Amphibious"
- "desc": "If the River King fails a saving throw, he can choose to succeed instead."
  "name": "Legendary Resistance (3/Day)"
- "desc": "The River King's weapon attacks are magical. When he hits with any weapon,\
    \ the weapon deals an extra 10 (3d6) poison damage (included in the attack)."
  "name": "Riparian Weapons"
"actions":
- "desc": "The River King makes two Longsword or Flood Blast attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +10 to hit, reach 5 ft., one target. Hit: 9\
    \ (1d8 + 5) slashing damage, or 10 (1d10 + 5) slashing damage if used with\
    \ two hands, plus 10 (3d6) poison damage."
  "name": "Longsword"
- "desc": "Ranged Spell Attack: +8 to hit, range 120 ft., one target. Hit: 21\
    \ (4d8 + 3) bludgeoning damage, and the target must succeed on a DC 18 Strength\
    \ saving throw or be pushed up to 30 feet away from the River King and knocked\
    \ [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)."
  "name": "Flood Blast"
- "desc": "The River King magically creates a swirling vortex of water centered on\
    \ a point he can see within 60 feet. The vortex appears in the shape of a cylinder\
    \ that is 15 feet tall with a 10-foot radius. Each creature in the area must make\
    \ a DC 18 Strength saving throw. On a failure, a creature takes 36 (8d8) bludgeoning\
    \ damage and is [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained).\
    \ On a success, a creature takes half the damage, isn't [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained),\
    \ and can choose to be pushed out of the whirlpool's space. A creature that chooses\
    \ not to be pushed suffers the consequences of a failed saving throw. While [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained),\
    \ a creature is unable to breathe unless it can breathe water, and it must succeed\
    \ on a DC 18 Strength saving throw at the end of each of its turns or take 18\
    \ (4d8) bludgeoning damage. A creature, including the [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ creature, can take an action to free the [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained)\
    \ creature by succeeding on a DC 18 Strength check. A creature with a swimming\
    \ speed has advantage on the saving throw and on the Strength check to escape."
  "name": "Grasping Whirlpool (Recharge 5-6)"
"reactions":
- "desc": "When a creature within 5 feet of the River King stands up from [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone),\
    \ he can make one Longsword attack against that creature."
  "name": "Blade Current"
"legendary_actions":
- "desc": "The River King makes a Longsword or Flood Blast attack."
  "name": "Attack"
- "desc": "The River King moves up to his walking speed, or swims up to half his swimming\
    \ speed, without provoking opportunity attacks."
  "name": "Flow"
- "desc": "The River King magically ripples like sunlight on the surface of water.\
    \ Until the start of his next turn, attack rolls against him have disadvantage."
  "name": "Ripple (Costs 2 Actions)"
"lair_actions":
- "desc": "On initiative count 20 (losing initiative ties), the River King takes a\
    \ lair action to cause one of the following effects; the River King can't use\
    \ the same effect two rounds in a row:"
  "name": ""
- "desc": "- Flash Flooding. The fey river swells and rushes over the land, or\
    \ the walls of the Hall buckle and allow the torrent in. A 60-foot line of water\
    \ that is 10 feet wide rushes from a point on a wall the River King can see within\
    \ 60 feet of him. Each creature in the line must succeed on a DC 18 Strength saving\
    \ throw or be pushed up to 20 feet away from the point on the wall, in the direction\
    \ of the water's flow, and take 9 (2d8) bludgeoning damage.  \n- Invoke Drowning.\
    \ River water fills the mouth and throat of one creature the River King can see\
    \ within 60 feet of him. The target must succeed on a DC 18 Constitution saving\
    \ throw or begin suffocating. A suffocating but conscious target can repeat the\
    \ saving throw at the end of each of its turns, ending the effect on itself on\
    \ a success. Any creature can take an action to force the water from the target's\
    \ lungs by succeeding on a DC 15 Wisdom ([Medicine](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Medicine))\
    \ check, ending the effect. Otherwise, the effect lasts until the River King uses\
    \ this lair action again or until the River King dies.  \n- Imperial Impression.\
    \ The River King's commanding and elegant presence in his magnificent lair overwhelms\
    \ one creature he can see within 120 feet. The target must succeed on a DC 18\
    \ Charisma saving throw or be charmed by the River King until initiative count\
    \ 20 on the next round.  "
  "name": ""
"regional_effects":
- "desc": "The region containing the River King's lair is warped by his magic, which\
    \ creates one or more of the following effects:"
  "name": ""
- "desc": "- Rushing Rapids. The currents of rivers and streams within 3 miles\
    \ of the lair become strong and erratic. Each creature swimming in these rivers\
    \ and streams has disadvantage on Strength ([Athletics](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Athletics))\
    \ checks to swim, unless it has a swimming speed.  \n- Stormy Weather. Rain\
    \ and thunderstorms are common within 6 miles of the lair, and they often build\
    \ to torrential downpours that obscure vision and cause waterways to overflow\
    \ their banks.  \n- Well-Stocked Waterways. Lakes, ponds, rivers, and streams\
    \ within 10 miles of the lair teem with fish and other wildlife.  "
  "name": ""
- "desc": "If the River King dies, these effects fade over the course of 1d10 days."
  "name": ""
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fey/token/river-king-tob1-2023.webp"
```
^statblock

## Environment

forest, planar
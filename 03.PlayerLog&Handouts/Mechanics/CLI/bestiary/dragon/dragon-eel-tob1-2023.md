---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/12
- ttrpg-cli/monster/environment/coastal
- ttrpg-cli/monster/environment/underwater
- ttrpg-cli/monster/size/huge
- ttrpg-cli/monster/type/dragon
statblock: inline
aliases: ["Dragon Eel"]
---
# [Dragon Eel](03 - Player Log & Handouts\Mechanics\CLI\bestiary\dragon/dragon-eel-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 111*  

*This slender aquatic creature sports a powerful single finned tail and wicked jaws like a matched pair of serrated blades.*

Dragon eels are wingless, slender, underwater dragons that vary widely in color from browns and blacks to brilliant iridescent hues in mottled patterns. Though not true dragons or drakes, they are no less fearsome and powerful.

## Fond of Servants

While most dragon eels are solitary and irascible, on rare instances some form pairs or small bands—and some gather humanoid servants.

## Magnetic and Lightning

Dragon eels make their natural homes in twisting underwater cave systems and prefer magnetically-aligned, metallic cavern formations navigable with their refined electric sight. Some dragon eels use their constant electric auras combined with acquired alchemical reagents to electroplate portions of their golden hoard onto the walls of their dwellings.

## Pirate Fleets and Dominions

Dragon eels claim large swaths of shoreline as their demesne. Although neither particularly cruel nor righteous, a dragon eel often lords over awed tribes, allowing locals to revere it as a mighty spirit. Some dragon eels use such tribes as the core of a pirate fleet or raiding parties carried on their backs. Their ability to swim through air during storms adds to their reputation as terrible thunder spirits.

## Bribable

Their deceptive moniker sometimes lulls foolish sailors into a false confidence when they expect to face a simple if dangerous eel beast, but instead find themselves dealing with intelligent draconic kings of the coastal shallows. Wise sailors traveling through known dragon eel territory bring tithes and offerings to placate them.

```statblock
"name": "Dragon Eel (ToB1-2023)"
"size": "Huge"
"type": "dragon"
"alignment": "Neutral"
"ac": !!int "18"
"ac_class": "natural armor"
"hp": !!int "195"
"hit_dice": "17d12 + 85"
"stats":
- !!int "26"
- !!int "12"
- !!int "20"
- !!int "14"
- !!int "13"
- !!int "14"
"speed": "20 ft., swim 60 ft."
"saves":
  "Charisma": !!int "6"
  "Dexterity": !!int "5"
  "Wisdom": !!int "5"
  "Intelligence": !!int "6"
  "Strength": !!int "12"
"skillsaves":
  "Athletics": !!int "12"
  "Insight": !!int "5"
  "Perception": !!int "5"
  "Acrobatics": !!int "5"
"damage_immunities": "lightning"
"condition_immunities": "[paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)"
"senses": "darkvision 60 ft., passive Perception 15"
"languages": "Common, Draconic, Primordial"
"cr": "12"
"traits":
- "desc": "The dragon eel can breathe air and water, but it needs to be submerged\
    \ at least once every 6 hours to avoid suffocating."
  "name": "Limited Amphibiousness"
- "desc": "A creature that touches the dragon eel or hits it with a melee attack while\
    \ within 5 feet of it takes 5 (1d10) lightning damage."
  "name": "Shocking Hide"
- "desc": "During storms with ample rain or lightning, the dragon eel gains a flying\
    \ speed equal to its swimming speed."
  "name": "Storm Glide"
"actions":
- "desc": "The dragon eel makes one Bite attack and one Tail Slap attack."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +12 to hit, reach 10 ft., one target. Hit: 26\
    \ (4d8 + 8) piercing damage plus 5 (1d10) lightning damage, and the target\
    \ must succeed on a DC 18 Constitution saving throw or become [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed)\
    \ for 1 minute. The target can repeat the saving throw at the end of each of its\
    \ turns, ending the effect on itself on a success."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +12 to hit, reach 10 ft., one target. Hit: 30\
    \ (5d8 + 8) bludgeoning damage plus 5 (1d10) lightning damage, and the target\
    \ must succeed on a DC 18 Strength saving throw or be pushed up to 10 feet away\
    \ from the eel. The dragon eel can choose to not push a target."
  "name": "Tail Slap"
- "desc": "The dragon eel exhales lightning in a 60-foot line that is 5 feet wide.\
    \ Each target in that line must make a DC 18 Dexterity saving throw, taking 55\
    \ (10d10) lightning damage on a failed save, or half as much damage on a successful\
    \ one."
  "name": "Lightning Breath (Recharge 6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/dragon/token/dragon-eel-tob1-2023.webp"
```
^statblock

## Environment

coastal, underwater
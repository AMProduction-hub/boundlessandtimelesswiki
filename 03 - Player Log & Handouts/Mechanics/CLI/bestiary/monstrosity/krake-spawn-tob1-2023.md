---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/14
- ttrpg-cli/monster/environment/arctic
- ttrpg-cli/monster/environment/underwater
- ttrpg-cli/monster/size/huge
- ttrpg-cli/monster/type/monstrosity
statblock: inline
aliases: ["Krake Spawn"]
---
# [Krake Spawn](03 - Player Log & Handouts\Mechanics\CLI\bestiary\monstrosity/krake-spawn-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 249*  

*This twisted, beast looks like the unholy union of squid and spider. Its shell-covered core has six small rubbery legs, peculiar antennae, and six tentacles around a squid's enormous beak.*

## Demonic Crossbreeds

Some believe krake spawn are demonic crossbreeds created by the aboleth, fusing kraken blood with demonic souls. Others say that krake spawn are the horrible creation of a long-forgotten meddling god, summoned to the mortal world by deep ones. Certainly, krake spawn respond to summoning magic, and spellcasters summon krake spawn through blood sacrifices to work evil in the world. However, they do so at considerable peril: unlike demons and devils, krake spawn are seldom bound by pacts of any kind.

## Outwit Humans

Though enormous and carrying an armored green shell on their six spindly legs, krake spawn are surprisingly quick and agile. Worse, they have a malicious and bloodthirsty intellect. A krake spawn is considerably smarter than most humans, who often mistake them for dumb beasts—an error that can often prove fatal.

## Iceberg Fortresses

Krake spawn live in remote, icy regions, where they fashion elaborate iceberg fortresses. These fortresses are stocked with frozen creatures (an emergency food supply), the krake spawn's treasure and library, slaves or prisoners of many races, and a hellish nest filled with the krake spawn's offspring.

```statblock
"name": "Krake Spawn (ToB1-2023)"
"size": "Huge"
"type": "monstrosity"
"alignment": "Neutral Evil"
"ac": !!int "16"
"ac_class": "natural armor"
"hp": !!int "175"
"hit_dice": "14d12 + 84"
"stats":
- !!int "24"
- !!int "12"
- !!int "22"
- !!int "17"
- !!int "15"
- !!int "18"
"speed": "20 ft., swim 60 ft."
"saves":
  "Charisma": !!int "9"
  "Intelligence": !!int "8"
  "Strength": !!int "12"
  "Constitution": !!int "11"
"damage_immunities": "cold, poison, psychic"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "blindsight 60 ft., darkvision 120 ft., passive Perception 12"
"languages": "Common, Infernal, Primordial, Void Speech"
"cr": "14"
"traits":
- "desc": "The krake spawn can breathe air and water."
  "name": "Amphibious"
"actions":
- "desc": "The krake spawn makes one Bite attack and eight Tentacle attacks, or it\
    \ makes four Freezing Water Bolt attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +12 to hit, reach 10 ft, one target. Hit: 12\
    \ (1d10 + 7) slashing damage."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +12 to hit, reach 15 ft., one target. Hit: 10\
    \ (1d6 + 7) bludgeoning damage. If the target is a Large or smaller creature,\
    \ it is [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ (escape DC 17). Until this grapple ends, the target is [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained).\
    \ The krake spawn has eight tentacles, each of which can grapple only one target."
  "name": "Tentacle"
- "desc": "Ranged Spell Attack: +9 to hit, range 60 ft., one target. Hit: 13\
    \ (2d8 + 4) bludgeoning damage plus 10 (3d6) cold damage."
  "name": "Freezing Water Bolt"
- "desc": "While underwater, the krake spawn emits a 20-foot-radius cloud of ink all\
    \ around itself. Each creature in the cloud must make a DC 17 Constitution saving\
    \ throw, taking 55 (10d10) poison damage on a failed save, or half as much damage\
    \ on a successful one. The area is heavily obscured for 1 minute, although a significant\
    \ current can disperse the ink."
  "name": "Ink Cloud (Recharge 5-6)"
- "desc": "The krake spawn sprays half‑digested food from its maw in a 30-foot cone.\
    \ Each creature in the area must make a DC 17 Dexterity saving throw. On a failure,\
    \ a creature takes 27 (6d8) acid damage plus 27 (5d10) poison damage and is\
    \ [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated).\
    \ On a success, a creature takes half the damage and isn't [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated)."
  "name": "Vomit Forth the Deeps (Recharge 5-6)"
"bonus_actions":
- "desc": "Each creature within 5 feet of the krake spawn must succeed on a DC 17\
    \ Dexterity saving throw or be knocked [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone).\
    \ The spawn then swims up to half its swimming speed without provoking opportunity\
    \ attacks. The spawn must be underwater to use this bonus action."
  "name": "Water Jet"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/monstrosity/token/krake-spawn-tob1-2023.webp"
```
^statblock

## Environment

arctic, underwater
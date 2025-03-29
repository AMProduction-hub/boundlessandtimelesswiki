---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/4
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/size/tiny
- ttrpg-cli/monster/type/celestial
statblock: inline
aliases: ["Ratatosk"]
---
# [Ratatosk](03 - Player Log & Handouts\Mechanics\CLI\bestiary\celestial/ratatosk-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 301*  

*The chattering squirrel creature has tiny tusks and fur that shimmers in a way that defies the surrounding light.*

## Sleek-Furred Celestials

The ratatosk is a celestial being that is very much convinced of its own indispensable place in the multiverse. Its fur is sleek, and it takes great pride in the cleaning and maintenance of its tusks.

## Planar Messengers

Ratatosks were created to carry messages across the planes, bearing word between gods and their servants. Somewhere across the vast march of ages, their nature twisted away from that purpose. Much speculation as to the exact cause of this change continues to occupy sages.

## Maddening Gossips

Ratatosks are insatiable tricksters. Their constant chatter is not the mere nattering of their animal counterparts; it is a never-ending celestial gossip network. Ratatosks delight in learning secrets and spreading those secrets in mischievous ways. It's common for two listeners to hear vastly different words when a ratatosk speaks—and for that misunderstanding to lead to blows.

```statblock
"name": "Ratatosk (ToB1-2023)"
"size": "Tiny"
"type": "celestial"
"alignment": "Chaotic Neutral"
"ac": !!int "14"
"hp": !!int "42"
"hit_dice": "12d4 + 12"
"stats":
- !!int "4"
- !!int "18"
- !!int "12"
- !!int "17"
- !!int "10"
- !!int "18"
"speed": "20 ft., climb 20 ft."
"saves":
  "Charisma": !!int "6"
  "Wisdom": !!int "2"
"skillsaves":
  "Deception": !!int "6"
  "Stealth": !!int "6"
  "Persuasion": !!int "6"
"damage_resistances": "bludgeoning, piercing, slashing from nonmagical attacks"
"senses": "darkvision 60 ft., passive Perception 10"
"languages": "Celestial, Common, telepathy 100 ft."
"cr": "4"
"traits":
- "desc": "The ratatosk casts one of the following spells, requiring no material or\
    \ somatic components and using Charisma as the spellcasting ability (save DC 14):\n\
    \nAt will: [animal messenger](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/animal-messenger.md),\
    \ [message](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/message.md)\n\
    \n1/day: [commune](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/commune.md)\
    \ (as an action)\n\n3/day each: [sending](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/sending.md),\
    \ [suggestion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/suggestion.md)"
  "name": "Spellcasting"
- "desc": "The ratatosk has advantage on saving throws against spells and other magical\
    \ effects."
  "name": "Magic Resistance"
"actions":
- "desc": "The ratatosk makes two Gore or Annoying Chitter attacks. It can replace\
    \ one attack with a use of Divisive Chatter, if available."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 6 (1d4\
    \ + 4) piercing damage plus 7 (2d6) psychic damage."
  "name": "Gore"
- "desc": "Ranged Spell Attack: +6 to hit, range 60 ft., one target. Hit: 14\
    \ (3d6 + 4) psychic damage."
  "name": "Annoying Chitter"
- "desc": "The ratatosk causes division and strife in up to four creatures it can\
    \ see within 30 feet of it. Each target must succeed on a DC 14 Charisma saving\
    \ throw or be irritated for 1 minute. While irritated, a creature must spend its\
    \ action on each of its turns arguing with, complaining about, or otherwise expressing\
    \ unhappiness toward one of its allies over a trivial matter. The creature can\
    \ repeat the saving throw at the end of each of its turns, ending the effect on\
    \ itself on a success."
  "name": "Divisive Chatter (Recharge 5-6)"
"bonus_actions":
- "desc": "The ratatosk takes the Dash, Disengage, or Hide action."
  "name": "Skitter"
"reactions":
- "desc": "When a creature the ratatosk can see targets it with an attack, the ratatosk\
    \ tells a lie while pointing to another creature within 5 feet of it. The attacker\
    \ must succeed on a DC 14 Wisdom saving throw or believe the lie and attack the\
    \ other creature instead."
  "name": "Desperate Lies"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/celestial/token/ratatosk-tob1-2023.webp"
```
^statblock

## Environment

planar
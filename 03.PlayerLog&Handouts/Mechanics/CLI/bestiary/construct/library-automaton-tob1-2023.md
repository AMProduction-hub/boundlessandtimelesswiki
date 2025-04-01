---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/1-2
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/small
- ttrpg-cli/monster/type/construct
statblock: inline
aliases: ["Library Automaton"]
---
# [Library Automaton](03 - Player Log & Handouts\Mechanics\CLI\bestiary\construct/library-automaton-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 252*  

*The humming of servos, ticking of gears, and petite discharges of steam precede the library's diminutive custodian.*

Library automatons are small constructs created to fulfill organizational responsibilities of huge libraries.

## Eyes of the Past

Each automaton includes a single humanoid eyeball mounted at the end of an articulated appendage. These eyes are typically donations from the library's ailing scholars, allow them to continue serving the repositories of knowledge that were their life's work.

## Telekinetic

The automatons can move and manipulate written materials telekinetically, and they can store such works in an extradimensional space within their bodies. The library automaton tirelessly pores through tomes, translates ancient texts, catalogs the institution's volumes, fetches texts for visitors, and occasionally rids the vast halls of uninvited pests.

## Scholarly Familiars

Many spellcasters have discovered library automatons make particularly effective caretakers for their spellbooks and scrolls while on adventure.

> [!note] Library Automaton Familiars
> 
> The library automaton's scholarly nature leads some of them to serve spellcasters and learn more of the world. Such automatons have the following trait.
> 
> **Familiar.** The library automaton can serve another creature as a familiar, forming a magic, telepathic bond with that willing companion. While the two are bonded, the companion can sense what the automaton senses as long as they are within 1 mile of each other. While the automaton is within 10 feet of its companion, the companion has resistance to psychic damage. At any time and for any reason, the automaton can end its service as a familiar, ending the telepathic bond.
^library-automaton-familiars

```statblock
"name": "Library Automaton (ToB1-2023)"
"size": "Small"
"type": "construct"
"alignment": "Lawful Neutral"
"ac": !!int "13"
"ac_class": "natural armor"
"hp": !!int "24"
"hit_dice": "7d6"
"stats":
- !!int "8"
- !!int "13"
- !!int "10"
- !!int "16"
- !!int "12"
- !!int "8"
"speed": "30 ft."
"skillsaves":
  "Investigation": !!int "5"
  "History": !!int "5"
"damage_immunities": "poison, psychic"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [petrified](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Petrified),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "blindsight 60 ft., truesight 10 ft., passive Perception 11"
"languages": "Common"
"cr": "1/2"
"traits":
- "desc": "The library automaton understands any written language it can see, provided\
    \ it is touching the surface on which the words are written."
  "name": "Bibliophile"
- "desc": "The library automaton is surrounded by an [invisible](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Invisible),\
    \ shapeless, magical force that can perform simple tasks at the automaton's command.\
    \ This force has a Strength equal to the automaton's Strength, and it can interact\
    \ with objects up to 15 feet away from the automaton. The automaton can use this\
    \ force to perform simple tasks that a Small humanoid with two hands could do,\
    \ such as opening a door, moving a bookshelf's ladder, picking up and organizing\
    \ books, and similar tasks. The automaton can't use this force to make attacks\
    \ or wield a weapon or shield."
  "name": "Bibliotelekinesis"
- "desc": "The library automaton's body contains a small, extradimensional space.\
    \ This space can hold up to 100 pounds of Small or smaller objects. This space\
    \ can hold only books, scrolls, parchment, or other written works on paper or\
    \ other paper- or wood-like materials. The automaton is the only creature capable\
    \ of retrieving items from this space while it is alive. If the automaton is destroyed,\
    \ the objects within its extradimensional space are ejected into an unoccupied\
    \ space nearest it."
  "name": "Book Safekeeper"
- "desc": "The library automaton doesn't require air, food, drink, or sleep."
  "name": "Construct Nature"
"actions":
- "desc": "Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 6 (2d4\
    \ + 1) bludgeoning damage."
  "name": "Piston-Powered Kick"
- "desc": "Ranged Spell Attack: +5 to hit, range 60 ft., one target. Hit: 6\
    \ (1d6 + 3) psychic damage, and the target must succeed on a DC 13 Wisdom saving\
    \ throw or have disadvantage on the next attack roll, ability check, or saving\
    \ throw it makes before the start of the automaton's next turn."
  "name": "Unnerving Gaze"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/construct/token/library-automaton-tob1-2023.webp"
```
^statblock

## Environment

urban
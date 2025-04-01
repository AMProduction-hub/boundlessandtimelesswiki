---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/13
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/undead
statblock: inline
aliases: ["Mask Wight"]
---
# [Mask Wight](03 - Player Log & Handouts\Mechanics\CLI\bestiary\undead/mask-wight-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 264*  

*The frame of this withered demon's corpse barely fills the ash-colored plate armor that encases it. It carries a khopesh made of violet smoke, and a horned ivory mask devoid of features is nailed to its face.*

## Children of Fiends

Long ago, a demon lord of shadow fell in love with a demon goddess of the underworld. The two devised a plan to not merely slay their peers, but expunge them from time itself, leaving only each other. Shortly thereafter, the mask wights were conceived.

## Rites of Annihilation

To create these undead, the lovers stole bodies of death knights from beneath the necropolis of an arch-lich and sacrificed a million condemned souls, draining their essence into ivory masks. Finally, the masks were hammered onto the knights with cold iron nails, and their armored husks were left at the bottom of the memory-draining River Styx for 600 years. When they rose, the mask wights marched out into the planes to bury knowledge and erase their quarry from memory and history.

```statblock
"name": "Mask Wight (ToB1-2023)"
"size": "Medium"
"type": "undead"
"alignment": "Neutral Evil"
"ac": !!int "19"
"ac_class": "natural armor"
"hp": !!int "207"
"hit_dice": "18d8 + 126"
"stats":
- !!int "22"
- !!int "18"
- !!int "24"
- !!int "15"
- !!int "16"
- !!int "18"
"speed": "40 ft."
"saves":
  "Charisma": !!int "9"
  "Dexterity": !!int "9"
  "Wisdom": !!int "8"
  "Intelligence": !!int "7"
  "Strength": !!int "11"
  "Constitution": !!int "12"
"damage_vulnerabilities": "radiant"
"damage_resistances": "acid; cold; fire; lightning; bludgeoning, piercing, slashing\
  \ from nonmagical attacks"
"damage_immunities": "necrotic, poison"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [petrified](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Petrified),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned),\
  \ [stunned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Stunned),\
  \ [unconscious](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Unconscious)"
"senses": "darkvision 60 ft., truesight 30 ft., passive Perception 13"
"languages": "Abyssal, Common, Infernal"
"cr": "13"
"traits":
- "desc": "The mask wight's weapon attacks are magical. When the mask wight hits with\
    \ any weapon, the weapon deals an extra 3d8 necrotic damage (included in the\
    \ attack)."
  "name": "Necrotic Weapons"
- "desc": "The mask wight has advantage on attack rolls against fiends and creatures\
    \ wielding fiendish power, such as tieflings or some sorcerers and warlocks."
  "name": "Single-Minded Purpose"
- "desc": "The mask wight doesn't require air, food, drink, or sleep."
  "name": "Undead Nature"
"actions":
- "desc": "The mask wight makes two Khopesh of Oblivion attacks and one Spiked Gauntlet\
    \ attack. If both Khopesh of Oblivion attacks hit one creature, the target must\
    \ succeed on a DC 17 Wisdom saving throw or forget cherished memories of one object\
    \ or location until it interacts with that object or location again. The object\
    \ or location can't be an object on the target or a location within its sight\
    \ when it fails this saving throw."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +11 to hit, reach 5 ft., one target. Hit: 15\
    \ (2d8 + 6) slashing damage plus 13 (3d8) necrotic damage."
  "name": "Khopesh of Oblivion"
- "desc": "Melee Weapon Attack: +11 to hit, reach 5 ft., one target. Hit: 13\
    \ (2d6 + 6) bludgeoning damage plus 13 (3d8) necrotic damage. If the target\
    \ is a Large or smaller creature, it must succeed on a DC 17 Strength saving throw\
    \ or be knocked [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)."
  "name": "Spiked Gauntlet"
- "desc": "The mask wight emits an ear‑piercing wail. Each creature within 30 feet\
    \ of the mask wight must make a DC 17 Charisma saving throw. On a failure, a creature\
    \ takes 35 (10d6) thunder damage and 27 (6d8) psychic damage and is [deafened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Deafened)\
    \ for 1 hour. On a success, a creature takes half the damage and isn't [deafened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Deafened).\
    \ A creature killed by this wail is erased from the memories of every creature\
    \ in the planes that ever saw or interacted with it, all written or pictorial\
    \ references to the target fade away, and its body is obliterated. Only divine\
    \ beings and creatures that saw the creature die are unaffected by this memory\
    \ erasure. The slain creature can be restored to life only by means of a true\
    \ resurrection or a [wish](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/wish.md)\
    \ spell."
  "name": "Wail of the Forgotten (Recharge 6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/undead/token/mask-wight-tob1-2023.webp"
```
^statblock

## Environment

planar
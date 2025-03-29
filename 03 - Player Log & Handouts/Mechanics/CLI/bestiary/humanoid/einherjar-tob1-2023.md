---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/7
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/humanoid
statblock: inline
aliases: ["Einherjar"]
---
# [Einherjar](03 - Player Log & Handouts\Mechanics\CLI\bestiary\humanoid/einherjar-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 156*  

*A line of stout, bearded warriors with golden auras stand ready, adorned in chain mail and carrying battle axes and oaken shields. Their badges and symbols are all different, and no two have the same braided pattern in their beards.*

The einherjar are great warriors chosen by the valkyries. They eat and drink their fill of boar and mead each night, then spend their days preparing for Ragnarok. Some of this is combat training, and other portions are raids against the giants fighting the gods. Regardless of how often they are slain, the einherjar reappear each morning in Odin's hall, leaving them without fear of death.

## Defenders of the Mortal World

Occasionally, ravenfolk guide a troop of einherjar against some of Loki's minions on the Material Plane. These raids are often small battles that further delay the inevitable rise of the world serpent and its many evil spawn. They fight against giants, demons, lindwurms, and other evil creatures, but the einherjar themselves are not exactly saintly. They can drink and carouse with the loudest and most boastful of humanoids. Though otherworldly and servants of Odin, einherjar are very humanlike, if somewhat larger than life.

## Fear Dragons

The einherjar are superstitiously fearful of dragons and dragonkin, the distant progeny of the world serpent.

## Never Speak to the Living

In theory, the einherjar are forbidden from speaking with the living: they must pass their words through a valkyrie, ratatosk, ravenfolk, or one of the other races allied with Odin. In practice, this rule is often flouted, though if Loki's servants notice it, they can dismiss any einherjar back to Valhalla for a day.

```statblock
"name": "Einherjar (ToB1-2023)"
"size": "Medium"
"type": "humanoid"
"alignment": "Chaotic Neutral"
"ac": !!int "18"
"ac_class": "[chain mail](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/items/chain-mail.md),\
  \ [shield](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/items/shield.md)"
"hp": !!int "119"
"hit_dice": "14d8 + 56"
"stats":
- !!int "19"
- !!int "16"
- !!int "19"
- !!int "10"
- !!int "14"
- !!int "11"
"speed": "30 ft."
"skillsaves":
  "Intimidation": !!int "6"
  "Animal Handling": !!int "5"
  "Perception": !!int "5"
"damage_resistances": "piercing from nonmagical attacks"
"senses": "truesight 60 ft., passive Perception 15"
"languages": "Celestial, Common"
"cr": "7"
"traits":
- "desc": "The einherjar has advantage on all attack rolls it makes while it is below\
    \ 30 hp."
  "name": "Battle Frenzy"
- "desc": "The stare of an einherjar is especially piercing to Humanoids. It has advantage\
    \ on any Charisma ([Intimidation](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Intimidation))\
    \ check it makes against a Humanoid."
  "name": "Fearsome Gaze"
- "desc": "The einherjar's weapon attacks are magical. When the einherjar hits with\
    \ any weapon, the weapon deals an extra 3d8 radiant damage (included in the\
    \ attack)."
  "name": "Runic Weapons"
"actions":
- "desc": "The einherjar makes two Battleaxe attacks, or it makes three Celestial\
    \ Bolt attacks. It can replace one attack with Celestial Blessing, if available."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 8 (1d8\
    \ + 4) slashing damage, or 9 (1d10 + 4) slashing damage if used with two hands,\
    \ plus 13 (3d8) radiant damage."
  "name": "Battleaxe"
- "desc": "Ranged Spell Attack: +5 to hit, range 60 ft., one target. Hit: 15\
    \ (3d8 + 2) radiant damage."
  "name": "Celestial Bolt"
- "desc": "The einherjar calls on its celestial patrons for one of the following blessings:\n\
    \n- Odin's Strength. The einherjar roars a battle prayer to Odin. Each friendly\
    \ creature within 60 feet of the einherjar and that can hear the prayer deals\
    \ an extra 4 (1d8) radiant damage when it hits with any weapon. In addition,\
    \ when an affected creature makes an attack roll, the creature can roll a d6\
    \ and add the number rolled to the attack roll.  \n- Valkyries' Mercy. The\
    \ einherjar pleads for the assistance of the valkyries to save one friendly creature\
    \ it can see within 60 feet of it that has been reduced to 0 hp. The creature\
    \ regains 13 3d8 hp. Once the einherjar has aided a creature with Valkyries'\
    \ Mercy, it can't target that creature with Valkyries' Mercy again until the creature\
    \ finishes a long rest.  "
  "name": "Celestial Blessing (Recharge 5-6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/humanoid/token/einherjar-tob1-2023.webp"
```
^statblock

## Environment

planar
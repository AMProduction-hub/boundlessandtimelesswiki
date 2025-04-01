---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/7
- ttrpg-cli/monster/environment/any
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/undead
statblock: inline
aliases: ["Risen Reaver"]
---
# [Risen Reaver](03 - Player Log & Handouts\Mechanics\CLI\bestiary\undead/risen-reaver-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 309*  

*A body that might once have been human now has four legs and nightmarishly long, thick arms. What's worse, its skin has been flayed off, revealing the dead muscle and sinew beneath.*

## Spirt of War

The risen reaver is an undead creature born from a warrior fallen on the battlefield. Its body becomes an avatar of combat, with four legs and a pair of long, heavy arms. In the process, it sheds its skin, becoming entirely undead muscle, bone, and sinew.

## Absorb Weapons

When risen reavers take form, they absorb all weapons around them. Some of these weapons pierce their bodies, while others become part of the risen reaver's armament. Their four legs are tipped with blades on which they walk like metallic spiders. Their arms are covered in weaponry infused into their flesh, which they use to crush and flay any living creatures they encounter

## Battle Mad

Risen reavers are battle-maddened spirits of vengeance and slaughter, obsessed with the chaos of combat that led to their own death. They hunt the living with the sole purpose of killing, and they thrive on violence and murder. As they died, so should others die.

```statblock
"name": "Risen Reaver (ToB1-2023)"
"size": "Large"
"type": "undead"
"alignment": "Chaotic Evil"
"ac": !!int "15"
"ac_class": "[studded leather](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/items/studded-leather-armor.md)"
"hp": !!int "168"
"hit_dice": "16d10 + 80"
"stats":
- !!int "19"
- !!int "16"
- !!int "20"
- !!int "9"
- !!int "7"
- !!int "6"
"speed": "40 ft."
"saves":
  "Dexterity": !!int "6"
"skillsaves":
  "Perception": !!int "1"
"senses": "darkvision 120 ft., passive Perception 11"
"languages": "the languages it knew in life"
"cr": "7"
"traits":
- "desc": "The risen reaver can pinpoint the location of creatures that aren't Constructs\
    \ or Undead within 60 feet of it and can sense the general direction of such creatures\
    \ within 1 mile of it."
  "name": "Blood Sense"
- "desc": "The risen reaver doesn't require air, food, drink, or sleep."
  "name": "Undead Nature"
"actions":
- "desc": "The risen reaver makes three Bladed Fist attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 15\
    \ (2d10 + 4) slashing damage."
  "name": "Bladed Fist"
"bonus_actions":
- "desc": "The risen reaver takes the Dash action."
  "name": "Skitter"
"reactions":
- "desc": "When the risen reaver is hit with a nonmagical melee weapon or when it\
    \ starts its turn in the same space as a nonmagical melee weapon that isn't being\
    \ worn or carried, it absorbs the weapon into its body. If the weapon is being\
    \ wielded by an attacker, the attacker must succeed on a DC 15 Strength saving\
    \ throw or lose its weapon. For 1 minute, the reaver has resistance to the type\
    \ of damage dealt by that weapon, and when it hits with its Bladed Fist, the fist\
    \ deals an extra 2 1d4 damage of the type dealt by the weapon. The reaver can\
    \ absorb no more than three weapons in this way every 24 hours."
  "name": "Infused Arsenal"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/undead/token/risen-reaver-tob1-2023.webp"
```
^statblock

## Environment

any
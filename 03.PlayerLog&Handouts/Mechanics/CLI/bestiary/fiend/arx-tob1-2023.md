---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/9
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/fiend
statblock: inline
aliases: ["Arx"]
---
# [Arx](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fiend/arx-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 26*  

*This spike-covered insectoid stands at the ready with a wicked spear grasped by two limbs. It decompresses its wings impossibly to fashion a pair of walls behind it, held together and connected to the insectoid by a stretchy pink goo.*

Arxes are fiendish creatures who serve other fiends as mobile field defenses. They can detach their elytra, the hardened shells that cover their wings, to provide cover for commanders who wish to direct their armies from forward lines. They use their telepathy and excellent vision to feed accurate overviews of the battlefield to these leaders, who use this intel to direct troops and make attacks from behind the arx's wall.

## Hirable Mercenaries

When they aren't fighting for legions of devils or demons, arxes willingly accept payment for their services. They are steadfast combatants who reliably follow orders, but they show no concern about individual allies over greater tactical advantages.

```statblock
"name": "Arx (ToB1-2023)"
"size": "Large"
"type": "fiend"
"alignment": "Lawful Evil"
"ac": !!int "17"
"ac_class": "natural armor"
"hp": !!int "171"
"hit_dice": "18d10 + 72"
"stats":
- !!int "20"
- !!int "8"
- !!int "19"
- !!int "11"
- !!int "15"
- !!int "8"
"speed": "30 ft., fly 20 ft."
"saves":
  "Strength": !!int "9"
"skillsaves":
  "Athletics": !!int "9"
  "Perception": !!int "6"
"damage_resistances": "cold, fire, lightning, poison"
"senses": "darkvision 90 ft., passive Perception 16"
"languages": "Abyssal, Infernal, telepathy 60 ft."
"cr": "9"
"traits":
- "desc": "The arx is immune to any spell or effect that would alter its form."
  "name": "Immutable Form"
- "desc": "The arx has advantage on saving throws against spells and other magical\
    \ effects."
  "name": "Magic Resistance"
- "desc": "A creature that touches the arx or hits it with a melee attack while within\
    \ 5 feet of it takes 4 (1d8) piercing damage. This trait also applies to the\
    \ arx's walls."
  "name": "Spiky Hide"
"actions":
- "desc": "The arx makes two Claw attacks and one Spear attack."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 18\
    \ (3d8 + 5) slashing damage."
  "name": "Claw"
- "desc": "Melee or Ranged Weapon Attack: +9 to hit, reach 5 ft. or range 20/60\
    \ ft., one target. Hit: 12 (2d6 + 5) piercing damage, or 14 (2d8 + 5) piercing\
    \ damage if used with two hands to make a melee attack."
  "name": "Spear"
- "desc": "If the arx has its wall set up (see Emplace Wall), it can briefly close\
    \ the panels of the wall in on each other. Each creature other than the arx between\
    \ the panels in a 10-foot cone from the corner where the panels meet must make\
    \ a DC 16 Dexterity saving throw, taking 28 (8d6) bludgeoning damage on a failed\
    \ save, or half as much damage on a successful one."
  "name": "Wall Smash"
"bonus_actions":
- "desc": "The arx extends its hardened elytra and casts them into the ground, creating\
    \ a wall. The wall is 3 inches thick and is composed of two 10-foot-by-10-foot\
    \ panels. The panels must connect perpendicular to each other, forming a corner\
    \ behind the arx. If the wall falls in a creature's space when the arx places\
    \ it, the creature must make a DC 16 Dexterity saving throw. On a failure, the\
    \ creature takes 10 (3d6) bludgeoning damage, and the arx determines to which\
    \ side of the wall the creature is pushed. On a success, the creature takes half\
    \ the damage and decides to which side of the wall it is pushed.\n\nEach 10-foot\
    \ panel has AC 17 and 50 hp. If a panel is destroyed, the arx can place only one\
    \ panel of wall with this bonus action. If both panels are destroyed, the arx\
    \ can't use this bonus action again until it finishes a long rest or until its\
    \ elytra are restored with a [regenerate](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/regenerate.md)\
    \ spell or similar magic.\n\nWhile the arx has at least one wall emplaced, it\
    \ must remain within 15 feet of at least one of its walls. The arx can retract\
    \ the walls into its body, ending this effect, as a bonus action."
  "name": "Emplace Wall (Recharge 3-6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fiend/token/arx-tob1-2023.webp"
```
^statblock

## Environment

planar
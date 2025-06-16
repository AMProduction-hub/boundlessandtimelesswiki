---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/cm
- ttrpg-cli/monster/cr/5
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/humanoid/any-race
statblock: inline
statblock-link: "#^statblock"
aliases:
- Master Sage
---
# [Master Sage](03.PlayerLog&Handouts\Mechanics\CLI\bestiary\humanoid/master-sage-cm.md)
*Source: Candlekeep Mysteries p. 9*  

Candlekeep's resident lore experts are master sages and sages who dedicate themselves to scholarship above all.

```statblock
"name": "Master Sage (CM)"
"size": "Medium"
"type": "humanoid"
"subtype": "any race"
"alignment": "Unaligned"
"ac": !!int "10"
"hp": !!int "54"
"hit_dice": "12d8"
"modifier": !!int "0"
"stats":
  - !!int "8"
  - !!int "10"
  - !!int "10"
  - !!int "20"
  - !!int "18"
  - !!int "11"
"speed": "30 ft."
"skillsaves":
  - "name": "[Arcana](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Arcana)"
    "desc": "+11"
  - "name": "[History](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#History)"
    "desc": "+11"
  - "name": "[Insight](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Insight)"
    "desc": "+7"
  - "name": "[Investigation](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Investigation)"
    "desc": "+11"
  - "name": "[Medicine](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Medicine)"
    "desc": "+10"
  - "name": "[Nature](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Nature)"
    "desc": "+11"
  - "name": "[Religion](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Religion)"
    "desc": "+11"
"senses": "passive Perception 14"
"languages": "Common plus any five languages"
"cr": "5"
"actions":
  - "desc": "Melee Spell Attack: +8 to hit (with advantage if the target is wearing\
      \ armor made of metal), reach 5 ft., one creature. Hit: 13 (3d8) lightning\
      \ damage, and the target can't take reactions until the start of its next turn."
    "name": "Shocking Grasp (Cantrip)"
  - "desc": "The sage creates a fiery explosion centered on a point it can see within\
      \ 150 feet of it. Each creature in a 20-foot-radius sphere centered on that\
      \ point must make a DC 14 Dexterity saving throw, taking 28 (8d6) fire damage\
      \ on a failed save, or half as much damage on a successful one. The fire spreads\
      \ around corners and ignites flammable objects in the area that aren't being\
      \ worn or carried."
    "name": "Fireball (3rd-Level Spell; 3/Day)"
  - "desc": "The sage casts one of the following spells, using Intelligence as the\
      \ spellcasting ability (save DC 14, +6 to hit with spell attacks):\n\nAt\
      \ will: [light](03.PlayerLog&Handouts/Mechanics/CLI/spells/light.md), [mage\
      \ hand](03.PlayerLog&Handouts/Mechanics/CLI/spells/mage-hand.md), [mending](03.PlayerLog&Handouts/Mechanics/CLI/spells/mending.md),\
      \ [prestidigitation](03.PlayerLog&Handouts/Mechanics/CLI/spells/prestidigitation.md)\n\
      \n3/day each: [comprehend languages](03.PlayerLog&Handouts/Mechanics/CLI/spells/comprehend-languages.md),\
      \ [detect magic](03.PlayerLog&Handouts/Mechanics/CLI/spells/detect-magic.md),\
      \ [dispel magic](03.PlayerLog&Handouts/Mechanics/CLI/spells/dispel-magic.md),\
      \ [identify](03.PlayerLog&Handouts/Mechanics/CLI/spells/identify.md), [levitate](03.PlayerLog&Handouts/Mechanics/CLI/spells/levitate.md),\
      \ [locate object](03.PlayerLog&Handouts/Mechanics/CLI/spells/locate-object.md),\
      \ [Tenser's Floating Disk](03.PlayerLog&Handouts/Mechanics/CLI/spells/tensers-floating-disk.md),\
      \ [unseen servant](03.PlayerLog&Handouts/Mechanics/CLI/spells/unseen-servant.md)\n\
      \n1/day each: [banishment](03.PlayerLog&Handouts/Mechanics/CLI/spells/banishment.md),\
      \ [contact other plane](03.PlayerLog&Handouts/Mechanics/CLI/spells/contact-other-plane.md),\
      \ [Drawmij's instant summons](03.PlayerLog&Handouts/Mechanics/CLI/spells/drawmijs-instant-summons.md),\
      \ [legend lore](03.PlayerLog&Handouts/Mechanics/CLI/spells/legend-lore.md),\
      \ [locate creature](03.PlayerLog&Handouts/Mechanics/CLI/spells/locate-creature.md),\
      \ [planar binding](03.PlayerLog&Handouts/Mechanics/CLI/spells/planar-binding.md),\
      \ [polymorph](03.PlayerLog&Handouts/Mechanics/CLI/spells/polymorph.md), [protection\
      \ from evil and good](03.PlayerLog&Handouts/Mechanics/CLI/spells/protection-from-evil-and-good.md),\
      \ [scrying](03.PlayerLog&Handouts/Mechanics/CLI/spells/scrying.md), [sending](03.PlayerLog&Handouts/Mechanics/CLI/spells/sending.md),\
      \ [true seeing](03.PlayerLog&Handouts/Mechanics/CLI/spells/true-seeing.md)"
    "name": "Spellcasting"
"reactions":
  - "desc": "When the sage is hit by an attack or targeted by a [magic missile](03.PlayerLog&Handouts/Mechanics/CLI/spells/magic-missile.md)\
      \ spell, it calls forth an [invisible](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Invisible)\
      \ barrier of magical force that protects it. Until the start of its next turn,\
      \ the sage has a +5 bonus to AC, including against the triggering attack, and\
      \ it takes no damage from magic missile."
    "name": "Shield (1st-Level Spell; 3/Day)"
"source":
  - "CM"
"image": "03.PlayerLog&Handouts/Mechanics/CLI/bestiary/humanoid/token/master-sage-cm.webp"
```
^statblock
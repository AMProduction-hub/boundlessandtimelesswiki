---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/ggr
- ttrpg-cli/monster/cr/26
- ttrpg-cli/monster/size/gargantuan
- ttrpg-cli/monster/type/dragon
statblock: inline
statblock-link: "#^statblock"
aliases:
- Niv-Mizzet
---
# [Niv-Mizzet](03.PlayerLog&Handouts\Mechanics\CLI\bestiary\npc/niv-mizzet-ggr.md)
*Source: Guildmasters' Guide to Ravnica p. 241*  

Possessed of arrogance and vanity that matches his vast intellect and tremendous power, Niv-Mizzet is the ancient dragon who founded and continues to control the Izzet League. From his private laboratory at the top of the Izzet guildhall, Niv-Mizzet directs the research and experiments of his countless underlings. He coordinates a tremendous number of apparently unrelated projects, working toward some mysterious end.

There can be little doubt that this ancient dragon is one of the most intelligent beings on Ravnica and one of the world's most powerful spellcasters. He is just as acquisitive as any dragon, but his treasure is scientific and magical knowledge. His ambition is a looming threat in the minds of all the other guildmasters, but confronting him directly is almost unthinkable thanks to the combination of his awesome magical power and the sheer physical threat of a fire-breathing, swordtoothed dragon.

```statblock
"name": "Niv-Mizzet (GGR)"
"size": "Gargantuan"
"type": "dragon"
"alignment": "Chaotic Neutral"
"ac": !!int "22"
"ac_class": "natural armor"
"hp": !!int "370"
"hit_dice": "19d20 + 171"
"modifier": !!int "2"
"stats":
  - !!int "29"
  - !!int "14"
  - !!int "29"
  - !!int "30"
  - !!int "17"
  - !!int "25"
"speed": "40 ft., climb 30 ft., fly 80 ft."
"saves":
  - "constitution": "+17"
  - "intelligence": "+18"
  - "wisdom": "+11"
"skillsaves":
  - "name": "[Arcana](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Arcana)"
    "desc": "+18"
  - "name": "[Insight](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Insight)"
    "desc": "+11"
  - "name": "[Perception](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Perception)"
    "desc": "+11"
"damage_resistances": "cold, psychic, thunder"
"damage_immunities": "fire, lightning"
"condition_immunities": "[charmed](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Charmed)"
"senses": "blindsight 60 ft., darkvision 120 ft., passive Perception 21"
"languages": "Common, Draconic"
"cr": "26"
"traits":
  - "desc": "Niv-Mizzet is a 20th-level Izzet spellcaster. His spellcasting ability\
      \ is Intelligence (spell save DC 26, +18 to hit with spell attacks). He has\
      \ the following wizard spells prepared:\n\nCantrips (at will): [fire bolt](03.PlayerLog&Handouts/Mechanics/CLI/spells/fire-bolt.md),\
      \ [light](03.PlayerLog&Handouts/Mechanics/CLI/spells/light.md), [prestidigitation](03.PlayerLog&Handouts/Mechanics/CLI/spells/prestidigitation.md),\
      \ [ray of frost](03.PlayerLog&Handouts/Mechanics/CLI/spells/ray-of-frost.md),\
      \ [shocking grasp](03.PlayerLog&Handouts/Mechanics/CLI/spells/shocking-grasp.md)\n\
      \n1st level (4 slots): [detect magic](03.PlayerLog&Handouts/Mechanics/CLI/spells/detect-magic.md),\
      \ [magic missile](03.PlayerLog&Handouts/Mechanics/CLI/spells/magic-missile.md),\
      \ [shield](03.PlayerLog&Handouts/Mechanics/CLI/spells/shield.md), [thunderwave](03.PlayerLog&Handouts/Mechanics/CLI/spells/thunderwave.md),\
      \ [unseen servant](03.PlayerLog&Handouts/Mechanics/CLI/spells/unseen-servant.md)\n\
      \n2nd level (3 slots): [blur](03.PlayerLog&Handouts/Mechanics/CLI/spells/blur.md),\
      \ [enlarge/reduce](03.PlayerLog&Handouts/Mechanics/CLI/spells/enlarge-reduce.md),\
      \ [flaming sphere](03.PlayerLog&Handouts/Mechanics/CLI/spells/flaming-sphere.md),\
      \ [hold person](03.PlayerLog&Handouts/Mechanics/CLI/spells/hold-person.md),\
      \ [scorching ray](03.PlayerLog&Handouts/Mechanics/CLI/spells/scorching-ray.md)\n\
      \n3rd level (3 slots): [counterspell](03.PlayerLog&Handouts/Mechanics/CLI/spells/counterspell.md),\
      \ [fireball](03.PlayerLog&Handouts/Mechanics/CLI/spells/fireball.md), [lightning\
      \ bolt](03.PlayerLog&Handouts/Mechanics/CLI/spells/lightning-bolt.md), [slow](03.PlayerLog&Handouts/Mechanics/CLI/spells/slow.md)\n\
      \n4th level (3 slots): [confusion](03.PlayerLog&Handouts/Mechanics/CLI/spells/confusion.md),\
      \ [dimension door](03.PlayerLog&Handouts/Mechanics/CLI/spells/dimension-door.md),\
      \ [fabricate](03.PlayerLog&Handouts/Mechanics/CLI/spells/fabricate.md)\n\n5th\
      \ level (2 slots): [conjure elemental](03.PlayerLog&Handouts/Mechanics/CLI/spells/conjure-elemental.md),\
      \ [polymorph](03.PlayerLog&Handouts/Mechanics/CLI/spells/polymorph.md), [wall\
      \ of fire](03.PlayerLog&Handouts/Mechanics/CLI/spells/wall-of-fire.md), [wall\
      \ of force](03.PlayerLog&Handouts/Mechanics/CLI/spells/wall-of-force.md)\n\n\
      6th level (1 slots): [chain lightning](03.PlayerLog&Handouts/Mechanics/CLI/spells/chain-lightning.md),\
      \ [disintegrate](03.PlayerLog&Handouts/Mechanics/CLI/spells/disintegrate.md),\
      \ [true seeing](03.PlayerLog&Handouts/Mechanics/CLI/spells/true-seeing.md)\n\
      \n7th level (1 slots): [project image](03.PlayerLog&Handouts/Mechanics/CLI/spells/project-image.md),\
      \ [reverse gravity](03.PlayerLog&Handouts/Mechanics/CLI/spells/reverse-gravity.md),\
      \ [teleport](03.PlayerLog&Handouts/Mechanics/CLI/spells/teleport.md)\n\n8th\
      \ level (1 slots): [control weather](03.PlayerLog&Handouts/Mechanics/CLI/spells/control-weather.md),\
      \ [maze](03.PlayerLog&Handouts/Mechanics/CLI/spells/maze.md), [power word stun](03.PlayerLog&Handouts/Mechanics/CLI/spells/power-word-stun.md)\n\
      \n9th level (1 slots): [prismatic wall](03.PlayerLog&Handouts/Mechanics/CLI/spells/prismatic-wall.md)"
    "name": "Spellcasting"
  - "desc": "If Niv-Mizzet fails a saving throw, he can choose to succeed instead."
    "name": "Legendary Resistance (3/Day)"
  - "desc": "Niv-Mizzet can maintain [concentration](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Concentration)\
      \ on two different spells at the same time. In addition, he has advantage on\
      \ saving throws to maintain [concentration](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Concentration)\
      \ on spells."
    "name": "Locus of the Firemind"
  - "desc": "Niv-Mizzet has advantage on saving throws against spells and other magical\
      \ effects."
    "name": "Magic Resistance"
  - "desc": "When Niv-Mizzet casts a spell that deals damage, he can change the spell's\
      \ damage to cold, fire, force, lightning, or thunder."
    "name": "Master Chemister"
"actions":
  - "desc": "Niv-Mizzet makes three attacks: one with his bite and two with his claws."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +17 to hit, reach 15 ft., one target. Hit:\
      \ 18 (2d8 + 9) piercing damage plus 14 (4d6) fire damage."
    "name": "Bite"
  - "desc": "Melee Weapon Attack: +17 to hit, reach 10 ft., one target. Hit:\
      \ 14 (2d4 + 9) slashing damage."
    "name": "Claw"
  - "desc": "Melee Weapon Attack: +17 to hit, reach 20 ft., one target. Hit:\
      \ 16 (2d6 + 9) bludgeoning damage."
    "name": "Tail"
  - "desc": "Niv-Mizzet exhales fire in a 90-foot cone. Each creature in that area\
      \ must make a DC 25 Dexterity saving throw, taking 91 (26d6) fire damage on\
      \ a failed save, or half as much damage on a successful one."
    "name": "Fire Breath (Recharge 5-6)"
"legendary_actions":
  - "desc": "Niv-Mizzet casts one of his cantrips."
    "name": "Cantrip"
  - "desc": "Niv-Mizzet makes a tail attack."
    "name": "Tail Attack"
  - "desc": "Niv-Mizzet beats his wings. Each creature within 15 feet of him must\
      \ succeed on a DC 25 Dexterity saving throw or take 14 (2d4 + 9) bludgeoning\
      \ damage and be knocked [prone](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Prone).\
      \ Niv-Mizzet can then fly up to half his flying speed."
    "name": "Wing Attack (Costs 2 Actions)"
  - "desc": "Niv-Mizzet regains a spell slot of 3rd level or lower."
    "name": "Dracogenius (Costs 3 Actions)"
"source":
  - "GGR"
"image": "03.PlayerLog&Handouts/Mechanics/CLI/bestiary/npc/token/niv-mizzet-ggr.webp"
```
^statblock
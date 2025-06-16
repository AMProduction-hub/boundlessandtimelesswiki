---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/toa
- ttrpg-cli/monster/cr/23
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/undead
statblock: inline
statblock-link: "#^statblock"
aliases:
- Acererak
---
# [Acererak](03.PlayerLog&Handouts\Mechanics\CLI\bestiary\npc/acererak-toa.md)
*Source: Tomb of Annihilation p. 209*  

Acererak is an archlich who travels between worlds and is known to take sick pleasure in devouring the souls of adventurers, whom he lures into trap-ridden dungeons where they suffer horrible deaths. One such dungeon lies under the lost city of Omu. This dungeon is called the Tomb of the Nine Gods, for Acererak slew nine false gods and sealed them within it. More recently, he built a necromantic device called the Soulmonger, then hid it in the heart of the tomb.

## Acererak's Traits

### Ideal

"Why be a god when I can be a creator of gods?"

### Bond

"I build dungeons to trap and slay powerful adventurers. Their deaths and souls are my nourishment."

### Flaw

"I underestimate the resolve of my enemies."

```statblock
"name": "Acererak (ToA)"
"size": "Medium"
"type": "undead"
"alignment": "Neutral Evil"
"ac": !!int "21"
"ac_class": "natural armor"
"hp": !!int "285"
"hit_dice": "30d8 + 150"
"modifier": !!int "3"
"stats":
  - !!int "13"
  - !!int "16"
  - !!int "20"
  - !!int "27"
  - !!int "21"
  - !!int "20"
"speed": "30 ft."
"saves":
  - "constitution": "+12"
  - "intelligence": "+15"
  - "wisdom": "+12"
"skillsaves":
  - "name": "[Arcana](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Arcana)"
    "desc": "+22"
  - "name": "[History](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#History)"
    "desc": "+22"
  - "name": "[Insight](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Insight)"
    "desc": "+12"
  - "name": "[Perception](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Perception)"
    "desc": "+12"
"damage_resistances": "cold, lightning"
"damage_immunities": "necrotic; poison; bludgeoning, piercing, slashing from nonmagical\
  \ attacks"
"condition_immunities": "[blinded](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Blinded),\
  \ [charmed](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Charmed), [deafened](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Deafened),\
  \ [exhaustion](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [frightened](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [paralyzed](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [petrified](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Petrified),\
  \ [poisoned](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Poisoned),\
  \ [stunned](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Stunned)"
"senses": "truesight 120 ft., passive Perception 22"
"languages": "Abyssal, Common, Draconic, Dwarvish, Elvish, Giant, Infernal, Primordial,\
  \ Undercommon"
"cr": "23"
"traits":
  - "desc": "Acererak is a 20th-level spellcaster. His spellcasting ability is Intelligence\
      \ (spell save DC 23, +15 to hit with spell attacks). Acererak has the following\
      \ wizard spells prepared:\n\nCantrips (at will): [mage hand](03.PlayerLog&Handouts/Mechanics/CLI/spells/mage-hand.md),\
      \ [ray of frost](03.PlayerLog&Handouts/Mechanics/CLI/spells/ray-of-frost.md),\
      \ [shocking grasp](03.PlayerLog&Handouts/Mechanics/CLI/spells/shocking-grasp.md)\n\
      \n1st level: [ray of sickness](03.PlayerLog&Handouts/Mechanics/CLI/spells/ray-of-sickness.md),\
      \ [shield](03.PlayerLog&Handouts/Mechanics/CLI/spells/shield.md)\n\n2nd level:\
      \ [arcane lock](03.PlayerLog&Handouts/Mechanics/CLI/spells/arcane-lock.md),\
      \ [knock](03.PlayerLog&Handouts/Mechanics/CLI/spells/knock.md)\n\n3rd level:\
      \ [animate dead](03.PlayerLog&Handouts/Mechanics/CLI/spells/animate-dead.md),\
      \ [counterspell](03.PlayerLog&Handouts/Mechanics/CLI/spells/counterspell.md)\n\
      \n4th level (3 slots): [blight](03.PlayerLog&Handouts/Mechanics/CLI/spells/blight.md),\
      \ [ice storm](03.PlayerLog&Handouts/Mechanics/CLI/spells/ice-storm.md), [phantasmal\
      \ killer](03.PlayerLog&Handouts/Mechanics/CLI/spells/phantasmal-killer.md)\n\
      \n5th level (3 slots): [cloudkill](03.PlayerLog&Handouts/Mechanics/CLI/spells/cloudkill.md),\
      \ [hold monster](03.PlayerLog&Handouts/Mechanics/CLI/spells/hold-monster.md),\
      \ [wall of force](03.PlayerLog&Handouts/Mechanics/CLI/spells/wall-of-force.md)\n\
      \n6th level (3 slots): [chain lightning](03.PlayerLog&Handouts/Mechanics/CLI/spells/chain-lightning.md),\
      \ [circle of death](03.PlayerLog&Handouts/Mechanics/CLI/spells/circle-of-death.md),\
      \ [disintegrate](03.PlayerLog&Handouts/Mechanics/CLI/spells/disintegrate.md)\n\
      \n7th level (3 slots): [finger of death](03.PlayerLog&Handouts/Mechanics/CLI/spells/finger-of-death.md),\
      \ [plane shift](03.PlayerLog&Handouts/Mechanics/CLI/spells/plane-shift.md),\
      \ [teleport](03.PlayerLog&Handouts/Mechanics/CLI/spells/teleport.md)\n\n8th\
      \ level (2 slots): [maze](03.PlayerLog&Handouts/Mechanics/CLI/spells/maze.md),\
      \ [mind blank](03.PlayerLog&Handouts/Mechanics/CLI/spells/mind-blank.md)\n\n\
      9th level (2 slots): [power word kill](03.PlayerLog&Handouts/Mechanics/CLI/spells/power-word-kill.md),\
      \ [time stop](03.PlayerLog&Handouts/Mechanics/CLI/spells/time-stop.md)"
    "name": "Spellcasting"
  - "desc": "Acererak carries the [Staff of the Forgotten One](03.PlayerLog&Handouts/Mechanics/CLI/items/staff-of-the-forgotten-one-toa.md).\
      \ He wears a [Talisman of the Sphere](03.PlayerLog&Handouts/Mechanics/CLI/items/talisman-of-the-sphere.md)\
      \ and has a [Sphere of Annihilation](03.PlayerLog&Handouts/Mechanics/CLI/items/sphere-of-annihilation.md)\
      \ under his control."
    "name": "Special Equipment"
  - "desc": "If Acererak fails a saving throw, he can choose to succeed instead."
    "name": "Legendary Resistance (3/Day)"
  - "desc": "Acererak's body turns to dust when he drops to 0 hit points, and his\
      \ equipment is left behind. Acererak gains a new body after d10 days, regaining\
      \ all his hit points and becoming active again. The new body appears within\
      \ 5 feet of Acererak's phylactery, the location of which is hidden."
    "name": "Rejuvenation"
  - "desc": "Acererak has advantage on saving throws against any effect that turns\
      \ undead."
    "name": "Turn Resistance"
"actions":
  - "desc": "Melee Spell Attack: +15 to hit, reach 5 ft., one creature. Hit:\
      \ 10 (3d6) cold damage, and the target must succeed on a DC 20 Constitution\
      \ saving throw or be [paralyzed](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed)\
      \ for 1 minute. The target can repeat the saving throw at the end of each of\
      \ its turns, ending the effect on itself on a success."
    "name": "Paralyzing Touch"
  - "desc": "Melee Weapon Attack: +11 to hit, reach 5 ft., one target. Hit:\
      \ 7 (1d6 + 4) bludgeoning damage plus 10 (3d6) necrotic damage, or 8 (1d8\
      \ + 4) bludgeoning damage plus 10 (3d6) necrotic damage when used with two\
      \ hands."
    "name": "Staff (+3 Quarterstaff)"
  - "desc": "While holding the Staff of the Forgotten One, Acererak expends 1 charge\
      \ from it and targets one creature he can see within 60 feet of him. The target\
      \ must succeed on a DC 23 Constitution saving throw or be cursed. Until the\
      \ curse is ended, the target can't regain hit points and has vulnerability to\
      \ necrotic damage. [Greater restoration](03.PlayerLog&Handouts/Mechanics/CLI/spells/greater-restoration.md),\
      \ [remove curse](03.PlayerLog&Handouts/Mechanics/CLI/spells/remove-curse.md),\
      \ or similar magic ends the curse on the target."
    "name": "Invoke Curse"
"legendary_actions":
  - "desc": "Acererak casts one of his at-will spells."
    "name": "At-Will Spell"
  - "desc": "Acererak uses Paralyzing Touch or makes one melee attack with his staff."
    "name": "Melee Attack"
  - "desc": "Acererak fixes his gaze on one creature he can see within 10 feet of\
      \ him. The target must succeed on a DC 20 Wisdom saving throw against this magic\
      \ or become [frightened](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Frightened)\
      \ for 1 minute. The [frightened](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Frightened)\
      \ target can repeat the saving throw at the end of each of its turns, ending\
      \ the effect on itself on a success. If a target's saving throw is successful\
      \ or the effect ends for it, the target its immune to Acererak's gaze for the\
      \ next 24 hours."
    "name": "Frightening Gaze (Costs 2 Actions)"
  - "desc": "Acererak uses his [Talisman of the Sphere](03.PlayerLog&Handouts/Mechanics/CLI/items/talisman-of-the-sphere.md)\
      \ to move the [Sphere of Annihilation](03.PlayerLog&Handouts/Mechanics/CLI/items/sphere-of-annihilation.md)\
      \ under his control up to 90 feet."
    "name": "Talisman of the Sphere (Costs 2 Actions)"
  - "desc": "Each creature within 20 feet of Acererak must make a DC 20 Constitution\
      \ saving throw against this magic, taking 42 (12d6) necrotic damage on a failed\
      \ save, or half as much damage on a successful one."
    "name": "Disrupt Life (Costs 3 Actions)"
"source":
  - "ToA"
"image": "03.PlayerLog&Handouts/Mechanics/CLI/bestiary/npc/token/acererak-toa.webp"
```
^statblock
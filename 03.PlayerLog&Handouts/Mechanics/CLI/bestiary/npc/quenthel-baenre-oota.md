---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/oota
- ttrpg-cli/monster/cr/22
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/humanoid/elf
statblock: inline
statblock-link: "#^statblock"
aliases:
- Quenthel Baenre
---
# [Quenthel Baenre](03.PlayerLog&Handouts\Mechanics\CLI\bestiary\npc/quenthel-baenre-oota.md)
*Source: Out of the Abyss p. 204*  

```statblock
"name": "Quenthel Baenre (OotA)"
"size": "Medium"
"type": "humanoid"
"subtype": "elf"
"alignment": "Neutral Evil"
"ac": !!int "19"
"ac_class": "[+3 scale mail](03.PlayerLog&Handouts/Mechanics/CLI/items/3-armor.md)"
"hp": !!int "132"
"hit_dice": "24d8 + 24"
"modifier": !!int "2"
"stats":
  - !!int "10"
  - !!int "14"
  - !!int "12"
  - !!int "18"
  - !!int "20"
  - !!int "18"
"speed": "30 ft."
"saves":
  - "constitution": "+8"
  - "wisdom": "+12"
  - "charisma": "+11"
"skillsaves":
  - "name": "[Insight](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Insight)"
    "desc": "+12"
  - "name": "[Perception](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Perception)"
    "desc": "+12"
  - "name": "[Religion](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Religion)"
    "desc": "+11"
  - "name": "[Stealth](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Stealth)"
    "desc": "+9"
"senses": "darkvision 120 ft., passive Perception 16"
"languages": "Elvish, Undercommon"
"cr": "22"
"traits":
  - "desc": "Quenthel is a 20th-level spellcaster. Her spellcasting ability is Wisdom\
      \ (save DC 20, +12 to hit with spell attacks). Quenthel has the following\
      \ cleric spells prepared:\n\nAt will: Any cleric spell up to 9th level.\n\
      \nCantrips (at will): [guidance](03.PlayerLog&Handouts/Mechanics/CLI/spells/guidance.md),\
      \ [poison spray](03.PlayerLog&Handouts/Mechanics/CLI/spells/poison-spray.md),\
      \ [resistance](03.PlayerLog&Handouts/Mechanics/CLI/spells/resistance.md), [spare\
      \ the dying](03.PlayerLog&Handouts/Mechanics/CLI/spells/spare-the-dying.md),\
      \ [thaumaturgy](03.PlayerLog&Handouts/Mechanics/CLI/spells/thaumaturgy.md)\n\
      \n1st level (4 slots): [animal friendship](03.PlayerLog&Handouts/Mechanics/CLI/spells/animal-friendship.md),\
      \ [cure wounds](03.PlayerLog&Handouts/Mechanics/CLI/spells/cure-wounds.md),\
      \ [detect poison and disease](03.PlayerLog&Handouts/Mechanics/CLI/spells/detect-poison-and-disease.md),\
      \ [ray of sickness](03.PlayerLog&Handouts/Mechanics/CLI/spells/ray-of-sickness.md)\n\
      \n2nd level (3 slots): [lesser restoration](03.PlayerLog&Handouts/Mechanics/CLI/spells/lesser-restoration.md),\
      \ [protection from poison](03.PlayerLog&Handouts/Mechanics/CLI/spells/protection-from-poison.md),\
      \ [web](03.PlayerLog&Handouts/Mechanics/CLI/spells/web.md)\n\n3rd level (3\
      \ slots): [conjure animals](03.PlayerLog&Handouts/Mechanics/CLI/spells/conjure-animals.md)\
      \ (2 giant spiders), [dispel magic](03.PlayerLog&Handouts/Mechanics/CLI/spells/dispel-magic.md)\n\
      \n4th level (3 slots): [divination](03.PlayerLog&Handouts/Mechanics/CLI/spells/divination.md),\
      \ [freedom of movement](03.PlayerLog&Handouts/Mechanics/CLI/spells/freedom-of-movement.md)\n\
      \n5th level (2 slots): [insect plague](03.PlayerLog&Handouts/Mechanics/CLI/spells/insect-plague.md),\
      \ [mass cure wounds](03.PlayerLog&Handouts/Mechanics/CLI/spells/mass-cure-wounds.md)"
    "name": "Spellcasting"
  - "desc": "Quenthel's spellcasting ability is Charisma (spell save DC 19). She can\
      \ innately cast the following spells, requiring no material components:\n\n\
      At will: [dancing lights](03.PlayerLog&Handouts/Mechanics/CLI/spells/dancing-lights.md)\n\
      \n1/day each: [darkness](03.PlayerLog&Handouts/Mechanics/CLI/spells/darkness.md),\
      \ [faerie fire](03.PlayerLog&Handouts/Mechanics/CLI/spells/faerie-fire.md),\
      \ [levitate](03.PlayerLog&Handouts/Mechanics/CLI/spells/levitate.md) (self only)"
    "name": "Innate Spellcasting"
  - "desc": "Quenthel has advantage on saving throws against being [charmed](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
      \ and magic can't put Quenthel to sleep."
    "name": "Fey Ancestry"
  - "desc": "While in sunlight, Quenthel has disadvantage on attack rolls, as well\
      \ as on Wisdom ([Perception](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Perception))\
      \ checks that rely on sight."
    "name": "Sunlight Sensitivity"
  - "desc": "Quenthel wields a [tentacle rod](03.PlayerLog&Handouts/Mechanics/CLI/items/tentacle-rod.md)."
    "name": "Special Equipment"
"actions":
  - "desc": "Quenthel makes two scourge attacks."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 5\
      \ (1d6 + 2) piercing damage plus 17 (5d6) poison damage."
    "name": "Scourge"
  - "desc": "Quenthel attempts to magically summon a [yochlol](03.PlayerLog&Handouts/Mechanics/CLI/bestiary/fiend/yochlol.md)\
      \ with a 30 percent chance of success. If the attempt fails, Quenthel takes\
      \ 5 (d10) psychic damage. Otherwise, the summoned demon appears in an unoccupied\
      \ space within 60 feet of its summoner, acts as an ally of its summoner, and\
      \ can't summon other demons. It remains for 10 minutes, until it or its summoner\
      \ dies, or until its summoner dismisses it as an action."
    "name": "Summon Demon (1/Day)"
  - "desc": "While seated on her throne, Quenthel can use an action on her turn to\
      \ cast [disintegrate](03.PlayerLog&Handouts/Mechanics/CLI/spells/disintegrate.md)\
      \ (save DC 19). A target that fails its saving throw takes 10d6 + 40 force\
      \ damage. If this damage reduces the target to 0 hit points, it is disintegrated."
    "name": "Throne Activation"
"source":
  - "OotA"
"image": "03.PlayerLog&Handouts/Mechanics/CLI/bestiary/npc/token/quenthel-baenre-oota.webp"
```
^statblock
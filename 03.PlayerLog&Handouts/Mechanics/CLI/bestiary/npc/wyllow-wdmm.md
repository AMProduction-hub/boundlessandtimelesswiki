---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/wdmm
- ttrpg-cli/monster/cr/12
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/humanoid/any-race
statblock: inline
statblock-link: "#^statblock"
aliases:
- Wyllow
---
# [Wyllow](03.PlayerLog&Handouts\Mechanics\CLI\bestiary\npc/wyllow-wdmm.md)
*Source: Waterdeep: Dungeon of the Mad Mage p. 70*  

Wyllow is a moon elf druid with eyes as green as emeralds. Butterflies nest in her tangled black hair, and small critters gather around her feet.

```statblock
"name": "Wyllow (WDMM)"
"size": "Medium"
"type": "humanoid"
"subtype": "any race"
"alignment": "Chaotic Neutral"
"ac": !!int "16"
"ac_class": "[hide armor](03.PlayerLog&Handouts/Mechanics/CLI/items/hide-armor.md),\
  \ [shield](03.PlayerLog&Handouts/Mechanics/CLI/items/shield.md)"
"hp": !!int "132"
"hit_dice": "24d8 + 24"
"modifier": !!int "2"
"stats":
  - !!int "10"
  - !!int "14"
  - !!int "12"
  - !!int "12"
  - !!int "20"
  - !!int "11"
"speed": "30 ft."
"saves":
  - "intelligence": "+5"
  - "wisdom": "+9"
"skillsaves":
  - "name": "[Medicine](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Medicine)"
    "desc": "+9"
  - "name": "[Nature](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Nature)"
    "desc": "+5"
  - "name": "[Perception](03.PlayerLog&Handouts/Mechanics/CLI/rules/skills.md#Perception)"
    "desc": "+9"
"senses": "darkvision 60 ft., passive Perception 19"
"languages": "Common, Druidic, Elvish"
"cr": "12"
"traits":
  - "desc": "Wyllow is an 18th-level spellcaster. Its spellcasting ability is Wisdom\
      \ (spell save DC 17, +9 to hit with spell attacks). It has the following druid\
      \ spells prepared:\n\nCantrips (at will): [druidcraft](03.PlayerLog&Handouts/Mechanics/CLI/spells/druidcraft.md),\
      \ [mending](03.PlayerLog&Handouts/Mechanics/CLI/spells/mending.md), [poison\
      \ spray](03.PlayerLog&Handouts/Mechanics/CLI/spells/poison-spray.md), [produce\
      \ flame](03.PlayerLog&Handouts/Mechanics/CLI/spells/produce-flame.md)\n\n1st\
      \ level (4 slots): [cure wounds](03.PlayerLog&Handouts/Mechanics/CLI/spells/cure-wounds.md),\
      \ [entangle](03.PlayerLog&Handouts/Mechanics/CLI/spells/entangle.md), [faerie\
      \ fire](03.PlayerLog&Handouts/Mechanics/CLI/spells/faerie-fire.md), [speak with\
      \ animals](03.PlayerLog&Handouts/Mechanics/CLI/spells/speak-with-animals.md)\n\
      \n2nd level (3 slots): [animal messenger](03.PlayerLog&Handouts/Mechanics/CLI/spells/animal-messenger.md),\
      \ [beast sense](03.PlayerLog&Handouts/Mechanics/CLI/spells/beast-sense.md),\
      \ [hold person](03.PlayerLog&Handouts/Mechanics/CLI/spells/hold-person.md)\n\
      \n3rd level (3 slots): [conjure animals](03.PlayerLog&Handouts/Mechanics/CLI/spells/conjure-animals.md),\
      \ [meld into stone](03.PlayerLog&Handouts/Mechanics/CLI/spells/meld-into-stone.md),\
      \ [water breathing](03.PlayerLog&Handouts/Mechanics/CLI/spells/water-breathing.md)\n\
      \n4th level (3 slots): [dominate beast](03.PlayerLog&Handouts/Mechanics/CLI/spells/dominate-beast.md),\
      \ [locate creature](03.PlayerLog&Handouts/Mechanics/CLI/spells/locate-creature.md),\
      \ [stoneskin](03.PlayerLog&Handouts/Mechanics/CLI/spells/stoneskin.md), [wall\
      \ of fire](03.PlayerLog&Handouts/Mechanics/CLI/spells/wall-of-fire.md)\n\n5th\
      \ level (3 slots): [commune with nature](03.PlayerLog&Handouts/Mechanics/CLI/spells/commune-with-nature.md),\
      \ [mass cure wounds](03.PlayerLog&Handouts/Mechanics/CLI/spells/mass-cure-wounds.md),\
      \ [tree stride](03.PlayerLog&Handouts/Mechanics/CLI/spells/tree-stride.md)\n\
      \n6th level (1 slots): [heal](03.PlayerLog&Handouts/Mechanics/CLI/spells/heal.md),\
      \ [heroes' feast](03.PlayerLog&Handouts/Mechanics/CLI/spells/heroes-feast.md),\
      \ [sunbeam](03.PlayerLog&Handouts/Mechanics/CLI/spells/sunbeam.md)\n\n7th\
      \ level (1 slots): [fire storm](03.PlayerLog&Handouts/Mechanics/CLI/spells/fire-storm.md)\n\
      \n8th level (1 slots): [animal shapes](03.PlayerLog&Handouts/Mechanics/CLI/spells/animal-shapes.md)\n\
      \n9th level (1 slots): [foresight](03.PlayerLog&Handouts/Mechanics/CLI/spells/foresight.md)"
    "name": "Spellcasting"
  - "desc": "Wyllow"
    "name": "Fey Ancestry"
  - "desc": "Wyllow"
    "name": "Mask of the Wild"
"actions":
  - "desc": "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 5\
      \ (1d6 + 2) slashing damage."
    "name": "Scimitar"
  - "desc": "Wyllow magically polymorphs into a beast or elemental with a challenge\
      \ rating of 6 or less, and can remain in this form for up to 9 hours. Wyllow\
      \ can choose whether its equipment falls to the ground, melds with its new form,\
      \ or is worn by the new form. Wyllow reverts to its true form if it dies or\
      \ falls [unconscious](03.PlayerLog&Handouts/Mechanics/CLI/rules/conditions.md#Unconscious).\
      \ Wyllow can revert to its true form using a bonus action on its turn.\n\nWhile\
      \ in a new form, Wyllow retains its game statistics and ability to speak, but\
      \ its AC, movement modes, Strength, and Dexterity are replaced by those of the\
      \ new form, and it gains any special senses, proficiencies, traits, actions,\
      \ and reactions (except class features, legendary actions, and lair actions)\
      \ that the new form has but that it lacks. It can cast its spells with verbal\
      \ or somatic components in its new form.\n\nThe new form's attacks count as\
      \ magical for the purpose of overcoming resistances and immunity to nonmagical\
      \ attacks."
    "name": "Change Shape (2/Day)"
"source":
  - "WDMM"
"image": "03.PlayerLog&Handouts/Mechanics/CLI/bestiary/npc/token/wyllow-wdmm.webp"
```
^statblock
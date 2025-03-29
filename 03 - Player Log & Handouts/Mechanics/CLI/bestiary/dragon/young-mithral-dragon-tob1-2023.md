---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/7
- ttrpg-cli/monster/environment/mountain
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/dragon
statblock: inline
aliases: ["Young Mithral Dragon"]
---
# [Young Mithral Dragon](03 - Player Log & Handouts\Mechanics\CLI\bestiary\dragon/young-mithral-dragon-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 123*  

*Light glints off the dragon's glossy scales, shining silver-white. Its tiny wings folded flush against its body open like a fan and expose shimmering, diaphanous membranes. Its narrow head, with bare slits for its eyes and nostrils, sits at the end of a slender neck atop an impossibly thin frame*.

## Rage in Youth

Younger mithral dragons raid and pillage as heavily as any chromatic dragon, driven largely by greed to acquire a worthy hoard, though they are less likely to kill for sport or out of cruelty. In adulthood and old age, however, mithral dragons are less concerned with material wealth and more inclined to value friendship, knowledge, and a peaceful life pursuing interesting goals.

## Peacemakers

Adult and older mithral dragons are diplomats and arbitrators by temperament (some dragons cynically call them referees). They enjoy bringing some peace to warring factions. Among all dragons, their strict neutrality and ability to negate magic make them well suited to these vital roles.

> [!note] Mithral Dragons in Midgard
> 
> Mithral dragons are rebellious dragons who once sought to make peace between chromatic and metallic dragons. Having failed in that, they declared themselves neutral and now seek opportunities to make peace elsewhere. They are the only dragons that advocate against the perpetual war of the Dragon Empire, and occasionally serve as mercenaries against the Mharoti.
^mithral-dragons-in-midgard

```statblock
"name": "Young Mithral Dragon (ToB1-2023)"
"size": "Large"
"type": "dragon"
"alignment": "Neutral"
"ac": !!int "16"
"ac_class": "natural armor"
"hp": !!int "170"
"hit_dice": "20d10 + 60"
"stats":
- !!int "12"
- !!int "18"
- !!int "17"
- !!int "16"
- !!int "17"
- !!int "16"
"speed": "40 ft., fly 80 ft."
"saves":
  "Charisma": !!int "6"
  "Dexterity": !!int "7"
  "Wisdom": !!int "6"
  "Constitution": !!int "6"
"skillsaves":
  "Stealth": !!int "7"
  "Insight": !!int "6"
  "Perception": !!int "9"
  "Persuasion": !!int "6"
"damage_resistances": "force"
"damage_immunities": "slashing"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed)"
"senses": "blindsight 30 ft., darkvision 120 ft., passive Perception 19"
"languages": "all, telepathy 60 ft."
"cr": "7"
"traits":
- "desc": "The dragon has advantage on saving throws against spells and other magical\
    \ effects."
  "name": "Magic Resistance"
"actions":
- "desc": "The dragon makes one Bite attack and two Claw attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +7 to hit, reach 10 ft., one target. Hit: 15\
    \ (2d10 + 4) piercing damage. Instead of dealing damage, the dragon can end\
    \ one magical effect of its choice of 3rd level or lower on the target."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 11\
    \ (2d6 + 4) slashing damage, and if the target isn't a Construct or Undead,\
    \ it must succeed on a DC 14 Constitution saving throw or lose 3 1d6 hp at the\
    \ start of each of its turns as a piece of metallic claw breaks off in the wound.\
    \ Any creature can take an action to remove the claw with a successful DC 12 Wisdom\
    \ ([Medicine](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Medicine))\
    \ check. The claw pops out of the wound if the target receives magical healing."
  "name": "Claw"
- "desc": "The mithral dragon spits metallic shards in a 30-foot cone. Each creature\
    \ in that area must make a DC 14 Dexterity saving throw, taking 28 (8d6) slashing\
    \ damage on a failed save, or half as much damage on a successful one. The area\
    \ becomes difficult terrain for 1 minute, then the shards dissolve into wisps\
    \ of silvery smoke."
  "name": "Shard Breath (Recharge 5-6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/dragon/token/young-mithral-dragon-tob1-2023.webp"
```
^statblock

## Environment

mountain
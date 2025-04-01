---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/9
- ttrpg-cli/monster/environment/any
- ttrpg-cli/monster/size/huge
- ttrpg-cli/monster/type/undead
statblock: inline
aliases: ["Necrohydra"]
---
# [Necrohydra](03 - Player Log & Handouts\Mechanics\CLI\bestiary\undead/necrohydra-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 283*  

*Five snaking necks sprout from this decayed, draconic body. However, instead of reptilian heads, each neck ends in a humanoid head.*

Necrohydras are created by powerful, evil necromancers and often used as guardians or placed at the vanguard of an undead army to strike fear and despair into the enemy. The wordless, heart-wrenching dirge the creature produces can drain all hope from listeners. The necrohydra can speak, though the few words it croaks out are usually only in response to questions by its master.

## Familiar Heads

Sometimes a necrohydra is created as an instrument of revenge or a tool to further damage the morale of a necromancer's enemies. In these instances, the necromancer uses the heads of humanoids that are familiar to those that will face the necrohydra—heroes, beloved leaders or officers, loved ones, or close allies. A necromancer may coach the necrohydra to say certain mocking phrases to strike at the hearts of the necromancer's enemies.

```statblock
"name": "Necrohydra (ToB1-2023)"
"size": "Huge"
"type": "undead"
"alignment": "Neutral Evil"
"ac": !!int "13"
"ac_class": "natural armor"
"hp": !!int "207"
"hit_dice": "18d12 + 90"
"stats":
- !!int "20"
- !!int "6"
- !!int "20"
- !!int "3"
- !!int "10"
- !!int "7"
"speed": "30 ft., swim 30 ft."
"saves":
  "Wisdom": !!int "4"
"skillsaves":
  "Perception": !!int "8"
"damage_resistances": "necrotic"
"damage_immunities": "poison"
"condition_immunities": "[exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 60 ft., passive Perception 18"
"languages": "the languages its heads knew in life"
"cr": "9"
"traits":
- "desc": "The necrohydra has five fleshy heads. While it has more than one head,\
    \ the necrohydra has advantage on saving throws against being [blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded),\
    \ [charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
    \ [deafened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Deafened),\
    \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
    \ [stunned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Stunned),\
    \ and knocked [unconscious](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Unconscious).\
    \ Whenever the necrohydra takes 25 or more damage in a single turn, one of its\
    \ fleshy heads dies. If all its fleshy heads die, the necrohydra can't use or\
    \ maintain Dreadful Dirge. At the end of its turn, it grows two skeletal heads\
    \ for each of its fleshy heads that died since its last turn, unless it has taken\
    \ radiant damage since its last turn. The necrohydra regains 10 hp for each skeletal\
    \ head regrown in this way."
  "name": "Multiple Heads"
- "desc": "For each head the necrohydra has beyond one, it gets an extra reaction\
    \ that can be used only for opportunity attacks."
  "name": "Reactive Heads"
- "desc": "The necrohydra doesn't require air, food, drink, or sleep."
  "name": "Undead Nature"
"actions":
- "desc": "The necrohydra makes as many Bite attacks as it has heads."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +9 to hit, reach 10 ft., one target. Hit: 7\
    \ (1d4 + 5) piercing damage plus 4 (1d8) necrotic damage."
  "name": "Bite"
- "desc": "The necrohydra's heads emit a cacophonous, moaning wail. Each creature\
    \ that isn't a Construct or Undead within 30 feet of the necrohydra that can hear\
    \ the wail must succeed on a DC 17 Wisdom saving throw or be [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)\
    \ until the wail ends. The necrohydra must take a bonus action on its subsequent\
    \ turns to continue wailing. It can stop wailing at any time. The wail ends if\
    \ the necrohydra is [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated).\
    \ A [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)\
    \ creature can repeat the saving throw at the end of each of its turns, ending\
    \ the effect on itself on a success."
  "name": "Dreadful Dirge"
- "desc": "The necrohydra spews rotten bile soaked in necrotic energy in a 30-foot\
    \ cone. Each creature in that area must make a DC 17 Dexterity saving throw, taking\
    \ 21 (6d6) poison damage and 18 (4d8) necrotic damage on a failed save, or\
    \ half as much damage on a successful one."
  "name": "Necrotic Bile (Recharge 6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/undead/token/necrohydra-tob1-2023.webp"
```
^statblock

## Environment

any
---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/5
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/size/small
- ttrpg-cli/monster/type/fey
statblock: inline
aliases: ["Aridni"]
---
# [Aridni](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fey/aridni-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 25*  

*The gray, moth-winged fey flies out from the trees in a hail of tiny arrows.*

Both more rugged and more ruthless than normal pixies, the aridni are an especially greedy breed of fey bandits and kidnappers.

## Pale Archers

These ashen-faced fey with gray moth wings fire green-glowing arrows with a sneer and a curse. Aridni prefer ranged combat whenever possible, and they are quite difficult to lure into melee. They sometimes accept a personal challenge or respond to accusations of cowardice.

## Caravan Raiders

Aridni have developed different magical abilities that aid them well when they raid caravans for captives, such as charming foes or putting them to sleep.

## Wealth for Status

They delight in taking plunder from humans and dwarves as a sign of their power over mortals and of their contempt for those who lack fey blood.

> [!note] Aridni in Midgard
> 
> When the elves abandoned the mortal world and returned to the elflands, not all of their fey servants went with them. Some stayed by choice; some were abandoned as tainted, feral broods; and some remained to become servants of local gods or human mages. Most of them are angry at humans for their corruption of, and rebellions against, the elven courts and empires in Midgard. They seek to regain some of their fallen fey wealth and glory from humans and dwarves by stealing from, corrupting, and killing their ancient enemies. Among these abandoned fey are the aridni ("slaver pixies"), evil pixies suborned by the Slavers of Reth-Saal.
^aridni-in-midgard

```statblock
"name": "Aridni (ToB1-2023)"
"size": "Small"
"type": "fey"
"alignment": "Neutral Evil"
"ac": !!int "15"
"hp": !!int "82"
"hit_dice": "15d6 + 30"
"stats":
- !!int "9"
- !!int "21"
- !!int "14"
- !!int "12"
- !!int "11"
- !!int "16"
"speed": "20 ft., fly 60 ft."
"saves":
  "Dexterity": !!int "8"
"skillsaves":
  "Stealth": !!int "11"
  "Perception": !!int "3"
  "Acrobatics": !!int "11"
"senses": "darkvision 60 ft., passive Perception 13"
"languages": "Common, Gnoll, Sylvan, Void Speech"
"cr": "5"
"traits":
- "desc": "The aridni casts one of the following spells, using Charisma as the spellcasting\
    \ ability (spell save DC 14):\n\nAt will: [dancing lights](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/dancing-lights.md),\
    \ [detect magic](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/detect-magic.md),\
    \ [invisibility](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/invisibility.md)\n\
    \n1/day: [spike growth](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/spike-growth.md)\n\
    \n3/day each: [charm person](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/charm-person.md),\
    \ [faerie fire](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/faerie-fire.md)"
  "name": "Spellcasting"
- "desc": "The aridni doesn't provoke opportunity attacks when it flies out of an\
    \ enemy's reach."
  "name": "Flyby"
- "desc": "The aridni has advantage on saving throws against spells and other magical\
    \ effects."
  "name": "Magic Resistance"
"actions":
- "desc": "The aridni makes three Shortsword or Pixie Bow attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 8 (1d6\
    \ + 5) piercing damage."
  "name": "Shortsword"
- "desc": "Ranged Weapon Attack: +8 to hit, range 40/160 ft., one target. Hit:\
    \ 10 (2d4 + 5) piercing damage."
  "name": "Pixie Bow"
"bonus_actions":
- "desc": "The aridni enchants one arrow with minor magic. The next time it hits a\
    \ creature with a Pixie Bow attack before the start of its next turn, the target\
    \ must succeed on a DC 14 Wisdom saving throw or suffer one of the following effects:\n\
    \n- Confusion. The target can't take reactions and acts randomly until the\
    \ end of its next turn, as if it had failed the saving throw against the [confusion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/confusion.md)\
    \ spell.  \n- Fear. The target is [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)\
    \ until the end of its next turn and must spend its next turn moving away from\
    \ the aridni by the safest available route.  \n- Laughter. The target falls\
    \ [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)\
    \ and is [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated)\
    \ with laughter until the end of its next turn.  \n- Sleep. The target falls\
    \ [unconscious](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Unconscious)\
    \ for 1 minute. It wakes up if it takes damage or if another creature takes an\
    \ action to shake it awake.  "
  "name": "Enchanted Arrows"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fey/token/aridni-tob1-2023.webp"
```
^statblock

## Environment

forest
---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/3
- ttrpg-cli/monster/environment/farmland
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/monstrosity
statblock: inline
aliases: ["Kot Bayun"]
---
# [Kot Bayun](03 - Player Log & Handouts\Mechanics\CLI\bestiary\monstrosity/kot-bayun-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 248*  

*This oddly colored cat appears at first to be a powerful panther of some kind. Its wide mouth pulls into something like a human grin, and its knowing eyes hint at intelligence beyond that of a typical jungle cat.*

Enemies of elves and blink dogs, kot bayuns are magical hunting cats gifted with eloquent speech and cunning abilities.

## Speaking Fey Cats

These brutal and temperamental creatures get along well with cruel-minded fey. Gentler fey rightfully find the creatures to be a menace. A kot bayun measures six feet long and weighs over 200 pounds. They are long-lived, and some stories record the same kot bayun in a region for over 400 years.

## Sing to Sleep

In addition to their stealthy natures and physical prowess, kot bayun have the ability to put prey to sleep with song. They carefully stalk victims for a time, learning the victim's strengths and weaknesses before making their attack. They lie in wait until their prey is vulnerable and then begin their song. Those resisting the call to slumber are always the kot bayun's first victims as the predator launches from cover and attempts to disembowel its prey. In forests with a thick canopy, a kot bayun stealthily creeps among tree limbs, tracking the movement of its prey below.

## Healing Poetry

If discovered by intelligent prey, a kot bayun opens with a parley instead of claws. In rare cases, a kot bayun finds something in its prey it likes, and cold predation turns to a lukewarm association. Befriending a kot bayun has benefits, as the creature's poems, tales, and sagas have healing power. A kot bayun tells its stories in the form of strange epics and poetry, ranging from simple rhyming folk poems to complex sonnets, and it heals listeners only at the end of the poem.

```statblock
"name": "Kot Bayun (ToB1-2023)"
"size": "Medium"
"type": "monstrosity"
"alignment": "Neutral"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "66"
"hit_dice": "12d8 + 12"
"stats":
- !!int "16"
- !!int "16"
- !!int "13"
- !!int "12"
- !!int "16"
- !!int "17"
"speed": "40 ft., climb 20 ft."
"saves":
  "Dexterity": !!int "5"
"skillsaves":
  "Stealth": !!int "5"
"senses": "darkvision 60 ft., passive Perception 13"
"languages": "Common, Sylvan"
"cr": "3"
"actions":
- "desc": "The kot bayun can use its Slumbering Song. It then makes one Bite attack\
    \ and two Claw attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 7 (1d8\
    \ + 3) piercing damage."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 8 (2d4\
    \ + 3) slashing damage."
  "name": "Claw"
- "desc": "The kot bayun magically turns [invisible](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Invisible)\
    \ until it attacks or uses Slumbering Song, or until its [concentration](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Concentration)\
    \ ends (as if [concentrating](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Concentration)\
    \ on a spell). Any equipment the kot bayun wears or carries is [invisible](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Invisible)\
    \ with it."
  "name": "Invisibility"
- "desc": "The kot bayun sings a magical song to one creature it can see within 60\
    \ feet of it. The target must succeed on a DC 13 Charisma saving throw on fall\
    \ [unconscious](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Unconscious)\
    \ for 1 minute. The target can repeat the saving throw at the end of each of its\
    \ turns, ending the effect on itself on a success. If the kot bayun uses a bonus\
    \ action on its subsequent turns to continue singing, the target has disadvantage\
    \ on this saving throw. Otherwise, the effect ends for a target if the target\
    \ takes damage while below half its hp maximum.\n\nIf a creature's saving throw\
    \ is successful or the effect ends for it, the creature is immune to the kot bayun's\
    \ Slumbering Song for the next 24 hours. The kot bayun can have up to two creatures\
    \ [unconscious](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Unconscious)\
    \ from its song at a time."
  "name": "Slumbering Song"
- "desc": "The kot bayun purrs at a creature it can see within 15 feet of it. The\
    \ target magically regains 10 (3d6) hp and is freed from any disease, poison,\
    \ blindness, or deafness."
  "name": "Healing Purr (2/Day)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/monstrosity/token/kot-bayun-tob1-2023.webp"
```
^statblock

## Environment

farmland, forest
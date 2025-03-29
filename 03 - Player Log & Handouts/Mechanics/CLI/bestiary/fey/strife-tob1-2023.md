---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/3
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/small
- ttrpg-cli/monster/type/fey
statblock: inline
aliases: ["Strife"]
---
# [Strife](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fey/strife-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 349*  

*The small, childlike creature with purple skin and an overly large mouth hovers in the shadows of the alleyway behind the tavern, giggling with delight as it watches fights break out.*

This strange, childlike fey feeds off the negative feelings that manifest from mortals who spread rumors and falsehoods about one another.

## False Legends

Due to its ability to remain unseen and its appearance wherever discord rises, many in the mortal world believe this fey is the physical embodiment of a feeling, a magical manifestation brought on by strong mortal emotions. Delighting in rumors and misinformation, the fey don't correct these interpretations and proudly use the mortal moniker, strife.

## Invasive Fey

Though strifes aren't physical embodiments of mortal emotions, negative feelings between mortals create a weakening between the Material Plane and the realms of the fey, allowing strifes to enter the material world. Once on the Material Plane, a strife lurks in the shadows of a settlement, fueling rumors until the populace erupts with chaos and discord. Travelers might come across a settlement and be greeted with abnormal hostility when a strife is present. Once its work is done, the strife returns to the fey realms to tell tales of its work before finding a new settlement to disturb. The most successful of strifes have caused kingdoms to fall to civil war when the government was painted as unfit by a strife's work. The strife does not revel in bloodshed, but in the unrest of the days or weeks that precede it.

```statblock
"name": "Strife (ToB1-2023)"
"size": "Small"
"type": "fey"
"alignment": "Chaotic Evil"
"ac": !!int "15"
"hp": !!int "60"
"hit_dice": "11d6 + 22"
"stats":
- !!int "8"
- !!int "20"
- !!int "14"
- !!int "13"
- !!int "14"
- !!int "16"
"speed": "40 ft., fly 40 ft."
"skillsaves":
  "Deception": !!int "7"
  "Stealth": !!int "9"
"senses": "darkvision 60 ft., passive Perception 12"
"languages": "Common, Sylvan"
"cr": "3"
"traits":
- "desc": "The strife can mimic Humanoid voices. A creature that hears the sounds\
    \ can tell they are imitations with a successful DC 17 Wisdom ([Insight](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Insight))\
    \ check."
  "name": "Mimicry"
- "desc": "When a creature within 30 feet of the strife takes psychic damage, the\
    \ strife gains 5 temporary hp or gains advantage on the next attack roll it makes\
    \ before the end of its next turn (the strife's choice)."
  "name": "Delight"
"actions":
- "desc": "The strife can use its Sow Discord. It then makes two Claw attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +7 to hit, reach 5 ft. one target. Hit: 8 (1d6\
    \ + 5) slashing damage."
  "name": "Claw"
- "desc": "The strife attempts to sow discord in up to two creatures it can see within\
    \ 30 feet of it. Each target must make a DC 13 Wisdom saving throw. On a failure,\
    \ a creature takes 7 (2d6) psychic damage and distrusts its allies until the\
    \ start of the strife's next turn. On a success, a creature takes half the damage\
    \ and doesn't distrust its allies. A creature that distrusts its allies can't\
    \ give or receive aid from its allies, including spells, class features like Sneak\
    \ Attack, and the Help action."
  "name": "Sow Discord"
- "desc": "The strife magically turns [invisible](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Invisible)\
    \ until it attacks or until its [concentration](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Concentration)\
    \ ends (as if [concentrating](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Concentration)\
    \ on a spell). Any equipment the strife wears or carries is [invisible](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Invisible)\
    \ with it."
  "name": "Invisibility"
"reactions":
- "desc": "If a creature misses the strife with an attack, the strife can cause the\
    \ attacker to doubt itself. The attacker must succeed on a DC 13 Wisdom saving\
    \ throw or each time it makes an attack roll or saving throw before the end of\
    \ its next turn, it must roll a d4 and subtract the number rolled from the attack\
    \ roll or saving throw."
  "name": "Induce Doubt"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fey/token/strife-tob1-2023.webp"
```
^statblock

## Environment

planar, urban
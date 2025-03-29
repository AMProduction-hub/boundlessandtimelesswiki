---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/bgdia
- ttrpg-cli/monster/cr/6
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/undead
statblock: inline
aliases: ["Gideon Lightward"]
---
# [Gideon Lightward](03 - Player Log & Handouts\Mechanics\CLI\bestiary\npc/gideon-lightward-bgdia.md)
*Source: Baldur's Gate: Descent Into Avernus p. 65*  

Gideon Lightward was a priest of Lathander who served Elturel and his deity proudly. Zariel saw that his fervor could be an asset to her, so she sent devils to corrupt him in the months leading up to the fall of Elturel. The devils posed as angels, offering Gideon increased power if he would dedicate himself to fighting the ever-present threat of demons.

Gideon slowly gave up his sanity and free will to the devils, leaving him corrupted by Zariel and fully serving her in the months leading up to Elturel's fall. He died during the destruction wrought as the city was drawn to Avernus, but the priest rose as an undead creature. Even as an undead, Gideon remains his mistress's most loyal servant in Elturel. He sees his cause as a noble one—fighting the demons whose chaos marks the end of all things. But his mind is broken and filled with hatred for those who refuse to follow his commands.

```statblock
"name": "Gideon Lightward (BGDIA)"
"size": "Medium"
"type": "undead"
"alignment": "Lawful Evil"
"ac": !!int "11"
"hp": !!int "136"
"hit_dice": "16d8 + 64"
"stats":
- !!int "18"
- !!int "13"
- !!int "18"
- !!int "10"
- !!int "18"
- !!int "13"
"speed": "30 ft."
"saves":
  "Dexterity": !!int "4"
  "Wisdom": !!int "7"
  "Constitution": !!int "7"
"skillsaves":
  "Religion": !!int "6"
  "Insight": !!int "7"
"damage_vulnerabilities": "radiant"
"damage_resistances": "bludgeoning, piercing, slashing from nonmagical attacks"
"damage_immunities": "necrotic, poison"
"condition_immunities": "[exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 60 ft., passive Perception 14"
"languages": "Common"
"cr": "6"
"traits":
- "desc": "Gideon regains 10 hit points at the start of each of his turns. If he takes\
    \ radiant damage, this trait doesn't function at the start of his next turn. Gideon\
    \ is destroyed only if he starts his turn with 0 hit points and doesn't regenerate."
  "name": "Regeneration"
"actions":
- "desc": "Gideon attacks twice with his fists."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 11\
    \ (2d6 + 4) bludgeoning damage."
  "name": "Fist"
- "desc": "Gideon targets one creature he can see within 60 feet of him. The target\
    \ must make a DC 15 Constitution saving throw, taking 22 (4d10) necrotic damage\
    \ on a failed save, or half as much damage on a successful one."
  "name": "Withering Gaze"
"source":
- "BGDIA"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/npc/token/gideon-lightward-bgdia.webp"
```
^statblock
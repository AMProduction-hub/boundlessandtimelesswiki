---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/5
- ttrpg-cli/monster/environment/coastal
- ttrpg-cli/monster/environment/desert
- ttrpg-cli/monster/environment/grassland
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/humanoid/subek
statblock: inline
aliases: ["Subek"]
---
# [Subek](03 - Player Log & Handouts\Mechanics\CLI\bestiary\humanoid/subek-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 352*  

*The merchant displayed his wares and smiled, the kindness in his eyes and softness of his smile juxtaposed with his crocodilian body and fangs.*

For most of the year, the subek are a kindly people, advising others and lending their physical and intellectual prowess to local projects. During the flood season, however, subek become violent and territorial, ruthlessly killing and consuming all trespassers.

## Riverbank Homes

Subek are crocodilian humanoids that dwell along the banks of great rivers. They have muscular physiques, surprisingly dexterous hands, and a frightening maw of sharp teeth. They are 9 feet tall, average 700 pounds, and can live up to 300 years. During the dry season, subek are friendly and thoughtful scholars, historians, and artisans.

## Flood Fever

Subek are well aware of their destructive and violent nature. When the waters rise, they distance themselves from other cultures, warning locals to keep away until the river recedes. Most migrate up or down river to an area with few inhabitants; some even construct underground prisons or cages and pay brave retainers to keep them locked up and fed during their time of savagery. During flood fever, subek do not recognize friends or colleagues. They discard all trappings of civilization and kill non-subek creatures indiscriminately. Once the fever clears, they remember nothing of their actions, though they are surrounded by undeniable, grisly reminders.

## Keep Their Distance

Despite the danger, subek are tolerated and even prized for their skill as engineers, historians, and teachers. They live on the outskirts of many human towns, maintaining a cautious distance from their neighbors. Subek marriage is pragmatic; they live with a mate long enough to foster a single egg and raise the hatchling for a decade before parting ways.

## Curious Duality

Subek scholars and oracles debate their duality. Some believe it to be an ancient curse, a shared ancestry with an ancient savage people, or some loathsome and primitive part of their soul exerting control. A rare few—shamans and oracles, mostly—embrace their duality and choose to live year-round in remote regions far from civilization.

```statblock
"name": "Subek (ToB1-2023)"
"size": "Large"
"type": "humanoid"
"subtype": "subek"
"alignment": "Lawful Neutral"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "114"
"hit_dice": "12d10 + 48"
"stats":
- !!int "19"
- !!int "10"
- !!int "18"
- !!int "14"
- !!int "13"
- !!int "13"
"speed": "30 ft., swim 20 ft."
"skillsaves":
  "Investigation": !!int "5"
  "History": !!int "5"
"senses": "darkvision 60 ft., passive Perception 11"
"languages": "Common"
"cr": "5"
"traits":
- "desc": "During flood season, the subek is overcome with bloodthirsty malice, becoming\
    \ more aggressive and losing its proficiency in Intelligence ([History](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#History))\
    \ and Intelligence ([Investigation](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Investigation))\
    \ checks. If it hasn't fed within the past 8 hours, it enters a frenzy, spending\
    \ each turn attacking the nearest creature it can see. If no creature is near\
    \ enough to move to and attack, the subek attacks an object, with preference for\
    \ an object smaller than itself. During the frenzy, it has advantage on melee\
    \ attack rolls against any creature that doesn't have all its hp. It continues\
    \ the frenzy until it has fed and enters the frenzy again every time it goes without\
    \ eating for 8 hours for the duration of the flood season."
  "name": "Flood Fever"
- "desc": "The subek can hold its breath for 15 minutes."
  "name": "Hold Breath"
"actions":
- "desc": "The subek makes one Bite attack and two Claw attacks. If both Claw attacks\
    \ hit one creature, the target must succeed on a DC 15 Strength saving throw or\
    \ take 7 (2d6) slashing damage as the subek tears into the target."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. it: 13 (2d8\
    \ + 4) piercing damage."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 11\
    \ (2d6 + 4) slashing damage."
  "name": "Claw"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/humanoid/token/subek-tob1-2023.webp"
```
^statblock

## Environment

coastal, desert, grassland
---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/3
- ttrpg-cli/monster/environment/desert
- ttrpg-cli/monster/environment/underdark
- ttrpg-cli/monster/size/small
- ttrpg-cli/monster/type/humanoid/tosculi
statblock: inline
aliases: ["Tosculi Warrior"]
---
# [Tosculi Warrior](03 - Player Log & Handouts\Mechanics\CLI\bestiary\humanoid/tosculi-warrior-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 367*  

*This humanoid wasp's gossamer wings beat out a soft, droning buzz. Flashing blades sing in each of her four clawed hands, and the air around her shimmers with magical*dust. Dozens more humanoid wasps in a variety of iridescent colors surround her, weapons raised protectively.

The tosculi are waspfolk that share the Golden Song of the hive, which unites them under the command of their queen. Each hive has its own song, and most tosculi hives are predatory, dangerous places.

## Bow Raiders

Tosculi elite bow raiders are smarter and more capable than drones and common warriors, with midnight black or deep green carapaces that shine with colorful iridescence. Their wings are blood red streaked with dark crimson veins. As rare and prized members of the hive, a bow raider's life is never thrown away or risked unnecessarily. Seldom does a tosculi warband contain more than a handful of these elite soldiers, and they frequently hold positions of command. Elite bow raiders always lead the honor guard for their queen, both within the hive and on those rare occasions when the queen ventures outside.

## Drones

Tosculi drones are the workers of the tosculi hive: the smallest, weakest, least intelligent, and most abundant of the waspfolk. Their carapaces are mostly iridescent blue with gold abdomens and lower legs, and they have vestigial wings, allowing them to glide but not truly fly. Drones function primarily as menial workers but, during times of war, they also act as highly expendable scouts and soldiers. Because the warriors know whatever a drone knows—thanks to the queen—a drone doesn't need to survive its scouting mission to deliver useful information.

## Warriors

Tosculi warriors are overseers of work crews and battle groups of drones, directing activities and relaying commands. Though subservient to the queen's orders, they are capable of acting independently or following their own best judgment, if necessary. The warriors' most important role in the hive is procuring live hosts for incubating tosculi eggs. Creatures paralyzed by warriors are brought to the queen's chamber to have eggs implanted in them, and after a few weeks, the larva hatches, devouring its still-living host.

## Hive Queen

The hive queen is the nerve center of a tosculi hive-city, simultaneously one of a hive's greatest strengths and weaknesses. The queen serves as a unifying force. She binds her swarm with an ironclad sense of purpose through a psychic web, known as the Golden Song, that links all tosculi within a hive. When the hive queen nears the end of her life, she selects the most promising of her immature heirs and feeds the heir a special concoction. This speeds the heir's maturation and makes her ready to become a full-fledged hive queen. The daughter's first action upon her metamorphosis is to devour her mother and all her sisters, absorbing and becoming the emitter of that hive's song. If a hive queen dies with no heir to anchor the hive mind or if the daughter's accession is disrupted, the hive-city plunges into chaos. Tosculi bereft of the hive-mind go berserk. A few fortunate ones might escape and become lone renegades, but their existence without the comforting presence of the hive is miserable and short. Unless one of the hive-queen's surviving daughters is mature enough and ruthless enough to step in and assert control, the hive is doomed.

```statblock
"name": "Tosculi Warrior (ToB1-2023)"
"size": "Small"
"type": "humanoid"
"subtype": "tosculi"
"alignment": "Lawful Evil"
"ac": !!int "15"
"hp": !!int "58"
"hit_dice": "9d6 + 27"
"stats":
- !!int "12"
- !!int "20"
- !!int "16"
- !!int "10"
- !!int "12"
- !!int "12"
"speed": "20 ft., fly 60 ft."
"senses": "darkvision 60 ft., passive Perception 11"
"languages": "Tosculi"
"cr": "3"
"traits":
- "desc": "The tosculi can share its space with up to one other tosculi. While sharing\
    \ its space with one other tosculi, it has advantage on attack rolls against a\
    \ creature if the other tosculi in its space isn't [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated)."
  "name": "Crowd Tactics"
- "desc": "The tosculi can pinpoint the location of its hive queen when she is within\
    \ 300 feet of it, and it can sense the general direction and distance to the hive\
    \ where its queen makes her home."
  "name": "Hive Sense"
"actions":
- "desc": "The tosculi warrior makes one Claw attack and one Stinger attack."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 10\
    \ (2d4 + 5) slashing damage."
  "name": "Claw"
- "desc": "Melee Weapon Attack: +7 to hit, reach 5 ft., one creature. Hit: 10\
    \ (2d4 + 5) piercing damage, and the target must succeed on a DC 13 Constitution\
    \ saving throw or be [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ for 1 minute. While [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ in this way, the target is also [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed).\
    \ A [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ target can repeat the saving throw at the end of each of its turns, ending the\
    \ effect on itself on a success."
  "name": "Stinger"
- "desc": "The tosculi extends the paralysis on a creature within 5 feet of it that\
    \ was [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed)\
    \ by a tosculi's Stinger attack. The [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed)\
    \ target must succeed on a DC 13 Constitution saving throw or be [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed)\
    \ for 8 hours and no longer makes saving throws to end the paralysis. The paralysis\
    \ ends if the target takes damage while below half its hp maximum. Otherwise,\
    \ a spell or effect that cures disease ends this paralysis."
  "name": "Prepare Host"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/humanoid/token/tosculi-warrior-tob1-2023.webp"
```
^statblock

## Environment

desert, underdark
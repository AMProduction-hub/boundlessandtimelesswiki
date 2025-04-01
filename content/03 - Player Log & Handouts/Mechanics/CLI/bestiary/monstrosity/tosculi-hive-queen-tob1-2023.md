---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/12
- ttrpg-cli/monster/environment/desert
- ttrpg-cli/monster/environment/underdark
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/monstrosity
statblock: inline
aliases: ["Tosculi Hive Queen"]
---
# [Tosculi Hive Queen](03 - Player Log & Handouts\Mechanics\CLI\bestiary\monstrosity/tosculi-hive-queen-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 366*  

*This humanoid wasp's gossamer wings beat out a soft, droning buzz. Flashing blades sing in each of her four clawed hands, and the air around her shimmers with magical dust. Dozens more humanoid wasps in a variety of iridescent colors surround her, weapons raised protectively*.

The tosculi are waspfolk that share the Golden Song of the hive, which unites them under the command of their queen. Each hive has its own song, and most tosculi hives are predatory, dangerous places.

## Bow Raiders

Tosculi elite bow raiders are smarter and more capable than drones and common warriors, with midnight black or deep green carapaces that shine with colorful iridescence. Their wings are blood red streaked with dark crimson veins. As rare and prized members of the hive, a bow raider's life is never thrown away or risked unnecessarily. Seldom does a tosculi warband contain more than a handful of these elite soldiers, and they frequently hold positions of command. Elite bow raiders always lead the honor guard for their queen, both within the hive and on those rare occasions when the queen ventures outside.

## Drones

Tosculi drones are the workers of the tosculi hive: the smallest, weakest, least intelligent, and most abundant of the waspfolk. Their carapaces are mostly iridescent blue with gold abdomens and lower legs, and they have vestigial wings, allowing them to glide but not truly fly. Drones function primarily as menial workers but, during times of war, they also act as highly expendable scouts and soldiers. Because the warriors know whatever a drone knows—thanks to the queen—a drone doesn't need to survive its scouting mission to deliver useful information.

## Warriors

Tosculi warriors are overseers of work crews and battle groups of drones, directing activities and relaying commands. Though subservient to the queen's orders, they are capable of acting independently or following their own best judgment, if necessary. The warriors' most important role in the hive is procuring live hosts for incubating tosculi eggs. Creatures paralyzed by warriors are brought to the queen's chamber to have eggs implanted in them, and after a few weeks, the larva hatches, devouring its still-living host.

## Hive Queen

The hive queen is the nerve center of a tosculi hive-city, simultaneously one of a hive's greatest strengths and weaknesses. The queen serves as a unifying force. She binds her swarm with an ironclad sense of purpose through a psychic web, known as the Golden Song, that links all tosculi within a hive. When the hive queen nears the end of her life, she selects the most promising of her immature heirs and feeds the heir a special concoction. This speeds the heir's maturation and makes her ready to become a full-fledged hive queen. The daughter's first action upon her metamorphosis is to devour her mother and all her sisters, absorbing and becoming the emitter of that hive's song. If a hive queen dies with no heir to anchor the hive mind or if the daughter's accession is disrupted, the hive-city plunges into chaos. Tosculi bereft of the hive-mind go berserk. A few fortunate ones might escape and become lone renegades, but their existence without the comforting presence of the hive is miserable and short. Unless one of the hive-queen's surviving daughters is mature enough and ruthless enough to step in and assert control, the hive is doomed.

## A Tosculi Hive Queen's Lair

Hive queens make their lairs deep within the most protected part of the hive. Dozens of corridors lead to her lair, allowing the hive's tosculi to reach their queen at a moment's notice should she need it. This is also the place where tosculi eggs hatch, making it a critical location for the survival of the hive. When encountered in her lair, the tosculi hive queen has a challenge rating of 13 (10,000 XP).

```statblock
"name": "Tosculi Hive Queen (ToB1-2023)"
"size": "Large"
"type": "monstrosity"
"alignment": "Lawful Evil"
"ac": !!int "17"
"hp": !!int "189"
"hit_dice": "18d10 + 90"
"stats":
- !!int "17"
- !!int "24"
- !!int "20"
- !!int "16"
- !!int "16"
- !!int "18"
"speed": "40 ft., fly 60 ft."
"saves":
  "Charisma": !!int "8"
  "Dexterity": !!int "11"
  "Wisdom": !!int "7"
  "Constitution": !!int "9"
"skillsaves":
  "Perception": !!int "7"
"damage_immunities": "poison"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 60 ft., passive Perception 17"
"languages": "Common, Deep Speech, Gnoll, Infernal, telepathy 120 ft., Tosculi"
"cr": "12"
"traits":
- "desc": "If the hive queen fails a saving throw, she can choose to succeed instead."
  "name": "Legendary Resistance (3/Day)"
- "desc": "The hive queen knows the direction and distance to all members of her hive\
    \ and the range of her telepathy extends to 20 miles when communicating with a\
    \ member of her hive."
  "name": "Hive's Heart"
"actions":
- "desc": "The tosculi hive queen makes four Scimitar attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +11 to hit, reach 5 ft., one target. Hit: 14\
    \ (2d6 + 7) slashing damage."
  "name": "Scimitar"
- "desc": "Melee Weapon Attack: +11 to hit, reach 5 ft., one creature. Hit:\
    \ 22 (6d4 + 7) piercing damage, and the target must succeed on a DC 17 Constitution\
    \ saving throw or be [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ for 1 minute. While [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ in this way, the target is also [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed).\
    \ A [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ target can repeat the saving throw at the end of each of its turns, ending the\
    \ effect on itself on a success. The hive queen's potent poison can be removed\
    \ only by the [greater restoration](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/greater-restoration.md)\
    \ spell or similar magic."
  "name": "Stinger"
- "desc": "The hive queen implants an egg into an [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated)\
    \ creature within 5 feet of her that isn't a Construct or Undead. Until the egg\
    \ hatches or is removed, the creature is [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned),\
    \ [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed),\
    \ and doesn't need to eat or drink. The egg hatches after 30 days, and the larval\
    \ tosculi bursts out of the host, killing the host in the process. A creature\
    \ can take its action to remove the egg by succeeding on a DC 20 Wisdom ([Medicine](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Medicine))\
    \ check. Alternatively, a spell or effect that cures disease disintegrates the\
    \ unhatched tosculi."
  "name": "Implant Egg"
"legendary_actions":
- "desc": "The hive queen flies up to half her flying speed without provoking opportunity\
    \ attacks."
  "name": "Flight"
- "desc": "The hive queen makes one Stinger attack."
  "name": "Stinger (Costs 2 Actions)"
- "desc": "The hive queen beats her wings and creates a cloud of glittering, golden\
    \ particles. Each non-tosculi creature within 20 feet of her must succeed on a\
    \ DC 17 Dexterity saving throw or be [blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded)\
    \ until the end of its next turn."
  "name": "Glitter Dust (Costs 2 Actions)"
"lair_actions":
- "desc": "On initiative count 20 (losing initiative ties), the hive queen takes a\
    \ lair action to cause one of the following effects; the hive queen can't use\
    \ the same effect two rounds in a row:"
  "name": ""
- "desc": "- Biting Brood. Hundreds of biting and stinging insects erupt from\
    \ a point on the ground the hive queen can see within 120 feet of her. Each creature\
    \ within 10 feet of that point must make a DC 17 Dexterity saving throw, taking\
    \ 10 (4d4) piercing damage on a failed save, or half as much damage on a successful\
    \ one.  \n- Healing Pheromones. Each tosculi within 60 feet of the hive queen\
    \ (including the hive queen) regains 10 3d6 hp.  \n- Restraining Resin.\
    \ The ceiling above one creature that the hive-queen can see within 120 feet of\
    \ her drips sticky resin. The creature must succeed on a DC 17 Dexterity saving\
    \ throw or be restrained by rapidly-hardening resin. A creature, including the\
    \ target, can take its action to free the restrained target by succeeding on a\
    \ DC 17 Strength check. If the creature is still restrained by the resin on initiative\
    \ count 20 of the next round, the resin fully hardens, and the target is petrified\
    \ in amber until freed or until the hive queen uses this lair action again. The\
    \ resin can be attacked and destroyed (AC 15; 20 hp; vulnerability to bludgeoning\
    \ damage; immunity to piercing, poison, and psychic damage), freeing the target.\
    \  "
  "name": ""
"regional_effects":
- "desc": "The region containing a tosculi hive queen's lair is warped by her presence,\
    \ which creates one or more of the following effects:"
  "name": ""
- "desc": "- Aggressive Wildlife. Beasts within 6 miles of the lair are more violent\
    \ than usual and prone to acts of aggression.  \n- Buzzing Migraine. Creatures\
    \ with an Intelligence of 5 or higher within 3 miles of the lair frequently suffer\
    \ headaches brought on by an insectile buzzing in their minds.  \n- Eyes and\
    \ Ears Everywhere. The hive queen can choose to see or hear through the senses\
    \ of any tosculi within 10 miles of her lair, provided the tosculi is a member\
    \ of her hive.  "
  "name": ""
- "desc": "If the tosculi hive-queen dies, the buzzing disappears immediately, but\
    \ other effects fade over the course of 1d10 days."
  "name": ""
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/monstrosity/token/tosculi-hive-queen-tob1-2023.webp"
```
^statblock

## Environment

desert, underdark
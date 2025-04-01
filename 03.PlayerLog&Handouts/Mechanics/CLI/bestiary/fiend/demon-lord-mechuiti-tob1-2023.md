---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/27
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/size/gargantuan
- ttrpg-cli/monster/type/fiend/demon
statblock: inline
aliases: ["Demon Lord Mechuiti"]
---
# [Demon Lord Mechuiti](03 - Player Log & Handouts\Mechanics\CLI\bestiary\fiend/demon-lord-mechuiti-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 78*  

*A yellow-green fire burns atop the head of this towering, redfurred demon, which resembles an enormous mandrill. It has massive, muscular arms tipped with razor-sharp claws, a slavering jaw filled with huge fangs, and tusks that curl back almost to its blue cheeks.*

Towering around 25 feet tall, Mechuiti, Lord of Cannibal Apes, can stand erect like a human or walk on his knuckles, like a great ape.

## Bloodskull Island

After being expelled from the sweltering jungles and deadly swamps of the Hell of Cannibals, Mechuiti was coughed out of a volcanic portal onto an island now called Bloodskull. Here, he schemes and plots his revenge while breeding demonic minions.

## Corruptor of the Behtu

When Mechuiti first arrived on the Material Plane, he enthralled a group of jungle-dwelling simians, known as the behtu, by visiting their leaders and priests in dreams and nightmares. After convincing these leaders to come to his volcanic home, he infected them with his demonic ichor, transforming them in mind and body, and taught them tattoo magic to give them fiendish power and strength. They returned to their people with this new power and knowledge of the ritual for transforming the rest of their people.

## Bound But Dangerous

Only with the most powerful magic and technology did the ancient people bind him within Bloodskull Island's volcano—the best they could accomplish, since they couldn't destroy him. Despite imprisonment, Mechuiti has remained a terror through the ages. The behtu have not found the key to their master's release, but they still torture and ensorcel unlucky explorers who stumble into their abode, hoping to find someone who can unlock their master's prison.

## Commander of Monsters

Mechuiti commands the behtu to breed fiendish beasts and lizards with his blood: dire apes, fiery giant lizards, and even demonic spiders. He has raised generations of flame dragons, which lair in the volcano's caldera, to guard his temple-fane and deal with threats beyond the behtus' reach.

## Mechuiti's Lair

Mechuiti is trapped within the volcano in his island prison. However, imprisonment hasn't prevented Mechuiti from mustering an army and turning his confinement into a nightmarish bastion.

```statblock
"name": "Demon Lord Mechuiti (ToB1-2023)"
"size": "Gargantuan"
"type": "fiend"
"subtype": "demon"
"alignment": "Chaotic Evil"
"ac": !!int "19"
"ac_class": "natural armor"
"hp": !!int "462"
"hit_dice": "25d20 + 200"
"stats":
- !!int "29"
- !!int "19"
- !!int "27"
- !!int "18"
- !!int "18"
- !!int "22"
"speed": "60 ft., climb 60 ft."
"saves":
  "Dexterity": !!int "12"
  "Wisdom": !!int "12"
  "Strength": !!int "17"
"skillsaves":
  "Intimidation": !!int "14"
  "Religion": !!int "12"
  "Insight": !!int "12"
  "Perception": !!int "12"
  "Arcana": !!int "12"
"damage_vulnerabilities": "cold"
"damage_immunities": "acid; fire; lightning; poison; bludgeoning, piercing, slashing\
  \ from nonmagical attacks"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned),\
  \ [stunned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Stunned)"
"senses": "truesight 120 ft., passive Perception 22"
"languages": "Abyssal, Celestial, Common, Draconic, Primordial, telepathy 300 ft."
"cr": "27"
"traits":
- "desc": "Mechuiti casts one of the following spells, requiring no material components\
    \ and using Charisma as the spellcasting ability (spell save DC 22):\n\nAt will:\
    \ [dispel magic](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/dispel-magic.md),\
    \ [hold monster](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/hold-monster.md),\
    \ [wall of fire](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/wall-of-fire.md)\n\
    \n3/day each: [fire storm](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/fire-storm.md),\
    \ [power word stun](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/power-word-stun.md)"
  "name": "Spellcasting"
- "desc": "When Mechuiti is subjected to piercing damage or slashing damage, a spray\
    \ of caustic blood spurts from his hide. Each creature within 10 feet of Mechuiti\
    \ must succeed on a DC 24 Constitution saving throw or becoming infected with\
    \ the Mechuiti's deadly ichor disease and be [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ until the disease is cured. Every 24 hours that elapse, the target must repeat\
    \ the saving throw, reducing its hp maximum by 14 (4d6) on a failure. This reduction\
    \ lasts until the disease is cured. The creature dies if the disease reduces its\
    \ hp maximum to 0. The disease can be cured by the [greater restoration](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/greater-restoration.md)\
    \ spell or similar magic or when the creature succeeds on three saving throws."
  "name": "Demon Lord's Ichor"
- "desc": "Mechuiti's weapon attacks are magical. When Mechuiti hits with any weapon,\
    \ the weapon deals an extra 6d6 fire damage (included in the attack)."
  "name": "Fiery Weapons"
- "desc": "At the start of each of Mechuiti's turns, each creature within 10 feet\
    \ of him takes 10 (3d6) fire damage and must succeed on a DC 24 Constitution\
    \ saving throw or catch fire. A creature that touches Mechuiti or hits him with\
    \ a melee attack while within 5 feet of him takes 10 (3d6) fire damage and must\
    \ succeed on a DC 24 Constitution saving throw or catch fire. Until a creature\
    \ uses an action to douse the fire, the creature on fire takes 7 (2d6) fire\
    \ damage at the start of each of its turns."
  "name": "Immolating Corona"
- "desc": "If Mechuiti fails a saving throw, he can choose to succeed instead."
  "name": "Legendary Resistance (3/Day)"
- "desc": "Mechuiti has advantage on saving throws against spells and other magical\
    \ effects."
  "name": "Magic Resistance"
- "desc": "Mechuiti can communicate with apes and monkeys as if they shared a language."
  "name": "Speak with Simians"
"actions":
- "desc": "Mechuiti can use his Frightful Presence. He then makes one Bite attack\
    \ and two Claw attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +17 to hit, reach 10 ft., one target. Hit: 31\
    \ (4d10 + 9) piercing damage plus 21 (6d6) fire damage."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +17 to hit, reach 20 ft., one target. Hit: 27\
    \ (4d8 + 9) slashing damage plus 21 (6d6) fire damage. If Mechuiti scores\
    \ a critical hit, he rolls damage dice three times, instead of twice."
  "name": "Claw"
- "desc": "Each creature of Mechuiti's choice that is within 120 feet of Mechuiti\
    \ and aware of him must succeed on a DC 24 Wisdom saving throw or become [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)\
    \ for 1 minute. A creature can repeat the saving throw at the end of each of its\
    \ turns, ending the effect on itself on a success. If a creature's saving throw\
    \ is successful or the effect ends for it, the creature is immune to Mechuiti's\
    \ Frightful Presence for the next 24 hours."
  "name": "Frightful Presence"
- "desc": "Mechuiti exhales fire and acid in a 60-foot cone. Each creature in that\
    \ area must make a DC 24 Dexterity saving throw, taking 49 (14d6) fire damage\
    \ and 49 (14d6) acid damage on a failed save, or half as much damage on a successful\
    \ one."
  "name": "Burning Acid Breath (Recharge 5-6)"
"legendary_actions":
- "desc": "Mechuiti moves up to his speed, or he climbs up to half his speed. This\
    \ movement doesn't provoke opportunity attacks."
  "name": "Move"
- "desc": "Mechuiti chooses a creature within 120 feet of him that is infected with\
    \ the Mechuiti's deadly ichor disease. The target must make a DC 24 Constitution\
    \ saving throw. On a failure, the target takes 10 (3d6) fire damage and 10 (3d6)\
    \ acid damage and catches fire. On a success, the target takes half the damage\
    \ and doesn't catch fire. Until a creature uses an action to douse the fire, the\
    \ target takes 7 (2d6) fire damage at the start of each of its turns."
  "name": "Burn from the Inside"
- "desc": "Mechuiti uses Spellcasting."
  "name": "Cast a Spell (Costs 2 Actions)"
"lair_actions":
- "desc": "On initiative count 20 (losing initiative ties), Mechuiti takes a lair\
    \ action to cause one of the following effects; Mechuiti can't use the same effect\
    \ two rounds in a row:"
  "name": ""
- "desc": "- Searing Torment. The pain of all creatures other than demons within\
    \ 120 feet of Mechuiti is intensified. Until initiative count 20 on the next round,\
    \ each time a creature within 120 feet of Mechuiti takes damage, it must succeed\
    \ on a DC 24 Constitution saving throw or be stunned until the end of its next\
    \ turn.  \n- Split the Earth. A small fissure of lava opens beneath one creature\
    \ Mechuiti can see within 120 feet of him. The target must make a DC 24 Dexterity\
    \ saving throw, taking 28 (8d6) fire damage on a failed save, or half as much\
    \ damage on a successful one.  \n- Toxic Gases. Volcanic gases form a cloud\
    \ in a 20-foot-radius sphere centered on a point Mechuiti can see within 120 feet\
    \ of him. The sphere spreads around corners, and its area is lightly obscured.\
    \ It lasts until initiative count 20 on the next round. Each creature that starts\
    \ its turn in the cloud must succeed on a DC 24 Constitution saving throw or be\
    \ poisoned until the end of its next turn. While poisoned in this way, a creature\
    \ is incapacitated.  \n- Tremor. The whole volcano trembles and shakes. Each\
    \ creature that isn't a demon and that is on a solid surface must succeed on a\
    \ DC 24 Dexterity saving throw or be knocked prone. All ground in the volcano\
    \ becomes difficult terrain for creatures that aren't demons until initiative\
    \ count 20 on the next round.  "
  "name": ""
"regional_effects":
- "desc": "The region containing Mechuiti's lair is warped by his presence, which\
    \ creates one or more of the following effects:"
  "name": ""
- "desc": "- Dream Calling. When a creature with an Intelligence score of 10 or\
    \ higher sleeps within 3 miles of the lair, it dreams of Mechuiti. The creature\
    \ must succeed on a DC 15 Wisdom saving throw when it wakes or be compelled to\
    \ seek out Mechuiti's cult.  \n- Pyroclastic Venting. Mechuiti can make the\
    \ volcano erupt no more than every 7 days. When he does, a cloud of hot ashes\
    \ and smoke covers the area within 6 miles of the volcano, and magma flows from\
    \ the volcano's cone.  \n- Unpotable Water. Water within 1 mile of the lair\
    \ carries disease. A creature that isn't a demon or behtu that drinks the water\
    \ must succeed on a DC 15 Constitution saving throw or become infected with a\
    \ disease and be poisoned until the disease is cured. Every 24 hours that elapse,\
    \ the target must repeat the saving throw, reducing its hp maximum by 5 (2d4)\
    \ on a failure. The disease is cured on a success. This reduction lasts until\
    \ the disease is cured. The creature dies if the disease reduces its hp maximum\
    \ to 0.  "
  "name": ""
- "desc": "If Mechuiti dies, these effects fade immediately."
  "name": ""
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/fiend/token/demon-lord-mechuiti-tob1-2023.webp"
```
^statblock

## Environment

forest, planar
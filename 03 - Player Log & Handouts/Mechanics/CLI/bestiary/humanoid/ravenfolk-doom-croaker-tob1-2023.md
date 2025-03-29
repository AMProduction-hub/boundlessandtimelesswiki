---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/5
- ttrpg-cli/monster/environment/any
- ttrpg-cli/monster/environment/arctic
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/humanoid/ravenfolk
statblock: inline
aliases: ["Ravenfolk Doom Croaker"]
---
# [Ravenfolk Doom Croaker](03 - Player Log & Handouts\Mechanics\CLI\bestiary\humanoid/ravenfolk-doom-croaker-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 305*  

*The creature's face resembles that of a great raven or crow, and it is covered in feathers from head to toe, though without wings.*

The ravenfolk are an avian race of scoundrels, schemers, and sneaks—but they are much more than that. Long ago when Odin brokered the truce that brought peace among the gods, the wily deity magically created the ravenfolk from feathers plucked from his ravens Huginn (Thought) and Muninn (Memory). He placed this new race into the world alongside elves, dwarves, humans, and others to be his eyes and ears.

## Odin's Children

To this day, the ravenfolk are Odin's agents and embody his thought and memory. They are thieves of objects, yes, but primarily, they are thieves of secrets. Their black feathers and long beaks are spotted on the road from place to place, trading information or helping to hatch plots. They are widely viewed as spies, informers, thieves, and troublemakers, but when the ravenfolk swear an oath, they abide by it. Odin grants the best of his ravenfolk magical runespears and runestaves, weapons enchanted to serve his messengers. The ravenfolk consider them special tokens meant for their use, and no one else's.

## Flightless But Bold

Though they have no wings and normally cannot fly, the physiology of ravenfolk is strikingly similar to that of true avians. They stand roughly 5 feet tall and, because of their hollow bones, weigh just 95–105 pounds. Albino ravenfolk are often found in southern climates. Ravenfolk eat almost anything, but they prefer raw meat and field grains, such as corn, soy, and alfalfa. They even scavenge days-old carrion, a practice that repulses most other humanoids.

## Feather Speech

The ravenfolk have two languages: a verbal language full of croaks and whistles and a language of feathers. Ravenfolk can communicate volumes without speaking a word through the dyeing, arrangement, preening, and rustling of their plumage. This language is inherent to ravenfolk, and though others may use magic to understand it, it can't be used by creatures without feathers.

> [!note] Ravenfolk in Midgard
> 
> If the ravenfolk of Midgard have a homeland, it is Beldestan to the East, on a branch of Wotan's tree in the North, or a high cliff of Horus' hidden temple in the South. They have settlements in Trollheim, Vidim, Domovogrod, Zobeck, Nuria Natal, and the Dragon Empire, but none are large.
> 
> They avoid the West and the Seven Cities most of the time and are highly honored in Nuria Natal, where they serve the temples of Horus as sworn guardians, assassins, and seekers of forgotten arcana. Some are said to be members of the Emerald Order, a society devoted to arcane mysteries.
^ravenfolk-in-midgard

```statblock
"name": "Ravenfolk Doom Croaker (ToB1-2023)"
"size": "Medium"
"type": "humanoid"
"subtype": "ravenfolk"
"alignment": "Neutral"
"ac": !!int "14"
"ac_class": "[studded leather](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/items/studded-leather-armor.md)"
"hp": !!int "88"
"hit_dice": "16d8 + 16"
"stats":
- !!int "10"
- !!int "14"
- !!int "12"
- !!int "12"
- !!int "18"
- !!int "14"
"speed": "30 ft."
"saves":
  "Wisdom": !!int "7"
  "Constitution": !!int "4"
"skillsaves":
  "Intimidation": !!int "5"
  "Deception": !!int "5"
  "Perception": !!int "10"
"senses": "darkvision 120 ft., passive Perception 20"
"languages": "Common, Feather Speech, Ravenfolk"
"cr": "5"
"traits":
- "desc": "The doom croaker has advantage on saving throws against spells and other\
    \ magical effects."
  "name": "Magic Resistance"
- "desc": "The doom croaker can mimic animal sounds and Humanoid voices. A creature\
    \ that hears the sounds can tell they are imitations with a successful DC 15 Wisdom\
    \ ([Insight](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Insight))\
    \ check."
  "name": "Mimicry"
- "desc": "The ravenfolk's weapon attacks are magical. When the ravenfolk hits with\
    \ any weapon, the weapon deals an extra 2d8 radiant damage (included in the\
    \ attack)."
  "name": "Rune-Powered Weapons"
"actions":
- "desc": "The doom croaker makes one Peck attack and one Runestaff attack, or it\
    \ makes two Rune Blast attacks. It can replace one attack with a use of Ghost\
    \ Wings or Prophetic Call, if available."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 7 (2d4\
    \ + 2) piercing damage plus 9 (2d8) radiant damage."
  "name": "Peck"
- "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d8\
    \ + 2) bludgeoning damage plus 9 (2d8) radiant damage."
  "name": "Runestaff"
- "desc": "Ranged Spell Attack: +7 to hit, range 120 ft., one target. Hit: 17\
    \ (3d8 + 4) radiant damage."
  "name": "Rune Blast"
- "desc": "The doom croaker furiously \"beats\" a set of phantasmal wings. Each creature\
    \ within 5 feet of the ravenfolk must succeed on a DC 15 Dexterity saving throw\
    \ or be [blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded)\
    \ until the start of its next turn."
  "name": "Ghost Wings"
- "desc": "The ravenfolk doom croaker can cast the [augury](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/augury.md)\
    \ spell and [thaumaturgy](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/thaumaturgy.md)\
    \ cantrip at will, requiring no material components and using Wisdom as the spellcasting\
    \ ability."
  "name": "Prophetic Magic"
- "desc": "The ravenfolk doom croaker caws a prophecy that sounds different to each\
    \ listener. Each creature within 30 feet of the ravenfolk that can hear it must\
    \ make a DC 15 Wisdom saving throw. Ravenfolk have advantage on the saving throw.\
    \ On a failure, a creature hears a prophecy of its doom and is [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)\
    \ for 1 minute. On a success, a creature hears a prophecy of its greatness and\
    \ has advantage on the first attack roll it makes on each of its turns for 1 minute.\
    \ A [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)\
    \ creature can repeat the saving throw at the end of each of its turns, ending\
    \ the effect on itself on a success."
  "name": "Prophetic Caw (Recharge 6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/humanoid/token/ravenfolk-doom-croaker-tob1-2023.webp"
```
^statblock

## Environment

any, arctic
---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/3
- ttrpg-cli/monster/environment/any
- ttrpg-cli/monster/environment/arctic
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/humanoid/ravenfolk
statblock: inline
aliases: ["Ravenfolk Warrior"]
---
# [Ravenfolk Warrior](03 - Player Log & Handouts\Mechanics\CLI\bestiary\humanoid/ravenfolk-warrior-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 304*  

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
"name": "Ravenfolk Warrior (ToB1-2023)"
"size": "Medium"
"type": "humanoid"
"subtype": "ravenfolk"
"alignment": "Neutral"
"ac": !!int "15"
"ac_class": "[studded leather armor](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/items/studded-leather-armor.md)"
"hp": !!int "78"
"hit_dice": "12d8 + 24"
"stats":
- !!int "12"
- !!int "16"
- !!int "14"
- !!int "10"
- !!int "15"
- !!int "10"
"speed": "30 ft."
"saves":
  "Dexterity": !!int "5"
  "Wisdom": !!int "4"
"skillsaves":
  "Deception": !!int "2"
  "Stealth": !!int "5"
  "Perception": !!int "4"
"senses": "darkvision 120 ft., passive Perception 14"
"languages": "Common, Feather Speech, Ravenfolk"
"cr": "3"
"traits":
- "desc": "The ravenfolk warrior can mimic animal sounds and Humanoid voices. A creature\
    \ that hears the sounds can tell they are imitations with a successful DC 12 Wisdom\
    \ ([Insight](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Insight))\
    \ check."
  "name": "Mimicry"
- "desc": "The ravenfolk's weapon attacks are magical. When the ravenfolk hits with\
    \ any weapon, the weapon deals an extra 1d8 radiant damage (included in the\
    \ attack)."
  "name": "Rune-Powered Weapons"
"actions":
- "desc": "The ravenfolk warrior makes one Peck attack and one Runespear attack, or\
    \ it makes two Longbow attacks. It can replace one attack with a use of Ghost\
    \ Wings."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 8 (2d4\
    \ + 3) piercing damage plus 4 (1d8) radiant damage."
  "name": "Peck"
- "desc": "Melee Weapon Attack: +5 to hit, reach 10 ft., one target. Hit: 7\
    \ (1d8 + 3) piercing damage plus 4 (1d8) radiant damage."
  "name": "Runespear"
- "desc": "Ranged Weapon Attack: +5 to hit, range 150/600 ft., one target. Hit:\
    \ 7 (1d8 + 3) piercing damage plus 4 (1d8) radiant damage."
  "name": "Longbow"
- "desc": "The ravenfolk warrior furiously \"beats\" a set of phantasmal wings. Each\
    \ creature within 5 feet of the ravenfolk must succeed on a DC 13 Dexterity saving\
    \ throw or be [blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded)\
    \ until the start of its next turn"
  "name": "Ghost Wings"
"reactions":
- "desc": "When the ravenfolk warrior takes damage while below half its hp maximum,\
    \ it moves up to half its speed without provoking opportunity attacks."
  "name": "Odin's Call (Recharge 6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/humanoid/token/ravenfolk-warrior-tob1-2023.webp"
```
^statblock

## Environment

any, arctic
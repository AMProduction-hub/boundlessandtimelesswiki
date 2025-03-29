---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/6
- ttrpg-cli/monster/environment/any
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/undead
statblock: inline
aliases: ["Angatra"]
---
# [Angatra](03 - Player Log & Handouts\Mechanics\CLI\bestiary\undead/angatra-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 17*  

*The withered creature wrapped in gore-stained rags pulls back a tattered hood to reveal glowing eyes hungry with bloodlust.*

In certain tribes, the breaking of local taboos invites terrible retribution from ancestral spirits, especially if the transgressor was a tribal leader or elder. The transgressor is cursed and cast out from the tribe, then it is hunted and executed.

## Bound Remains Entombed

The body is wrapped head to toe in lamba cloth to soothe the spirit and to bind it within the mortal husk, then sealed in a tomb far from traditional burial grounds so none may disturb it and its unclean spirit does not taint the blessed dead.

## Slow Ritual Cleansing

Each such body is visited every ten years as the tribe performs the famadihana ritual, replacing the lamba bindings and soothing the suffering of the ancestors. Over generations, this ritual expiates their guilt, until at last the once-accursed ancestor is admitted through the gates of the afterlife. If a spirit's descendants abandon their task, or if the sealed tomb is violated, the accursed soul becomes an angatra.

## Angry Spirit

The creature's form becomes animated by a powerful and malicious ancestor spirit, undergoing a horrible metamorphosis within its decaying cocoon. Its fingernails grow into scabrous claws, its skin becomes hard and leathery, and its withered form is imbued with unnatural speed and agility. Within days, the angatra gathers strength and tears its bindings into rags. It seeks out its descendants to share the torment and wrath it endured while its spirit lingered.

```statblock
"name": "Angatra (ToB1-2023)"
"size": "Medium"
"type": "undead"
"alignment": "Neutral Evil"
"ac": !!int "17"
"ac_class": "natural armor"
"hp": !!int "85"
"hit_dice": "10d8 + 40"
"stats":
- !!int "14"
- !!int "20"
- !!int "18"
- !!int "8"
- !!int "12"
- !!int "15"
"speed": "50 ft."
"skillsaves":
  "Stealth": !!int "8"
  "Perception": !!int "4"
"damage_resistances": "necrotic; bludgeoning, piercing, slashing from nonmagical attacks"
"damage_immunities": "poison"
"condition_immunities": "[charmed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Charmed),\
  \ [exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion),\
  \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "darkvision 60 ft., passive Perception 14"
"languages": "the languages it knew in life"
"cr": "6"
"traits":
- "desc": "When a creature that can see the angatra's eyes starts its turn within\
    \ 30 feet of the angatra, the angatra can force it to make a DC 13 Charisma saving\
    \ throw if the angatra isn't [incapacitated](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Incapacitated)\
    \ and can see the creature. On a failed saving throw, the creature's pain threshold\
    \ lowers, and it becomes vulnerable to all damage types until the end of its next\
    \ turn.\n\nUnless surprised, a creature can avert its eyes to avoid the saving\
    \ throw at the start of its turn. If the creature does so, it can't see the angatra\
    \ until the start of its next turn, when it can avert its eyes again. If the creature\
    \ looks at the angatra in the meantime, it must immediately make the save."
  "name": "Agonizing Gaze"
- "desc": "The angatra immediately recognizes any individual descended from its tribe.\
    \ It has advantage on attack rolls against such creatures, and those creatures\
    \ have disadvantage on saving throws against the angatra's traits and attacks."
  "name": "Ancestral Wrath"
- "desc": "The angatra doesn't require air, food, drink, or sleep."
  "name": "Undead Nature"
"actions":
- "desc": "The angatra makes two Claw attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +8 to hit, reach 5 ft., one creature. Hit: 14\
    \ (2d8 + 5) piercing damage, and the creature must succeed on a DC 15 Constitution\
    \ saving throw or be [paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed)\
    \ by pain until the end of its next turn."
  "name": "Claw"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/undead/token/angatra-tob1-2023.webp"
```
^statblock

## Environment

any
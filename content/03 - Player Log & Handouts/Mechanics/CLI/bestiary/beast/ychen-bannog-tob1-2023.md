---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/11
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/grassland
- ttrpg-cli/monster/size/gargantuan
- ttrpg-cli/monster/type/beast
statblock: inline
aliases: ["Ychen Bannog"]
---
# [Ychen Bannog](03 - Player Log & Handouts\Mechanics\CLI\bestiary\beast/ychen-bannog-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 401*  

*The massive oxen shakes its head, sending a flock of birds flying. It groans out a yawn that sets nearby trees rattling.*

Ychen bannogs are massive, ox-like beasts with thick, wooly coats and great horns like the gods' battering rams. They stand over forty feet tall at the shoulder and weigh hundreds of tons. Despite their awe-inspiring size, these towering creatures are peaceful wanderers in the wilderness, where their calls echo for miles.

## Strongest Beasts in the World

Legends are built on the sturdy backs of ychen bannog. They are the strongest beasts of burden in the known world. Tamed ychen bannogs can haul entire communities, or even small castles, and a clever dwarf with a ychen bannog at its disposal can carve out enormous riverbeds, haul enormous stones, or reshape entire valleys with ease.

## Ychen Warships

Giants have a particular affinity with the ychen bannogs. In times of war, giants sometimes build complex siege platforms atop these beasts, making effective transport for small armies of giants. Thankfully, ychen bannogs are rare enough that even seeing one in an army is a tale to be told for generations.

## Louder Than Thunder

When riled, an ychen bannog can bellow loudly enough to shatter stones and knock down walls.

```statblock
"name": "Ychen Bannog (ToB1-2023)"
"size": "Gargantuan"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "17"
"ac_class": "natural armor"
"hp": !!int "186"
"hit_dice": "12d20 + 60"
"stats":
- !!int "28"
- !!int "10"
- !!int "21"
- !!int "3"
- !!int "12"
- !!int "10"
"speed": "50 ft."
"damage_resistances": "bludgeoning"
"condition_immunities": "[exhaustion](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Exhaustion)"
"senses": "passive Perception 11"
"languages": ""
"cr": "11"
"traits":
- "desc": "The ychen bannog deals double damage to objects and structures."
  "name": "Siege Monster"
"actions":
- "desc": "The ychen bannog makes one Gore attack and two Stomp attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +13 to hit, reach 15 ft., one target. Hit: 25\
    \ (3d10 + 9) piercing damage. If the ychen bannog scores a critical hit, it\
    \ rolls damage dice three times, instead of twice."
  "name": "Gore"
- "desc": "Melee Weapon Attack: +13 to hit, reach 10 ft., one target. Hit: 22\
    \ (3d8 + 9) bludgeoning damage. If the target is a creature, it must succeed\
    \ on a DC 17 Strength saving throw or be knocked [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)."
  "name": "Stomp"
- "desc": "The ychen bannog delivers a fearsome bellow in a 60-foot cone that is audible\
    \ out to 1 mile. Each creature in the area must make a DC 17 Constitution saving\
    \ throw. On a failure, a creature takes 44 (8d10) thunder damage and is [deafened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Deafened)\
    \ for 1 hour. On a success, a creature takes half the damage and isn't [deafened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Deafened).\
    \ A creature made of inorganic material such as stone, crystal, or metal has disadvantage\
    \ on this saving throw."
  "name": "Deafening Bellow (Recharge 5-6)"
- "desc": "The ychen bannog moves up to 30 feet in a straight line and can move through\
    \ the space of any Large or smaller creature. This movement doesn't provoke opportunity\
    \ attacks. The first time the ychen bannog enters a creature's space during this\
    \ move, that creature must make a DC 17 Dexterity saving throw. On a failure,\
    \ a creature takes 54 (12d8) bludgeoning damage and is knocked [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone).\
    \ On a success, a creature takes half the damage and isn't knocked [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)."
  "name": "Overrun (Recharge 6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/beast/token/ychen-bannog-tob1-2023.webp"
```
^statblock

## Environment

forest, grassland
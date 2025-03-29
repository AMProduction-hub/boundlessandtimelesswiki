---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/13
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/underwater
- ttrpg-cli/monster/size/gargantuan
- ttrpg-cli/monster/type/beast
statblock: inline
aliases: ["Spinosaurus Dinosaur"]
---
# [Spinosaurus Dinosaur](03 - Player Log & Handouts\Mechanics\CLI\bestiary\beast/spinosaurus-dinosaur-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 103*  

*This massive, blue-skinned saurian lumbers out of the river, depositing a platoon of armed lizardfolk on the bank before releasing a terrifying roar.*

## Friend to Lizardfolk

The spinosaurus is a special saurian bred for size and loyalty by lizardfolk. Lizardfolk prize them like prime warhorses, and lavish them with food and care. As spinosauruses age slowly, most large lizardfolk tribes have several young spinosauruses and one adult spinosaurus in their care, reserving the massive adult for major engagements or when the entire tribe must move at once.

## Enormous Size and Color

This immense saurian has a long, tooth-filled maw, powerful claws, and colorful spines running the length of its back. An adult spinosaurus is 70 feet long and weighs 35,000 pounds or more, while a young spinosaurus is a mere 20 feet long, weighing 6,000 pounds or more.

## Swift Predator

A spinosaurus is at home on both land and water, chasing prey from one to the other when necessary. Though they are carnivores, they have an affinity for lizardfolk and other reptilian humanoids, eating such creatures only if the creatures horribly mistreat them or if they experience extreme starvation with such creatures as the only option for food.

> [!note] Spinosauruses in the Southlands
> 
> The lizardfolk of Veles-Sa in the Southlands use spinosauruses as a mode of transportation. The creatures are large enough to pull barges or to carry a crew of raiders anywhere on the rivers, and they are swift overland. Lizardfolk scouts are especially fond of these enormous reptiles, as they are powerful combatants and can carry a dozen lizardfolk warriors.
> 
> In addition to their role as trained raiders in Veles-Sa, some spinosauruses live in or along most of the major river systems of the Southlands—including the River Nuria. There they are also called "river dragons" or sometimes "river walkers," and they are frequently associated with the worship of Baal-Hotep and Set. They are kept as sacred animals in several river temples, where they are fed regular meals and have been known to grow to enormous size and strength.
> 
> Finally, along the Spice Coast, spinosauruses carry high-value spice cargoes along the coast when banditry is rife or when a lizardfolk mercenary company is available to guard materials going north toward Mhalmet, Nuria, or Ishadia. These Spice Coast beasts are often especially bred for gaudy coloration: green-andorange, blue‑and-gold, and even red-and-black bloodlines have been spotted in the Spice Coast harbors.
^spinosauruses-in-the-southlands

> [!note] Spinosauruses as Mounts
> 
> Spinosauruses mate each year in the winter. A male spinosaurus brings food and helps build an enormous nest of reeds, sticks, and mud. Then the male departs, leaving the female to lay and care for the eggs. Spinosaurus eggs are typically found in nests along riversides or deep in marshes. They are sometimes stolen and sold, generally to lizardfolk and sometimes to daring humans with a knack for training animals. These eggs are worth as much as 2,000 gp apiece; live young are worth twice that. Characters eager for spinosaurus mounts, however, should note that buying or domesticating such an enormous carnivore requires vast quantities of food and patience. They do not take easily to domestication.
> 
> Before it can be ridden in combat, a spinosaurus must practice bearing the weight of its trainer and passengers. They rarely master more than a handful of tricks, but they are extremely comfortable in the water and can be trained to be are aware that some of their riders may not breathe water.
> 
> An adult spinosaurus can carry up to six tons as cargo. Riding a spinosaurus requires an exotic saddle, riding platform, or howdah.
^spinosauruses-as-mounts

```statblock
"name": "Spinosaurus Dinosaur (ToB1-2023)"
"size": "Gargantuan"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "232"
"hit_dice": "15d20 + 75"
"stats":
- !!int "25"
- !!int "9"
- !!int "21"
- !!int "2"
- !!int "11"
- !!int "10"
"speed": "60 ft., swim 40 ft."
"skillsaves":
  "Perception": !!int "5"
"senses": "passive Perception 15"
"languages": ""
"cr": "13"
"traits":
- "desc": "The spinosaurus can hold its breath for 1 hour."
  "name": "Hold Breath"
- "desc": "The spinosaurus never willingly attacks a reptilian Humanoid, such as a\
    \ lizardfolk or dragonborn, unless attacked first. If magically forced to attack\
    \ such a creature, the spinosaurus has disadvantage on attack rolls against it.\
    \ This trait doesn't function if the spinosaurus's rider or tamer directs it to\
    \ attack."
  "name": "Reptilian Affinity"
- "desc": "The spinosaurus deals double damage to objects and structures."
  "name": "Siege Monster"
"actions":
- "desc": "The spinosaurus makes one Bite attack and two Claw attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +12 to hit, reach 15 ft., one target. Hit: 33\
    \ (4d12 + 7) piercing damage. If the target is a Large or smaller creature,\
    \ it is [grappled](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Grappled)\
    \ (escape DC 18). Until this grapple ends, the target is [restrained](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Restrained),\
    \ and the spinosaurus can't Bite another target."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +12 to hit, reach 10 ft., one target. Hit: 21\
    \ (4d6 + 7) slashing damage."
  "name": "Claw"
- "desc": "Melee Weapon Attack: +12 to hit, reach 20 ft., one target. Hit: 16\
    \ (2d8 + 7) bludgeoning damage."
  "name": "Tail"
- "desc": "Each creature of the spinosaurus' choice that is within 120 feet of the\
    \ spinosaurus and aware of it must succeed on a DC 18 Wisdom saving throw or become\
    \ [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)\
    \ for 1 minute. A creature can repeat the saving throw at the end of each of its\
    \ turns, ending the effect on itself on a success. If a creature's saving throw\
    \ is successful or the effect ends for it, the creature is immune to the spinosaurus's\
    \ Frightful Presence for the next 24 hours."
  "name": "Frightful Presence"
"legendary_actions":
- "desc": "The spinosaurus moves up to half its speed without provoking opportunity\
    \ attacks."
  "name": "Move"
- "desc": "The spinosaurus uses Frightful Presence."
  "name": "Roar"
- "desc": "The spinosaurus makes one Tail attack."
  "name": "Tail Attack (Costs 2 Actions)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/beast/token/spinosaurus-dinosaur-tob1-2023.webp"
```
^statblock

## Environment

forest, underwater
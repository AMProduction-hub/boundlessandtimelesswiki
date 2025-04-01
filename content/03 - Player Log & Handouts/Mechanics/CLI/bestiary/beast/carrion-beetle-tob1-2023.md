---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/4
- ttrpg-cli/monster/environment/underdark
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/beast
statblock: inline
aliases: ["Carrion Beetle"]
---
# [Carrion Beetle](03 - Player Log & Handouts\Mechanics\CLI\bestiary\beast/carrion-beetle-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 50*  

*The beetles wore golden bridles and carried huge leather sacks of stone and guano. They marched without stopping; dozens, even hundreds, bringing fresh earth to the white-fungus trees of the great forests. Their claws skittered with a sound like horseshoes slipping on stone, but their multiple legs ensured they never fell. The air around them singed the nostrils with the taint of acid*.

## Beasts of Burden and War

Carrion beetles are powerful beasts of burden with strong jaws and the ability to both climb and burrow. With a wide back, serrated, spiky forelegs, and a narrow head, the carrion beetle is too large to ride on comfortably, but it makes an excellent platform for ballistae and howdahs. Its thick exoskeleton varies from drab brown, tan, and black to shimmering blue green, purple-green, and a highly prized yellow‑orange. The largest carrion beetles make a distinctive wheezing sound when their spiracles are stressed; this noise creates a hum when multiple beetles run or charge on the field of battle.

## Devour Fungi and Carrion

Carrion beetles rarely gather in groups larger than a breeding pair and a small cluster of offspring in the wild. Domesticated varieties travel in herds of 20–40 to feed on fungal forests, scavenge battlefields, devour cave lichen, and scour sewage pits. When breeding season hits, carrion beetles feast on the bodies of large animals. They are often found in symbiotic relationships with deathcap myconids, darakhul, and related species. Many species in the deep underworld consider carrion beetles food and use their exoskeletons to fashion shields and armor (though their chitin is too brittle for weaponry). Purple worms are their major predators. The worms swallow entire caravans when they find the beetles within.

## Domesticated by Ghouls

Domesticated by the darakhul, the carrion beetles live a more complex life. They begin as simple pack animals, with the strongest being trained as war beetles. War beetles often carry ballistae and harpoons fitted with lines for use against flying foes. In late life, the beetles are used as excavators, scouring out tunnels with their acid. After death, their exoskeletons are used both as animated scouting vehicles (ghouls hide within the shell to approach hostile territory) and as armored undead platforms packed with archers and spellcasters.

```statblock
"name": "Carrion Beetle (ToB1-2023)"
"size": "Large"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "127"
"hit_dice": "15d10 + 45"
"stats":
- !!int "19"
- !!int "12"
- !!int "17"
- !!int "1"
- !!int "13"
- !!int "10"
"speed": "30 ft., burrow 20 ft., climb 10 ft."
"condition_immunities": "[paralyzed](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Paralyzed)"
"senses": "darkvision 60 ft., passive Perception 11"
"languages": ""
"cr": "4"
"actions":
- "desc": "The beetle makes one Bite attack and two Claw attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +6 to hit, reach 5 ft, one target. Hit: 10 (1d12\
    \ + 4) piercing damage."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +6 to hit, reach 10 ft., one target. Hit: 7\
    \ (1d6 + 4) slashing damage."
  "name": "Claw"
- "desc": "The carrion beetle spits acid in a 30-foot line that is 5 feet wide. Each\
    \ creature in that line must make a DC 13 Dexterity saving throw, taking 26 (4d12)\
    \ acid damage on a failed save, or half as much damage on a successful one."
  "name": "Acid Spit (Recharge 5-6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/beast/token/carrion-beetle-tob1-2023.webp"
```
^statblock

## Environment

underdark
---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/2
- ttrpg-cli/monster/environment/underdark
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/dragon
statblock: inline
aliases: ["Cave Dragon Wyrmling"]
---
# [Cave Dragon Wyrmling](03 - Player Log & Handouts\Mechanics\CLI\bestiary\dragon/cave-dragon-wyrmling-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 115*  

*Covered in black spikes, the dragon's eyeless head swings from side to side. Darkness creeps from its strange, eel-like hide, spreading like ink in water.*

Apex predators of the underworld, cave dragons are the stuff of nightmare for creatures with little else to fear. They can speak, but they value silence, speaking rarely except when bargaining for food.

## Born to Darkness

Eyeless, these dragons have long, thin spikes that help them navigate tunnels or seal passages around them, preventing foes from outflanking them. Their stunted wings are little more than feelers, useful in rushing down tunnels. Their narrow snouts poke into tight passages, which their tongues scour free of bats and vermin. Young cave dragons and wyrmlings can fly, poorly, but older specimens lose the gift of flight. Cave dragon hide is more like eel skin than reptilian scales, and it grows mottled with brown and black as it ages.

## Ravenous Marauders

Cave dragons are always hungry and ready to eat everything. They devour undead, plant creatures, or anything organic. When feeding, they treat all nearby creatures as both a threat and the next course. Alliances they make only last so long as their allies make themselves scarce when the dragon feeds. They can be bribed with food as easily as with gold, but other attempts at diplomacy typically fail. Cave dragons do form alliances with peoples of the underworld, joining them in battle against enemies, but there is always a price to be paid in flesh, bone, and marrow. Wise allies keep a cave dragon well fed.

## A Hard Life

Limited food underground makes truly ancient cave dragons almost unheard of. The eldest tend to die of starvation after stripping their territory bare of prey. Their nigh-endless hunger leaves the ancients the most likely of cave dragons to form alliances, especially with allies that promise—and deliver—food. On occasion, cave dragons climb to the surface to feed, but their earthbound, plodding pace leaves them outcompeted by other predators or unable to keep up with swift or flying prey. They prefer tight tunnels where they can ambush and outmaneuver prey.

## Edible Hoards and Vertical Lairs

Due to the scarcity of food in their subterranean world, a cave dragon's hoard may consist largely of food sources: bat colonies, enormous beetles, carcasses in states of decay, a cavern infested with shriekers, and whatever else the dragon doesn't immediately devour. Cave dragons are fond of bones and items with strong taste or smell. Vast collections of bones, teeth, ivory, and the shells of huge insects litter their lairs, arranged like artful ossuaries. Large vertical chimneys serve as nesting sites for eggs and are popular resting places when a cave dragon sleeps within its lair. Chimneys just wide enough to hold young cave dragons make preferred ambush sites, as the dragons' tough spikes help hold them in position until prey passes beneath. The oldest cave dragons also retreat to vertical chimneys near nesting sites or within their lairs to die in peace. Stories claim that enormous treasures are heaped up in these ledges, abysses, and other inaccessible locations.

```statblock
"name": "Cave Dragon Wyrmling (ToB1-2023)"
"size": "Medium"
"type": "dragon"
"alignment": "Neutral Evil"
"ac": !!int "16"
"ac_class": "natural armor"
"hp": !!int "52"
"hit_dice": "7d8 + 21"
"stats":
- !!int "19"
- !!int "12"
- !!int "17"
- !!int "8"
- !!int "10"
- !!int "12"
"speed": "30 ft., burrow 20 ft., fly 20 ft."
"saves":
  "Charisma": !!int "3"
  "Dexterity": !!int "3"
  "Wisdom": !!int "2"
  "Constitution": !!int "5"
"skillsaves":
  "Stealth": !!int "3"
  "Perception": !!int "4"
"damage_immunities": "poison"
"condition_immunities": "[blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "blindsight 10 ft., tremorsense 60 ft., passive Perception 14"
"languages": "Draconic"
"cr": "2"
"traits":
- "desc": "The cave dragon naturally suppresses light near it. Bright light within\
    \ 15 feet of the dragon becomes dim light, and dim light within 15 feet becomes\
    \ nonmagical darkness."
  "name": "Darkness Shroud"
- "desc": "The cave dragon can burrow through nonmagical unworked earth and stone.\
    \ While doing so, the dragon can choose whether to leave the material it moves\
    \ through undisturbed or leave a 5-foot diameter tunnel in its wake."
  "name": "Magical Tunneler"
"actions":
- "desc": "Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 9 (1d10\
    \ + 4) piercing damage plus 3 (1d6) poison damage."
  "name": "Bite"
- "desc": "The dragon exhales a cone of black, poisonous gas in a 15-foot cone. Each\
    \ creature in that area must make a DC 13 Constitution saving throw. On a failure,\
    \ a creature takes 14 (4d6) poison damage and is [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ until the end of its next turn. On a success, a creature takes half the damage\
    \ and isn't [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)."
  "name": "Poison Breath (Recharge 5-6)"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/dragon/token/cave-dragon-wyrmling-tob1-2023.webp"
```
^statblock

## Environment

underdark
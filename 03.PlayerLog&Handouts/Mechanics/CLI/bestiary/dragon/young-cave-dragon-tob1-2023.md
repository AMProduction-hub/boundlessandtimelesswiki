---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/9
- ttrpg-cli/monster/environment/underdark
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/dragon
statblock: inline
aliases: ["Young Cave Dragon"]
---
# [Young Cave Dragon](03 - Player Log & Handouts\Mechanics\CLI\bestiary\dragon/young-cave-dragon-tob1-2023.md)
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
"name": "Young Cave Dragon (ToB1-2023)"
"size": "Large"
"type": "dragon"
"alignment": "Neutral Evil"
"ac": !!int "17"
"ac_class": "natural armor"
"hp": !!int "189"
"hit_dice": "18d10 + 90"
"stats":
- !!int "23"
- !!int "12"
- !!int "21"
- !!int "10"
- !!int "12"
- !!int "14"
"speed": "40 ft., burrow 20 ft., climb 20 ft., fly 20 ft."
"saves":
  "Charisma": !!int "6"
  "Dexterity": !!int "5"
  "Wisdom": !!int "5"
  "Constitution": !!int "9"
"skillsaves":
  "Stealth": !!int "5"
  "Perception": !!int "9"
"damage_immunities": "poison"
"condition_immunities": "[blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "blindsight 30 ft., tremorsense 90 ft., passive Perception 19"
"languages": "Common, Darakhul, Draconic"
"cr": "9"
"traits":
- "desc": "The cave dragon naturally suppresses light near it. Bright light within\
    \ 30 feet of the dragon becomes dim light, and dim light within 30 feet becomes\
    \ nonmagical darkness. If this shroud overlaps bright light created by a spell\
    \ of 2nd level or lower, the spell creating the light is dispelled."
  "name": "Darkness Shroud"
- "desc": "The cave dragon can burrow through nonmagical unworked earth and stone.\
    \ While doing so, the dragon can choose whether to leave the material it moves\
    \ through undisturbed or leave a 5-foot diameter tunnel in its wake."
  "name": "Magical Tunneler"
- "desc": "The dragon uses its spikes to hold itself in place while climbing, allowing\
    \ it to climb difficult surfaces, including upside down on ceilings, without needing\
    \ to make an ability check. If it climbs upside down on a ceiling or suspends\
    \ itself on a vertical surface while leaving its claws free, it can't use the\
    \ Ruff Spikes reaction."
  "name": "Spiked Climb"
"actions":
- "desc": "The dragon makes one Bite attack and two Claw attacks."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +10 to hit, reach 10 ft., one target. Hit: 17\
    \ (2d10 + 6) piercing damage plus 7 (2d6) poison damage."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +10 to hit, reach 5 ft., one target. Hit: 13\
    \ (2d6 + 6) slashing damage."
  "name": "Claw"
- "desc": "The dragon exhales a cone of black, poisonous gas in a 30-foot cone. Each\
    \ creature in that area must make a DC 17 Constitution saving throw. On a failure,\
    \ a creature takes 42 (12d6) poison damage and is [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ for 1 minute. On a success, a creature takes half the damage and isn't [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned).\
    \ A creature can repeat the saving throw at the end of each of its turns, ending\
    \ the effect on itself on a success."
  "name": "Poison Breath (Recharge 5-6)"
"reactions":
- "desc": "When a creature moves to a space within 5 feet of the cave dragon, the\
    \ dragon flares its many feelers and spikes. The creature must succeed on a DC\
    \ 17 Dexterity saving throw or take 4 (1d8) piercing damage and be prevented\
    \ from entering that space."
  "name": "Ruff Spikes"
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/dragon/token/young-cave-dragon-tob1-2023.webp"
```
^statblock

## Environment

underdark
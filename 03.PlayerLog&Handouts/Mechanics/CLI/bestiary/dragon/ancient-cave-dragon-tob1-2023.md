---
obsidianUIMode: preview
cssclasses: json5e-monster
tags:
- ttrpg-cli/compendium/src/5e/tob1-2023
- ttrpg-cli/monster/cr/25
- ttrpg-cli/monster/environment/underdark
- ttrpg-cli/monster/size/gargantuan
- ttrpg-cli/monster/type/dragon
statblock: inline
aliases: ["Ancient Cave Dragon"]
---
# [Ancient Cave Dragon](03 - Player Log & Handouts\Mechanics\CLI\bestiary\dragon/ancient-cave-dragon-tob1-2023.md)
*Source: Tome of Beasts 1 (2023 Edition) p. 113*  

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

## A Cave Dragon's Lair

Labyrinthine systems of tunnels, caverns, and chasms make up the world of cave dragons. They claim miles of cave networks as their own. Depending on the depth of their domain, some consider the surface world their territory as well, though they visit only to eliminate potential rivals.

```statblock
"name": "Ancient Cave Dragon (ToB1-2023)"
"size": "Gargantuan"
"type": "dragon"
"alignment": "Neutral Evil"
"ac": !!int "20"
"ac_class": "natural armor"
"hp": !!int "507"
"hit_dice": "26d20 + 234"
"stats":
- !!int "30"
- !!int "12"
- !!int "29"
- !!int "14"
- !!int "16"
- !!int "18"
"speed": "40 ft., burrow 40 ft., climb 40 ft."
"saves":
  "Charisma": !!int "12"
  "Dexterity": !!int "9"
  "Wisdom": !!int "11"
  "Constitution": !!int "17"
"skillsaves":
  "Stealth": !!int "9"
  "Perception": !!int "19"
"damage_immunities": "poison"
"condition_immunities": "[blinded](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Blinded),\
  \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)"
"senses": "blindsight 60 ft., tremorsense 120 ft., passive Perception 29"
"languages": "Common, Darakhul, Draconic"
"cr": "25"
"traits":
- "desc": "The cave dragon emits magical darkness in a 30-foot radius around it. The\
    \ darkness moves with the dragon and spreads around corners. Darkvision can't\
    \ penetrate this darkness, and no natural light can illuminate it. If any of the\
    \ darkness overlaps with an area of light created by a spell of 4th level or lower,\
    \ the spell creating the light is dispelled. At the start of each of its turns,\
    \ the dragon chooses whether this aura is active. A successful [dispel magic](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/dispel-magic.md)\
    \ (DC 15) cast on the dragon suppresses this aura for 1 minute."
  "name": "Darkness Aura"
- "desc": "If the dragon fails a saving throw, it can choose to succeed instead."
  "name": "Legendary Resistance (3/Day)"
- "desc": "The cave dragon can burrow through any unworked earth and stone. While\
    \ doing so, the dragon can choose whether to leave the material it moves through\
    \ undisturbed or leave a 15-foot diameter tunnel in its wake."
  "name": "Magical Tunneler"
- "desc": "The dragon uses its spikes to hold itself in place while climbing, allowing\
    \ it to climb difficult surfaces, including upside down on ceilings, without needing\
    \ to make an ability check. If it climbs upside down on a ceiling or suspends\
    \ itself on a vertical surface while leaving its claws free, it can't use the\
    \ Ruff Spikes reaction."
  "name": "Spiked Climb"
"actions":
- "desc": "The dragon uses its Frightful Presence. It then makes three attacks: one\
    \ with its Bite and two with its Claws."
  "name": "Multiattack"
- "desc": "Melee Weapon Attack: +18 to hit, reach 15 ft., one target. Hit: 21\
    \ (2d10 + 10) piercing damage plus 14 (4d6) poison damage."
  "name": "Bite"
- "desc": "Melee Weapon Attack: +18 to hit, reach 10 ft., one target. Hit: 17\
    \ (2d6 + 10) slashing damage."
  "name": "Claw"
- "desc": "Melee Weapon Attack: +18 to hit, reach 20 ft., one target. Hit: 19\
    \ (2d8 + 10) bludgeoning damage."
  "name": "Tail"
- "desc": "Each creature of the dragon's choice that is within 120 feet of the dragon\
    \ and aware of it must succeed on a DC 20 Wisdom saving throw or become [frightened](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Frightened)\
    \ for 1 minute. A creature can repeat the saving throw at the end of each of its\
    \ turns, ending the effect on itself on a success. If a creature's saving throw\
    \ is successful or the effect ends for it, the creature is immune to the dragon's\
    \ Frightful Presence for the next 24 hours."
  "name": "Frightful Presence"
- "desc": "The dragon exhales a cone of black, poisonous gas in a 90-foot cone. Each\
    \ target in that area must make a DC 25 Constitution saving throw. On a failure,\
    \ a creature takes 91 (26d6) poison damage and is [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)\
    \ until cured by the [greater restoration](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/spells/greater-restoration.md)\
    \ spell or similar magic. On a success, a creature takes half the damage and isn't\
    \ [poisoned](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Poisoned)."
  "name": "Poison Breath (Recharge 5-6)"
"reactions":
- "desc": "When a creature moves to a space within 10 feet of the cave dragon, the\
    \ dragon flares its many feelers and spikes. The creature must succeed on a DC\
    \ 25 Dexterity saving throw or take 13 (3d8) piercing damage and be prevented\
    \ from entering that space."
  "name": "Ruff Spikes"
"legendary_actions":
- "desc": "The dragon makes a Wisdom ([Perception](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/skills.md#Perception))\
    \ check."
  "name": "Detect"
- "desc": "The dragon makes a Tail attack."
  "name": "Tail Attack"
- "desc": "The dragon sweeps its wingless limbs outward. Each creature within 10 feet\
    \ of the dragon must succeed on a DC 25 Dexterity saving throw or take 15 (2d6\
    \ + 8) bludgeoning damage and be pushed up to 10 feet away from the dragon and\
    \ knocked [prone](03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/rules/conditions.md#Prone)."
  "name": "Limb Sweep (Costs 2 Actions)"
"lair_actions":
- "desc": "On initiative count 20 (losing initiative ties), the dragon takes a lair\
    \ action to cause one of the following effects; the dragon can't use the same\
    \ effect two rounds in a row:"
  "name": ""
- "desc": "- Cave-In. The ceiling collapses above one creature the dragon can\
    \ see within 120 feet of it. The creature must make a DC 15 Dexterity saving throw.\
    \ On a failure, a creature takes 10 (3d6) bludgeoning damage and is knocked\
    \ prone and buried. On a success, a creature takes half the damage and isn't knocked\
    \ prone or buried. A buried creature is restrained and unable to breathe or stand\
    \ up. A creature, including the buried creature, can take an action to free the\
    \ buried creature by succeeding on a DC 15 Strength check.  \n- Release the\
    \ Vermin. A 20-foot radius sphere of insects appears centered on a point the\
    \ dragon can see within 120 feet of it. When a creature enters the cloud of insects\
    \ for the first time on a turn or starts its turn there, that creature must make\
    \ a DC 15 Constitution saving throw, taking 11 (2d10) piercing damage on a failed\
    \ save, or half as much damage on a successful one. The cloud of insects lasts\
    \ until initiative count 20 on the next round.  \n- Split the Earth. A crack\
    \ appears in the ground within 120 feet of the dragon that is 10 feet long, 10\
    \ feet wide, and 20 feet deep. Each creature standing on a spot where the crack\
    \ opens must succeed on a DC 15 Dexterity saving throw or fall in, taking falling\
    \ damage. A creature that successfully saves moves with the crack's edge as it\
    \ opens. The crack remains open for 1 minute, until the dragon uses this lair\
    \ action again, or until the dragon dies  "
  "name": ""
"regional_effects":
- "desc": "The region containing a legendary cave dragon's lair is warped by the dragon's\
    \ magic, which creates one or more of the following effects:"
  "name": ""
- "desc": "- Flight of the Beetles. Swarms of vermin within 1 mile of the lair\
    \ increase in both size and number as their populations try to survive the dragon's\
    \ undiscriminating hunger.  \n- Toxic Air. Once each hour, poisonous and odorless\
    \ gases fill random passages and caverns for 1 minute, and just as quickly disperse,\
    \ within 6 miles of the dragon's lair.  \n- Water Underground. Each time the\
    \ dragon's temper flares, but no more often than once every 30 days, flash flooding\
    \ turns tunnels into death traps as tremors create fissures in the stone within\
    \ 6 miles of the lair. On the surface, ponds drain away, and long-dry creek beds\
    \ break their banks in flood.  "
  "name": ""
- "desc": "If the dragon dies, these effects fade over the course of 1d10 days."
  "name": ""
"source":
- "ToB1-2023"
"image": "03%20-%20Player%20Log%20&%20Handouts/Mechanics/CLI/bestiary/dragon/token/ancient-cave-dragon-tob1-2023.webp"
```
^statblock

## Environment

underdark
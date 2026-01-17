## **Characters (as the players experience them this session)**

**Sephire.** Alert, hand never far from his weapon — the absence of obvious evil feels like a trap.

**Minerva.** Quietly unsettled; this place feels _engineered_, not natural.

**Froggo.** Hackles raised — something in the forest is watching.

**Verdian Suyanti.** Taken by the beauty first; danger second.

**Kairos.** Suspicious of how “clean” everything looks.

**Asep.** Immediately clocking wards, roads, and infrastructure — peace here is expensive.

---

## **STRONG START – “The Chase Through the Treeline” (Cold Open, No Rolls Yet)**

**Camera: not on the players.**

Wet leaves. Cracking twigs.  
A woman’s breathing — sharp, ragged, controlled panic.

Boots pounding against soft forest floor. Mist coils between blackened trees. The air is too still.

Behind her — something moves. Not seen. Felt.

A scrape against bark. A ripple through the mist.  
Closer. Faster.

Her foot catches — she stumbles, scrambles up, keeps running.

The trees break open.

---

## **Cut to Lake Zarovich**

The **Pequod** tears through the sky and descends toward the mirror-still lake.  
A pale, visible sun hangs overhead — cold, distant, _deliberate_.

Mist clings to the shoreline… then parts.

On the bank, the woman bursts from the treeline.

Silver hair. Torn cloak. Selûnite moon at her throat. Blood on her sleeve — not mortal.

She looks up — sees the ship.

Relief cracks across her face.

> “Thank Selûne… you’re real.”

Then —

The **thing in the forest moves again.**

---

## **SCENE 1 — THE WELCOMING HORROR (FIRST COMBAT)**

```statblock
"name": "Mistbound Warden"
"size": "Large"
"type": "undead"
"alignment": "Lawful Evil"
"ac": !!int "20"
"ac_class": "mist-forged armor"
"hp": !!int "185"
"hit_dice": "14d10 + 84"
"stats":
- !!int "18"   # STR
- !!int "12"   # DEX
- !!int "22"   # CON
- !!int "10"   # INT
- !!int "14"   # WIS
- !!int "10"   # CHA
"speed": "30 ft., hover (5 ft.)"
"saves":
 "Constitution": !!int "10"
 "Wisdom": !!int "7"
"skillsaves":
  "Perception": !!int "7"
"senses": "darkvision 120 ft., passive Perception 17"
"languages": "Understands Common, but does not speak"
"cr": "9"
"traits":
- "name": "Mistbound Bulwark"
  "desc": "While the Warden has at least 1 mist point (see Reactions), it has resistance to nonmagical bludgeoning, piercing, and slashing damage."
- "name": "Anchor of Dread"
  "desc": "Creatures within 10 ft. of the Warden cannot teleport or be forcibly moved unless they succeed on a DC 17 Strength saving throw."
- "name": "Unyielding"
  "desc": "If reduced to 0 hit points, the Warden instead drops to 1 hit point once per combat as mist knits it back together."
"actions":
- "name": "Grave Halberd"
  "desc": "Melee Weapon Attack: +10 to hit, reach 10 ft., one target. Hit: 19 (3d8+6) slashing damage plus 7 (2d6) necrotic damage."
- "name": "Chain the Living (Recharge 5–6)"
  "desc": "The Warden lashes a creature within 10 ft. with mist. The target must succeed on a DC 17 Strength saving throw or be restrained until the end of the Warden’s next turn."
"reactions":
- "name": "Mist Interposition (2/turn)"
  "desc": "When a creature the Warden can see within 15 ft. is hit, the Warden reduces the damage by 10 and gains 1 mist point (max 3)."
"source":
- "Homebrew"
```

```statblock
"name": "Gloam Stalker"
"size": "Medium"
"type": "undead"
"alignment": "Neutral Evil"
"ac": !!int "18"
"ac_class": "flickering shadow"
"hp": !!int "120"
"hit_dice": "12d8 + 48"
"stats":
- !!int "14"   # STR
- !!int "20"   # DEX
- !!int "16"   # CON
- !!int "12"   # INT
- !!int "14"   # WIS
- !!int "10"   # CHA
"speed": "40 ft., climb 30 ft."
"saves":
 "Dexterity": !!int "10"
"skillsaves":
  "Stealth": !!int "12"
  "Acrobatics": !!int "10"
"senses": "darkvision 120 ft., passive Perception 14"
"languages": "Understands Common"
"cr": "8"
"traits":
- "name": "Shadow Leap"
  "desc": "As a bonus action, the Stalker can teleport up to 30 ft. between shadows."
- "name": "Predator’s Focus"
  "desc": "Once per turn, when the Stalker hits a creature that is not within 10 ft. of an ally, it deals an extra 14 (4d6) necrotic damage."
- "name": "Mist-Shroud"
  "desc": "When first bloodied, the Stalker becomes lightly obscured until the end of its next turn."
"actions":
- "name": "Razor Talons"
  "desc": "Melee Weapon Attack: +10 to hit, reach 5 ft., one target. Hit: 15 (2d8+6) slashing damage plus 7 (2d6) necrotic damage."
- "name": "Hunting Lunge"
  "desc": "The Stalker moves up to its speed without provoking opportunity attacks and makes one Razor Talons attack at the end."
"source":
- "Homebrew"

```

```statblock
"name": "Veiled Reaper (Mist-Binder)"
"size": "Medium"
"type": "undead"
"alignment": "Lawful Evil"
"ac": !!int "17"
"ac_class": "swirling grave-mist"
"hp": !!int "105"
"hit_dice": "10d8 + 50"
"stats":
- !!int "10"   # STR
- !!int "14"   # DEX
- !!int "20"   # CON
- !!int "16"   # INT
- !!int "18"   # WIS
- !!int "14"   # CHA
"speed": "30 ft., fly 30 ft. (hover)"
"saves":
 "Constitution": !!int "10"
 "Wisdom": !!int "9"
"skillsaves":
  "Arcana": !!int "8"
  "Perception": !!int "9"
"senses": "truesight 60 ft., passive Perception 19"
"languages": "Common, Barovian"
"cr": "8"
"traits":
- "name": "Mist Sovereignty"
  "desc": "All mist within 30 ft. of the Reaper counts as difficult terrain for enemies."
- "name": "Tether of Silence"
  "desc": "Creatures restrained by mist within 30 ft. have disadvantage on Constitution saves to maintain concentration."
"actions":
- "name": "Grave Scepter"
  "desc": "Melee or Ranged Spell Attack: +9 to hit, reach 5 ft. or range 60 ft., one target. Hit: 14 (3d6+4) necrotic damage."
- "name": "Bind in the Mist (Recharge 4–6)"
  "desc": "The Reaper chooses a 20-ft. radius area within 60 ft. Creatures in the area must make a DC 18 Strength saving throw or be restrained by clinging mist until the end of their next turn."
- "name": "Snuff the Light"
  "desc": "The Reaper targets one creature it can see. The target must succeed on a DC 18 Constitution saving throw or have disadvantage on attack rolls until the end of its next turn."
"source":
- "Homebrew"

```
---


### HAWA in the fight (character-revealing, not overpowered)

- She does **not panic.**
    
- She casts **calm, precise radiant spells.**
    
- She _positions herself between the creature and the forest_ — not between it and the players.
    

If asked why later:

> “If it returns to the treeline, it will hunt again tonight.”

---

### Aftermath (very important tone moment)

The creature dissolves into mist and is dragged screaming back into the forest.

HAWA exhales slowly. Not relieved. _Resolved._

She turns to the party.

> “Welcome to Barovia.”

No fanfare. No bravado.

---

## **SCENE 2 — THE SHORE OF LAKE ZAROVICH**

HAWA thanks them — calmly, evenly.

Key lines to seed your theme:

- “Barovia is stable. Stability is not the same as safety.”
    
- “What you just saw is what _slips through the cracks._”
    

Players can:

- Inspect the ground (cold, wrong)
    
- Notice that the mist recoils slightly from holy symbols
    
- See ward-markers along the shoreline, some broken
    

---

## **SCENE 3 — THE WALK TO VALLAKI**

Everything you already wrote stays, just framed differently:

- Maintained road
    
- Warded waystones
    
- Patrol signs
    
- Clear signs of organization, not chaos
    

HAWA explains:

- Vampires are “registered.”
    
- Feeding is regulated.
    
- Violence is punished swiftly.
    

She never smiles while saying this.

---

## **SCENE 4 — FIRST NIGHT IN VALLAKI**

Same as your original, but now it lands harder because:

They have already seen the _cost_ of peace.

Details to highlight:

- Laughter exists — but stops when strangers enter
    
- A “Registered Vampire” at a tavern keeps their hands visible
    
- A Selûnite ward hangs over the town gate
    

A child points at the party and whispers:

> “Are they here to help… or to change things?”

---

## **SCENE 5 — ADAM (OBSERVED, NOT INTRODUCED)**

Keep exactly as you had it:

- Seen at a distance
    
- Gone when approached
    
- Always watching the treeline more than the town
    

If players try to track him → the trail simply ends.

---

## **SCENE 6 — THE QUESTION OF STRAHD**

Same line, but now heavier:

> “Strahd von Zarovich is gone. Barovia survived him.”

Implied meaning:

- _Survived — at a cost._
    

---

## **SECRETS AND CLUES (Revised & Sharpened)**

- The sun is **ritual-maintained**, not natural.
    
- Castle Ravenloft is avoided — not forbidden.
    
- Vampires are rationed, marked, and monitored.
    
- Some villages are missing from records.
    
- ADAM is not Barovian, yet moves like he owns the land.
    
- HAWA calls vampires “entities,” never “people.”
    
- Roads are safe. Forests are not.
    
- Mist respects holy symbols more than daylight.
    
- Vallaki’s Burgomaster defers to HAWA quietly.
    
- The lake is strangely barren of life.
    

---

## **FANTASTIC LOCATIONS (unchanged, but more ominous now)**

**Lake Zarovich:** pale sunlight, obedient mist, wrong stars at night

**Vallaki:** orderly, watchful, afraid to admit it is afraid

**Old Svalich Road:** warded, patrolled, expensive peace

**The Treeline:** hungry, patient, not broken

---

## **IMPORTANT NPCs**

**HAWA.** Calm, compassionate, terrifyingly certain.

**ADAM.** Silent enforcer — the price of peace given a face.

**Vallaki Burgomaster.** Rules in name; obeys in practice.

**Registered Vampire.** Polite. Grateful. Tired. A little afraid.

---

## **POTENTIAL MONSTERS (for later sessions)**

- Feral vampire spawn (unregistered)
    
- Mist-touched wolves
    
- Barovian wraiths
    
- The “thing in the tower” of Ravenloft — watching, not yet hostile
    

---

## **POTENTIAL TREASURE**

- Selûnite ward tokens (minor protection charms)
    
- Barovian travel permits (access to restricted zones)
    
- A journal from the _first year after Strahd’s fall_
    
- A cracked holy symbol that still glows faintly
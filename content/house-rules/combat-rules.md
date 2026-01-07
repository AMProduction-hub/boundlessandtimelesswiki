---
title: "Combat Rules"
weight: 40
---

# Combat Rules

These house rules add tactical depth to combat through modified critical hit mechanics, additional Armor Class types, and maneuvers for all martial characters.

---

## Critical Damage

This campaign uses the **Chris Perkins Critical Hit Formula** for more consistent and exciting critical damage.

### How It Works

When you score a critical hit:
1. **Maximize one set** of your weapon's damage dice
2. **Roll one set** of your weapon's damage dice normally
3. **Add** your normal modifiers

{{< hint info >}}
**Formula**: Critical Hit = Max Damage Dice + Rolled Damage Dice + Modifiers
{{< /hint >}}

### Examples

**Greatsword Critical Hit** (2d6 damage)
- Normal hit: 2d6 + STR modifier
- Critical hit: **12** (max 2d6) + 2d6 + STR modifier

**Dagger Sneak Attack Critical Hit** (1d4 + 3d6 sneak attack)
- Normal hit: 1d4 + 3d6 + DEX modifier
- Critical hit: **4** (max 1d4) + **18** (max 3d6) + 1d4 + 3d6 + DEX modifier

**Firebolt Critical Hit** (2d10 fire damage)
- Normal hit: 2d10 fire damage
- Critical hit: **20** (max 2d10) + 2d10 fire damage

### Why This Change?

Standard 5e critical hits can be disappointing (rolling all 1s feels terrible). This method:
- Guarantees meaningful damage on crits
- Still maintains variability with the rolled dice
- Makes critical hits feel impactful

---

## Armor Class Variants

In addition to standard AC, this campaign uses **Touch AC** and **Flat-Footed AC** for certain situations.

### Touch Armor Class (Touch AC)

Touch AC represents how hard you are to touch, ignoring physical armor.

**Touch AC = 10 + Dexterity Modifier + Dodge/Deflection Bonuses + Size Modifier**

{{< hint warning >}}
**Important**: Touch AC does NOT include armor bonuses or shield bonuses.
{{< /hint >}}

#### When Touch AC Is Used

Touch AC is used for attacks that bypass physical armor:
- Spells that require a physical touch (Shocking Grasp, Chill Touch)
- Incorporeal touch attacks (ghosts, specters)
- Certain special abilities that ignore armor

#### Calculating Touch AC

| Armor Type | Standard AC | Touch AC Calculation | Example Touch AC |
|:-----------|:------------|:--------------------|:----------------|
| **Unarmored** (10 + DEX) | 15 | 10 + DEX (+5) | **15** |
| **Leather Armor** (11 + DEX) | 16 | 10 + DEX (+5) | **15** |
| **Chain Mail** (16) | 16 | 10 + DEX (+0) | **10** |
| **Plate Armor** (18) | 18 | 10 + DEX (+0) | **10** |
| **Plate + Shield** (20) | 20 | 10 + DEX (+0) | **10** |

#### Special Cases

**Monk's Unarmored Defense**: Monks add their Wisdom modifier to Touch AC
- Touch AC = 10 + DEX + WIS + Dodge bonuses

**Barbarian's Unarmored Defense**: Barbarians do NOT add Constitution to Touch AC
- Touch AC = 10 + DEX + Dodge bonuses

{{< hint tip >}}
**Quick Rule**: If an attack specifically states it targets Touch AC, calculate it. Otherwise, use standard AC.
{{< /hint >}}

---

### Flat-Footed Armor Class (Flat-Footed AC)

Flat-Footed AC represents your defense when caught off-guard and unable to react.

**Flat-Footed AC = 10 + Armor Bonus + Shield Bonus + Size Modifier**

{{< hint warning >}}
**Important**: Flat-Footed AC does NOT include Dexterity modifier or dodge bonuses.
{{< /hint >}}

#### When Flat-Footed AC Is Used

You use Flat-Footed AC when:
- You are surprised at the start of combat
- You haven't acted yet in the first round of combat
- You are restrained or paralyzed
- An attacker is hidden from you (Sneak Attack)
- You are unconscious or incapacitated

#### Calculating Flat-Footed AC

| Armor Type | Standard AC | Flat-Footed AC Calculation | Example Flat-Footed AC |
|:-----------|:------------|:--------------------------|:---------------------|
| **Unarmored** (10 + DEX) | 15 | 10 only | **10** |
| **Leather Armor** (11 + DEX) | 16 | 11 (base armor) | **11** |
| **Chain Mail** (16) | 16 | 16 (armor only) | **16** |
| **Plate Armor** (18) | 18 | 18 (armor only) | **18** |
| **Plate + Shield** (20) | 20 | 18 + 2 (shield) | **20** |

{{< hint tip >}}
**Quick Rule**: Heavy armor users are relatively safe when Flat-Footed. Dexterity-based characters are vulnerable!
{{< /hint >}}

---

## Superiority Dice & Maneuvers

All martial classes gain access to **Superiority Dice** and **Maneuvers**, giving them more tactical options in combat.

### Superiority Die Overview

- **All martial classes** (Fighter, Barbarian, Ranger, Paladin, Rogue, Monk) gain Superiority Dice
- You start with **1 Superiority Die** at level 3
- Superiority Dice recharge on a **short or long rest**
- **Battle Masters** gain additional Superiority Dice as per their subclass

#### Superiority Die Scaling

| Level Range | Die Size |
|:-----------:|:--------:|
| **1–9** | d6 |
| **10–16** | d8 |
| **17+** | d10 |

---

## Maneuver Progression

You learn maneuvers as you level up, gaining access to more powerful options at higher levels.

### Maneuvers Known Table

| Level | Maneuvers Known | Tier Unlocked |
|:-----:|:---------------:|:--------------|
| **3** | 2 | Basic Maneuvers |
| **5** | 3 | Advanced Maneuvers |
| **7** | 4 | Tactical Maneuvers |
| **9** | 5 | Expert Maneuvers |
| **11** | 6 | Legendary Maneuvers |
| **13** | 7 | Legendary Maneuvers |
| **15** | 8 | Mythic Maneuvers |
| **17** | 9 | Mythic Maneuvers |
| **19** | 10 | Mythic Maneuvers |

{{< hint info >}}
**Battle Masters**: You gain extra Superiority Dice as normal for your subclass. This system gives all martials baseline maneuvers.
{{< /hint >}}

---

## Maneuver List

### Basic Maneuvers (Level 3+)

| Maneuver | Type | Effect |
|:---------|:-----|:-------|
| **Precision Strike** | Attack | Add Superiority Die to an attack roll |
| **Parry** | Defense | Reduce incoming damage by Superiority Die + DEX modifier |
| **Riposte** | Reaction | Make a melee attack against an enemy who misses you |
| **Trip Attack** | Attack | Knock target prone if they fail a STR save (DC = 8 + Prof + STR/DEX) |

### Advanced Maneuvers (Level 5+)

| Maneuver | Type | Effect |
|:---------|:-----|:-------|
| **Disarming Strike** | Attack | Force enemy to drop a weapon/item (STR save) |
| **Menacing Strike** | Attack | Cause fear in the target (WIS save) |
| **Brace** | Reaction | Attack an enemy who moves into your reach |

### Tactical Maneuvers (Level 7+)

| Maneuver | Type | Effect |
|:---------|:-----|:-------|
| **Tactical Push** | Attack | Push enemy 10 feet back (STR save) |
| **Quickstep** | Movement | Move 10 feet as a reaction without provoking opportunity attacks |

### Expert Maneuvers (Level 9+)

| Maneuver | Type | Effect |
|:---------|:-----|:-------|
| **Commanding Shout** | Tactical | Give an ally an extra attack (they use their reaction) |
| **Unbreakable Will** | Defense | Gain advantage on all saves until your next turn |

### Legendary Maneuvers (Level 11+)

| Maneuver | Type | Effect |
|:---------|:-----|:-------|
| **Sweeping Strike** | Attack | Hit two adjacent enemies with one attack |
| **Overpowering Blow** | Attack | Knock enemy back 20 feet (STR save) |
| **Master Duelist** | Attack | Reroll a missed attack once per short rest |

### Mythic Maneuvers (Level 15+)

| Maneuver | Type | Effect |
|:---------|:-----|:-------|
| **Deathblow** | Attack | If target is below 50% HP, they make a CON save or die |
| **Legendary Endurance** | Defense | Ignore one level of exhaustion & resist all damage for 1 turn |
| **Storm of Blades** | Attack | Make 3 attacks using 1 action (Level 19+) |

---

## How Maneuvers Work in Play

1. **Using a Maneuver**: When you use a maneuver, you expend one Superiority Die
2. **Adding the Die**: Roll the Superiority Die and add it to the effect (damage, defense, etc.)
3. **Saving Throws**: If a maneuver requires a save, the DC = 8 + Proficiency Bonus + STR or DEX modifier (your choice)
4. **Recovery**: You regain all expended Superiority Dice on a short or long rest

### Example

**Precision Strike (Level 3 Fighter with 1d6 Superiority Die)**
- You attack with your longsword: roll 14 + 5 (STR) = 19 to hit
- The enemy's AC is 20 (you would miss)
- You use Precision Strike, rolling 1d6 = 4
- New attack roll: 19 + 4 = 23 (hit!)

**Parry (Level 10 Fighter with 1d8 Superiority Die, DEX +2)**
- An enemy hits you for 18 damage
- You use Parry as a reaction
- Roll 1d8 = 6, add DEX +2 = 8 total
- Reduce damage by 8: you take only 10 damage

---

## Strategic Tips

### Building a Combat Style
- **Aggressive Fighters**: Focus on attack maneuvers (Precision Strike, Trip Attack, Sweeping Strike)
- **Defensive Fighters**: Focus on defensive maneuvers (Parry, Riposte, Unbreakable Will)
- **Tactical Leaders**: Focus on support maneuvers (Commanding Shout, Brace)

### Resource Management
- You only have 1 Superiority Die per short rest (unless you're a Battle Master)
- Save it for crucial moments or use it early to gain advantage
- Consider multiclassing with Battle Master for more dice

### Synergy with Class Features
- **Rogues**: Use maneuvers to set up Sneak Attacks
- **Paladins**: Combine with Divine Smite for massive damage
- **Barbarians**: Use while Raging for even better effects

{{< hint tip >}}
**Remember**: Battle Masters get EXTRA Superiority Dice on top of this system, making them the ultimate masters of combat maneuvers!
{{< /hint >}}

---

*These combat rules give martial characters more tactical options and make every fight more dynamic!*

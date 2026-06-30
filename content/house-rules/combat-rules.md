---
title: "Combat Rules"
weight: 40
---

# Combat Rules

These house rules add tactical depth to combat through modified critical hit mechanics and additional Armor Class types.

{{< hint info >}}
**Looking for Maneuvers & Superiority Dice?** That system moved to its own page: **[Maneuvers]({{< relref "maneuvers" >}})**
{{< /hint >}}

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

In addition to standard AC, this campaign uses **Touch AC** and **Flat-Footed AC** for certain situations, plus a cap on how much Dexterity can boost Light armor.

{{< hint tip >}}
**Do I need to track these on my sheet?** Touch AC and Flat-Footed AC only come up in specific situations (see below). You don't need to write them on your sheet — just know how to calculate them quickly when your GM calls for one.
{{< /hint >}}

### Light Armor Dexterity Cap

{{< hint warning >}}
**New Rule**: Light armor now caps your Dexterity bonus to AC, similar to how Medium armor already works in standard 5e.
{{< /hint >}}

In standard 5e, Light armor lets you add your full Dexterity modifier to AC with no limit — meaning a high-Dex character can scale their AC indefinitely just through ability score growth alone. In a high-power campaign where ability scores routinely exceed 20, this lets Light armor users out-scale Heavy armor tanks entirely, which isn't the intended power fantasy.

**Light Armor Dexterity bonus to AC is capped at +5.**

| Armor Type | Dex Bonus Cap | Example at Dex +8 |
|:-----------|:--------------|:-------------------|
| **Light Armor** (Padded, Leather, Studded Leather) | **+5 max** | AC uses +5, not +8 |
| **Medium Armor** (unchanged, standard 5e) | +2 max | AC uses +2, not +8 |
| **Heavy Armor** (unchanged, standard 5e) | No Dex bonus | N/A |

{{< hint info >}}
**Example**: A Rogue with Studded Leather (base AC 12) and a +8 Dexterity modifier would normally have AC 20. With this rule, their Dex bonus is capped at +5, giving them **AC 17** instead.
{{< /hint >}}

This applies to all Light armor types equally and stacks with magic armor bonuses as normal (a Studded Leather +1 still adds its +1 on top of the capped Dex bonus).

{{< hint tip >}}
**Why this matters**: This keeps armor categories meaningfully different at high level. Heavy armor users get a flat, reliable AC. Light armor users get mobility and stealth, but their AC ceiling is now closer to parity with armored frontliners rather than exceeding them indefinitely.
{{< /hint >}}

---

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

{{< hint warning >}}
**Important Interaction**: If your character has low Wisdom, Intelligence, or Charisma, failed saves against Paralysis, Hold Person, and similar effects will drop you to Flat-Footed AC immediately. Combined with the standard 5e rule that **melee attacks against a paralyzed creature are automatic critical hits**, and that **ranged attacks against a paralyzed creature have advantage**, this can turn a single failed save into a very dangerous turn. High-Dex, low-mental-save builds should plan around this — don't rely on AC alone as your only defense.
{{< /hint >}}

---

## Quick Reference: AC Types At A Glance

| AC Type | Includes | Used When |
|:--------|:---------|:----------|
| **Standard AC** | Armor + Dex (capped per armor type) + Shield | Default — almost every attack |
| **Touch AC** | Dex only, no armor/shield | Touch spells, incorporeal attacks |
| **Flat-Footed AC** | Armor + Shield only, no Dex | Surprised, paralyzed, restrained, hidden attacker, unconscious |

---

*These combat rules make every fight more dynamic without slowing down the table. For Maneuvers and Superiority Dice, see the [Maneuvers]({{< relref "maneuvers" >}}) page.*

# 00 — Problem Statement

This document states precisely what is to be proved or disproved. Read it together with
[02-background.md](02-background.md), which supplies the standard facts behind every
definition used here.

## 0. Scope

The target is the **classical Riemann Hypothesis** for the Riemann zeta function `ζ(s)`.
This is *not* the Generalized, Extended, or Grand Riemann Hypothesis (those concern
Dirichlet, Dedekind, and automorphic L‑functions; see [02-background.md](02-background.md)
§7). A proof of GRH would imply RH and is acceptable, but the deliverable bar is RH alone.

## 1. The Riemann zeta function

For complex `s = σ + it` with `σ = Re(s) > 1`, define

```
        ∞
ζ(s)  =  Σ  n^(-s)        (absolutely convergent for Re(s) > 1)
        n=1
```

Equivalently, by the **Euler product** (valid for `Re(s) > 1`):

```
ζ(s)  =  ∏  (1 − p^(-s))^(-1)      product over all primes p.
         p
```

The Euler product is the analytic fingerprint of the primes and the property that
distinguishes ζ from look‑alike Dirichlet series (see doc 06). It implies `ζ(s) ≠ 0`
for `Re(s) > 1`.

### Analytic continuation

`ζ(s)` extends to a meromorphic function on all of `ℂ`, holomorphic everywhere except
for a **single simple pole at `s = 1` with residue `1`**. This continuation is unique
(identity theorem) and is what is meant by "`ζ(s)`" at points with `Re(s) ≤ 1`.

### Functional equation

Define the **completed zeta function**

```
ξ(s)  =  ½ · s · (s − 1) · π^(−s/2) · Γ(s/2) · ζ(s).
```

Then `ξ` is **entire** (the factors cancel the pole at `s=1` and the trivial zeros), and it
satisfies the symmetric functional equation

```
ξ(s)  =  ξ(1 − s).
```

Unwinding gives the asymmetric form

```
ζ(s)  =  2^s · π^(s−1) · sin(πs/2) · Γ(1 − s) · ζ(1 − s).
```

## 2. Zeros of ζ

- **Trivial zeros:** `s = −2, −4, −6, …` (the negative even integers). These come from
  the `sin(πs/2)` / `Γ(s/2)` factors and are fully understood. They are *not* the subject
  of RH.
- **Non‑trivial zeros:** all other zeros. A standard consequence of the Euler product and
  the functional equation is that every non‑trivial zero `ρ` lies in the **critical strip**

  ```
  0 < Re(ρ) < 1.
  ```

  There are infinitely many of them. By `ζ(s̄) = \overline{ζ(s)}` and the functional
  equation, the non‑trivial zeros are symmetric under both `ρ ↦ ρ̄` and `ρ ↦ 1 − ρ`; hence
  they are symmetric about the real axis and about the **critical line** `Re(s) = 1/2`.

## 3. The statement to prove (or disprove)

> **Riemann Hypothesis.** Every non‑trivial zero `ρ` of `ζ(s)` satisfies
> `Re(ρ) = 1/2`.

Equivalently: `ξ(s) = 0 ⟹ Re(s) = 1/2`. Equivalently: `ζ(s)` has no zeros in the open
region `1/2 < Re(s) < 1` (by the symmetry `ρ ↦ 1 − ρ`, ruling out this half rules out the
other).

### Deliverable, stated as a formal theorem target

```
Theorem (RH).  ∀ s ∈ ℂ,  ζ(s) = 0  ∧  ¬(∃ k ∈ ℤ_{>0}, s = −2k)   ⟹   Re(s) = 1/2.
```

or, more cleanly via the completed function,

```
Theorem (RH).  ∀ s ∈ ℂ,  ξ(s) = 0  ⟹   Re(s) = 1/2.
```

A **disproof** is the negation: a demonstration (constructive or non‑constructive but
rigorous) that there exists `s` with `ξ(s) = 0` and `Re(s) ≠ 1/2`.

## 4. What "solved" requires

This statement is the *what*. The *bar* — what a correct argument must satisfy to be
accepted — is defined in [01-acceptance-criteria.md](01-acceptance-criteria.md) and must
be read before any work begins. In one line: a complete rigorous proof of the theorem
above, every step justified or cited, surviving the verification protocol in doc 07 and
the litmus tests in doc 06.

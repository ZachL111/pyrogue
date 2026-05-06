# pyrogue

`pyrogue` keeps a focused Python implementation around game engines. The project goal is to generate deterministic dungeons with field of view and turn scheduling.

## Reason For The Project

I want this repository to be useful as a quick reading exercise: fixtures first, implementation second, verifier last.

## Pyrogue Review Notes

The first comparison I would make is `turn pressure` against `collision risk` because it shows where the rule is most opinionated.

## What It Does

- `fixtures/domain_review.csv` adds cases for turn pressure and map entropy.
- `metadata/domain-review.json` records the same cases in structured form.
- `config/review-profile.json` captures the read order and the two review questions.
- `examples/pyrogue-walkthrough.md` walks through the case spread.
- The Python code includes a review path for `turn pressure` and `collision risk`.
- `docs/field-notes.md` explains the strongest and weakest cases.

## How It Is Put Together

The repository has two validation layers: the original compact policy fixture and the domain review fixture. They are separate so one can change without hiding failures in the other.

The Python code keeps the review rule close to the tests.

## Run It

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/verify.ps1
```

## Check It

The check exercises the source code and the review fixture. `stale` is the high score at 263; `edge` is the low score at 94.

## Boundaries

The fixture set is small enough to audit by hand. The next useful expansion is malformed input coverage, not extra surface area.

# Review Journal

The repository goal stays the same: generate deterministic dungeons with field of view and turn scheduling. This note explains the added review angle.

The local checks classify each case as `ship`, `watch`, or `hold`. That gives the project a small review vocabulary that matches its game engines focus without claiming live deployment or external usage.

## Cases

- `baseline`: `turn pressure`, score 120, lane `watch`
- `stress`: `map entropy`, score 150, lane `ship`
- `edge`: `collision risk`, score 94, lane `hold`
- `recovery`: `visibility`, score 225, lane `ship`
- `stale`: `turn pressure`, score 263, lane `ship`

## Note

A future change should add new cases before it changes the scoring rule.

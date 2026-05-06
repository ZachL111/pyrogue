# Field Notes

The useful part of this repository is the small rule set around turn pressure and collision risk.

The domain cases cover `turn pressure`, `map entropy`, `collision risk`, and `visibility`. They sit beside the smaller starter fixture so the project has both a compact scoring check and a domain-flavored review check.

The model rewards signal and confidence, then pulls back for drag. In this fixture, `edge` shows where that pullback matters most.

The language-specific addition keeps the review model in plain dataclasses and unittest checks.

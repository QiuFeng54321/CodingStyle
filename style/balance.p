DECLARE StartingSaving : REAL
DECLARE ExpectedSaving : REAL

REPEAT
    OUTPUT "Input your starting saving: "
    INPUT StartingSaving
UNTIL StartingSaving > 0

ExpectedSaving <- StartingSaving * (1.05 POW 5)
OUTPUT "Expected saving in 5 years (5%):", ExpectedSaving
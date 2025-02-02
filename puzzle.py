from logic import Symbol, And, Or, Not, model_check

# Defining symbols for each character's type
AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")
BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")
CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Each character must be either a knight or a knave, but not both
base_rules = And(
    Or(AKnight, AKnave), Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave), Not(And(BKnight, BKnave)),
    Or(CKnight, CKnave), Not(And(CKnight, CKnave))
)

# Puzzle 0: A says "I am both a knight and a knave."
knowledge0 = And(
    base_rules,
    AKnave  # Since the statement is false, A must be a knave
)

# Puzzle 1: A says "We are both knaves."
knowledge1 = And(
    base_rules,
    AKnave,  # A must be a knave because the statement is false
    BKnight  # Since the statement "We are both knaves" is false, B must be a knight
)

# Puzzle 2: A says "We are the same kind." B says "We are of different kinds."
knowledge2 = And(
    base_rules,
    AKnave,  # A must be a knave, meaning the statement "We are the same kind" is false
    BKnight  # If they are different, and A is a knave, then B must be a knight
)

# Puzzle 3:
knowledge3 = And(
    base_rules,
    AKnight,  # A must be a knight, since C (a truthful knight) says so
    BKnave,   # B is a knave since he lied about A's statement
    CKnight   # C is a knight, since B falsely claimed otherwise
)

def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")

if __name__ == "__main__":
    main()

import check50
from logic import Symbol, And, model_check
from knights import AKnight, AKnave, BKnight, BKnave, CKnight, CKnave, knowledge0, knowledge1, knowledge2, knowledge3

@check50.check()
def exists():
    "knights.py exists"
    check50.exists("knights.py")

@check50.check(exists)
def test_puzzle0():
    "Puzzle 0 correctly identifies A as a knave"
    assert model_check(knowledge0, AKnave), "A should be a knave in Puzzle 0"
    assert not model_check(knowledge0, AKnight), "A should not be a knight in Puzzle 0"

@check50.check(exists)
def test_puzzle1():
    "Puzzle 1 correctly identifies A as a knave and B as a knight"
    assert model_check(knowledge1, AKnave), "A should be a knave in Puzzle 1"
    assert model_check(knowledge1, BKnight), "B should be a knight in Puzzle 1"
    assert not model_check(knowledge1, AKnight), "A should not be a knight in Puzzle 1"
    assert not model_check(knowledge1, BKnave), "B should not be a knave in Puzzle 1"

@gitcheck50.check(exists)
def test_puzzle2():
    "Puzzle 2 correctly identifies A as a knave and B as a knight"
    assert model_check(knowledge2, AKnave), "A should be a knave in Puzzle 2"
    assert model_check(knowledge2, BKnight), "B should be a knight in Puzzle 2"
    assert not model_check(knowledge2, AKnight), "A should not be a knight in Puzzle 2"
    assert not model_check(knowledge2, BKnave), "B should not be a knave in Puzzle 2"

@check50.check(exists)
def test_puzzle3():
    "Puzzle 3 correctly identifies A as a knight, B as a knave, and C as a knight"
    assert model_check(knowledge3, AKnight), "A should be a knight in Puzzle 3"
    assert model_check(knowledge3, BKnave), "B should be a knave in Puzzle 3"
    assert model_check(knowledge3, CKnight), "C should be a knight in Puzzle 3"
    assert not model_check(knowledge3, AKnave), "A should not be a knave in Puzzle 3"
    assert not model_check(knowledge3, BKnight), "B should not be a knight in Puzzle 3"
    assert not model_check(knowledge3, CKnave), "C should not be a knave in Puzzle 3"

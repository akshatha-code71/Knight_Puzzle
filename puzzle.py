from constraint import Problem

def solve_logic_puzzle():
    # Create a problem instance
    problem = Problem()
    
    # Define variables and their possible values
    people = ["Alice", "Bob", "Charlie"]
    colors = ["Red", "Blue", "Green"]
    problem.addVariables(people, colors)
    
    # Constraints
    problem.addConstraint(lambda a, b, c: a != b and b != c and a != c, people)
    problem.addConstraint(lambda alice: alice != "Red", ["Alice"])
    problem.addConstraint(lambda bob: bob != "Blue", ["Bob"])
    problem.addConstraint(lambda charlie: charlie == "Green", ["Charlie"])
    
    # Find and print solutions
    solutions = problem.getSolutions()
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    solve_logic_puzzle()

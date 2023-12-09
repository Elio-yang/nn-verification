from z3 import *

# Create a Z3 variable
x = Real('x')

# Define the Taylor series expansion for exp(x)
exp_taylor_series = 1 + x + x**2 / 2 + x**3 / 6 + x**4 / 24 + x**5 / 120

# Create a Z3 solver
solver = Solver()

# Add a constraint
constraint = exp_taylor_series > -1

solver.add(constraint)

# Check for satisfiability
result = solver.check()

# Get the model if satisfiable
if result == sat:
    model = solver.model()
    # Get the value of x that satisfies the constraint
    x_value = model[x].as_decimal(18)  # Adjust the precision as needed
    print(f"Satisfiable: x = {x_value}")
else:
    print("Not satisfiable")

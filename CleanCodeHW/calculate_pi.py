import random

# Constants
CIRCLE_RADIUS = 1  # The radius of the circle
NUM_RANDOM_POINTS = 1000000  # Number of random points to generate
CIRCLE_AREA_MULTIPLIER = 4  # Multiplier to calculate the area of the circle
SQUARE_EXPONENT = 2  # Exponent used for calculating squares of x and y
POINT_INCREMENT = 1  # Increment for counting points inside the circle

points_inside_circle = 0

# Randomly generate points and count those inside the circle
for _ in range(NUM_RANDOM_POINTS):
    x = random.uniform(-CIRCLE_RADIUS, CIRCLE_RADIUS)
    y = random.uniform(-CIRCLE_RADIUS, CIRCLE_RADIUS)
    if x**SQUARE_EXPONENT + y**SQUARE_EXPONENT <= CIRCLE_RADIUS**SQUARE_EXPONENT:
        points_inside_circle += POINT_INCREMENT

# Estimate pi based on the number of points inside the circle
estimated_pi = (points_inside_circle / NUM_RANDOM_POINTS) * CIRCLE_AREA_MULTIPLIER

print(f"Estimated value of pi is: {estimated_pi}")

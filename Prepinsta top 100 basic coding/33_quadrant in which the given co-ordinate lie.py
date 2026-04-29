"""
Concept:
A coordinate (x, y) lies in different quadrants based on the signs of x and y.
- (+, +) → Quadrant I
- (-, +) → Quadrant II
- (-, -) → Quadrant III
- (+, -) → Quadrant IV
If x = 0 or y = 0 → lies on axes.

Example:
(3, 4) → Quadrant I
(-2, 5) → Quadrant II

Program: Find Quadrant of a Coordinate
Description:
    Method 1: Using conditional statements (if-elif).
    Method 2: Using tuple of signs for mapping.
Complexity:
    Method 1: Time O(1) | Space O(1)
    Method 2: Time O(1) | Space O(1)
"""

# Method 1: Using if-elif (your standard approach)
x = 3
y = 4

if x > 0 and y > 0:
    print("Point lies in Quadrant I")
elif x < 0 and y > 0:
    print("Point lies in Quadrant II")
elif x < 0 and y < 0:
    print("Point lies in Quadrant III")
elif x > 0 and y < 0:
    print("Point lies in Quadrant IV")
elif x == 0 and y == 0:
    print("Point lies at the Origin")
elif x == 0:
    print("Point lies on Y-axis")
else:
    print("Point lies on X-axis")


# Method 2: Using mapping (intentional different input)
x = -2
y = -3

mapping = {
    (1, 1): "Quadrant I",
    (-1, 1): "Quadrant II",
    (-1, -1): "Quadrant III",
    (1, -1): "Quadrant IV"
}

if x == 0 and y == 0:
    print("Point lies at the Origin")
elif x == 0:
    print("Point lies on Y-axis")
elif y == 0:
    print("Point lies on X-axis")
else:
    sign = (1 if x > 0 else -1, 1 if y > 0 else -1)
    print(f"Point lies in {mapping[sign]}")


# Method 1 output : Point lies in Quadrant I
# Method 2 output : Point lies in Quadrant III

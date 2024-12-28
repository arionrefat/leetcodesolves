import math


def circle_intersection_area(x1, y1, r1, x2, y2, r2):
    # Calculate the distance between the centers
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    # Case 1: No overlap
    if d >= r1 + r2:
        return 0.0

    # Case 2: One circle is inside the other
    if d <= abs(r1 - r2):
        return math.pi * min(r1, r2) ** 2

    # Case 3: Partial overlap
    part1 = r1**2 * math.acos((d**2 + r1**2 - r2**2) / (2 * d * r1))
    part2 = r2**2 * math.acos((d**2 + r2**2 - r1**2) / (2 * d * r2))
    part3 = 0.5 * math.sqrt(
        (-d + r1 + r2) * (d + r1 - r2) * (d - r1 + r2) * (d + r1 + r2)
    )

    area = part1 + part2 - part3

    return area


# Example usage
x1, y1, r1 = 0, 0, 5
x2, y2, r2 = 7, 0, 5
intersection_area = circle_intersection_area(x1, y1, r1, x2, y2, r2)

# Print result with 6 decimal precision
print(f"Intersection area: {intersection_area:.6f}")

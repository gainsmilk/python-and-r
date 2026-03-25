"""
Should a dispatch company accept a freight load?

This perceptron helps dispatchers decide whether to accept a freight load.
Layer 1 (p1) checks if the load makes financial sense - good rate, reasonable
fuel cost, and profitable distance. Rate per mile has the highest weight
because it directly determines revenue.

Layer 2 (p2) checks operational readiness - is a driver free, is a truck
nearby, and can we meet the deadline. Truck location has highest weight
because repositioning an empty truck kills profit.

The final perceptron requires BOTH financial and operational factors to
pass (threshold=2). If either side fails, the load gets rejected. This
prevents dispatchers from accepting loads that look profitable but can't
actually be fulfilled, or loads they can handle but would lose money on.
"""


def perceptron(inputs, weights, threshold):
    return 1 if sum(x * w for x, w in zip(inputs, weights)) >= threshold else 0


# factor 1: is the load financially worth it?
# rate per mile good (1=yes), fuel cost reasonable (1=yes), load distance profitable (1=yes)
p1 = perceptron([1, 1, 0], [3, 2, 1], 4)

# factor 2: can we actually handle this load?
# driver available (1=yes), truck in right area (1=yes), delivery deadline realistic (1=yes)
p2 = perceptron([1, 0, 1], [2, 3, 1], 3)

# final decision: combine financial + operational readiness
result = perceptron([p1, p2], [1, 1], 2)

print("Accept the load:", "YES" if result else "NO")

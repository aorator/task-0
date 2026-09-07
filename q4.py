import numpy as np

hrs = np.array([5, 2, 7, 4, 1, 6, 3, 8, 2, 5])
att = np.array([85, 60, 92, 75, 50, 88, 70, 95, 55, 80])
prev = np.array([70, 55, 80, 65, 40, 75, 60, 85, 45, 68])
final = np.array([78, 50, 90, 70, 38, 85, 62, 94, 42, 75])

for name, arr in [("Hours", hrs), ("Attendance", att), ("Previous", prev), ("Final", final)]:
    print(name, "shape:", arr.shape, "dtype:", arr.dtype)

print("Mean final score:", final.mean())
print("Max final score:", final.max())
print("Min final score:", final.min())
print("Std final score:", final.std())

bonus = final + 5
print("With bonus:", bonus)

pass_mask = final >= 75
print("Pass mask:", pass_mask)
print("Scores >= 75:", final[pass_mask])

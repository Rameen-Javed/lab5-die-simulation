
import numpy as np
import matplotlib.pyplot as plt

rolls = np.random.randint(1, 7, size=1000)

print("First 10 rolls:", rolls[:10])

faces, counts = np.unique(rolls, return_counts=True)

print("\nFace Count Empirical_P Theoretical_P")

for face, count in zip(faces, counts):
    empirical = count / 1000
    theoretical = 1/6

    print(f"{face}      {count}      {empirical:.3f}         {theoretical:.4f}")

plt.hist(rolls,
         bins=np.arange(0.5,7.5,1),
         edgecolor='black')

plt.xlabel("Die Face")
plt.ylabel("Frequency")
plt.title("1000 Die Rolls")

plt.xticks(range(1,7))

plt.savefig("die_rolls.png")

print("\nSaved die_rolls.png")

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pandas as pd
import os

# Always run from this script's directory
os.chdir(os.path.dirname(__file__))
print("Looking for files in:", os.getcwd())
img = mpimg.imread("Fig1_Rubin1978.png")
df = pd.read_csv("NGC4378_Table4_composite.csv")

fig, ax = plt.subplots(figsize=(7,5))
ax.imshow(img, extent=[0,25,0,350], aspect='auto')
ax.plot(df["R_kpc"], df["V_kms"], 'o', mfc='k', mec='w', ms=6, zorder=5, label='NGC 4378 (Table 4)')
ax.set_xlim(0,25); ax.set_ylim(0,350)
ax.set_xlabel('DISTANCE FROM NUCLEUS (kpc)')
ax.set_ylabel('ROTATIONAL VELOCITY (km s$^{-1}$)')
ax.legend(frameon=False, loc='lower right')
plt.tight_layout()
plt.savefig("NGC4378_overlay.png", dpi=300)

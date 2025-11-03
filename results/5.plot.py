import lammps_logfile
import matplotlib.pyplot as plt
import numpy as np

log = lammps_logfile.File("./log.lammps")

# Plot all keywords in the log file
"""
for keyword in log.keywords:
    plt.figure()
    plt.plot(step, log.get(keyword), label=keyword)
    plt.xlabel('Timestep')
    plt.title(keyword)
    plt.legend()
plt.show()
"""

# Plot selected the log file
# Step   Time   Temp   PotEng   KinEng     TotEng  Press    Density     Lx     Ly   Lz  Volume
# Step   Time   Temp   TotEng   c_msdCl[1]  c_msdCl[2]  c_msdCl[3]   c_msdCl[4]

x = (log.get("Time", run_num=1)/1000)
y1 = log.get("TotEng", run_num=1)
y2 = log.get("Press", run_num=1)
y3 = log.get("Lx", run_num=1)
y4 = log.get("Lz", run_num=1)

fig, axs = plt.subplots(2, 2, figsize=(8, 5))
fig.suptitle("Lx evolution vs Time", fontsize=14)

# Plot 1: 
axs[0, 0].plot(x, y1+53900, color='blue')
axs[0, 0].set_title("Total Energy")
axs[0, 0].set_xlabel("Time (ps)")
axs[0, 0].set_ylabel("Energy (kcal/mol)")

# Plot 2: 
axs[0, 1].plot(x, y2, color='green')
axs[0, 1].set_title("Pressure")
axs[0, 1].set_xlabel("Time (ps)")
axs[0, 1].set_ylabel("P (GPa)")

# Plot 3: 
axs[1, 0].plot(x, y3, color='purple')
#axs[1, 0].set_title("Scatter plot")
axs[1, 0].set_xlabel("Time (ps)")
axs[1, 0].set_ylabel("Lx (Å)")

# Plot 4: 
from pandas import Series
axs[1, 1].plot(x, y4, color='red')
#axs[1, 1].set_title("Smoothed (rolling average)")
axs[1, 1].set_xlabel("Time (ps)")
axs[1, 1].set_ylabel("Lz (Å)")

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()


import re
import pandas as pd

# Plot the density_z.dat file
path = "./density_z.dat"  # ajusta ruta si es necesario

def is_numeric_tokens(tokens):
    try:
        [float(t) for t in tokens]
        return True
    except Exception:
        return False

def parse_density_chunks(path):
    blocks, headers = [], []
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        lines = [ln.strip() for ln in f if ln.strip() != ""]
    i, n = 0, len(lines)
    # saltar cabecera comentada
    while i < n and lines[i].startswith("#"):
        i += 1
    # parseo por bloques: 1 línea (3 nums) + varias líneas (4 nums)
    while i < n:
        tok = re.split(r"\s+", lines[i])
        if len(tok) == 3 and is_numeric_tokens(tok):
            headers.append([float(x) for x in tok])
            i += 1
        else:
            i += 1
            continue
        rows = []
        while i < n:
            if lines[i].startswith("#"):
                i += 1
                continue
            tk = re.split(r"\s+", lines[i])
            if len(tk) == 3 and is_numeric_tokens(tk):  # nuevo bloque
                break
            if len(tk) >= 4 and is_numeric_tokens(tk[:4]):
                rows.append([float(t) for t in tk[:4]])
            i += 1
        if rows:
            df = pd.DataFrame(rows, columns=["col1", "col2", "col3", "col4"])
            blocks.append(df)
    return blocks, headers

blocks, headers = parse_density_chunks(path)

# 1) Último paso: X=col2, Y=col3
last = blocks[-1]
plt.figure(figsize=(7,5))
plt.plot(last["col2"], last["col3"], marker='o', linestyle='-', linewidth=1.6)
plt.xlabel("Column 2")
plt.ylabel("Column 3")
plt.title("Last step: Column 2 vs Column 3")
plt.grid(alpha=0.3)
plt.show()

# 2) Cada 10 pasos superpuestos
plt.figure(figsize=(7,5))
for k in range(0, len(blocks), 10):
    dfk = blocks[k]
    label = f"Time {k+1}0000"
    plt.plot(dfk["col2"], dfk["col3"], linewidth=1.2, label=label)
plt.xlabel("Column 2")
plt.ylabel("Column 3")
plt.title("Every 10th step: Column 2 vs Column 3")
plt.grid(alpha=0.3)
plt.legend(fontsize=8, ncol=2)
plt.show()



# Plot density profiles
#Cambia el nombre del archivo si es necesario
path = "dprof_w.csv"

# Leer el archivo CSV
df = pd.read_csv(path, sep=";", skipinitialspace=True, engine="python")

# Mostrar las primeras filas para verificar
print(df.head())

# Asumimos que las dos primeras columnas son X e Y
x = (df.iloc[:, 0]+2323.333333)/100
y = 1+df.iloc[:, 1]/75

# --- Plot ---
plt.figure(figsize=(7,5))
plt.plot(x, y, marker='', linestyle='-', color='gray', linewidth=1.5)
plt.xlabel(df.columns[0])
plt.ylabel(df.columns[1])
plt.title("Plot of column 2 vs column 1")
plt.grid(alpha=0.3)

plt.show()

# --- Plot combinado: CSV + último paso density_z.dat ---
csv_path = "dprof_Cl.csv"  # Cambia al nombre real de tu CSV

# Leer CSV separado por ';' y espacios
df_csv = pd.read_csv(csv_path, sep=r";\s*", engine="python")
x_csv = (df_csv.iloc[:, 0]+2323.333333)/100
y_csv = 0.5+df_csv.iloc[:, 1]/23

# Extraer último bloque de density_z.dat ya cargado
last = blocks[-1]
x_den = last["col2"]
y_den = last["col3"]

# --- Plot conjunto ---
plt.figure(figsize=(7,3))
plt.plot(x_den, y_den, '', linewidth=2, color='purple', label="Cl_lammps")
plt.plot(x_csv, y_csv, '', linewidth=2, color='violet', label="Cl_travis")
plt.plot(x, y, '', linewidth=2, color='royalblue', label="water_travis")
plt.ylabel("Density (scaled)")
plt.xlabel("distance z (Å)")
#plt.title("CSV data + Last density_z.dat block")
plt.grid(alpha=0.3)
plt.legend()
plt.show()



# Plot MSD
csv1 = "msd_Cl_#2.csv"   # Primer CSV

# Leer ambos CSV (separados por ';' y espacios)
df1 = pd.read_csv(csv1, sep=r";\s*", engine="python")

# --- Del primer archivo: Y = col1, X = col2 ---
x1 = (df1.iloc[:, 1]/1000)
y1 = df1.iloc[:, 0]

# --- Regresión lineal ---
coef = np.polyfit(x1, y1, 1)
poly = np.poly1d(coef)
yfit = poly(x1)
r2 = 1 - np.sum((y1 - yfit)**2) / np.sum((y1 - np.mean(y1))**2)

# --- Plot ---d
plt.figure(figsize=(7,3))
plt.plot(x1, y1, 'o-', linewidth=2, color='red', label='Travis MSD')
plt.plot(x, y, 'o-', color='blue', linewidth=2, label='LAMMPS MSD')
#plt.plot(x1, yfit, '-', color='red', label=f"Linear fit: y={coef[0]:.3e}x+{coef[1]:.3e}, R²={r2:.3f}")
plt.xlabel("time (ps)")
plt.ylabel("MSD (pm²/ps)")
#plt.title("Combined plot of two CSV files")
plt.grid(alpha=0.3)
plt.legend()
plt.show() 

"""
Model 1: 2D FDTD Chirped Acoustic Wave Propagation Solver
Simulates spherical acoustic wave focusing to the core focal spot.
"""

import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# 1. FDTD GRID & MEDIUM PARAMETERS
# ==========================================

nx, ny = 200, 200            # Grid resolution
c0 = 1780.0                  # Sound speed in liquid Pb83Li17 (m/s)
rho0 = 9380.0                # Fluid density (kg/m^3)
dx = 0.0085                  # Spatial step size (8.5 mm/cell)
dt = dx / (c0 * np.sqrt(2))  # CFL stability limit

# Time Array
steps = 300
p = np.zeros((nx, ny))       # Pressure field
u = np.zeros((nx, ny))       # X-velocity
v = np.zeros((nx, ny))       # Y-velocity

# Source Ring (Simulating Geodesic Array at r = 0.85 m)
x_center, y_center = nx // 2, ny // 2
radius_cells = 80
angles = np.linspace(0, 2 * np.pi, 64)
source_x = (x_center + radius_cells * np.cos(angles)).astype(int)
source_y = (y_center + radius_cells * np.sin(angles)).astype(int)

# ==========================================
# 2. FDTD TIME-STEPPING ENGINE
# ==========================================

print("Executing 2D Acoustic FDTD Simulation...")
for t_step in range(steps):
    # Velocity field updates
    u[:-1, :] -= (dt / (rho0 * dx)) * (p[1:, :] - p[:-1, :])
    v[:, :-1] -= (dt / (rho0 * dx)) * (p[:, 1:] - p[:, :-1])
    
    # Pressure field update
    p[1:, 1:] -= (rho0 * c0**2 * dt / dx) * (
        (u[1:, 1:] - u[:-1, 1:]) + (v[1:, 1:] - v[1:, :-1])
    )
    
    # Inject Chirped Acoustic Source Pulse
    chirp_freq = 100e3 + (400e3 * (t_step / steps)) # 100 kHz -> 500 kHz Sweep
    source_val = 1e6 * np.sin(2 * np.pi * chirp_freq * t_step * dt)
    p[source_x, source_y] = source_val

# ==========================================
# 3. FIELD VISUALIZATION & REPORT
# ==========================================

peak_focal_pressure_GPa = np.max(p[x_center-2:x_center+2, y_center-2:y_center+2]) / 1e9

print("=== ACOUSTIC FDTD SIMULATION REPORT ===")
print(f"Grid Domain:                     {nx}x{ny} Cells ({nx*dx:.2f} m x {ny*dx:.2f} m)")
print(f"Medium Speed of Sound:           {c0} m/s (Liquid Pb83Li17)")
print(f"Acoustic Chirp Range:            100 kHz -> 500 kHz")
print(f"Calculated Focal Spot Pressure:  {peak_focal_pressure_GPa:.2f} GPa (Constructive Stagnation)")

plt.figure(figsize=(7, 6))
plt.imshow(p, cmap='seismic', origin='lower', extent=[-0.85, 0.85, -0.85, 0.85])
plt.colorbar(label='Acoustic Pressure (Pa)')
plt.title("2D Acoustic FDTD Wave Focusing Field at Stagnation")
plt.xlabel("X Position (Meters)")
plt.ylabel("Y Position (Meters)")
plt.tight_layout()
plt.show()

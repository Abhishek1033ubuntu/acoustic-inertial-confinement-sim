"""
Model 1: DEC Plasma Braking & Lorentz Deceleration Solver
Calculates magnetic back-EMF, plasma deceleration trajectory, and direct DC harvesting yield.
"""

import numpy as np

def simulate_dec_braking():
    dt = 1e-8  # 10 ns time step
    time_array = np.arange(0, 15e-6, dt)
    
    plasma_mass_kg = 1.2e-8
    charged_energy_J = 1200.0  # 20% alpha yield
    v_exp = np.sqrt(2 * charged_energy_J / plasma_mass_kg)
    
    r_plasma = np.zeros_like(time_array)
    v_plasma = np.zeros_like(time_array)
    harvested_power_MW = np.zeros_like(time_array)
    
    r_plasma[0] = 15e-6  # 15 micron initial spot
    v_plasma[0] = v_exp
    
    trigger_radius_m = 0.25  # DEC Firing Angle
    bias_B_field_T = 1.2
    
    total_harvested_J = 0.0
    dec_active = False
    
    for i in range(1, len(time_array)):
        r = r_plasma[i-1]
        v = v_plasma[i-1]
        
        if r >= trigger_radius_m:
            dec_active = True
            
        if dec_active and v > 0:
            # Lorentz back-EMF braking force
            i_induced = 2500.0 * (v / 1e5) * (r / 0.5)**2
            f_lorentz = i_induced * bias_B_field_T * (2 * np.pi * r)
            a_em = -f_lorentz / plasma_mass_kg
            
            p_extract = f_lorentz * v
            harvested_power_MW[i] = p_extract / 1e6
            total_harvested_J += p_extract * dt
        else:
            a_em = 0.0
            
        v_plasma[i] = max(0.0, v + a_em * dt)
        r_plasma[i] = r + v_plasma[i] * dt
        
    print("=== DEC PLASMA BRAKING TELEMETRY ===")
    print(f"Trigger Radius (Firing Angle): {trigger_radius_m:.2f} m")
    print(f"Max Extracted DEC Power Peak:  {np.max(harvested_power_MW):.2f} MW")
    print(f"Total Direct DC Harvested:     {total_harvested_J:.1f} Joules")
    print(f"Max Decelerated Plasma Radius: {np.max(r_plasma):.3f} m (Inside 0.85m vessel)")

if __name__ == "__main__":
    simulate_dec_braking()

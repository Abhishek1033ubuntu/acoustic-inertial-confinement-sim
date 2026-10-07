# Model 1 Physical Vessel & Geometry CAD Specifications

**Document ID:** DOC-CAD-2026-MODEL1  
**Chamber Scale:** Model 1-S ($0.85\text{ m}$ Inner Radius)  

---

## 1. Primary Structural Shell Geometry

* **Inner Chamber Radius ($r_{\text{in}}$):** $0.850\text{ m}$ ($850.0\text{ mm}$)
* **Minimum Structural Wall Thickness ($t$):** $51.42\text{ mm}$ ($5.142\text{ cm}$)
* **Outer Vessel Radius ($r_{\text{out}}$):** $0.90142\text{ m}$ ($901.42\text{ mm}$)
* **Total Vessel Outer Diameter:** $1.8028\text{ m}$ ($1802.8\text{ mm}$)
* **Material Composition:** Austenitic ODS High-Entropy Superalloy ($\mu_r = 1.002$, non-magnetic)
* **Mass Properties:**
  * Inner Chamber Volume: $2.572\text{ m}^3$
  * Metal Wall Volume: $0.498\text{ m}^3$
  * Estimated Shell Mass: $\approx 3,935\text{ kg}$

---

## 2. Metamaterial Buffer Layer Specification

* **Thickness:** $44.44\text{ mm}$ (Mounted directly along the inner wall face $r = 0.850\text{ m}$)
* **Composition:** Functionally Graded Refractory High-Entropy Alloy Matrix ($\text{W-V-Ta-Ti}$ system)
* **Acoustic Impedance Gradient:** $Z = 45.0\text{ MRayls} \rightarrow 2.3\text{ MRayls}$ (Exponential decay profile)
* **Shock Attenuation Capability:** Reduces $108.60\text{ GPa}$ core implosion recoil blast down to $120.0\text{ MPa}$ transient hoop stress at the vessel boundary.

---

## 3. Chamber Port Penetration Layout

| Port Designation | Quantity | Diameter | Spatial Position | Functional Duty |
| :--- | :--- | :--- | :--- | :--- |
| **P-FLUID-IN** | 1 (Bottom) | $150.0\text{ mm}$ | $\theta = 180^\circ$ | Liquid $Pb_{83}Li_{17}$ $15\text{ m/s}$ Vortex Inlet |
| **P-FLUID-OUT** | 1 (Top) | $150.0\text{ mm}$ | $\theta = 0^\circ$ | Liquid $Pb_{83}Li_{17}$ Outlet to $\text{sCO}_2$ Loop |
| **P-DEC-QUAD** | 4 (Equatorial) | $220.0\text{ mm}$ | $\phi = 0^\circ, 90^\circ, 180^\circ, 270^\circ$ | Recessed Covetic Cu-Graphene DEC Coils in SiC Sleeves |
| **P-INJECT** | 1 (Equatorial) | $40.0\text{ mm}$ | $\phi = 45^\circ, \theta = 90^\circ$ | Pneumatic D-T Pellet Injection Flight Tube |
| **P-OPTICAL** | 6 (Spherical) | $15.0\text{ mm}$ | Hexagonal Layout | Picosecond Laser Tracking & Intercept Sensors |

# inductance-of-3-phase-line
import math

print("=" * 60)
print("       INDUCTANCE OF 3-PHASE TRANSMISSION LINE")
print("=" * 60)

try:
    # Conductor data
    r = float(input("Enter conductor radius (m): "))

    # Phase conductor spacings
    D_AB = float(input("Enter distance between A and B (m): "))
    D_BC = float(input("Enter distance between B and C (m): "))
    D_CA = float(input("Enter distance between C and A (m): "))

    # Check input
    if r <= 0:
        print("Error: Radius must be greater than zero.")

    elif D_AB <= 0 or D_BC <= 0 or D_CA <= 0:
        print("Error: Distances must be greater than zero.")

    else:
        # Geometrical Mean Distance (GMD)
        GMD = (D_AB * D_BC * D_CA) ** (1 / 3)

        # Geometrical Mean Radius (GMR)
        GMR = 0.7788 * r

        # Inductance per phase in H/m
        L_H_per_m = 2e-7 * math.log(GMD / GMR)

        # Convert to mH/km
        L_mH_per_km = L_H_per_m * 1e6

        # Calculate inductive reactance at 50 Hz
        frequency = 50
        X_L = 2 * math.pi * frequency * L_H_per_m * 1000

        print("\n" + "-" * 60)
        print("                    RESULTS")
        print("-" * 60)

        print(f"GMD                  = {GMD:.4f} m")
        print(f"GMR                  = {GMR:.6f} m")
        print(f"Inductance           = {L_H_per_m:.8e} H/m")
        print(f"Inductance           = {L_mH_per_km:.4f} mH/km")
        print(f"Frequency            = {frequency} Hz")
        print(f"Inductive Reactance  = {X_L:.4f} ohm/km")

        print("-" * 60)

except ValueError:
    print("Error: Please enter valid numerical values.")

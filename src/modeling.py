import numpy as np

def ion_tunneling(energy, barrier_height, barrier_width, mass=9.109e-31): # mass of electron as default, can be changed for ions
    """Calculates the quantum tunneling probability through a rectangular potential barrier.

    Args:
        energy (float): Energy of the particle (Joule).
        barrier_height (float): Height of the potential barrier (Joule).
        barrier_width (float): Width of the potential barrier (meter).
        mass (float): Mass of the particle (kg). Default is electron mass.

    Returns:
        float: Tunneling probability.
    """
    if energy >= barrier_height:
        return 1.0  # Particle goes over the barrier

    hbar = 1.0545718e-34  # Reduced Planck's constant (Joule-second)

    kappa = np.sqrt(2 * mass * (barrier_height - energy)) / hbar
    tunneling_probability = np.exp(-2 * kappa * barrier_width)

    return tunneling_probability

def microtubule_dynamics():
    pass
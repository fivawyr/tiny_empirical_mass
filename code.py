from random import uniform
from vpython import graph, color, gcurve, canvas, vector, sphere
import math
 
type f32 = float 
type i32 = int 

a = float(input("Please enter your desiered input for the mass number (A): "))
z = float(input("Please enter your desiered input for the atomic number (Z): "))
a_1 = 15.8
a_2 = 18.3
a_3 = 0.714
a_4 = 23.2

def calc_binding(a: f32, z: f32) -> float: 
    n = a - z    
    if z % 2 == 0 and n % 2 == 0:
        a_5 = 12.0
    elif z % 2 != 0 and n % 2 != 0:
        a_5 = -12.0
    else:
        a_5 = 0.0

    b = a_1 * a - a_2 * (a**(2/3)) - a_3 * (z**2 / a**(1/3)) - a_4 * ((a - 2*z)**2 / a)+ (a_5 / (a**(1/2)))
    return b 
graph(title="binding energy per nucleon", xtitle="A", ytitle="B/A [MeV]")
curve = gcurve(color=color.red)
for A in range(10, 260): 
    Z_max = max(range(1, A), key=lambda Z: calc_binding(A, Z))
    curve.plot(A, calc_binding(A, Z_max) / A)

def show_core(A, Z):
    canvas(title=f"A = {A}, Z = {Z}", width = 700, height = 500)
    R = 1.2 * A**(1/3)
    for idx in range(A): 
        while True: 
            point = vector(*(uniform(-R, R) for _ in range(3))) # Get a random number in the range [a, b) or [a, b] depending on rounding ~pydoc
            if point.mag <= R: 
                break
        sphere(pos=point, radius=0.45, color=color.orange if idx < Z else color.cyan)

show_core(56, 26)

# print(f"the binding energy is: {b_energy:.4} MeV.")
# print(f"also the binding energy per nuclean: {b_energy / a}")

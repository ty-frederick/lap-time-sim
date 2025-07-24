import numpy as np

# Problem Constrants 
amax = 49.0  # max total acceleration about 5g
r = 320.0  # curve radius (m)
track_length = 4022.5  # full track length (m)
ds = 0.1  # spatial resolution (m)
tolerance = 1e-3  # time within (s)
initial_speed = 25.0  # starting speed (m/s) nascar rolling start

# Track defined 
circle_length = np.pi * r
straight_length = (track_length - 2 * circle_length) / 2

# Segments: list of (length, is_curve)
segments = [
    (straight_length, False),
    (circle_length, True),
    (straight_length, False),
    (circle_length, True)
]

#Make track 
track = []
for length, is_curve in segments:
    i = int(length / ds)
    for _ in range(i):
        track.append({'is_curve': is_curve, 'radius': r if is_curve else np.inf})

i_total = len(track)

#Find max speed of curves 
for point in track:
    radius = point['radius']
    if np.isinf(radius):
        point['v_max'] = np.inf
    else:
        # v_max = sqrt(a_max * r) from a_c = v^2 / r
        point['v_max'] = np.sqrt(amax * radius)

# One Lap
def simulate_lap(v_start):
    v_profile = np.zeros(i_total)
    v_profile[0] = v_start

    #Speed up
    for j in range(1, i_total):
        r_j = track[j - 1]['radius']
        a_c = 0 if np.isinf(r_j) else (v_profile[j - 1] ** 2) / r_j  # a_c = v^2 / r
        if a_c >= amax:
            a_t = 0
        else:
            # a_t = sqrt(a_max^2 - a_c^2)
            a_t = np.sqrt(amax ** 2 - a_c ** 2)

        # v^2 = v0^2 + 2*a*ds
        v_possible = np.sqrt(v_profile[j - 1] ** 2 + 2 * a_t * ds)
        # curve speed limit
        v_profile[j] = min(v_possible, track[j]['v_max'])

    #breaking 
    for j in reversed(range(i_total - 1)):
        r_j = track[j + 1]['radius']
        a_c = 0 if np.isinf(r_j) else (v_profile[i + 1] ** 2) / r_j  # a_c = v^2 / r
        if a_c >= amax:
            a_t = 0
        else:
            # a_t = sqrt(a_max^2 - a_c^2)
            a_t = np.sqrt(amax ** 2 - a_c ** 2)

        # braking: v^2 = v_next^2 + 2*a*ds (a is positive; slowing down)
        v_possible = np.sqrt(max(v_profile[j + 1] ** 2 + 2 * a_t * ds, 0))
        # limit current speed if can't slow down in time
        v_profile[j] = min(v_profile[j], v_possible)

    # Time calculations 
    times = ds / np.maximum(v_profile, 1e-5)  # dt = ds / v
    total_time = np.sum(times)

    return total_time, v_profile[0], v_profile[-1]

# Until Convergence 
lap_times = []
v_start = initial_speed
max_laps = 100

for lap in range(1, max_laps + 1):
    lap_time, v0, vf = simulate_lap(v_start)
    lap_times.append(lap_time)

    print(f"Lap {lap} - Time: {lap_time:.4f} s, Final speed: {vf:.4f} m/s")

    if lap > 1 and abs(lap_times[-1] - lap_times[-2]) < tolerance:
        print(f"Converged after {lap} laps.")
        break

    v_start = vf  # Use final speed as starting speed for next lap
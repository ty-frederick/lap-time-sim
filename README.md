# Lab Simulator – Physics-Based Lap Time Estimator

This project was created for a physics-focused class to simulate the fastest possible lap time around a racetrack under a 5g total acceleration limit. The code uses physics equations to handle centripetal and tangential acceleration, solving the problem through recursive simulation over multiple laps.

While this is technically a coding project, it was more of a physics simulation that used programming to make the analysis possible. The main goal was to explore how acceleration limits constrain a car’s lap time, particularly around curves.

---

## What I Learned

- **How to apply physics concepts (acceleration limits, circular motion)** to computational simulations.
- **How to use loops and step-based simulation** to solve time-dependent problems.
- **How recursive feedback (convergence)** can help simulate stable physical systems.
- **Importance of input flexibility and code optimization** for large-scale simulations.

---

## Future Improvements

- **Add user input options** for track length, radius, and acceleration limits.
- **Improve UI/UX** to make the tool easier for non-programmers to use.
- **Visualize the velocity profile** across the track using graphs.
- **Optimize data handling and reduce unnecessary recursion** to improve performance.

---

## How to Run

You need Python and NumPy installed.

1. Open a terminal.
2. Navigate to the folder with the script.
3. Run:

```bash
python lab_simulator.py
```
---
## Output Example 

THe simulator prints the lap time and final velocity for each lap until system stabilizes:

```
Lap 1 - Time: 101.5428 s, Final speed: 37.2134 m/s
Lap 2 - Time: 101.1112 s, Final speed: 37.3249 m/s
Lap 3 - Time: 100.9785 s, Final speed: 37.3548 m/s
Converged after 3 laps.
```
---
## Acknowledgments 

This project was created for a freshman-level lab course at Purdue. It reflects early efforts to combine real-world physics with basic programming tools.
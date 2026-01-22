<!-- ======================= -->
<!-- PROBLEM 2.21            -->
<!-- ======================= -->
## Problem 2.21

### Part a

For $A = |\mathbf{A}| < 1$ we have the standard polar equation of a Kepler ellipse with focus at the origin

$$
r(\theta) = \frac{l}{1 + A \cos\theta}, \quad l = \frac{J^2}{m k}.
$$

For an ellipse with eccentricity $e$ and semi-major axis $a$ we have

$$
l = a(1 - e^2), \quad A = e.
$$

Therefore,

$$
a = \frac{l}{1 - A^2} = \frac{J^2/m k}{1 - A^2}.
$$

The semi-minor axis $b$ is given by $b = a\sqrt{1 - e^2} = a\sqrt{1 - A^2}$, so that the area of the ellipse is

$$
\text{Area} = \pi ab = \pi \frac{J^4}{m^2 k^2 (1 - A^2)^{3/2}}. \tag{2.21.1}
$$

### Part b

In the plane of mition, the swept area rate is given by

$$
\frac{dS}{dt} = \frac{1}{2}|\mathbf{x} \times \dot{\mathbf{x}}| = \frac{1}{2m}|\mathbf{x} \times \mathbf{p}| = \frac{J}{2m}.
$$

Over a full period $T$ the total area swept is the area of the ellipse, so

$$
S(T) = \mathrm{Area} = \frac{J}{2m} T \stackrel{(2.21.1)}{=} \pi a^2\sqrt{1 - A^2} \tag{2.21.2}
$$

Recall that

$$
A^2 = 1 + \frac{2J^2}{mk^2} E \quad\Rightarrow\quad J = k \sqrt{\frac{m(1 - A^2)}{-2E}}. \tag{2.21.3}
$$

Substituting (2.21.3) into (2.21.2) we find

$$
\begin{align}
T &= \frac{2m\pi a^2\sqrt{1 - A^2}}{k\sqrt{m(1 - A^2)/-2E}} \\
&= \frac{2\pi a^2 \sqrt{m}}{k} \sqrt{-2E} \\
&= \frac{\pi k}{\sqrt{2}} m^{1/2}(-E)^{-3/2} \\
&= \pi GM (-\tilde{E})^{3/2} \quad \text{where } \tilde{E} = E/m.
\end{align}
$$

In the last step we used the fact that $a = -k/2E$, which can be derived by finding the roots of the equation $Er^2 + kr - J^2/2m = 0$ for $r$: $r_\pm$ and realizing that $r_- + r_+ = 2a$.

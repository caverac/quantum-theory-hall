# Chapter 2: A First Approach to Classical Mechanics

<!-- ======================= -->
<!-- PROBLEM 2.1             -->
<!-- ======================= -->

## Problem 2.1

If the particle starts at $x_0 < x_1$ ($t=0$) then it will be moving to the right, and $dx/dt > 0$, which means

$$
\frac{dx}{dt} = +\sqrt{\frac{2}{m}\left(E_0 - V(x)\right)}.
$$

Or equivalently, the time it would take to move from $x_0$ to $x_1$ is given by

$$
\int_0^t dt = \int_{x_0}^{x_1} dx \sqrt{\frac{m}{2\left(E_0 - V(x)\right)}} = t.
$$

Assuming

![Potential Energy](assets/generated/potential_energy.png)

*Figure 2.1: Sketch of the potential energy as a function of position. Points $x_0$ and $x_1$ are marked, indicating the region $x_0 \leq x \leq x_1$ such that $V(x) < E_0$.*

<!-- ======================= -->
<!-- PROBLEM 2.2             -->
<!-- ======================= -->

## Problem 2.2

### Part a

Assume that $V$ is at least $C^2$ near $x_1$, using a Taylor expansion about $x_1$ we have

$$
\begin{align}
V(x) &= V(x_1) + V'(x_1)(x - x_1) + \mathcal{O}((x - x_1)^2) \\
&\simeq E_0 + V'(x_1)(x - x_1),
\end{align}
$$

and since $x < x_1$ we can write

$$
E_0 - V(x) \simeq V'(x_1)(x_1 - x),
$$

with $V'(x_1) > 0$ since the potential is increasing at $x_1$. Consider now $\epsilon > 0$ such that the time to reach $x_1$ from $x_0$ can be split as

$$
\begin{align}
t &= \int_{x_0}^{x_1}dx \sqrt{\frac{m}{2\left(E_0 - V(x)\right)}} \\
&= \underbrace{\int_{x_0}^{x_1 - \epsilon}dx \sqrt{\frac{m}{2\left(E_0 - V(x)\right)}}}_{\tau, ~\text{finite}} + \int_{x_1 - \epsilon}^{x_1}dx \sqrt{\frac{m}{2\left(E_0 - V(x)\right)}} \\
&\approx \tau + \int_{x_1 - \epsilon}^{x_1}dx \sqrt{\frac{m}{2V'(x_1)(x_1 - x)}} \\
&= \tau + \sqrt{\frac{m}{2V'(x_1)}} \int_{x_1 - \epsilon}^{x_1}dx (x_1 - x)^{-1/2} \\
&= \tau + 2\sqrt{\frac{m}{2V'(x_1)}} \epsilon^{1/2},
\end{align}
$$

which is finite as $\epsilon \to 0$. Therefore, the time to reach $x_1$ is finite.

### Part b

In this case

$$
\begin{align}
V(x) &= E_0 + V'(x_1)(x - x_1) + \frac{1}{2}V''(x_1)(x - x_1)^2 + \mathcal{O}((x - x_1)^3) \\
& \simeq E_0 + \frac{1}{2}V''(x_1)(x - x_1)^2,
\end{align}
$$

or

$$
E_0 - V(x) = -\frac{1}{2}V''(x_1)(x - x_1)^2.
$$

The argument follows as before, splitting the time integral. So we we will only consider the integral close to $x_1$:

$$
\int_{x_1 - \epsilon}^{x_1} dx ~ (x_1 - x)^{-1} \to \infty.
$$

Thus, the time to reach $x_1$ diverges.

<!-- ======================= -->
<!-- PROBLEM 2.3             -->
<!-- ======================= -->

## Problem 2.3

![Pendulum](assets/generated/pendulum.png)

*Figure 2.3a: We want to find the time the pendulum takes to swing from the initial angle $\theta(0) = \pi - \delta$ to the final angle $\theta_0$ (shaded blue region).*

The potential energy for the mass on the pendulum is given by

$$
V(\theta) = mgL(1 - \cos\theta),
$$

and the kinetic energy is

$$
K(\theta) = \frac{1}{2}mL^2 \dot{\theta}^2.
$$

The total energy is then

$$
E = \frac{1}{2}mL^2 \dot{\theta}^2 + mgL(1 - \cos\theta).
$$

We can evaluate the total energy at $t=0$ ($\dot{\theta}(0) = 0$):

$$
E = mgL (1 - \cos(\pi - \delta)) = mgL(1 + \cos\delta).
$$

Therefore

$$
mgL(1 + \cos\delta) = \frac{1}{2}mL^2 \dot{\theta}^2 + mgL(1 - \cos\theta),
$$

or equivelently

$$
\dot{\theta}^2 = 2 \omega^2 (\cos\theta + \cos\delta), \quad \omega^2 = g/L.
$$

The time it takes the pendulum to swing from $\theta(0) = \pi - \delta$ to $\theta_0$ is given by

$$
t(\delta) = \frac{1}{\sqrt{2}\omega}\int_{\theta_0}^{\pi - \delta} d\theta \frac{1}{\sqrt{\cos \theta + \cos\delta}}.
$$

Define $\phi = \pi - \theta$, such that $\phi(0) = \delta$ and

$$
t(\delta) = \frac{1}{\sqrt{2}\omega}\int_{\delta}^{\phi_0} d\phi \frac{1}{\sqrt{\cos \delta - \cos\phi}}.
$$

For small $\delta$, or oquivalently for $\phi$ close to zero, we can write

$$
\cos\delta - \cos\phi \simeq \frac{1}{2}(\phi^2 - \delta^2).
$$

Take $\epsilon$ and split the integral as

$$
t(\delta) = \frac{1}{\sqrt{2}\omega}\left(\int_\delta^\epsilon + \int_{\epsilon}^{\phi_0} \right) \frac{d\phi}{\sqrt{\cos \delta - \cos\phi}}.
$$

The second integral is bounded as $\delta \to 0$, the first intgral on the other hand can be approximated

$$
\frac{1}{\sqrt{2}\omega} \int_\delta^\epsilon d\phi \frac{\sqrt{2}}{\sqrt{\phi^2 - \delta^2}} = \frac{1}{\omega} \mathrm{arccosh}\left(\frac{\epsilon}{\delta}\right) \approx \frac{1}{\omega}\ln \left(\frac{1}{\delta}\right)
$$

![Pendulum](assets/generated/pendulum_time.png)

*Figure 2.3b: Time it takes for the pendulum to swing from the initial angle $\theta(0) = \pi - \delta$ to the final angle $\theta_0$ as a function of $\delta$. The time diverges logarithmically as $\delta \to 0$. Added $\omega t(\delta)$ for reference.*

Figure 2.3b shows a plot of the time it takes for the pendulum to swing from the initial angle $\theta(0) = \pi - \delta$ to the final angle $\theta_0$ as a function of $\delta$. As expected, the time diverges logarithmically as $\delta \to 0$.

<!-- ======================= -->
<!-- PROBLEM 2.4             -->
<!-- ======================= -->
## Problem 2.4

The time $t(X)$ it takes for the particle to travel from $x_0$ to $X$ is given by

$$
t(X) = \int_{x_0}^{X} dx \frac{1}{\sqrt{2(E_0 + x^a)}}, \tag{2.3.1}
$$

where I have assumd $m=1$ and $E$ is

$$
E = \frac{1}{2}v_0^2 - x_0^a.
$$

For $a > 0$ and $x \geq x_0$ we have

$$
E + x^a \geq E + x_0^a = \frac{1}{2}v_0^2  > 0. \tag{2.3.2}
$$

Now, pick $X$ large enough such that $x^a \geq 2|E|$ for $x \geq X$. That is always possible since $a > 0$  and $E$ is finite. Therefore, for $x \geq X$ we have (Recall $E \geq -|E|$)

$$
E + x^a \geq x^a - |E| \geq \frac{1}{2} x^a,
$$

so that

$$
\frac{1}{\sqrt{2(E + x^a)}} \leq \frac{1}{2\sqrt{x^a}/2} = x^{-a/2}.
$$

The time it takes to reach infinity can be written as

$$
\begin{align}
t_\infty &=
\int_{x_0}^{X} dx \frac{1}{\sqrt{2(E + x^a)}} + \int_{X}^{\infty} dx \frac{1}{\sqrt{2(E + x^a)}} \\
&\leq \int_{x_0}^{X} dx \frac{1}{\sqrt{2(E + x^a)}} + \int_{X}^{\infty} dx ~ x^{-a/2}.
\end{align}
$$

The first term is finite, so we are only concerned about the second term. The integral converges if and only if $a/2 > 1$, or equivalently if $a > 2$. Thus, the time to reach infinity is finite if and only if $a > 2$.

<!-- ======================= -->
<!-- PROBLEM 2.5             -->
<!-- ======================= -->
## Problem 2.5

Consider solutions of the form $x(t) = e^{\alpha t}$. Plugging into the equation of motion

$$
m \alpha^2 + \gamma \alpha + k = 0.
$$

For $k, m$ fixed, the solutions for $\alpha$ are

$$
2m \alpha = -\gamma \pm \sqrt{\gamma^2 - 4mk} = -\gamma \pm \sqrt{\gamma^2 - \gamma_c^2}, \tag{eqn-2.4.1}
$$

with $\gamma_c = 2\sqrt{mk}$. For $\gamma < \gamma_c$ the solutions are complex with negative real part, leading to oscillatory motion with exponentially decaying amplitude. For $\gamma > \gamma_c$ there are two distinct real negative solutions, leading to non-oscillatory motion that is a sum of two exponentials with different decay rates.

<!-- ======================= -->
<!-- PROBLEM 2.6             -->
<!-- ======================= -->
## Problem 2.6

### Case 1: Underdamped

For this case $\gamma < \gamma_c$ solutions of Eqn. (2.4.1) are complex, meaning that the solutions $x$(t) are of the form

$$
x(t) = e^{-\frac{\gamma}{2m}t}\left(A \cos(\omega_d t) + B \sin(\omega_d t)\right),
$$

therefore,

$$
r(\gamma) = \frac{\gamma}{2m} ~\quad \gamma < \gamma_c.
$$

This is a strictly increasing function of $\gamma$, the maximum is reached at $\gamma \to \gamma_c^-$:

### Case 2: Overdamped

For this case $\gamma > \gamma_c$ solutions of Eqn. (2.4.1) are real, and

$$
x(t) = A e^{\alpha_+ t} + B e^{\alpha_- t},
$$

with

$$
r(\gamma) = \min(-\alpha_+, -\alpha_-) = \frac{\gamma - \sqrt{\gamma^2 - \gamma_c^2}}{2m} \quad \gamma > \gamma_c.
$$

We want to show that this is at most equal to $\gamma_c$, that is

$$
\gamma - \sqrt{\gamma^2 - \gamma_c^2} \leq \gamma_c,
$$

or equivalently

$$
\begin{align}
\gamma^2 - \gamma_c^2 \geq (\gamma - \gamma_c)^2 &= \gamma^2 - 2\gamma \gamma_c + \gamma_c^2 \\
\iff -\gamma_c^2 &\geq -2\gamma \gamma_c + \gamma_c^2 \\
\iff 2\gamma \gamma_c &\geq 2\gamma_c^2 \\
\iff \gamma &\geq \gamma_c.
\end{align}
$$

Hence

$$
r(\gamma) \leq \frac{\gamma_c}{2m} \quad \gamma > \gamma_c.
$$

### Case 3: Critically damped

This is one is trivial as $\gamma = \gamma_c$.

<!-- ======================= -->
<!-- PROBLEM 2.7             -->
<!-- ======================= -->
## Problem 2.7

For

$$
\mathbf{F}(x_1, x_2) = \left( -\frac{x_2}{x_1^2 + x_2^2}, \frac{x_1}{x_1^2 + x_2^2} \right),
$$

we have

$$
\begin{align}
\frac{\partial F_1}{\partial x_2} - \frac{\partial F_2}{\partial x_1} &=
\frac{- (x_1^2 + x_2^2) + 2x_2^2}{(x_1^2 + x_2^2)^2} - \frac{(x_1^2 + x_2^2) - 2x_1^2}{(x_1^2 + x_2^2)^2} \\
&= \frac{-2x_1^2 - 2x_2^2 + 2x_2^2 + 2x_1^2}{(x_1^2 + x_2^2)^2} \\
&= 0.
\end{align}
$$

Let's assume now that there exists a potential $V(x_1, x_2)$ such that $\mathbf{F} = -\nabla V$. Then,

$$
\begin{align}
\frac{\partial V}{\partial x_1} &= \frac{x_2}{x_1^2 + x_2^2}, \\
\frac{\partial V}{\partial x_2} &= -\frac{x_1}{x_1^2 + x_2^2}.
\end{align}
$$

Integrating the first equation with respect to $x_1$ we have

$$
V(x_1, x_2) = \int dx_1 \frac{x_2}{x_1^2 + x_2^2} = x_2 \tan^{-1}\left(\frac{x_1}{x_2}\right) + f(x_2),
$$

where $f(x_2)$ is an arbitrary function of $x_2$. Differentiating with respect to $x_2$ we have

$$
\frac{\partial V}{\partial x_2} = \tan^{-1}\left(\frac{x_1}{x_2}\right) - \frac{x_1}{x_1^2 + x_2^2} + f'(x_2).
$$

Setting this equal to the second equation above we have

$$
\tan^{-1}\left(\frac{x_1}{x_2}\right) - \frac{x_1}{x_1^2 + x_2^2} + f'(x_2) = -\frac{x_1}{x_1^2 + x_2^2},
$$

or equivalently

$$
f'(x_2) = -\tan^{-1}\left(\frac{x_1}{x_2}\right).
$$

This is a contradiction since the left-hand side is only a function of $x_2$ while the right-hand side depends on both $x_1$ and $x_2$. Therefore, there is no potential $V(x_1, x_2)$ such that $\mathbf{F} = -\nabla V$.

<!-- ======================= -->
<!-- PROBLEM 2.8             -->
<!-- ======================= -->
## Problem 2.8

$$
\begin{align}
\frac{d}{dt}E(\mathbf{x}, \mathbf{v}) &=
\frac{d}{dt}\left(\frac{1}{2}m\mathbf{v}^2 + V(\mathbf{x})\right) \\
&= m\mathbf{v} \cdot \frac{d\mathbf{v}}{dt} + \nabla V(\mathbf{x}) \cdot \mathbf{v} \\
&= \mathbf{v} \cdot \mathbf{F}(\mathbf{x}, \mathbf{v}) + \nabla V(\mathbf{x}) \\
&= \mathbf{v} \cdot (-\nabla V(\mathbf{x}) + \mathbf{F}_2(\mathbf{x}, \mathbf{v})) + \nabla V(\mathbf{x}) \cdot \mathbf{v} \\
&= \mathbf{v} \cdot \mathbf{F}_2(\mathbf{x}, \mathbf{v}) \\
&= 0.
\end{align}
$$

<!-- ======================= -->
<!-- PROBLEM 2.9             -->
<!-- ======================= -->
## Problem 2.9

### Part a

In polar coordinates

$$
r = \sqrt{x_1^2 + x_2^2}, \quad \theta = \tan^{-1}\left(\frac{x_2}{x_1}\right),
$$

so that

$$
\begin{align}
\frac{\partial \theta}{\partial x_1} = \frac{1}{x_2^2/x_1^2 + 1} \left(-\frac{x_2}{x_1^2}\right) &= -\frac{x_2}{x_1^2 + x_2^2} = -\frac{x_2}{r^2}, \\
\frac{\partial \theta}{\partial x_2} = \frac{1}{x_2^2/x_1^2 + 1} \left(\frac{1}{x_1}\right) &= \frac{x_1}{x_1^2 + x_2^2} = \frac{x_1}{r^2}.
\end{align}
$$

### Part b

$$
\begin{align}
\frac{d}{dt}\theta(\mathbf{x}(t)) &= -\frac{x_2}{r^2} \frac{dx_1}{dt} + \frac{x_1}{r^2} \frac{dx_2}{dt} \\
&= -\frac{x_2}{r^2} v_1 + \frac{x_1}{r^2} v_2 \\
&= \frac{1}{r^2}(x_1 v_2 - x_2 v_1) \\
&= \frac{1}{mr^2}J(\mathbf{x}(t), \mathbf{p}(t)).
\end{align}
$$

<!-- ======================= -->
<!-- PROBLEM 2.10            -->
<!-- ======================= -->
## Problem 2.10

# Chapter 3: A First Approach to Quantum Mechanics

<!-- ======================= -->
<!-- PROBLEM 3.1             -->
<!-- ======================= -->

## Problem 3.1

Let $f(t) := \langle \phi(t), \psi(t) \rangle$, and consider

$$
\begin{align}
\frac{f(t + h) - f(t)}{h} &= \frac{\langle \phi(t+h), \psi(t+h) \rangle - \langle \phi(t), \psi(t) \rangle}{h} \\
&= \frac{\langle \phi(t+h), \psi(t+h) \rangle - \langle \phi(t + h), \psi(t) \rangle}{h} \\
& \quad + \frac{\langle \phi(t + h), \psi(t) \rangle - \langle \phi(t), \psi(t) \rangle}{h} \\
&= \langle \phi(t + h), \frac{\psi(t + h) - \psi(t)}{h} \rangle + \langle \frac{\phi(t + h) - \phi(t)}{h}, \psi(t) \rangle.
\end{align}
$$

Consider the first term for now, since $d\phi/dt$ converges in norm we have

$$
|\phi(t + h) - \phi(t)| = |h| \left| \frac{\phi(t + h) - \phi(t)}{h} \right| \to 0 \quad \text{as } h \to 0,
$$

or equivalently $\phi(t + h) \to \phi(t)$ as $h \to 0$ in norm. And

$$
\frac{\psi(t + h) - \psi(t)}{h} \to \frac{d\psi}{dt}(t) \quad \text{as } h \to 0.
$$

We just need to show that if $x_h \to x$ and $y_h \to y$ in norm, then $\langle x_h, y_h \rangle \to \langle x, y \rangle$,

$$
\begin{align}
| \langle x_h, y_h \rangle - \langle x, y \rangle | & \leq | \langle x_h, y_h - y \rangle | + | \langle x_h - x, y \rangle | \\
& \leq |x| |y_h - y| + |x_h - x| |y| \to 0 \quad \text{as } h \to 0.
\end{align}
$$

Therefore,

$$
\lim_{h \to 0} \langle \phi(t + h), \frac{\psi(t + h) - \psi(t)}{h} \rangle = \langle \phi(t), \frac{d\psi}{dt}(t) \rangle.
$$

And similarly for the second term. Thus we have

$$
\frac{df}{dt}(t) = \langle \phi(t), \frac{d\psi}{dt}(t) \rangle + \langle \frac{d\phi}{dt}(t), \psi(t) \rangle.
$$

<!-- ======================= -->
<!-- PROBLEM 3.2             -->
<!-- ======================= -->
## Problem 3.2

$$
c\mathrm{tr}(I) = c \dim \mathbf{H} = \mathrm{tr}(AB - BA) = \mathrm{tr}(AB) - \mathrm{tr}(BA) = 0 \implies c = 0.
$$

<!-- ======================= -->
<!-- PROBLEM 3.3             -->
<!-- ======================= -->
## Problem 3.3

## Part a
$$
\langle (cA)^* \phi, \psi \rangle = \langle  \phi, (cA) \psi \rangle = c \langle \phi, A \psi \rangle = c \langle A^* \phi, \psi \rangle = \langle \overline{c} A^* \phi, \psi \rangle.
$$

Since the adjoint is unique, we have $(cA)^* = \overline{c} A^*$.

## Part b

First note that

$$
\langle (AB)^* \phi, \psi \rangle = \langle \phi, AB \psi \rangle = \langle A^* \phi, B \psi \rangle = \langle B^* A^* \phi, \psi \rangle,
$$

which means that $(AB)^* = B^* A^*$. Also note that

$$
\begin{align}
\langle (A + B)^* \phi, \psi \rangle &= \langle \phi, (A + B) \psi \rangle = \langle \phi, A \psi \rangle + \langle \phi, B \psi \rangle \\
&= \langle A^* \phi, \psi \rangle + \langle B^* \phi, \psi \rangle = \langle (A^* + B^*) \phi, \psi \rangle,
\end{align}
$$

from which we conclude that $(A + B)^* = A^* + B^*$. Finally

$$
\begin{align}
\left(\frac{1}{i\hbar}[A, B]\right)^* &= \frac{1}{-i\hbar} [A, B]^* = \frac{1}{-i\hbar}(AB - BA)^* \\
&= \frac{1}{-i\hbar}(B^* A^* - A^* B^*) = \frac{1}{i\hbar}[A^*, B^*] \\
&= \frac{1}{i\hbar}[A, B].
\end{align}
$$

Therefore, $[A, B]/(i\hbar)$ is self-adjoint.

<!-- ======================= -->
<!-- PROBLEM 3.4             -->
<!-- ======================= -->
## Problem 3.4

First we claim that

$$
[P, f(X)] = -i\hbar f'(X), \tag{3.4.1}
$$

for a sufficiently smooth function $f$. In fact

$$
(Pf(X)\psi)(x) = -i\hbar \frac{d}{dx}(f(x)\psi(x)) = -i\hbar (f'(x)\psi(x) + f(x)\psi'(x)),
$$

while

$$
(f(X)P\psi)(x) = f(x)\left(-i\hbar \frac{d}{dx}\psi(x)\right) = -i\hbar f(x)\psi'(x).
$$

Therefore,

$$
\begin{align}
([P, f(X)]\psi)(x) &= (P f(X)\psi)(x) - (f(X) P \psi)(x) = -i\hbar f'(x) \psi(x) \\
&= (-i\hbar f'(X) \psi)(x).
\end{align}
$$

Where $f'(X): \psi(x) \mapsto f'(x)\psi(x)$. This proves the claim.

---

Using

$$
\hat{H} = \frac{1}{2m}P^2(t) + V(X(t)),
$$

we have

$$
\begin{align}
[P, H] &= \left[P, \frac{1}{2m}P^2 + V(X)\right] = \frac{1}{2m}[P, P^2] + [P, V(X)] = [P, V(X)] \\
&= -i\hbar V'(X).
\end{align}
$$

Therefore,

$$
\begin{align}
\frac{d}{dt}\langle P \rangle _{\psi(t)} &= \frac{1}{i\hbar} \langle [P, H] \rangle_{\psi(t)} = \frac{1}{i\hbar} \langle [P, V(X)] \rangle_{\psi(t)} \\
&= \frac{1}{i\hbar} \langle -i\hbar V'(X) \rangle_{\psi(t)} \\
&= - \langle V'(X) \rangle_{\psi(t)}.
\end{align}
$$

Similarly,

$$
\begin{align}
[X, H] &= \left[X, \frac{1}{2m}P^2 + V(X)\right] = \frac{1}{2m}[X, P^2] + [X, V(X)] = \frac{1}{2m}[X, P^2] \\
&= \frac{1}{2m}(P[X, P] + [X, P]P) = \frac{1}{2m}(P(i\hbar) + (i\hbar)P) = \frac{i\hbar}{m}P.
\end{align}
$$

And

$$
\frac{d}{dt}\langle X \rangle_{\psi(t)} = \frac{1}{i\hbar} \langle [X, H] \rangle_{\psi(t)} = \frac{1}{i\hbar} \langle \frac{i\hbar}{m} P \rangle_{\psi(t)} = \frac{1}{m} \langle P \rangle_{\psi(t)}.
$$

<!-- ======================= -->
<!-- PROBLEM 3.5             -->
<!-- ======================= -->
## Problem 3.5

$$
\begin{align}
0 &< \langle (X - \langle X \rangle)^2 \rangle _{\psi} \\
&= \int_{\mathbb{R}} dx\, \overline{\psi(x)} (x - \langle X \rangle_{\psi})^2\psi(x) \\
&= \int_{\mathbb{R}} dx\, (x - \langle X \rangle_{\psi})^2 |\psi(x)|^2 \\
&= \int_{\mathbb{R}} dx\, (x^2 - 2x\langle X \rangle_{\psi} + \langle X \rangle_{\psi}^2) |\psi(x)|^2 \\
&= \int_{\mathbb{R}} dx\, x^2 |\psi(x)|^2 - 2\langle X \rangle_{\psi} \int_{\mathbb{R}} dx\, x |\psi(x)|^2 + \langle X \rangle_{\psi}^2 \int_{\mathbb{R}} dx\, |\psi(x)|^2 \\
&= \langle X^2 \rangle_{\psi} - 2\langle X \rangle_{\psi}^2 + \langle X \rangle_{\psi}^2 \\
&= \langle X^2 \rangle_{\psi} - \langle X \rangle_{\psi}^2.
\end{align}
$$

Therefore

$$
\langle X^2 \rangle_{\psi} > \langle X \rangle_{\psi}^2.
$$

Note that for the integral to be strictly zerp. we would require

$$
(x - \langle X \rangle_{\psi}) \psi(x) = 0 \quad \text{for almost every } x \in \mathbb{R},
$$

but, since $(x - \langle X \rangle)^2_\psi = 0$ only at the point $x = \langle X \rangle_{\psi}$, this would imply that $\psi(x) = 0$ for almost every $x \neq \langle X \rangle_{\psi}$, which is impossible since $\psi$ is supposed to be normalizable.

This means the inequality is strict.

<!-- ======================= -->
<!-- PROBLEM 3.6             -->
<!-- ======================= -->
## Problem 3.6

I will write everything in terms of $\omega^2 = k/m$, and normalize the $psi_0(x)$ to 1.

$$
\psi_0(x) = \left(\frac{m\omega}{\pi \hbar}\right)^{1/4} e^{-m\omega x^2/2\hbar}.
$$

The normalization constant is not important, but I will keep it anyway for completeness.

$$
\begin{align}
\hat{H}\psi_0(x) &= -\frac{\hbar^2}{2m} \frac{d^2}{dx^2} \psi_0(x) + \frac{1}{2} m \omega^2 x^2 \psi_0(x) \\
&= -\frac{\hbar^2}{2m} \frac{d^2}{dx^2} \left( \left(\frac{m\omega}{\pi \hbar}\right)^{1/4} e^{-m\omega x^2/2\hbar} \right) + \frac{1}{2} m \omega^2 x^2 \left(\frac{m\omega}{\pi \hbar}\right)^{1/4} e^{-m\omega x^2/2\hbar} \\
&= \left(\frac{m\omega}{\pi \hbar}\right)^{1/4} \left( -\frac{\hbar^2}{2m} \frac{d^2}{dx^2} e^{-m\omega x^2/2\hbar} + \frac{1}{2} m \omega^2 x^2 e^{-m\omega x^2/2\hbar} \right) \\
&= \left(\frac{m\omega}{\pi \hbar}\right)^{1/4} \left( -\frac{\hbar^2}{2m} \left( \frac{m^2 \omega^2 x^2}{\hbar^2} - \frac{m\omega}{\hbar} \right) e^{-m\omega x^2/2\hbar} + \frac{1}{2} m \omega^2 x^2 e^{-m\omega x^2/2\hbar} \right) \\
&= \left(\frac{m\omega}{\pi \hbar}\right)^{1/4} \left( \frac{\hbar \omega}{2} e^{-m\omega x^2/2\hbar} \right) \\
&= \frac{\hbar \omega}{2} \psi_0(x).
\end{align}
$$

<!-- ======================= -->
<!-- PROBLEM 3.7             -->
<!-- ======================= -->
## Problem 3.7

### Position

$$
[X, H] = \frac{1}{2m}[X, P^2] + [X, V(X)] = \frac{i\hbar}{m}P
$$

Plugging that into Heisenberg's equation

$$
\frac{dX(t)}{dt} = \frac{1}{i\hbar}[X(t), H] = \frac{1}{i\hbar}([X, H]) (t) = \frac{1}{i\hbar}\left(\frac{i\hbar}{m}P\right)(t) = \frac{1}{m} P(t).
$$

### Momentum

$$
[P, H] = \frac{1}{2m}[P, P^2] + [P, V(X)] \stackrel{(3.4.1)}{=} -i\hbar V'(X).
$$

Plugging that into Heisenberg's equation

$$
\frac{dP(t)}{dt} = \frac{1}{i\hbar}[P(t), H] = \frac{1}{i\hbar}([P, H])(t) = \frac{1}{i\hbar}(-i\hbar V'(X))(t) = - V'(X(t)).
$$

<!-- ======================= -->
<!-- PROBLEM 3.8             -->
<!-- ======================= -->
## Problem 3.8

### Part a: Negative energies

Consider solutions of the form $\psi(x) = A e^{ax}$, where $a \in \mathbb{C}$. Then


$$
-\frac{\hbar^2}{2m} \frac{d^2}{dx^2} e^{ax} = -\frac{\hbar^2}{2m} a^2 e^{ax} = E e^{ax} \implies E = -\frac{\hbar^2 a^2}{2m}.
$$

For $E < 0$ we require $a^2 > 0$, so $a$ is real and non-zero. Solution is then

$$
\psi(x) = A e^{+\sqrt{-2mE}/\hbar x} + B e^{-\sqrt{-2mE}/\hbar x}.
$$

With the bounday conditions $\psi(0) = 0$ and $\psi(L) = 0$, we have

$$
0 = \psi(0) = A + B \implies B = -A,
$$

so that

$$
\psi(x) = A \left( e^{+\sqrt{-2mE}/\hbar x} - e^{-\sqrt{-2mE}/\hbar x} \right) = 2A \sinh\left(\frac{\sqrt{-2mE}}{\hbar} x\right).
$$

The second boundary condition gives

$$
0 = \psi(L) = 2A \sinh\left(\frac{\sqrt{-2mE}}{\hbar} L\right).
$$

The second factor is zero only if $E = 0$, which is not allowed, so we must have $A = 0$. Therefore, there are no non-trivial solutions for $E < 0$.

### Part b: Zero energy

For $E = 0$, Schrodinger's equation becomes

$$
-\frac{\hbar^2}{2m} \frac{d^2}{dx^2} \psi(x) = 0,
$$

Whose general solution is

$$
\psi(x) = A x + B.
$$

With the boundary conditions $\psi(0) = 0$ and $\psi(L) = 0$, we have

$$
0 = \psi(0) = B \implies B = 0,
$$

and

$$
0 = \psi(L) = A L \implies A = 0.
$$

Therefore, there are no non-trivial solutions for $E = 0$.

<!-- ======================= -->
<!-- PROBLEM 3.9             -->
<!-- ======================= -->
## Problem 3.9

$$
\begin{align}
\langle \phi, H \psi \rangle &= \int_0^L dx\, \overline{\phi(x)} \left( -\frac{\hbar^2}{2m} \frac{d^2}{dx^2} \psi(x) \right) \\
&= \underbrace{-\frac{\hbar^2}{2m} \left[ \overline{\phi(x)} \frac{d}{dx} \psi(x) \right]_0^L}_{0} + \frac{\hbar^2}{2m} \int_0^L dx\, \frac{d}{dx} \overline{\phi(x)} \frac{d}{dx} \psi(x) \\
&= \frac{\hbar^2}{2m} \int_0^L dx\, \frac{d}{dx} \overline{\phi(x)} \frac{d}{dx} \psi(x) \\
&= \underbrace{\frac{\hbar^2}{2m} \left[ \frac{d}{dx} \overline{\phi(x)} \psi(x) \right]_0^L}_{0} - \frac{\hbar^2}{2m} \int_0^L dx\, \left(\frac{d^2}{dx^2}\overline{\phi(x)}\right)  \psi(x) \\
&= \langle H \phi, \psi \rangle.
\end{align}
$$

Note that if the boundary conditions do not force the boundary terms to be zero, then they will not cancel out, and the equality will not hold in general.

<!-- ======================= -->
<!-- PROBLEM 3.10            -->
<!-- ======================= -->
## Problem 3.10

(See Problem [Problem 2.19](chapter02.2.md#problem-2.19) for a similar solution in classical mechanics.) With $J_i = \epsilon_{ijk}X_j P_k$

$$
\begin{align}
[J_i, J_j] &= [\epsilon_{i k l} X_k P_l, \epsilon_{j m n} X_m P_n] \\
&= \epsilon_{i k l} \epsilon_{j m n} [X_k P_l, X_m P_n] \\
&= \epsilon_{i k l} \epsilon_{j m n} (X_k [P_l, X_m P_n] + [X_k, X_m P_n] P_l) \\
&= \epsilon_{i k l} \epsilon_{j m n} (X_k X_m [P_l, P_n] + X_k[P_l, X_m] P_n + X_m[X_k, P_n] P_l + [X_k, X_m ] P_nP_l) \\
&= \epsilon_{i k l} \epsilon_{j m n} (0 + X_k (-i\hbar \delta_{l m}) P_n + X_m (i\hbar \delta_{k n}) P_l + 0) \\
&= -i\hbar \epsilon_{i k l} \epsilon_{j l n} X_k P_n + i\hbar \epsilon_{i k l} \epsilon_{j m k} X_m P_l \\
&= -i\hbar \epsilon_{l i k} \epsilon_{l n j} X_k P_n + i\hbar \epsilon_{k l i} \epsilon_{k j m} X_m P_l \\
&= -i\hbar (\delta_{i n} \delta_{k j} - \delta_{i j} \delta_{k n}) X_k P_n + i\hbar (\delta_{l j} \delta_{i m} - \delta_{l m} \delta_{i j}) X_m P_l \\
&= -i\hbar X_j P_i + i\hbar \delta_{i j} X_k P_k + i\hbar X_i P_j - i\hbar \delta_{i j} X_l P_l \\
&= i\hbar (X_i P_j - X_j P_i) \\
&= i\hbar \epsilon_{i j k} J_k.
\end{align}
$$

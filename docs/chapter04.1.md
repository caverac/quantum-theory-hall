# Chapter 4: The Schrödinger Equation

<!-- ======================= -->
<!-- PROBLEM 4.1             -->
<!-- ======================= -->
## Problem 4.1

### Part a: "Pointwise ➡ Weak"

Assume $\psi$ satisfies the free Shrödinger equation pointwise:

$$
\frac{\partial \psi}{\partial t} - \frac{i\hbar}{2m} \frac{\partial^2 \psi}{\partial x^2} = 0. \tag{4.1.1}
$$

Take $\chi \in C_c^\infty(\mathbb{R}^2)$ a smooth compactly supported function and integrate

$$
0 = \int_{\mathbb{R}^2} dt\, dx\, \left( \frac{\partial \psi}{\partial t} - \frac{i\hbar}{2m} \frac{\partial^2 \psi}{\partial x^2} \right) \chi(t,x).
$$

Let's integrate by parts, first in $t$:

$$
\begin{align}
\int_{\mathbb{R}^2} dt\, dx\, \frac{\partial \psi}{\partial t} \chi(t,x) &= \int_{\mathbb{R}} dx\, \Bigl[ \psi(t,x)\chi(t,x) \Bigr]_{t=-\infty}^{t=+\infty} - \int_{\mathbb{R}^2} dt\, dx\, \psi(t,x) \frac{\partial \chi}{\partial t}(t,x) \\
&= - \int_{\mathbb{R}^2} dt\, dx\, \psi(t,x) \frac{\partial \chi}{\partial t}(t,x),
\end{align}
$$

where we used that $\chi$ is compactly supported, so it vanishes at $t = \pm \infty$.

The second term produces


$$
\begin{align}
\int_{\mathbb{R}^2} dt\, dx\, \frac{i\hbar}{2m} \frac{\partial^2 \psi}{\partial x^2} \chi(t,x) &= \frac{i\hbar}{2m} \int_{\mathbb{R}} dt\, \Bigl[ \frac{\partial \psi}{\partial x}(t,x) \chi(t,x) \Bigr]_{x=-\infty}^{x=+\infty} \\
& \quad- \frac{i\hbar}{2m} \int_{\mathbb{R}^2} dt\, dx\, \frac{\partial \psi}{\partial x}(t,x) \frac{\partial \chi}{\partial x}(t,x) \\
&=  \frac{i\hbar}{2m} \int_{\mathbb{R}^2} dt\, dx\, \psi(t,x) \frac{\partial^2 \chi}{\partial x^2}(t,x),
\end{align}
$$

so that Eqn. (4.1.1) becomes

$$
0 = \int_{\mathbb{R}^2} dt\, dx\, \psi(t,x) \left( -\frac{\partial \chi}{\partial t}(t,x) - \frac{i\hbar}{2m} \frac{\partial^2 \chi}{\partial x^2}(t,x) \right).
$$

That's the weak form of the Schrödinger equation.

### Part a: "Weak ➡ Pointwise"

Assume the weak form of the Schrödinger equation holds:

$$
\int_{\mathbb{R}^2} dt\, dx\, \psi(t,x) \left(\frac{\partial \chi}{\partial t}(t,x) + \frac{i\hbar}{2m} \frac{\partial^2 \chi}{\partial x^2}(t,x) \right) = 0, \quad \forall \chi \in C_c^\infty(\mathbb{R}^2).
$$

Since $\psi$ is locally integrable we can repeat the same integration by parts as in part a, obtaining

$$
\int_{\mathbb{R}^2} dt\, dx\, \left( \frac{\partial \psi}{\partial t} - \frac{i\hbar}{2m} \frac{\partial^2 \psi}{\partial x^2} \right) \chi(t,x) = 0, \quad \forall \chi \in C_c^\infty(\mathbb{R}^2).
$$

Applying the result of Proposition A.23 we conclude that (with $f_2 = 0$)

$$
\frac{\partial \psi}{\partial t} - \frac{i\hbar}{2m} \frac{\partial^2 \psi}{\partial x^2} = 0
$$

### Part b

Fix $\chi \in C_c^\infty(\mathbb{R}^2)$, for each $t$, $\chi(\cdot, t) \in C_c^\infty(\mathbb{R})$ and so are $\partial_x \chi(\cdot, t)$ and $\partial_x^2 \chi(\cdot, t)$. Define

$$
S\chi(x, t) = \frac{\partial \chi}{\partial t}(x,t) + \frac{i\hbar}{2m} \frac{\partial^2 \chi}{\partial x^2}(x,t).
$$

For a fixed $t$

$$
\int_{\mathbb{R}} dx\, \psi(x,t) S\chi(x,t) = \frac{1}{2\pi}\int_{\mathbb{R}} dk\, \hat{\psi}(k, t) \widehat{S\chi}(-k,t), \tag{4.1.2}
$$

We need to calculate now $\widehat{S\chi}(k,t)$.

**Time derivative:**

$$
\frac{\partial \chi}{\partial t}(x,t) \xrightarrow{\mathcal{F}} \frac{\partial \hat{\chi}}{\partial t}(k,t).
$$

**Second spatial derivative:**

$$
\frac{\partial^2 \chi}{\partial x^2}(x,t) \xrightarrow{\mathcal{F}} -(ik)^2 \hat{\chi}(k,t) = -k^2 \hat{\chi}(k,t).
$$

Putting these together we have

$$
\widehat{S\chi}(k,t) = \frac{\partial \hat{\chi}}{\partial t}(k,t) - \frac{i\hbar}{2m} k^2 \hat{\chi}(k,t). \tag{4.1.3}
$$

Replacing Eqn. (4.1.3) into Eqn. (4.1.2) and integrating in time we obtain

$$
\begin{align}
\int_{\mathbb{R}^2} dt\, dx\, \psi(x,t) S\chi(x,t) &= \frac{1}{2\pi} \int_{\mathbb{R}^2} dt\,dk\, \hat{\psi}(k,t) \left( \frac{\partial }{\partial t}\hat{\chi}(-k,t) - \frac{i\hbar}{2m} k^2 \hat{\chi}(-k,t) \right) \\
&= -\frac{1}{2\pi} \int_{\mathbb{R}^2} dt\,dk\, \left( \frac{\partial}{\partial t}\hat{\psi}(k,t) + \frac{i\hbar}{2m} k^2 \hat{\psi}(k,t) \right) \hat{\chi}(-k,t) \\
&= -\frac{1}{2\pi} \int_{\mathbb{R}^2} dt\,dk\, \left( -\frac{i\hbar k^2}{2m}\hat{\psi}(k, t) + \frac{i\hbar}{2m} k^2 \hat{\psi}(k,t) \right) \hat{\chi}(-k,t) \\
&= 0
\end{align}
$$

That is, $\psi$ satisfies the weak form of the Schrödinger equation.

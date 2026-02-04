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

<!-- ======================= -->
<!-- PROBLEM 4.2             -->
<!-- ======================= -->
## Problem 4.2


### Part a

To prove

$$
\left(\int_{-\infty}^\infty dx\, e^{-x^2/2a} \right)^2 = \int_{-\infty}^\infty \int_{-\infty}^\infty dx\, dy\, e^{-(x^2 + y^2)/2a},
$$

first we need to show that RHS converges,

$$
\int_{-\infty}^\infty \int_{-\infty}^\infty dx\, dy\, |e^{-(x^2 + y^2)/2a}| = \int_{-\infty}^\infty \int_{-\infty}^\infty dx\, dy\, e^{-(x^2 + y^2)\Re(1/2a)}.
$$

Let's consider three cases:

**1. $\Re(a) < 0$**

In that case the exponential blows up and the integral diverges.

**2. $\Re(a) = 0$**

The modulus is constant, so the integral does not converge absolutely. Fubini's theorem does not apply directly; this case requires a separate argument (see [Part c](#part-c)).

**3. $\Re(a) > 0$**

Call

$$
\gamma = \Re\left(\frac{1}{2a}\right) > 0,
$$

then

$$
\int_{-\infty}^\infty \int_{-\infty}^\infty dx\, dy\, e^{-(x^2 + y^2)\Re(1/2a)} = \int_{-\infty}^\infty \int_{-\infty}^\infty dx\, dy\, e^{-\gamma (x^2 + y^2)}.
$$

This integral converges since $\gamma > 0$, equivalently $\Re(a) > 0$, since

$$
\Re\left(\frac{1}{2a}\right) = \frac{\Re(a)}{2|a|^2}.
$$

We then have

$$
\int_{-\infty}^\infty \int_{-\infty}^\infty dx\, dy\, |e^{-(x^2 + y^2)/2a}| < \infty,
$$

which allows us to use Fubini's theorem to write

$$
\begin{align}
\int_{-\infty}^\infty \int_{-\infty}^\infty dx\, dy\, e^{-(x^2 + y^2)/2a} &= \int_{-\infty}^\infty dx\, e^{-x^2/2a} \left(\int_{-\infty}^\infty dy\, e^{-y^2/2a} \right) \\
&= \left(\int_{-\infty}^\infty dx\, e^{-x^2/2a} \right)^2.
\end{align}
$$

Now we can calculate the integral for the $\Re(a) > 0$ case. Using polar coordinates $x = r\cos\theta$, $y = r\sin\theta$, $dx\, dy = r\, dr\, d\theta$ we have

$$
\begin{align}
\int_{-\infty}^\infty \int_{-\infty}^\infty dx\, dy\, e^{-(x^2 + y^2)/2a} &= \int_0^{2\pi} d\theta \int_0^\infty dr\, r\, e^{-r^2/2a} \\
&= 2\pi \int_0^\infty dr\, r\, e^{-r^2/2a} \\
&= 2\pi \left[-a e^{-r^2/2a} \right]_{r=0}^{r=\infty} \\
&= 2\pi a.
\end{align}
$$

Thus

$$
\int_{-\infty}^\infty dx\, e^{-x^2/2a} = \sqrt{2\pi a}, \quad \Re(a) > 0.
$$

### Part b


$$
\begin{align}
\frac{d}{dx}\left(\frac{a}{x}e^{-x^2/2a}\right) &= -\frac{a}{x^2}e^{-x^2/2a} + \frac{a}{x} \left(-\frac{x}{a}\right) e^{-x^2/2a} \\
&= -\frac{a}{x^2}e^{-x^2/2a} - e^{-x^2/2a}.
\end{align}
$$

Thus

$$
\int_A^B dx\, e^{-x^2/2a} = -\left.\frac{a}{x} e^{-x^2/2a} \right|_{A}^{B} - \int_A^B dx\, \frac{a}{x^2}e^{-x^2/2a}.
$$

!!! warning "Typo in book"
    There is a typo in the book's version of this equation: the second term on the right-hand side is missing a minus sign.


!!! question "$x=0$?"
    I've been going around in circles about the statement $A, B > 0$ in the problem, I think it should be $0 < A < B$ to avoid the singularity at $x=0$, which was introduced when integrating by parts, the factors $a/x$ and $a/x^2$ are not defined at $x=0$, which would make the equation invalid.

    I will come back to this later.

### Part c

**Step 1: Uniform bound on the tail integral.**

Let $a = \alpha + i\beta$ with $\beta \neq 0$ fixed and $\alpha \in [0, 1]$. From Part b, we have the identity

$$
\int_A^\infty dx\, e^{-x^2/2a} = -\left.\frac{a}{x} e^{-x^2/2a} \right|_{A}^{\infty} - \int_A^\infty dx\, \frac{a}{x^2}e^{-x^2/2a}.
$$

Consider each term separately.

**For the boundary term**

Note that

$$
|a| = |\alpha + i\beta| = \sqrt{\alpha^2 + \beta^2}  \leq \sqrt{1 + \beta^2},
$$

therefore

$$
\left|\frac{a}{x} e^{-x^2/2a}\right| = \frac{|a|}{x} e^{-x^2 \Re(1/2a)} = \frac{|a|}{x} e^{-x^2 \alpha/(2|a|^2)} \leq \frac{\sqrt{1 + \beta^2}}{x} \to 0.
$$

At $x = A$:

$$
\left|\frac{a}{A} e^{-A^2/2a}\right| \leq \frac{\sqrt{1 + \beta^2}}{A}.
$$

**For the integral term**

$$
\left|\int_A^\infty dx\, \frac{a}{x^2} e^{-x^2/2a}\right| \leq |a| \int_A^\infty dx\, \frac{1}{x^2} e^{-x^2 \alpha/(2|a|^2)} \leq |a| \int_A^\infty dx\, \frac{1}{x^2} = \frac{|a|}{A}.
$$

Combining these estimates:

$$
\left|\int_A^\infty dx\, e^{-x^2/2a}\right| \leq \frac{2|a|}{A} \leq \frac{2\sqrt{1 + \beta^2}}{A}.
$$

This bound is uniform in $\alpha \in [0, 1]$ and vanishes as $A \to \infty$.

**Step 2: Extension to $\Re(a) = 0$.**

For $\alpha > 0$, we have established that

$$
\int_{-\infty}^\infty dx\, e^{-x^2/2a} = \sqrt{2\pi a}.
$$

By symmetry of the integrand, this equals $2\int_0^\infty dx\, e^{-x^2/2a}$.

Fix $\beta \neq 0$ and define $f(\alpha) = \int_0^\infty dx\, e^{-x^2/2(\alpha + i\beta)}$ for $\alpha \in [0, 1]$. Split the integral:

$$
f(\alpha) = \int_0^A dx\, e^{-x^2/2(\alpha + i\beta)} + \int_A^\infty dx\, e^{-x^2/2(\alpha + i\beta)}.
$$

The first integral is a continuous function of $\alpha$ (the integrand is continuous and bounded on $[0, A] \times [0, 1]$). By Step 1, the second integral is bounded by $2\sqrt{1+\beta^2}/A$ uniformly in $\alpha$, for each $\varepsilon > 0$, we can then choose $A$ large enough so that the second integral is smaller than $\varepsilon/2$, thus

$$
|f(\alpha) - f(0)| \leq \left|\int_0^A dx\, \left(e^{-x^2/2(\alpha + i\beta)} - e^{-x^2/2(i\beta)}\right)\right| + \varepsilon.
$$

As $\alpha \to 0^+$, the first term vanishes by continuity. Thus $f$ is continuous at $\alpha = 0$, and

$$
\int_0^\infty dx\, e^{-x^2/2(i\beta)} = \lim_{\alpha \to 0^+} \int_0^\infty dx\, e^{-x^2/2(\alpha + i\beta)} = \lim_{\alpha \to 0^+} \frac{1}{2}\sqrt{2\pi(\alpha + i\beta)} = \frac{1}{2}\sqrt{2\pi i\beta}.
$$

Therefore, for $a = i\beta$ with $\beta \neq 0$:

$$
\int_{-\infty}^\infty dx\, e^{-x^2/2a} = \sqrt{2\pi a}.
$$

The formula extends to all $a$ with $\Re(a) \geq 0$ and $a \neq 0$.

### Part d

$$
\begin{align}
\frac{1}{2\pi}\int_{-\infty}^\infty dk\, e^{ikx} e^{-i\hbar k^2 t/2m} &= \frac{1}{2\pi} \int_{-\infty}^\infty dk\, e^{- \frac{i\hbar t}{2m} \left( k^2 - \frac{2m x}{\hbar t} k \right)} \\
&= \frac{1}{2\pi} \int_{-\infty}^\infty dk\, e^{- \frac{i\hbar t}{2m} \left( k - \frac{m x}{\hbar t} \right)^2 + \frac{i m x^2}{2\hbar t}} \\
&= \frac{1}{2\pi} e^{i m x^2/2\hbar t} \int_{-\infty}^\infty dk\, e^{- \frac{i\hbar t}{2m} \left( k - \frac{m x}{\hbar t} \right)^2 } \\
&= \frac{1}{2\pi} e^{i m x^2/2\hbar t} \int_{-\infty}^\infty dk'\, e^{- \frac{i\hbar t}{2m} k'^2 } \\
&= \frac{1}{2\pi} e^{i m x^2/2\hbar t} \sqrt{2\pi \frac{2m}{i\hbar t}} \\
&= \sqrt{\frac{m}{2\pi i \hbar t}} e^{i m x^2/2\hbar t}.
\end{align}
$$

<!-- ======================= -->
<!-- PROBLEM 4.3             -->
<!-- ======================= -->
## Problem 4.3

We need to prove three things

### Well-definedness

Since Shcwartz functions are in $L^2(\mathbb{R})$, then

$$
|(\phi * \psi)(x)| \leq \int_{-\infty}^\infty dy\, |\phi(x - y)| |\psi(y)| \leq \|\phi\|_{L^2} \|\psi\|_{L^2} < \infty,
$$


### Differentiability

Consider

$$
\frac{(\phi * \psi)(x + h) - (\phi * \psi)(x)}{h} = \int_{-\infty}^\infty dy\, \frac{\phi(x + h - y) - \phi(x - y)}{h} \psi(y).
$$

By the mean value theorem, for each $y$ there exists $\xi_h \in (x - y, x + h - y)$ such that

$$
\frac{\phi(x + h - y) - \phi(x - y)}{h} = \phi'(\xi_h).
$$

Since $\phi \in \mathcal{S}(\mathbb{R})$, its derivative $\phi' \in \mathcal{S}(\mathbb{R})$ as well. In particular, $\phi'$ is bounded: $|\phi'(z)| \leq M$ for all $z \in \mathbb{R}$.

Thus the integrand is bounded by

$$
\left|\frac{\phi(x + h - y) - \phi(x - y)}{h} \psi(y)\right| \leq M |\psi(y)|,
$$

which is integrable since $\psi \in L^2(\mathbb{R})$. More precisely, we use that $\phi' \in L^2$ to get

$$
\int_{-\infty}^\infty dy\, |\phi'(x - y)| |\psi(y)| \leq \|\phi'\|_{L^2} \|\psi\|_{L^2} < \infty.
$$

By the dominated convergence theorem, we can pass the limit inside the integral:

$$
\begin{align}
(\phi * \psi)'(x) &= \lim_{h \to 0} \int_{-\infty}^\infty dy\, \frac{\phi(x + h - y) - \phi(x - y)}{h} \psi(y) \\
&= \int_{-\infty}^\infty dy\, \phi'(x - y) \psi(y) = (\phi' * \psi)(x).
\end{align}
$$

!!! warning "$L_2$ vs $L_1$"
    The statement "bounded by $M|\psi(y)|$, which is integrable" may be wrong. I am not convinced that being in $L^2$ implies being in $L^1$. Come back to this later.

### Smoothness

Since $\phi \in \mathcal{S}(\mathbb{R})$, all derivatives $\phi^{(n)} \in \mathcal{S}(\mathbb{R})$. By induction, applying the [Differentiability](#differentiability) argument repeatedly leads to

$$
(\phi * \psi)^{(n)} = \phi^{(n)} * \psi.
$$

Each $\phi^{(n)}$ is Schwartz, hence in $L^2$, so the same argument shows each derivative exists and is continuous.

Therefore $\phi * \psi \in C^\infty(\mathbb{R})$.

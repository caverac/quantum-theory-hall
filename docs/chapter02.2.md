<!-- ======================= -->
<!-- PROBLEM 2.11            -->
<!-- ======================= -->
## Problem 2.11

!!! Typo
    I think there's a typo, and the correct transformation is $H(\mathbf{x} + \mathbf{a}, \mathbf{p})$, not $H(\mathbf{x} + \mathbf{a}, \mathbf{p} + \mathbf{a})$.

From the equations of motion

$$
\begin{align}
\frac{dp_k}{dt} &= \sum_{j=1}^N \frac{dp_k^j}{dt} \\
&= -\sum_{j=1}^N \frac{\partial}{\partial x_k^j}H(\mathbf{x}^1 + \mathbf{a}, \cdots, \mathbf{x}^N + \mathbf{a}, \mathbf{p}^1, \dots, \mathbf{p}^N).  \tag{2.11.1}
\end{align}
$$

Define $F: \mathbb{R}^n \to \mathbb{R}$, $F(\mathbf{a}) = H(\mathbf{x}^1 + \mathbf{a}, \cdots, \mathbf{x}^N + \mathbf{a}, \mathbf{p}^1, \dots, \mathbf{p}^N)$, and let's calculate

$$
\begin{align}
\left.\frac{\partial F}{\partial a_k}(\mathbf{a})\right|_{\mathbf{a} = 0}
&= \sum_{j=1}^N \sum_{l=1}^n \left.\frac{\partial H}{\partial x_l^j}(\mathbf{x}^1 + \mathbf{a}, \cdots, \mathbf{x}^N + \mathbf{a}, \mathbf{p}^1, \dots, \mathbf{p}^N) \frac{\partial}{\partial a_k}(x_l^j + a_l) \right|_{\mathbf{a} = 0}  \\
&= \sum_{j=1}^N \left.\frac{\partial H}{\partial x_k^j}(\mathbf{x}^1 + \mathbf{a}, \cdots, \mathbf{x}^N + \mathbf{a}, \mathbf{p}^1, \dots, \mathbf{p}^N)\right|_{\mathbf{a} = 0} \\
&= \sum_{j=1}^N \frac{\partial H}{\partial x_k^j}(\mathbf{x}^1, \cdots, \mathbf{x}^N, \mathbf{p}^1, \dots, \mathbf{p}^N) \\
&\stackrel{(2.11.1)}{=} -\frac{dp_k}{dt}.
\end{align}
$$

which means that $\mathbf{p}$ is constant if and only iff $F$ is constant with respect to $\mathbf{a}$, i.e., iff $H$ does not depend on $\mathbf{a}$.

<!-- ======================= -->
<!-- PROBLEM 2.12            -->
<!-- ======================= -->
## Problem 2.12

With $J = x_1p_2 - x_2 p_1$ we have

$$
\begin{align}
\{f, J \} &= \frac{\partial f}{\partial x_1} \frac{\partial J}{\partial p_1} + \frac{\partial f}{\partial x_2} \frac{\partial J}{\partial p_2} - \frac{\partial f}{\partial p_1} \frac{\partial J}{\partial x_1} - \frac{\partial f}{\partial p_2} \frac{\partial J}{\partial x_2} \\
&= \frac{\partial f}{\partial x_1} (-x_2) + \frac{\partial f}{\partial x_2} (x_1) - \frac{\partial f}{\partial p_1} (p_2) - \frac{\partial f}{\partial p_2} (-p_1) \\
&= -x_2 \frac{\partial f}{\partial x_1} + x_1 \frac{\partial f}{\partial x_2} - p_2 \frac{\partial f}{\partial p_1} + p_1 \frac{\partial f}{\partial p_2} \\
&= \frac{\partial f}{\partial x_1} (A \mathbf{x})_1 + \frac{\partial f}{\partial x_2} (A \mathbf{x})_2 + \frac{\partial f}{\partial p_1} (A \mathbf{p})_1 + \frac{\partial f}{\partial p_2} (A \mathbf{p})_2 \\
&= \nabla_{\mathbf{x}} f \cdot (A \mathbf{x}) + \nabla_{\mathbf{p}} f \cdot (A \mathbf{p}) \\
&= \left.\frac{d}{d\theta} f(e^{A \theta} \mathbf{x}, e^{A \theta} \mathbf{p})\right|_{\theta=0} \\
&= \frac{d}{d\theta} f(R_\theta\mathbf{x}, R_\theta \mathbf{p}) \Big|_{\theta=0}.
\end{align}
$$

where

$$
R_\theta = e^{A \theta} = \begin{pmatrix}\cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}\quad\text{and}\quad
A = \begin{pmatrix}0 & -1 \\ 1 & 0 \end{pmatrix}.
$$

<!-- ======================= -->
<!-- PROBLEM 2.13            -->
<!-- ======================= -->
## Problem 2.13

If at least one of $f$, $g$ has compact support, then $\{f, g\}$ is also compactly supported, since it is a sum of products of partial derivatives of $f$ and $g$

$$
\begin{align}
I &= \int_{\mathbb{R}^n}\int_{\mathbb{R}^n} d^n\mathbf{x} \, d^n\mathbf{p}\, \{f, g\} (\mathbf{x}, \mathbf{p}) \\
&= \sum_{j=1}^n\int_{\mathbb{R}^n}\int_{\mathbb{R}^n} d^n\mathbf{x} \, d^n\mathbf{p}\, \left( \frac{\partial f}{\partial x_j} \frac{\partial g}{\partial p_j} - \frac{\partial f}{\partial p_j} \frac{\partial g}{\partial x_j} \right) \\
&= \sum_{j=1}^n \int_{\mathbb{R}^n}\int_{\mathbb{R}^n} d^n\mathbf{x} \, d^n\mathbf{p}\, \left[ \frac{\partial}{\partial x_j}\left(f \frac{\partial g}{\partial p_j} \right) - \frac{\partial}{\partial p_j}\left(f \frac{\partial g}{\partial x_j} \right) \right] \\
&+ \sum_{j=1}^n \int_{\mathbb{R}^n}\int_{\mathbb{R}^n} d^n\mathbf{x} \, d^n\mathbf{p}\, \left[ f \frac{\partial^2 g}{\partial x_j \partial p_j} - f \frac{\partial^2 g}{\partial p_j \partial x_j} \right] \\
&= 0
\end{align}
$$

The first term vanishes by the divergence theorem since $f$ and $g$ have compact support, and the second term vanishes since mixed partial derivatives commute.

<!-- ======================= -->
<!-- PROBLEM 2.14            -->
<!-- ======================= -->
## Problem 2.14

$$
\begin{align}
[X, Y]f &= X(Yf) - Y(Xf) \\
&= \sum_{i=1}^n a_i(\mathbf{x}) \frac{\partial}{\partial x_i} \left( \sum_{j=1}^n b_j(\mathbf{x}) \frac{\partial f}{\partial x_j} \right) - \sum_{j=1}^n b_j(\mathbf{x}) \frac{\partial}{\partial x_j} \left( \sum_{i=1}^n a_i(\mathbf{x}) \frac{\partial f}{\partial x_i} \right) \\
&= \sum_{i,j=1}^n a_i(\mathbf{x}) \frac{\partial b_j}{\partial x_i} \frac{\partial f}{\partial x_j} + \sum_{i,j=1}^n a_i(\mathbf{x}) b_j(\mathbf{x}) \frac{\partial^2 f}{\partial x_i \partial x_j} \\
&- \sum_{i,j=1}^n b_j(\mathbf{x}) \frac{\partial a_i}{\partial x_j} \frac{\partial f}{\partial x_i} - \sum_{i,j=1}^n b_j(\mathbf{x}) a_i(\mathbf{x}) \frac{\partial^2 f}{\partial x_j \partial x_i} \\
&= \sum_{j=1}^n \left( \sum_{i=1}^n a_i(\mathbf{x}) \frac{\partial b_j}{\partial x_i} - \sum_{i=1}^n b_i(\mathbf{x}) \frac{\partial a_j}{\partial x_i} \right) \frac{\partial f}{\partial x_j} \\
&= \sum_{j=1}^n c_j(\mathbf{x}) \frac{\partial f}{\partial x_j},
\end{align}
$$

with

$$
c_j(\mathbf{x}) = \sum_{i=1}^n \left( a_i(\mathbf{x}) \frac{\partial b_j}{\partial x_i} - b_i(\mathbf{x}) \frac{\partial a_j}{\partial x_i} \right).
$$

$[X, Y]$ is thus a vector field.

<!-- ======================= -->
<!-- PROBLEM 2.15            -->
<!-- ======================= -->
## Problem 2.15

$$
\begin{align}
X_{\{f, g\}}h &= \{\{f, g\}, h\} \\
&= \{f, \{g, h\}\} - \{g, \{f, h\}\} \\
&= X_f(X_g h) - X_g(X_f h) \\
&= [X_f, X_g]h.
\end{align}
$$

<!-- ======================= -->
<!-- PROBLEM 2.16            -->
<!-- ======================= -->
## Problem 2.16

### Part a
Let

$$
X_f = \frac{\partial f}{\partial x}\frac{\partial}{\partial p} - \frac{\partial f}{\partial p} \frac{\partial}{\partial x}
$$

#### "➡"
We want to show if $X = X_f$ for some $f$, then $\nabla \cdot X = 0$.

In this case

$$
g_1(x, p)\frac{\partial}{\partial x} + g_2(x, p)\frac{\partial}{\partial p} X = X_f = \frac{\partial f}{\partial x}\frac{\partial}{\partial p} - \frac{\partial f}{\partial p} \frac{\partial}{\partial x},
$$

which means that $g_1 = -\partial f / \partial p$ and $g_2 = \partial f / \partial x$. Thus [@lee2012introduction]

$$
\nabla \cdot X = \frac{\partial g_1}{\partial x} + \frac{\partial g_2}{\partial p} = -\frac{\partial^2 f}{\partial x \partial p} + \frac{\partial^2 f}{\partial p \partial x} = 0.
$$

#### "⬅"
Assume

$$
\nabla \cdot X = \frac{\partial g_1}{\partial x} + \frac{\partial g_2}{\partial p} = 0.
$$

We want to show that there exists $f$ such that

$$
X_f = \frac{\partial f}{\partial x}\frac{\partial}{\partial p} - \frac{\partial f}{\partial p} \frac{\partial}{\partial x}  = X
$$

If $X = X_f$ then, that statement is equivalent to show that there's a function $f$ such that

$$
\frac{\partial f}{\partial x} = g_2 \quad\text{and}\quad -\frac{\partial f}{\partial p} = g_1.
$$

Using the results of Proposition 2.7 with $h_1 = g_2$, $h_2 = -g_1$ we get

$$
\frac{\partial g_2}{\partial p} = -\frac{\partial g_1}{\partial x} \iff \frac{\partial g_1}{\partial x} + \frac{\partial g_2}{\partial p} = 0,
$$

which is true by assumption. Thus there exists $f$ such that the above equations hold, and thus $X = X_f$.

### Part b

Define  $g_1 = x_1$, $g_2 = -x_2$, $g_3 = 0 = g_4$ (all linear components). Then

$$
\nabla \cdot X = \frac{\partial g_1}{\partial x_1} + \frac{\partial g_2}{\partial x_2} + \frac{\partial g_3}{\partial p_1} + \frac{\partial g_4}{\partial p_2} = 1 - 1 + 0 + 0 = 0,
$$

which shoes that it is possible to have divergence-free vector fields in $\mathbb{R}^4$ that are not Hamiltonian.

Now, assume for contradiction that $X = X_f$, then

$$
\begin{align}
\frac{\partial f}{\partial p_1} &= -g_1 = -x_1 \\
\frac{\partial f}{\partial p_2} &= -g_2 = x_2 \\
\frac{\partial f}{\partial x_1} &= g_3 = 0 \\
\frac{\partial f}{\partial x_2} &= g_4 = 0.
\end{align}
$$

From the last two expression we see that $f = f(p_1, p_2)$. But that contracts the first two expressions, which depend on $x_1$ and $x_2$. Therefore no such $f$ exists, even though $\nabla \cdot X = 0$.

<!-- ======================= -->
<!-- PROBLEM 2.17            -->
<!-- ======================= -->
## Problem 2.17

Let $f, g$ be homogeneous polynomials of degree $2# on $\mathbb{R}^{2n}$. Then each derivative $\partial f / \partial x_j$, $\partial f / \partial p_j$, $\partial g / \partial x_j$, $\partial g / \partial p_j$ is a homogeneous polynomial of degree $1$. For each $k$

- $\partial f / \partial x_k \cdot \partial g / \partial p_k$ is the product of two homogeneous polynomials of degree $1$, thus it is a homogeneous polynomial of degree $2$.
- $\partial f / \partial p_k \cdot \partial g / \partial x_k$ is the product of two homogeneous polynomials of degree $1$, thus it is a homogeneous polynomial of degree $2$.
- Their difference is thus also a homogeneous polynomial of degree $2$.

Therefore

$$
\{f, g\} = \sum_{k=1}^n \left( \frac{\partial f}{\partial x_k} \frac{\partial g}{\partial p_k} - \frac{\partial f}{\partial p_k} \frac{\partial g}{\partial x_k} \right)
$$

is a sum of homogeneous polynomials of degree $2$, thus it is also a homogeneous polynomial of degree $2$.

<!-- ======================= -->
<!-- PROBLEM 2.18            -->
<!-- ======================= -->
## Problem 2.18

For $f(x, p) = xp$

$$
\frac{dx}{dt} = \frac{\partial f}{\partial p} = x \qquad \frac{dp}{dt} = -\frac{\partial f}{\partial x} = -p.
$$

Therefore

$$
\varphi_t: \mathbb{R}^2 \to \mathbb{R}^2, \quad \varphi_t(x, p) = (e^t x, e^{-t} p).
$$

<!-- ======================= -->
<!-- REFERENCES              -->
<!-- ======================= -->

## References

\bibliography

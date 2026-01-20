<!-- ======================= -->
<!-- PROBLEM 2.11             -->
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

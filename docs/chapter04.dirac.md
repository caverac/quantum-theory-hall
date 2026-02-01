This is a small proof that The kernel $K_t$ converges to $\delta$ in the distribution sense as $t \to 0$.

Define

$$
\hat{K_t}(k) = \exp\left(-\frac{i\hbar t}{2m}k^2\right),
$$

so that

$$
K_t(x) = \frac{1}{2\pi}\int_{\mathbb{R}} dk\, \hat{K_t}(k)e^{ikx}.
$$

Let $\phi \in \mathcal{S}(\mathbb{R})$ be a Schwartz function, then

$$
\begin{align}
\int_{\mathbb{R}} d x\, K_t(x)\phi(x) &= \frac{1}{2\pi}\int_{\mathbb{R}} dk\, \hat{K_t}(-k)\hat{\phi}(k) \\
&= \frac{1}{2\pi}\int_{\mathbb{R}} dk\, \hat{K_t}(k)\hat{\phi}(k) \\
&= \frac{1}{2\pi}\int_{\mathbb{R}} dk\, e^{-i(\hbar t/2m)k^2}\hat{\phi}(k).
\end{align}
$$

As $t\to 0$ the phase factor goes to $1$ pointwise (e.g. for every fixed $k$, the phase becomes $1$ as $t \to 0$). Also, we have

- $|e^{-i(\hbar t/2m)k^2}| = 1$
- $\hat{\phi} \in \mathcal{S}(\mathbb{R})$ implies that $\hat{\phi}$ is integrable ($\mathcal{S}(\mathbb{R}) \subset L^1(\mathbb{R})$).

Thus, by the dominated convergence theorem, we can exchange the limit and the integral:

$$
\lim_{t \to 0} \int_{\mathbb{R}} d x\, K_t(x)\phi(x) = \frac{1}{2\pi}\int_{\mathbb{R}} dk\, \hat{\phi}(k) = \phi(0).
$$

That is exactly the definition of convergence to the Dirac delta in the distribution sense.

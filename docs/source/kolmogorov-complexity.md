# Kolmogorov Complexity

```{admonition} Definition
:class: definition
For $x \in \{0,1\}^*$,

$$
C(x) = \min \{\,|\pi| \mid \pi \in \{0,1\}^*,\; U(\pi) = x \}
$$

where $U$ is a universal Turing machine (TM).

$$
K(x) = \min \{\,|\pi| \mid \pi \in \{0,1\}^*,\; U(\pi) = x \}
$$

where $U$ is a universal prefix TM.
```

```{admonition} Fact
:class: fact
$$
\exists\,c \,\forall\,x.\quad C(x)\;\le\;K(x)\;\le\;C(x)\;+\;2\,\log|x|\;+\;c
$$
```

```{admonition} Definition
:class: definition
The (algorithmic) dimension of sequence $S \in \mathbf{C}$ is

$$
\dim(S)
= \liminf_{n \to \infty} \frac{K(S[0 \ldots n-1])}{n}
= \liminf_{n \to \infty} \frac{K(S \restriction n)}{n}.
$$
```

```{admonition} Definition
:class: definition
For $x \in \mathbb{R}^n$ and $r \in \mathbb{N}$, the Kolmogorov complexity of $x$ at precision $r$ is

$$
K_r(x) = \min \{\, K(q) \mid q \in \mathbb{Q}^n \,\land\, |q - x| \le 2^{-r}\}.
$$
```

```{admonition} Definition
:class: definition
The dimension of a point $x \in \mathbb{R}^n$ is

$$
\dim(x) = \liminf_{r \to \infty}\,\frac{K_r(x)}{r}.
$$
```

```{admonition} Fact
:class: fact
For any $x \in \mathbb{R}^n$:

1. $0 \le \dim(x) \le n$
2. $x \textup{ is computable} \implies \dim(x) = 0$
3. $x \textup{ is random} \implies \dim(x) = n$
```

```{admonition} Theorem (Point-to-Set Principle)
:class: theorem
For $E \subseteq \mathbb{R}^n$,

$$
\dim_H(E) = \min_{A \subseteq \mathbb{N}} \,\sup_{x \in E}\,\dim^A(x)
$$

where $\dim_H$ is the Classical Hausdorff Dimension.
```
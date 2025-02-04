# Computability Theory


```{admonition} Definition
:class: definition

A subprobability measure on $\set{0,1}^*$ is a function $p: \set{0,1}^* \ to {[0,1]}$ such that 

$$\sum_{x\in\set{0,1}^*}p(x)\leq 1$$

```



```{admonition} Definition
:class: definition

A probability measure on $\set{0,1}^*$ is a function $p: \set{0,1} \to {[0,1]}$ such that 


$$ \sum_{x\in\set{0,1}^*}p(x)= 1$$

```

```{admonition} Definition
:class: definition
A function $f : \{0,1\}^* \to \mathbb{R}$ is **computable** if there is a computable function 

$$
\hat{f} : \{0,1\}^* \times \mathbb{N} \to \mathbb{Q}
$$

such that, for all $x \in \{0,1\}^*$ and $r \in \mathbb{N}$,

$$
|\hat{f}(x,r) - f(x)| \;\le\; 2^{-r}.
$$

The variable $r$ is called the **precision parameter**.
```

```{admonition} Definition
:class: definition
A function $f : \{0,1\}^* \to \mathbb{R}$ is **upper semicomputable** if there is a computable function

$$
\hat{f} : \{0,1\}^* \times \mathbb{N} \to \mathbb{Q}
$$
with the following two properties:

1. For all $x \in \{0,1\}^*$ and $t \in \mathbb{N}$:

   $$
   \hat{f}(x,t) \;\le\; \hat{f}(x,t+1) \;\le\; f(x).
   $$

2. For all $x \in \{0,1\}^*$:

   $$
   \lim_{t \to \infty} \hat{f}(x,t) \;=\; f(x).
   $$


The variable $t$ is called the **patience parameter**.
```

```{admonition} Definition
:class: definition

A function $f : \{0,1\}^* \to \mathbb{R}$ is **lower semicomputable** if $-f$ is upper semicomputable.
```

```{admonition} Definition
:class: definition
A real number $\alpha \in \mathbb{R}$ is **computable** if the constant function$K_\alpha : \{0,1\}^* \to \mathbb{R}$

$$
 K_\alpha(w) = \alpha
$$

is computable.
```

Fix a standard enumeration $M_0, M_1, M_2, \ldots$ of all Turing machines with inputs and outputs in $\mathbb{N}$. For each $i \in \mathbb{N}$, let 
$\varphi_i : \mathbb{N} \to \mathbb{N}$ be the partial function computed by $M_i$.

```{admonition} Definition
:class: definition
The **(diagonal) halting problem** is the set

$$
K = \{\,k \in \mathbb{N} \mid M_k(k) \downarrow\}.
$$
```

```{admonition} Fact
:class: fact
$K$ is **computably enumerable** but **not decidable**.
```

```{admonition} Definition
:class: definition
A **property of programs** is a set $P \subseteq \mathbb{N}$. We say $P$ is **trivial** if $P = \varnothing$ or $P = \mathbb{N}$. Otherwise, $P$ is **non-trivial**.
```

```{admonition} Definition
:class: definition
An I/O property of programs is a property $P \subseteq \mathbb{N}$ satisfying

$$
\varphi_i = \varphi_j \;\;\Longrightarrow\;\; \bigl[i \in P \iff j \in P\bigr].
$$
```

```{admonition} Rice's Theorem
:class: theorem
Every non-trivial I/O property is undecidable.
```

```{admonition} Definition
:class: definition
An **enforcer** of an I/O property $P$ of programs is a function $f : \mathbb{N} \to \mathbb{N}$ such that for all $i \in \mathbb{N}$:

1. $f(i) \in P$,
2. $i \in P \Longrightarrow \varphi_{f(i)} = \varphi_i.$
```

```{admonition} Definition 
:class: definition
Let $P \subseteq \mathbb{N}$. We say $P$ is **computably enforceable** if there exists a computable function $f : \mathbb{N} \to \mathbb{N}$ that enforces $P$.
```

```{admonition} Definition
:class: definition
A **prefix set** is a language $A \subseteq \{0,1\}^*$ such that for all $x, y \in \{0,1\}^*$,

$$
x \sqsubseteq y \;\Longrightarrow\; x = y,
$$

i.e., no element of $A$ is a prefix of any other element of $A$.
```

```{admonition} Definition
:class: definition

Define

$$
P_{\mathtt{pref}} = \{\,i \in \mathbb{N} \mid \textup{$\mathrm{dom}\varphi_i$ is a prefix set}\}.
$$
```

```{admonition} Theorem
:class: theorem

$P_{\mathtt{pref}}$ is computably enforceable.

*(Proof: TODO.)*
```


Since $P_{\mathtt{pref}}$ is computably enforceable, there is an enumeration of all  [^1] prefix Turing Machines, $\hat{M}_0, \hat{M}_1, \hat{M}_2, \ldots$. We call this the **standard enumeration** of all prefix TMs.

[^1]: Technically, this enumeration does not “hit” every prefix Turing Machine object itself, but it does hit **every behavior** that any prefix TM can have.

```{admonition} Definition
:class: definition

A **universal prefix TM** is a prefix Turing Machine $\hat{U}$ such that, for all $n \in \mathbb{N}$ and $\pi \in \{0,1\}^*$,

$$
\hat{U}(\,0^n 1 \,\pi) \;\cong\; \hat{M}_n(\pi).
$$
```

```{admonition} Definition
:class: definition

Let $M$ be a Turing Machine.

1. For each $x \in \{0,1\}^*$, the set of programs for $x$ on $M$ is

   $$
   \mathrm{PROG}_M(x) \;=\; \{\,\pi \in \{0,1\}^* \mid M(\pi) = x\}.
   $$

2. The set of valid programs on $M$ is

   $$
   \mathrm{PROG}_M \;=\; \{\,\pi \in \{0,1\}^* \mid M(\pi)\!\downarrow\}.
   $$
```

```{admonition} Observation
:class: observation
For every TM $M$,

$$
\mathrm{PROG}_M \;=\; \bigcup_{x \in \{0,1\}^*} \mathrm{PROG}_M(x),
$$

which is a union of disjoint sets $\mathrm{PROG}_M(x)$.
```

```{admonition} Optimality Theorem
:class: theorem

For each prefix TM $M$, there is an **optimality constant** $c_M \in \mathbb{N}$ such that, for all $x \in \{0,1\}^*$,

$$
K(x) \le K_M(x) + c_M.
$$
```

# Metric Spaces

## Euclidean Space

```{admonition} Definition 1.1
:class: definition
$$\mathbb{R}^n = \left\{ (x_1, \ldots, x_n) \mid \forall i \cdot x_i \in \mathbb{R} \right\}$$
```

```{admonition} Definition 1.2
:class: definition

The Euclidean **metric** on $\mathbb{R}^n$ is the function $d: \mathbb{R} \times \mathbb{R} \to {[0,\infty)}$ is defined by

$$d((x_1,\ldots,x_n),(y_1,\ldots,y_n))=\sqrt{\sum_{i=1}^{n}(x_i-y_i)^2}$$

<span class="material-icons face"></span>

where $\mathbb{R}$ is the set of real numbers and $n \in\mathbb{Z}^+$
```

```{admonition} Definition 1.3
:class: definition

$d$ is a metric if it satisfies:

1. $d(x,y)\geq0$ with equality if and only if $x=y$
2. $d(x,y)=d(y,x)$
3. $d(x,z)\leq d(x,y)+d(y,z)$ [*Triangle Inequality*]

```

```{admonition} Fact 1.4
:class: fact

For each $n\in\mathbb{Z}^+$, the set $\mathbb{R}^n$ is uncountable, with $\lvert {\mathbb{R^n}} \rvert = \lvert {\mathbb{R}} \rvert = 2^{\aleph_0} = \mathfrak{c}$


```

```{admonition} Definition 1.5
:class: definition

A set $D\subseteq\mathbb{R}^n$ is dense if for every $x\in\mathbb{R}^n$ and $\varepsilon>0$ there exists a point $q\in D$ such that

$$0<d(q,x)<\varepsilon$$
```

```{admonition} Fact 1.6
:class: fact

$\mathbb{Q}^n$ is dense in $\mathbb{R}^n$ and $\mathbb{Q}^n$ is countable with $\lvert {\mathbb{Q}^n} \rvert = \lvert {\mathbb{N}} \rvert = \aleph_0$

*(Proof: [see this post](https://math.stackexchange.com/questions/2708832/prove-that-mathbbqnis-dense-subset-of-mathbbrn))*

```

```{admonition} Definition 1.7
:class: definition

A metric space $(X,d)$ is separable if it has a countable dense subset.

```

```{admonition} Definition 1.8
:class: definition

An open ball of radius $r$ about $x$, denoted $B_r(x)$ is defined as

$$B_r(x)=B(x,r)=\set{y\in\mathbb{R}^n\mid d(x,y)<r}$$

*(See also: [{octicon}`link-external` Open Ball](https://mathworld.wolfram.com/OpenBall.html))*

```

*Examples: an interval in $\mathbb{R}$, a circle in $\mathbb{R}^2$, a sphere in $\mathbb{R}^3$*, etc.

```{admonition} Definition 1.9
:class: definition

A closed ball of radius $r$ about $x$, denoted $\bar B_r(x)$ is defined as

$$\bar B_r(x)=\bar B(x,r)=\set{y\in\mathbb{R}^n\mid d(x,y)\leq r}$$
```

```{admonition} Definition 1.10
:class: definition
A set $G\subseteq\mathbb{R}^n$ is open if there is a set $\cal B$ of open balls in $\mathbb{R}^n$ such that 

$$G=\cup{\cal B}=\cup_{B\in {\cal B}}B$$

```

```{admonition} Definition 1.11
:class: definition
A set $F\subseteq\mathbb{R}^n$ is closed if $\mathbb{R}^n\setminus F$ is open.
```

```{admonition} Fact 1.12
:class: fact
The only clopen (sets that are closed and open) are $\emptyset$ and $\mathbb{R}^n$
```

```{admonition} Definition 1.13
:class: definition

A set $Z\subseteq\mathbb{R}$ has measure 0 if for every $\varepsilon>0$ there is a countable set $\cal I$ of open intervals in $\mathbb{R}$ with the following properties:

1. $Z\subseteq\cup{\cal I}_\varepsilon$ [i.e., $\cal I$ covers $Z$]
2. $\sum_{I\in{\cal I}}\textup{length}(I)<\varepsilon$

*({octicon}`comment` See also: [this question](https://math.stackexchange.com/questions/620415/what-is-set-of-measure-zero) on Math Stack Exchange.)*
```

## Cantor Space

```{admonition} Definition 1.14
:class: definition

$\mathbf{C}=\set{0,1}^\infty = \set{0,1}^\omega=2^\omega$ is the set of all (infinite binary) sequences $s$, 

$$ s=b_1b_2b_3\ldots $$

where each $b_i\in\set{0,1}$
```

```{admonition} Definition 1.15
:class: definition

$\set{0,1}^*=2^{<\omega}$ is the set of all (finite binary) strings

$$w=b_1\ldots b_n$$

where $n\in\mathbf{N}$ and each $b_i\in\set{0,1}$. The length of the string is $\lvert w \rvert =n$. If $n=0$ this is the empty string, denoted $\lambda$
```

```{admonition} Definition 1.16
:class: definition

Define $\set{0,1}^{\leq\omega}=\set{0,1}^{<\omega}\cup\mathbf{C}$

``` 

```{admonition} Definition 1.17
:class: definition

Let $w\in\set{0,1}^*$ and $y\in\set{0,1}^{\leq\omega}$. $w$ is a prefix of $y$, and we write $w\sqsubseteq y$ if there exists $z\in\set{0,1}^{\leq w}$ such that

$$wz=y$$

*({octicon}`comment` note: here $wz$ is the concatenation of $w$ and $z$)*
```

```{admonition} Definition 1.18
:class: definition

$w$ is a proper prefix of $y$, and we write $w\sqsubset y$ if $w\sqsubseteq y$ and $w\neq y$ 
```

```{admonition} Definition 1.19
:class: definition

The cylinder generated by a string $w\in\set{0,1}^*$ is the set 

$$\mathbf{C}_w=\set{S\in\mathbf{C} \mid w\sqsubseteq S}$$

*({octicon}`comment` note: $\Rightarrow$ the set of all infinite sequences that start with $w$, see also [cylinder set on Wikipedia](https://en.wikipedia.org/wiki/Cylinder_set)
)*
```

```{admonition} Definition 1.20
:class: definition

The **standard metric** in $\mathbf{C}$ is the function $d:{\mathbf{C}\times\mathbf{C}} \to {[0,1]}$ defined by

$$d(S,T)=2^{-\max\set{\lvert w \rvert: w\sqsubseteq S\land w\sqsubseteq T}}$$

*({octicon}`comment` note: This perfectly matches the idea of "longest common prefix" {octicon}`arrow-both`  "how soon they differ". The deeper the common prefix, the closer the two sequences are in this metric.)*
```

This is a metric. In fact, it is an [ultrametric](https://mathworld.wolfram.com/Ultrametric.html), meaning that it satisfies the strengthening of the triangle inequality:

$$d(S,U)\leq \max\set{d(S,T),d(T,U)}$$

```{admonition} Fact 1.21
:class: fact
$\mathbf{C}$ is uncountable, with $\lvert \mathbf{C} \rvert = \lvert \mathbb{R} \rvert =2^{\aleph_0}$
```

````{admonition} Fact 1.22
:class: fact

The countable set 

$$D=\set{w0^w\mid w\in\set{0,1}^*}$$

testifies that $\mathbf{C}$ is separable.

```{dropdown} Brief Proof

- **countable**: [prove $\set{0,1}^*$ is countable](https://math.stackexchange.com/questions/2560968/is-the-set-of-all-possible-binary-strings-countable)
- **dense**: for every $\varepsilon>0$ and given $w \in \mathbb{C}$,
    - $w$ is an infinite binary sequence
    - find a large $n$ such that $2^{-n}<\varepsilon$
    - match the prefix of $w$ with the length $n$, denoted $w_n$, we have $w_n 0 ^{w_n} \in D$ and $d(w,w_n 0 ^{w_n})=2^{-n}<\varepsilon$
```

````

```{admonition} Definition 1.23
:class: definition

The (uniform, or Lebesgue product) measure of a cylinder $\mathbb{C}_w$ is 

$$\mu(\mathbb{C}_w)=\mu(w)=2^{-\lvert w \rvert}$$

*({octicon}`comment` note: all strings in the cylinder have the metric distance $2^{-\lvert w \rvert}$ with $w$, which is the upper bound of the metric distance between any two strings in the cylinder)*

```

```{admonition} Definition 1.24
:class: definition
A set $G \subseteq \mathbf{C}$ is open if it is a union of cylinders.
```

```{admonition} Definition 1.25
:class: definition
A set $F \subseteq \mathbf{C}$ is closed if $\mathbf{C} \setminus F$ is open.
```

```{admonition} Fact 1.26
:class: fact
The set $\varnothing$ and $\mathbf{C}$ are clopen in $\mathbf{C}$, but there are many other clopen sets. (Exercise)
```

```{admonition} Definition 1.27
:class: definition
A set $Z \subseteq \mathbf{C}$ has measure 0, and we write $\mu(Z) = 0$ if for every $\varepsilon > 0$ there is a countable set $\mathbf{C}_\varepsilon$ of cylinders with the following two properties:

1. $ Z \subseteq \bigcup \mathbf{C}_\varepsilon = \bigcup_{C \in \mathbf{C}_\varepsilon} C $

2. $ \sum_{C \in \mathbf{C}_\varepsilon} \mu(C) < \varepsilon $
```

```{admonition} Definition 1.28
:class: definition
A set $Z \subseteq \mathbf{C}$ has algorithmic measure 0, if there exists a computable function 

$$f : \mathbb{N} \times \mathbb{N} \to \{0,1\}^*$$

such that for every $k \in \mathbb{N}$
1. $ Z \subseteq \bigcup_{l=0}^{\infty} \mathbf{C}_{f(k,l)} $
2. $ \sum_{l=0}^{\infty} 2^{-|f(k,l)|} < 2^{-k} $
```

**Remark.**  There are certain edge cases in the above definition that can be dealt with by perhaps defining $\emptyset$ as a cylinder.

```{admonition} Definition 1.29
:class: definition
A sequence $z\in\mathbb{C}$ is (algorithmically, or [Martin-Löf](https://en.wikipedia.org/wiki/Algorithmically_random_sequence)) random [^1] if $\set{z}$ does not have algorithmic measure 0.
```

[^1]: See also: [An introduction to
(algorithmic) randomness](https://www.nieuwarchief.nl/serie5/pdf/naw5-2018-19-1-044.pdf)

# Metric Spaces

## Euclidean Space

```{admonition} Definition 1.1
:class: definition
$$\mathbb{R}^n = \left\{ (x_1, \ldots, x_n) \mid \forall i \cdot x_i \in \mathbb{R} \right\}$$
```

```{admonition} Definition 1.2
:class: definition

The Euclidean metric on $\mathbb{R}^n$ is the function $d: \mathbb{R} \times \mathbb{R} \to {[0,\infty)}$ is defined by

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
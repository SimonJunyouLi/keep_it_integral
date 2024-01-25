# Keep It Integral
This is a solution for fractional rounding of the standard Linear Programming relaxation of maximum matching. 

## Problem Statement
The input of the probelm is an optimal fractional solution to the following Linear Program,

```math 
\begin{align*}
\text{max} & \sum_{e \in E} x_w  \\
\text{subject to:} & \sum_{e \in \delta(v)} x_e \le 1 \quad \forall v \in V \\
& x_e \le 1 \quad \forall e \in E \\
& x_e \ge 0 \quad \forall e \in E
\end{align*}
```

where $G$ is a bipartite graph, $E$ is the set of edges of $G$, $V$ is the set of nodes of $G$ and $\delta(v)$ denotes the set of edges of $G$ that are incident to $v$.

The desired output is a rounded, integral solution to the above Linear Program. 

## Proof of the algorithm
The algorithm is based on the proof [here](https://people.eecs.berkeley.edu/~satishr/cs270/sp11/rough-notes/matching.pdf).

Special thanks to [GlazeGlopMike](https://github.com/GlazeGlopMike) for helping with this problem.
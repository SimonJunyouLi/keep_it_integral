# keep_it_integral
Fractional Rounding for the standard Linear Programming relaxation of maximum matching

Given an optimal fractional to the following Linear Program,

```math 
\begin{align*}
\text{max} & \sum_{e \in E} x_w  \\
\text{subject to:} & \sum_{e \in \delta(v)} x_e \le 1 \quad \forall v \in V \\
& x_e \le 1 \quad \forall e \in E \\
& x_e \ge 0 \quad \forall e \in E
\end{align*}
```

where $E$ is the set of edges of $G$, $V$ is the set of nodes of $G$ and $\delta(v)$ denotes the set of edges of $G$ that are incident to $v$.
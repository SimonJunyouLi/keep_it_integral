# keep_it_integral
Fractional Rounding for the standard Linear Programming relaxation of maximum matching

```math 
\begin{center}
\begin{align*}
\text{max} & \sum_{e \in E} x_w  \\
\text{subject to:} & \sum_{e \in \delta(v)} x_e \le 1 \quad \forall v \in V \\
& x_e \le 1 \quad \forall e \in E \\
& x_e \ge 0 \quad \forall e \in E
\end{align*}
\end{center}
```
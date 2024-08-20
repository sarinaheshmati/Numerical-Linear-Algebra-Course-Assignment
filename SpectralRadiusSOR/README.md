# Spectral Radius Convergence of the SOR Method

This project explores the behavior of the Spectral Radius (ρ) in the Successive Over-Relaxation (SOR) method as the dimensions of the given system increase. Specifically, it demonstrates how the optimal spectral radius of the SOR method approaches 1 as the size of the matrix grows.

<img width="396" alt="Screenshot 1403-05-30 at 10 25 55 AM" src="https://github.com/user-attachments/assets/0a380cba-51e8-49b1-bedd-1746ff52463f">

## Overview

The project provides a Python implementation to compute the optimal spectral radius for SOR by analyzing the Jacobi iteration matrix derived from a tridiagonal system. By progressively increasing the matrix size, the code shows that the optimal relaxation parameter (ω) decreases, leading the spectral radius toward 1.

### Key Concepts:
- **Spectral Radius (ρ)**: A measure of the convergence rate of an iterative method.
- **SOR Method**: An iterative technique used to solve linear systems, particularly effective for large, sparse matrices.

### Interpretation:
As the dimensionality of the system increases, the convergence rate of the SOR method slows down, with the spectral radius tending toward 1. This indicates diminishing efficiency of the SOR method for very large systems, reflecting a fundamental limitation in its applicability to high-dimensional problems.

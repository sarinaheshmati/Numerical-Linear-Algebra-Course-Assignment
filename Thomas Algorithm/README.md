# Thomas Algorithm for Solving Tridiagonal Systems

This repository contains an implementation of the Thomas algorithm in Python, which efficiently solves tridiagonal systems of linear equations. The algorithm is optimized for matrices where non-zero elements are present only on the main diagonal, the sub-diagonal, and the super-diagonal.

## Features

- **Efficient Solution**: The Thomas algorithm is a simplified form of Gaussian elimination specifically designed for tridiagonal matrices, providing an efficient solution with reduced computational complexity.
- **Performance Measurement**: The implementation includes time measurement to evaluate the performance of the algorithm.

## How It Works

The algorithm follows these steps:
1. **Forward Elimination**: The algorithm eliminates variables from the tridiagonal matrix, transforming it into an upper triangular matrix.
2. **Back Substitution**: The solution vector is computed by back substitution, starting from the last equation and moving upward.

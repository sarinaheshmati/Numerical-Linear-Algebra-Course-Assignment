# Power and Inverse Iteration for Eigenvalue Computation

This project implements scaled power iteration and inverse power iteration methods to find the largest and smallest eigenvalues, as well as their corresponding eigenvectors, of the given matrix.

<img width="198" alt="Screenshot 1403-05-30 at 10 32 20 AM" src="https://github.com/user-attachments/assets/5e3f0ce7-f8d2-41f9-bffd-a194abf8bfce">

## Overview

The project focuses on using iterative methods to compute:
- **Largest Eigenvalue & Eigenvector**: Using the power iteration method.
- **Smallest Eigenvalue & Eigenvector**: Using the inverse power iteration method.

### Key Concepts:
- **Power Iteration**: An algorithm to find the dominant eigenvalue and its corresponding eigenvector.
- **Inverse Power Iteration**: A method to find the smallest eigenvalue and its eigenvector by applying power iteration to the inverse of the matrix.

### Process:
1. **Power Iteration**: The algorithm iteratively multiplies a random initial vector by the matrix, normalizing at each step to approximate the dominant eigenvalue and its eigenvector.
2. **Inverse Power Iteration**: The algorithm applies power iteration to the inverse of the matrix to approximate the smallest eigenvalue and its eigenvector.

This code performs five iterations of both methods and outputs the largest and smallest eigenvalues, as well as the corresponding eigenvectors.

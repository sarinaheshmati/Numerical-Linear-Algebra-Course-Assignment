# QR Factorization Algorithm

This repository contains an implementation of the QR factorization algorithm in Python. The algorithm is based on the Gram-Schmidt process, which decomposes a given matrix into an orthogonal matrix \( Q \) and an upper triangular matrix \( R \).

## Features

- **QR Factorization**: Decomposes any given matrix into the product of an orthogonal matrix \( Q \) and an upper triangular matrix \( R \).
- **Gram-Schmidt Process**: Uses the classical Gram-Schmidt orthogonalization method to achieve the decomposition.

## How It Works

The implementation follows these steps:
1. **Gram-Schmidt Orthogonalization**: The input matrix is orthogonalized using the Gram-Schmidt process.
2. **QR Decomposition**: The orthogonalized matrix is then used to compute the \( Q \) and \( R \) matrices.

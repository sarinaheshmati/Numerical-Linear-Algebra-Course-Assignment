# Low-Rank Image Compression using SVD

This project demonstrates the use of Singular Value Decomposition (SVD) for compressing images by approximating them with low-rank matrices. The goal is to represent the image using fewer singular values, thus reducing the amount of data needed to store the image while retaining most of its visual information.

## Overview

The project involves:
1. **Image Decomposition**: The image is first decomposed into three color channels (Red, Green, Blue), each represented by a matrix.
2. **Singular Value Decomposition (SVD)**: SVD is applied to each color channel to decompose it into three matrices: \( U \), \( S \), and \( V \).
3. **Low-Rank Approximation**: The image is reconstructed using only the first \( k \) singular values, where \( k \) is varied to observe the effect on the image quality and storage efficiency.

### Key Concepts:
- **SVD**: A mathematical technique that decomposes a matrix into three components: \( U \), \( S \), and \( V \), where \( S \) contains the singular values.
- **Low-Rank Approximation**: Reducing the rank of the matrix by keeping only the largest singular values, leading to a compressed version of the original matrix.

### Experiment:
The image is compressed using different values of \( k \) (10, 20, 40, 80, 160), which determine the number of singular values used in the reconstruction. As \( k \) increases, the reconstructed image becomes closer to the original, but requires more data to store.

### Results:
- **\( k = 10 \)**: The image is highly compressed with noticeable loss in detail.

![compressed_k_10](https://github.com/user-attachments/assets/a53e4b3a-f695-4b36-9aae-fcf8485faa18)

- **\( k = 20 \)**: Some details are restored, but compression artifacts are still visible.
  
![compressed_k_20](https://github.com/user-attachments/assets/b004a90e-7b4d-4c6b-9732-169561ef423e)

- **\( k = 40 \)**: The image quality improves further, with most essential features retained.

![compressed_k_40](https://github.com/user-attachments/assets/f4ca3eb7-fc76-4477-93d3-3f21f7b79023)

- **\( k = 80 \)**: The image is nearly indistinguishable from the original.

![compressed_k_80](https://github.com/user-attachments/assets/aef356eb-c7b7-4391-ac96-fbb2f1392977)

- **\( k = 160 \)**: The reconstructed image is almost identical to the original, with minimal compression.
  
![compressed_k_160](https://github.com/user-attachments/assets/ad090e36-af74-4d5e-95fc-8f327787d4ee)

This project illustrates the trade-off between image quality and data storage, providing a practical example of SVD-based image compression.

import numpy as np
from PIL import Image

# Load image
B = np.array(Image.open('khayyam.jpg'))

# Convert image to double precision
I = B.astype(float) / 255.0

kArr = [10, 20, 40, 80, 160]

for k in kArr:
    A = np.zeros_like(I)

    for i in range(3):
        # Perform Singular Value Decomposition
        U, S, V = np.linalg.svd(I[:, :, i])
        
        # Reconstruct the image using k singular values
        A[:, :, i] = U[:, :k] @ np.diag(S[:k]) @ V[:k, :]
        
    # Clip the pixel values to [0, 1]
    A = np.clip(A, 0, 1)

    # Save the compressed image in the same directory as the input image
    Image.fromarray(np.uint8(A * 255)).save('compressed_k_{}.jpg'.format(k))

    # Display the image
    Image.fromarray(np.uint8(A * 255)).show()


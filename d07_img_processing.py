import numpy as np  
import imageio  
import matplotlib.pyplot as plt  

# Load image and convert to NumPy array  
image = imageio.imread("messi.jpeg")  
image_array = np.array(image)  
print("Image shape:", image_array.shape)  

# Convert to grayscale  
gray_image = np.mean(image_array, axis=2).astype(np.uint8)  
print("Grayscale Image Shape:", gray_image.shape)  

# Flip image vertically
flipped_image = np.flip(gray_image, axis=1)  

# Adjust brightness  
brighter_image = np.clip(gray_image + 50, 0, 255).astype(np.uint8)  

# Display images using Matplotlib  
fig, ax = plt.subplots(1, 4, figsize=(16, 4))  

ax[0].imshow(image_array)  
ax[0].set_title("Original Image")  
ax[0].axis("off")  

ax[1].imshow(gray_image, cmap="gray")  
ax[1].set_title("Grayscale Image")  
ax[1].axis("off")  

ax[2].imshow(flipped_image, cmap="gray")  
ax[2].set_title("Flipped Image")  
ax[2].axis("off")  

ax[3].imshow(brighter_image, cmap="gray")  
ax[3].set_title("Brighter Image")  
ax[3].axis("off")  

plt.show()  

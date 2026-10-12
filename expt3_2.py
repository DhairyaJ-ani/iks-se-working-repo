import cv2
import matplotlib.pyplot as plt

# Replace 'temple.jpg' with the actual filename of the temple image on your computer
image_path = 'temple.jpg' 

# Load the image
img = cv2.imread(image_path)

if img is None:
    print(f"Error: Could not load image at '{image_path}'. Please ensure the image file is in the same directory or provide the full path.")
else:
    # OpenCV loads images in BGR format, convert to RGB for Matplotlib display
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # 1. Convert to Grayscale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 2. Apply Edge Detection (Canny Edge Detector)
    # Applying a slight Gaussian blur first helps reduce noise for better edge detection
    blurred = cv2.GaussianBlur(img_gray, (5, 5), 0)
    
    # The thresholds can be adjusted based on the image's contrast
    edges = cv2.Canny(blurred, threshold1=50, threshold2=150)
    
    # Create a figure to display the original, grayscale, and edge-detected images
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    
    # Plot Original Image
    axes[0].imshow(img_rgb)
    axes[0].set_title("Original Architecture")
    axes[0].axis('off')
    
    # Plot Grayscale Image
    axes[1].imshow(img_gray, cmap='gray')
    axes[1].set_title("Grayscale Form")
    axes[1].axis('off')
    
    # Plot Edge Detection
    axes[2].imshow(edges, cmap='gray')
    axes[2].set_title("Architectural Edges (Canny)")
    axes[2].axis('off')
    
    plt.suptitle("Highlighting the Architecture of the Konark Sun Temple", fontsize=16)
    plt.tight_layout()
    
    # Save the resulting figure
    output_filename = "temple_architecture_analysis.png"
    plt.savefig(output_filename, bbox_inches='tight')
    print(f"Analysis complete! Saved visual output to {output_filename}")
    
    # Display the plot
    plt.show()

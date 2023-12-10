import os
import tensorflow as tf
from tensorflow.keras.models import load_model

def print_model_shapes(model_path):
    print(f"Model: {model_path}")
    # Check if the path exists
    if not os.path.exists(model_path):
        print(f"Error: Model file {model_path} not found.")
        return

    # Load the model
    model = load_model(model_path)

    # Print the shapes of each layer
    for i, layer in enumerate(model.layers):
        print(f"Layer {i + 1}: {layer.name} - Output Shape: {layer.output_shape}")

if __name__ == "__main__":
    # Assuming .h5 files are in the current directory
    current_directory = os.getcwd()
    
    # List all files in the current directory with a .h5 extension
    h5_files = [f for f in os.listdir(current_directory) if f.endswith('.h5')]

    # Print the shapes for each .h5 file
    for h5_file in h5_files:
        print(f"\nModel: {h5_file}")
        model_path = os.path.join(current_directory, h5_file)
        print_model_shapes(model_path)

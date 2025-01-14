import tensorflow as tf

# List available physical GPUs
physical_devices = tf.config.list_physical_devices('GPU')
if physical_devices:
    print(f"GPU is available: {physical_devices}")
else:
    print("GPU is not available")

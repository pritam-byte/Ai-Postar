import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing import image
import numpy as np

def classify_xray():
    print("\n--- Chest X-ray Classifier ---")
    path = input("Enter path to chest X-ray image: ")

    try:
        model = tf.keras.applications.MobileNetV2(weights="imagenet", include_top=True)
        img = image.load_img(path, target_size=(224, 224))
        x = image.img_to_array(img)
        x = preprocess_input(np.expand_dims(x, axis=0))

        preds = model.predict(x)
        decoded = tf.keras.applications.imagenet_utils.decode_predictions(preds, top=3)[0]

        print("Top Predictions:")
        for (_, name, prob) in decoded:
            print(f"{name}: {prob:.2f}")
    except Exception as e:
        print(f"Error loading image or model: {e}")

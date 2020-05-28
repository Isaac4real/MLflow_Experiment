import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

import tensorflow as tf
from tensorflow.keras.layers import Input, Conv2D, Dense, Flatten, Dropout, GlobalMaxPooling2D
from tensorflow.keras.models import Model

import mlflow
from mlflow import pyfunc
import mlflow.tensorflow
import warnings
import mlflow.pyfunc
import sys

# Load in the data
fashion_mnist = tf.keras.datasets.fashion_mnist

(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0
print("x_train.shape:", x_train.shape)

# the data is only 2D!
# convolution expects height x width x color
x_train = np.expand_dims(x_train, -1)
x_test = np.expand_dims(x_test, -1)
print(x_train.shape)

# Enable auto-logging to MLflow to capture TensorBoard metrics.
mlflow.tensorflow.autolog()

def mlflow_run(params, run_name="Tracking Experiment: TensorFlow - CNN "):
  with mlflow.start_run(run_name=r_name) as run:
    # get current run and experiment id
    runID = run.info.run_uuid
    experimentID = run.info.experiment_id
        
    # number of classes
    K = len(set(y_train))
    print("number of classes:", K)
    # Build the model using the functional API
    i = Input(shape=x_train[0].shape)
    x = Conv2D(32, params['convSize'], strides=2, activation='relu')(i)
    x = Conv2D(64, params['convSize'], strides=2, activation='relu')(x)
    x = Conv2D(128, params['convSize'], strides=2, activation='relu')(x)
    x = Flatten()(x)
    x = Dropout(0.2)(x)
    x = Dense(512, activation='relu')(x)
    x = Dropout(0.2)(x)
    x = Dense(K, activation='softmax')(x)

    model = Model(i, x)

    # Compile and fit
    # Note: make sure you are using the GPU for this!
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    r = model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=params['epochs'])
    
    # Plot accuracy per iteration
    plt.plot(r.history['accuracy'], label='acc')
    plt.plot(r.history['val_accuracy'], label='val_acc')
    plt.legend()
      
  return (experimentID, runID)

# Use the model
if __name__ == '__main__':
   # suppress any deprecated warnings
   warnings.filterwarnings("ignore", category=DeprecationWarning)

   convSize = int(sys.argv[1]) if len(sys.argv) > 1 else 10
   epochs = int(sys.argv[2]) if len(sys.argv) > 2 else (3,3)
   params = {'epochs': epochs,
            'convSize': convSize}
   (exp_id, run_id) = mlflow_run(params)

   print(f"Finished Experiment id={exp_id} and run id = {run_id}")
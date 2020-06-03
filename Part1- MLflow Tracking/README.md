<img src="https://www.mlflow.org/docs/latest/_static/MLflow-logo-final-black.png" width="200">

#### MLflow Lab Part 1: Tracking Module
         
The goal of this example is to show how easy and straightforward it is to implement MLflow to a standard ML model.

**Simple steps to convert a ML model to MLflow:**
1. Import the required MLflow packages
2. Use MLflow Automatic Logging to log every metric and parameter of the model.
3. Iniciate the training model with `mlflow.start_run` to start logging.

|

|

|

#### Classification Problem using CNNs with Tensorflow

This is a very simple classification problem where we will be using the Fashion MNIST dataset from Keras.

<img src="https://timesofdatascience.com/wp-content/uploads/2019/02/fashion-846x515.jpg"
         alt="Fashion MNIST dataset " width="400">
         
**The Fasion MNIST dataset includes:**

* 60,000 training examples
* 10,000 testing examples
* 10 classes 
* 28x28 grayscale/single channel images

**The ten fashin labels include:**

1. T-shirt/top
2. Trouser/pants
3. Pullover shirt
4. Dress
5. Coat
6. Sandal
7. Shirt
8. Sneaker
9. Bag
10. Ankle boot

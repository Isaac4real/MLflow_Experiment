<img src="https://www.mlflow.org/docs/latest/_static/MLflow-logo-final-black.png" width="200">

#### MLflow Lab Part 3: Model Registry Demo
         
The goal of this lab to demonstrate how easy it is to register models with different `flavors` and to transition them trough different stages (using MLflow UI and MLflow API for that)

**What we will do (core principles):**
1. Train and track a XGBoost model
2. Register the best iteration of that model and stage it in `production`
3. Load and evaluate the current `production` model
4. Create a second model version using TensorFlow
5. Transition this model to `stagging`
6. Compare both `stagging` and `production` models
7. Transition the model from `stagging` to `production`

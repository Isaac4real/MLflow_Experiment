<img src="https://www.mlflow.org/docs/latest/_static/MLflow-logo-final-black.png" width="200">

#### MLflow Lab Part 3: Model Registry Demo
         
The goal of this lab to demonstrate how easy it is to register models with different `flavors` and to transition them trough different stages (using MLflow UI and MLflow API for that)

**What we will do (core principles):**
1. Train and track a XGBoost model
2. Register the best iteration of that model and stage it in `production`
3. Load and evaluate the current `production` model
4. Create a second model version using TensorFlow
5. Transition this model to `staging`
6. Compare both `staging` and `production` models
7. Transition the model from `staging` to `production`


 Series  Part 3 of 4
-----------
Other parts:
- [Part 1](https://github.com/Isaac4real/MLflow_Experiment/tree/master/Part1-%20MLflow%20Tracking)
- [Part 2](https://github.com/Isaac4real/MLflow_Experiment/tree/master/Part2-%20MLflow%20Projects%26Models)
- [Part 4](https://github.com/Isaac4real/MLflow_Experiment/tree/master/Part4-%20MLflow%20Registry_locally)
<img src="https://www.mlflow.org/docs/latest/_static/MLflow-logo-final-black.png" width="200">

#### MLflow Lab Part 4: Model Registry Demo - Locally

In [lab 3](https://github.com/Isaac4real/MLflow_Experiment/tree/master/Part3-%20MLflow%20Registry) we registered different models and transitioned them into different stages (All done in Azure Databricks as in the previous parts).
In this lab 4 our goals will be to replicate essentially the same thing in your machine (locally).

Setup environment
----------------------------------

1. ```git clone git@github.com:Isaac4real/MLflow_Experiment.git or git clone https://github.com/Isaac4real/MLflow_Experiment.git```
2. `cd <your_cloned_directory>/Part4- MLflow Registry_locally`
3. Install MLflow and the required Python modules within your [conda activated environment](https://docs.conda.io/projects/conda/en/latest/user-guide/install/) or [pipenv environment](https://pypi.org/project/pipenv) if using it
    * `pip install -r req.txt` or `pip3 install -r req.txt`
5. `cd src`
6. If using PyCharm or IntelliJ, create a project and load source files in into your project or use your choice of syntax-highlighted editor, like Sublime or vim
7. [How to use PyCharm and MLflow](https://www.youtube.com/watch?v=yzn1hNkQuWA&feature=youtu.be)


Lab 4 - Guidelines
-----------------

We'll use localhost (or your laptop) to run and register models with Model Registry, followed by
deploying a "production" model as a REST endpoint locally.

Stage 1 - Train and Track the model
-------------------

1. `python run_MNSITmodel.py`
2. launch `mlflow ui --backend-store-uri sqlite:///mlruns.db`
3. Got to `http://127.0.0.1:5000`
4. Pick the best model, register with Model Registry as `Fashion_MNISTmodel`
5. Choose second best model and create version 2 in the Model Registry
   * Transition the best model into `Production`
   * Transition the second best model into `Staging`

stage 2 - Deploy and make predictions
-------------------
 
Let's take our production model from our Model Registry and [deploy and serve models](https://www.mlflow.org/docs/latest/models.html#deploy-mlflow-models) locally as a REST endpoint to a server launched by MLflow CLI. 

1. From the same directory run:
 * ```./deploy_model.sh``` 
 
This launches a gunicorn server serving at the localhost `127.0.0.1:5000`. Now you can score locally
on the deployed produciton model as a REST point.
 
2. From another terminal send a POST request with our JSON payload
  * ```python make_predictions.py```

 

     
 Series Part 4 of 4
-----------
Other parts:
- [Part 1](https://github.com/Isaac4real/MLflow_Experiment/tree/master/Part1-%20MLflow%20Tracking)
- [Part 2](https://github.com/Isaac4real/MLflow_Experiment/tree/master/Part2-%20MLflow%20Projects%26Models)
- [Part 3](https://github.com/Isaac4real/MLflow_Experiment/tree/master/Part3-%20MLflow%20Registry)
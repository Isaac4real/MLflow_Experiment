import mlflow
import warnings
import mlflow.pyfunc
import pandas as pd
import numpy as np

#
# Short example how to run a MLflow GitHub Project programmatically using
# MLflow Fluent APIs https://mlflow.org/docs/latest/python_api/mlflow.html#mlflow.run
#

if __name__ == '__main__':

   # Suppress any deprcated warnings
   warnings.filterwarnings("ignore", category=DeprecationWarning)
   parameters = {'convSize': 2, 'epochs': 5}
   ml_project_uri ="git://github.com/Isaac4real/MLflow_Project.git"

   # Iterate over three different runs with different parameters
   print("Running with param = ",parameters)
   res_sub = mlflow.run(ml_project_uri, parameters=parameters)
   print("status= ", res_sub.get_status())
   print("run_id= ", res_sub.run_id)
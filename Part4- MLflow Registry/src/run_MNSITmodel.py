import mlflow

from cls.XGBoostModel import XGBoostModel
from cls.utils import Utils

"""
This program will use the MLflow Model Registry to build a machine learning application that forecasts the 
daily power output of a wind farm. Wind farm power output depends on weather conditions: generally, more energy 
is produced at higher wind speeds. Accordingly, the machine learning models used in program predict power output 
based on weather forecasts with three features: wind direction, wind speed, and air temperature.

It uses altered data from the National WIND Toolkit dataset provided by NREL, which is publicly available and cited as follows:

Draxl, C., B.M. Hodge, A. Clifton, and J. McCaa. 2015. Overview and Meteorological Validation of the Wind Integration National Dataset Toolkit (Technical Report, NREL/TP-5000-61740). Golden, CO: National Renewable Energy Laboratory.

Draxl, C., B.M. Hodge, A. Clifton, and J. McCaa. 2015. "The Wind Integration National Dataset (WIND) Toolkit." Applied Energy 151: 355366.

Lieberman-Cribbin, W., C. Draxl, and A. Clifton. 2014. Guide to Using the WIND Toolkit Validation Code (Technical Report, NREL/TP-5000-62595). Golden, CO: National Renewable Energy Laboratory.

King, J., A. Clifton, and B.M. Hodge. 2014. Validation of Power Output for the WIND Toolkit (Technical Report, NREL/TP-5D00-61714). Golden, CO: National Renewable Energy Laboratory.
"""

if __name__ == "__main__":
   # Use sqlite:///mlruns.db as the local store for tracking and registery
   mlflow.set_tracking_uri("sqlite:///mlruns.db")

   # Get Validation data
   (x_train, y_train), (val_x, val_y) = Utils.load_data()

   # Train, fit and register our model
   params_list = [
      {'max_depth': 10, 'eta': 0.1, 'num_round': 2}]
      #{'max_depth': 15, 'eta': 2, 'num_round': 2},]

   # Iterate over few different tuning parameters
   #model_name = "MNISTModel"
   for params in params_list:
      XGBoost_obj = XGBoostModel(x_train, val_x, y_train, val_y,
                                 max_depth=params['max_depth'],
                                 eta=params['eta'],
                                 num_round=params['num_round'])
      run_id = XGBoost_obj.mlflow_run()
      print("MLflow run_id={}".format(run_id))



   '''
   # Load test data
   score_df = val_x
   # Our JSON payload for scoring the model
   # Use as payload on the REST call to the deployed model
   # on the local host
   print(score_df.to_json(orient="records"))'''



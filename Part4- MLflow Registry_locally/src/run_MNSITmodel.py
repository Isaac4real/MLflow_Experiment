import mlflow

from cls.XGBoostModel import XGBoostModel
from cls.utils import Utils

if __name__ == "__main__":
   # Use sqlite:///mlruns.db as the local store for tracking and registery
   mlflow.set_tracking_uri("sqlite:///mlruns.db")

   # Get Validation data
   (x_train, y_train), (val_x, val_y) = Utils.load_data()

   # Set of parameters
   params_list = [
      {'max_depth': 10, 'eta': 0.1, 'num_round': 2},
      {'max_depth': 15, 'eta': 2, 'num_round': 2},]

   # Iterate over few different tuning parameters
   for params in params_list:
      XGBoost_obj = XGBoostModel(x_train, val_x, y_train, val_y,
                                 max_depth=params['max_depth'],
                                 eta=params['eta'],
                                 num_round=params['num_round'])
      run_id = XGBoost_obj.mlflow_run()
      print("MLflow run_id={}".format(run_id))

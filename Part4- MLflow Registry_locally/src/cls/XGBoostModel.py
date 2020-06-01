import mlflow
import mlflow.xgboost
import xgboost as xgb

class XGBoostModel():
   def __init__(self, x_train, x_test, y_train, y_test, max_depth, eta, num_round):
      self.dtrain = xgb.DMatrix(x_train.reshape(x_train.shape[0], -1), label=y_train)
      self.dtest = xgb.DMatrix(x_test.reshape(x_test.shape[0], -1), label=y_test)
      self.evalist = [(self.dtest, 'eval'), (self.dtrain, 'train')]
      self.num_round = num_round
      self.k = len(set(y_train))
      self.param = {'max_depth': max_depth,
                    'eta': eta,
                    'objective': 'multi:softmax',
                    'num_class': self.k,
                    'eval_metric': 'merror'}

   def mlflow_run(self, run_name="XGBOOST: MNIST Model"):
      with mlflow.start_run(run_name=run_name) as run:
         # Automatically capture the model's parameters, metrics, artifacts,
         # and source code with the autolog() function
         mlflow.xgboost.autolog()
         xgb.train(self.param, self.dtrain, num_boost_round=self.num_round, evals=self.evalist)
      return run.info.run_id


#!/usr/bin/env sh

echo "Deploying Production model name=Fashion_MNISTmodel"

# Set enviorment variable for the tracking URL where the Model Registry is
export MLFLOW_TRACKING_URI=sqlite:///mlruns.db
# Serve the production model from the model registry
mlflow models serve --model-uri models:/Fashion_MNISTmodel/production --no-conda

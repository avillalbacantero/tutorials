REM Builds the Pytorch Docker image
docker build . --file Dockerfile_pyTorch_TransformersBase -t sentiment_classifiction_pytorch:0.0.1
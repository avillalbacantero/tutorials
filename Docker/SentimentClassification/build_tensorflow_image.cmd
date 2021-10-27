REM Builds the Tensorflow Docker image
docker build . -f Dockerfile_Tensorflow_NVIDIA_NGC_Base -t sentiment_classification_tensorflow:0.0.1
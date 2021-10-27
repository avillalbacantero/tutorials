@REM Run the Pytorch image
@REM docker run -it ^
@REM --rm ^
@REM --name sentiment_classificator_torch ^
@REM --gpus=all ^
@REM --mount type=bind,source=C:\Users\Ana\Documents\Formacion\Tutorials\tutorials\Docker\SentimentClassification\data,target=/usr/src/sentiment_analysis/data ^
@REM sentiment_classification:0.0.1 --file data/input_file.txt

@REM Run the Pytorch image with text
@REM docker run -it ^
@REM --rm ^
@REM --name sentiment_classificator_torch ^
@REM --gpus=all ^
@REM --mount type=bind,source=C:\Users\Ana\Documents\Formacion\Tutorials\tutorials\Docker\SentimentClassification\data,target=/usr/src/sentiment_analysis/data ^
@REM sentiment_classification:0.0.1 --text "I love you"

@REM Run the Tensorflow image
@REM docker run -it ^
@REM --rm ^
@REM --name sentiment_classificator_tf ^
@REM --gpus=all ^
@REM --mount type=bind,source=C:\Users\Ana\Documents\Formacion\Tutorials\tutorials\Docker\SentimentClassification\data,target=/usr/src/sentiment_analysis/data ^
@REM sentiment_classification_tensorflow:0.0.1 --file data/input_file.txt

@REM Run the Tensorflow image with text
docker run -it ^
--rm ^
--name sentiment_classificator_tf ^
--gpus=all ^
--mount type=bind,source=C:\Users\Ana\Documents\Formacion\Tutorials\tutorials\Docker\SentimentClassification\data,target=/usr/src/sentiment_analysis/data ^
sentiment_classification_tensorflow:0.0.1 --text "I love you"
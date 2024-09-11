# aws-lambda-selenium-layer
Precompiled layer of selenium for headless enviroments in aws lambda. Supports python 3.8 / 3.11. \

Pridat navod na upload cez S3 - nezabudnite vymazat bucket S3 - ulozene to bude v lambde \
Test cez examples \


chromedriver and healdess chrome version - 86.0.4240.111 \
python versions \
                  3.8   NO \
                  3.9   YES \
                  3.10  YES \
                  3.11  YES \
                  3.12  NO \
selenium version - 4.31.1 \


Sources:
serverless-chrome: https://github.com/adieuadieu/serverless-chrome v1.0.0-57 \
built-on: https://github.com/diegoparrilla/headless-chrome-aws-lambda-layer \

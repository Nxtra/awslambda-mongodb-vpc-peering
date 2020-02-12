cd src/Function
export OLDPWD=$(pwd)
echo $OLDPWD
pip install -r requirements.txt -t ./package
cd package
zip -r ${OLDPWD}/function.zip .
cd ${OLDPWD}
zip -g function.zip mongodb_lambda.py
cd ../..
sam deploy --guided
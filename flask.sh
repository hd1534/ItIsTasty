export FLASK_APP=ItIsTasty
export FLASK_DEBUG=true
export FLASK_RUN_PORT=5000

export UPLOAD_FOLDER=/home/test/helloNewWorld/upload

export DAPP_DB_NAME=itistasty
export DAPP_DB_USER=itistasty
export DAPP_DB_PASSWORD=itistasty
export DAPP_DB_ADDRESS=127.0.0.1:3306

flask db migrate
flask db upgrade

flask run --host=0.0.0.0
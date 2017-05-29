#!/bin/bash
LOGFILE='data/gunicorn.log'
ERRORFILE='data/gunicorn-error.log'

NUM_WORKERS=3

ADDRESS=0.0.0.0:8000

exec gunicorn odyssy.wsgi:application \
-w $NUM_WORKERS --bind=$ADDRESS \
--reload \
--log-level=debug \
--log-file=$LOGFILE 2>>$LOGFILE  1>>$ERRORFILE &

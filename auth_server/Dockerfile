FROM python:3
WORKDIR /app
ENV FLASK_APP=app.py
ENV FLASK_DEBUG=1
COPY . .
RUN pip install -r requirements.txt
RUN chmod u+x ./entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
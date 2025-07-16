FROM apache/airflow:latest-python3.9
COPY requirements.txt .
COPY src/ .
ENV PYTHONPATH=/opt/airflow/src:$PYTHONPATH
COPY dags/ .
RUN pip install -r requirements.txt
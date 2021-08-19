FROM python:latest
RUN pip install flask psycopg2 yaml2
COPY . .
ENTRYPOINT [ "python", "show_result.py"]
FROM python:3.10-slim
WORKDIR /app
COPY environment.yml .
RUN pip install pandas==2.2.0 numpy==1.26.3 statsmodels==0.14.1 pyyaml==6.0.1
COPY . .
CMD ["python", "src/main.py"]

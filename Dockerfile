FROM python:3.12.7

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirement.txt

ENV PORT 8080

EXPOSE 8080

ENTRYPOINT ["streamlit", "run", "webapp_insurance.py", "--server=8080", "--server.address=0.0.0.0"]


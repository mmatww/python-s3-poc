FROM python:3.11-alpine as base

FROM base as builder
COPY requirements.txt /requirements.txt
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install -r /requirements.txt

FROM base
COPY --from=builder /opt/venv /opt/venv
COPY app.py /app/app.py
WORKDIR /app
ENV PATH="/opt/venv/bin:$PATH"
CMD ["python", "app.py"]

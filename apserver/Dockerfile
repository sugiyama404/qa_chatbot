FROM python:3.12-slim-bullseye AS builder

WORKDIR /opt
COPY requirements.txt .

# hadolint ignore=DL3013
RUN pip install --no-cache-dir -r requirements.txt  --default-timeout=3000

COPY . .

# 実行ステージ
FROM python:3.12-slim-bullseye

ARG USERNAME=nonroot
WORKDIR /opt
COPY --from=builder /opt ${WORKDIR}

COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages

RUN useradd -m ${USERNAME} && chown -R ${USERNAME}:${USERNAME} .
USER ${USERNAME}

EXPOSE 8000
CMD ["python","app/main.py"]

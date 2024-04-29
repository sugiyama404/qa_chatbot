FROM python:3.12-slim-bullseye AS builder

RUN apt-get update && \
    apt-get -y install --no-install-recommends \
    locales=2.31-13+deb11u8 && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8 && \
    apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

WORKDIR /root/opt
COPY requirements.txt .

# hadolint ignore=DL3013
RUN pip install --no-cache-dir -r requirements.txt  --default-timeout=3000

COPY . .

# 実行ステージ
FROM python:3.12-slim-bullseye

ARG USERNAME=nonroot

WORKDIR /root/opt
COPY --from=builder /root/opt .
RUN useradd -m ${USERNAME}

COPY --from=builder /usr/lib /usr/lib
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages

RUN chown -R ${USERNAME}:${USERNAME} .
USER ${USERNAME}

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

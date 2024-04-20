FROM python:3.12-slim-bullseye AS builder

RUN apt-get update && \
    apt-get -y install --no-install-recommends \
    locales=2.31-13+deb11u8 tzdata=2024a-0+deb11u1 default-libmysqlclient-dev=1.0.7 \
    pkg-config=0.29.2-1 fonts-ipafont=00303-21 gcc=4:10.2.1-1 && \
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
RUN pip install  --no-cache-dir --upgrade pip setuptools
RUN pip install  --no-cache-dir -r requirements.txt

COPY . .

# 実行ステージ
FROM python:3.12-slim-bullseye

ARG USERNAME=nonroot

WORKDIR /root/opt
COPY --from=builder /root/opt .
RUN useradd --shell /bin/bash -m ${USERNAME}

COPY --from=builder /usr/local/lib /usr/local/lib
COPY --from=builder /lib/python3.13 /lib/python3.13

RUN chown -R ${USERNAME}:${USERNAME} .
USER ${USERNAME}

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

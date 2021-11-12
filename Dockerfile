FROM ubuntu:latest

ENV PYTHON_VERSION 3.10.0
ENV TZ=Europe/Madrid
ENV DEBIAN_FRONTEND noninteractive

# set working directory
WORKDIR /app

# set dependencies for pyenv
RUN apt-get update \
        && apt-get install -y --no-install-recommends make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget ca-certificates \
           curl llvm libncurses5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev mecab-ipadic-utf8 git

# set-up necessary Env vars for PyEnv
ENV PYENV_ROOT /root/.pyenv
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH

# install pyenv
RUN set -ex \
    && curl https://pyenv.run | bash \
    && pyenv update \
    && pyenv install $PYTHON_VERSION \
    && pyenv global $PYTHON_VERSION \
    && pyenv rehash

# install poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python - \
    && export PATH="$HOME/.local/bin:$PATH"

ENV PATH="${PATH}:$HOME/.local/bin"

# copy necessary files
COPY . .

# configure poetry & install dependencies
RUN $HOME/.local/bin/poetry config virtualenvs.create false \
  && $HOME/.local/bin/poetry install --no-interaction --no-ansi

# remove unecessary .git directory
RUN rm -rf .git

ENTRYPOINT [ "pyenv","version" ]
ENTRYPOINT [ "cd","app/excel-validator/excel_validator" ]
ENTRYPOINT [ "chmod","755 excel_validator.py" ]

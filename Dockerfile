FROM python:3.13.1-bullseye

ENV PYTHONUNBUFFERED=1

RUN apt update

ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$HOME/.local/bin:$PATH"

RUN apt install gettext -y
# Create a virtual environment
RUN python3 -m venv $VIRTUAL_ENV

# Install Poetry globally
RUN pip install --upgrade pip && pip install poetry

# Set up working directory
RUN mkdir -p /code
WORKDIR /code

# Copy Poetry files for dependency installation
COPY pyproject.toml poetry.lock ./

# Install dependencies
RUN poetry install --no-root

# Copy project files
COPY . .
RUN chmod 755 /code/start-django.sh

# Expose port
EXPOSE 8000

# Run the application
ENTRYPOINT [ "/code/start-django.sh" ]
# --- Stage 1: The "Builder" Stage (The Messy Kitchen) ---
FROM python:3.9 AS builder

WORKDIR /app

# Copy requirements first for caching
COPY requirements.txt .

# Create a virtual environment and install dependencies into it
RUN python3 -m venv /opt/venv
RUN /opt/venv/bin/pip install --upgrade pip
RUN /opt/venv/bin/pip install -r requirements.txt

# Copy the rest of the source code
COPY . .

# Install our package into the virtual environment
RUN /opt/venv/bin/pip install .


# --- Stage 2: The "Final" Stage (The Clean Cake Box) ---
# Start from a clean, lightweight base image
FROM python:3.9-slim

WORKDIR /app

# The magic step: Copy ONLY the populated virtual environment from the builder.
# This contains our application AND all its dependencies like 'click'.
COPY --from=builder /opt/venv /opt/venv

# Set the PATH so the shell can find our 'wordcount' command inside the venv
ENV PATH="/opt/venv/bin:$PATH"

# Set the entrypoint to our installed command
ENTRYPOINT ["wordcount"]
CMD ["--help"]
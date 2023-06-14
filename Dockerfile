# Use a minimal Ubuntu base image
FROM ubuntu:20.04 AS base

# Set the working directory
WORKDIR /app

# Install required dependencies
RUN apt-get update && apt-get install -y software-properties-common

# Add the deadsnakes PPA to get Python 3.11
RUN add-apt-repository ppa:deadsnakes/ppa

# Update package lists again
RUN apt-get update

# Install Python 3.11 and pip
RUN apt-get install -y python3.11 python3.11-distutils python3.11-dev python3.11-venv curl
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python3.11 get-pip.py

# Copy only the requirements file to leverage Docker caching
COPY requirements.txt .

# Install the requirements with progress bar
RUN --mount=type=cache,target=/root/.cache/pip \
    python3.11 -m pip install --cache-dir=/root/.cache/pip --progress-bar=on -r requirements.txt


# Use a separate stage for the final image to minimize size
FROM base AS final

# Copy all files from the previous stage
COPY . .

# Expose the desired port for the server (change it as per your server configuration)
EXPOSE 5000

# Run the Python server
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]

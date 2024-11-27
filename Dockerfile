# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Upgrade pip to the latest version
RUN pip install --upgrade pip

# Install the latest version of setuptools
RUN pip install --upgrade setuptools

# Copy the entire project into the container
COPY . .

# Set the default command to run the test suite
CMD ["python", "-m", "unittest", "discover", "-s", "."]
# Stage 1: Frontend build
FROM node:18 AS frontend-builder

# Set up the working directory
WORKDIR /frontend

# Install NPM dependencies
COPY package*.json ./
RUN npm install

# Copy TypeScript source files
COPY src/static/src/ src/static/src/

# Build TypeScript
COPY tsconfig.json ./
COPY webpack.config.js ./
RUN npm run build



# Stage 2: Backend build
FROM python:3.13-slim

# Set up the working directory
WORKDIR /app

# Set the PYTHONPATH environment variable
ENV PYTHONPATH=/app/src

# Expose the Flask app port
EXPOSE 5000

# Use Gunicorn for a production-grade server
RUN pip install --upgrade pip && \
	pip install --no-cache-dir gunicorn==23.0.0

# Install system dependencies
RUN apt-get update -y && \
	apt-get install -y --no-install-recommends \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy everything in the src folder
COPY src/ src/
RUN rm -rf src/static/dist
COPY --from=frontend-builder frontend/src/static/dist src/static/dist
RUN rm -rf src/static/src

# Run the application with Gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "src.app:app"]

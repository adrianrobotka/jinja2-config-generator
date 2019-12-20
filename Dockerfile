FROM python:3.7-alpine

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME

#Copy requirements to install
COPY requirements.txt .

# Install production dependencies.
RUN pip install --no-cache-dir -r requirements.txt

COPY . ./
CMD ["python3", "generator.py"]


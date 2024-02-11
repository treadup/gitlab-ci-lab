FROM python:3.6-alpine as dependencies

# Set all docker commands to use /app as the working directory
WORKDIR /app

# Install python dependencies
COPY requirements.txt /app
RUN pip3 install -r requirements.txt

FROM dependencies

# By default Flask listens on port 5000
EXPOSE 5000

# Run the application using Gunicorn
COPY app.py /app
CMD ["gunicorn", "-b=0.0.0.0:8000", "app:app"]

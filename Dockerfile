# Using an official Python runtime as a parent image
FROM python:3.9


# Installing OpenGL and git libraries
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libegl1-mesa \
    libglew-dev \
    libglfw3 \
    libglu1-mesa \
    libgl1-mesa-dri \
    mesa-utils \
    libosmesa6-dev \
    libglu1-mesa-dev \
    freeglut3-dev \
    git


# Setting up the working directory inside the container
WORKDIR /code

# Copying the dependencies file to the working directory
COPY ./requirements.txt /code/requirements.txt

# Installing all the needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copying all the files from app directory to the working directory
COPY ./app /code/app
COPY ./mobile_sam.pt ./mobile_sam.pt

# Exposeing the port 8000 for FastAPI
EXPOSE 8000

# Command that need to run the FastAPI application
CMD ["fastapi", "run", "app/main.py", "--port", "8000"]

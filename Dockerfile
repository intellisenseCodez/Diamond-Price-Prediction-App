# This sets up the container with Python:3.10 Installed
FROM python:3.10-slim

# Copy the current directory contents into the container at /usr/src/app
COPY . /usr/src/app

# Set the working directory in the container
WORKDIR /usr/src/app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# This tells Docker to listen to port 80 at runtime
EXPOSE 80

# This command creates a .stremlit directory in the home directory 
RUN mkdir ~/.streamlit

# copy the streamlit credentials into .streamlit directory
RUN cp config.toml ~/.streamlit/config.toml

# copy the streamlit credentials into .streamlit directory
RUN cp credentials.toml ~/.streamlit/credentials.toml

# This set up the default command for the container to run the app with streamlit
ENTRYPOINT [ "streamlit", "run" ]

# This command tells streamlit to run app.py scripts when the container starts
CMD [ "app.py" ]
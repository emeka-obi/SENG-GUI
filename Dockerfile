#Python is the base image
FROM python:3.7
WORKDIR /program

COPY . /program

# Defining the owner of the Image
LABEL author="Emeka Obi"
LABEL email="obiemeka262@gmail.com"


RUN pip install flask && pip3 install --no-cache-dir -r requirements.txt
EXPOSE 5000
RUN ["chmod", "+x", "docker.sh"]
ENTRYPOINT ["bash", "./docker.sh"]

# To access the container from your local use localhost:<portnumber>. For example localhost:5000 
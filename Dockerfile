FROM python:3.14.0b2-slim

#Create a dictionary inside a container
WORKDIR /example

# From my computer copy this image to the container
COPY  calculator.py /example/

# command to used to run that python code within the caintainer
CMD ["python" , "calculator.py" ]



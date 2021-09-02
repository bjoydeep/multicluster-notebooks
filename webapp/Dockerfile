FROM python:3.7

RUN pip install virtualenv
ENV VIRTUAL_ENV=/venv
RUN virtualenv venv -p python3
ENV PATH="VIRTUAL_ENV/bin:$PATH"

RUN mkdir /.streamlit


COPY . /app
WORKDIR /app

# Install dependencies
RUN pip install -r requirements.txt

RUN chgrp -R 0 /app && chmod -R g=u /app
RUN chgrp -R 0 /.streamlit && chmod -R g=u /.streamlit


# Expose port 
EXPOSE 8501

# cmd to launch app when container is run
CMD streamlit run app.py
#########

# FROM registry.access.redhat.com/ubi8/ubi-minimal:8.4
# RUN microdnf install make
# EXPOSE 8501
# WORKDIR /app

# RUN microdnf install python3.8 python3-pip

# COPY requirements.txt ./requirements.txt
# RUN pip3.8 install -r requirements.txt
# COPY . /app

# CMD streamlit run app.py


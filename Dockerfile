FROM python:3

ENV PYTHONUNBUFFRED=1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

RUN adduser myuser

USER myuser

WORKDIR /project

COPY --chown=myuser:myuser requirements.txt requirements.txt

RUN pip install --user -r requirements.txt
RUN pip install --user mysqlclient
RUN pip install --user pymysql

ENV PATH="/project/.local/bin:${PATH}"

COPY --chown=myuser:myuser . .

RUN echo $(ls -al ../)

RUN echo $(ls -al)

# ADD ./ .

# RUN pip install -r requirements.txt

# RUN pip install mysqlclient

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
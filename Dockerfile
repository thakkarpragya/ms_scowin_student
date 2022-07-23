FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app/
# RUN git clone https://github.com/thakkarpragya/ms_scowin_student.git
COPY . /usr/src/app/
RUN ls -lah
# RUN apk update && apk add py-pip
RUN pwd
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt
EXPOSE 8084
RUN python student/producer.py
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8084" ]
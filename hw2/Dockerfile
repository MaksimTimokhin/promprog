FROM python:3-onbuild
EXPOSE 8000
CMD ["python", "mysite/manage.py", "makemigrations", "questions"]
CMD ["python", "mysite/manage.py", "migrate"]
CMD ["python", "mysite/manage.py", "runserver", "0.0.0.0:8000"]

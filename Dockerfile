# 
FROM python:3.9

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Install pytesseract and required libraries
RUN pip install pytesseract

# 
COPY ./app /code/app

# Install pytesseract and any other dependencies
RUN apt-get update && apt-get install -y tesseract-ocr
RUN pip install pytesseract

# 
CMD ["uvicorn", "app.main:app", "--reload"] 
#, "--host", "0.0.0.0", "--port", "8000"]

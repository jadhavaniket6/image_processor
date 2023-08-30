FastAPI OCR Image Scanning App

This is a FastAPI application that utilizes Optical Character Recognition (OCR) to extract text from images. The extracted text is then stored in a PostgreSQL database hosted on AWS RDS.

Prerequisites
Python 3.6+
Tesseract OCR
PostgreSQL
AWS RDS PostgreSQL database
AWS credentials configured

Installation
Clone the repository:
git clone https://github.com/jadhavaniket6/image_processor.git

cd image_processor

Usage:
Build a docker image from the Dockerfile:
docker build -t image-scanner .

Create a docker container that starts the application:
docker run --rm -p 8002:8001 image-scanner

Access the FastAPI Swagger documentation:

Open your browser and navigate to http://localhost:8002/docs to interact with the API and test the OCR functionality.

Upload an image and scan text:

Use the API endpoint to upload an image. The application will perform OCR using Tesseract and store the extracted text in the AWS RDS PostgreSQL database.

Contributing
Contributions are welcome! Feel free to open issues and pull requests.

Acknowledgements:
This project was inspired by the need to automate text extraction from images and store them in a cloud-based database.


Feel free to expand or modify the README to suit your project's unique requirements and provide clear instructions for others to understand how to set up and use your FastAPI OCR Image Scanning App.

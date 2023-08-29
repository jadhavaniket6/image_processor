from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from PIL import Image
import pytesseract
import re
from datetime import datetime
import psycopg2
import datetime

# Database connection parameters
dbname = "my_db"
user = "aniket"
password = "Aniket!07"
host = "localhost"
port = "5432"  # Default PostgreSQL port is 5432


app = FastAPI()


def remove_extra_whitespace(text):
    return " ".join(text.split())

def remove_non_alphanumeric(text):
    return re.sub(r'[^a-zA-Z0-9\s]', '', text)

def fix_capitalization(text):
    return text.lower()

def fix_ocr_errors(text):
    return text.replace('1', 'l').replace('3', 'e')

# def expand_abbreviations(text):
#     abbreviations = {
#         "USA": "United States of America"
#     }
#     for abbreviation, expansion in abbreviations.items():
#         text = text.replace(abbreviation, expansion)
#     return text

def remove_unwanted_line_breaks(text):
    return text.replace('\n', ' ').strip()

def format_numbers_dates(text):
    text = re.sub(r'\$\s*(\d{1,3}(?:,\d{3})*(?:\.\d{2})?)', r'$\1', text)
    text = re.sub(r'(\d{4})-(\d{2})-(\d{2})', lambda m: datetime.strptime(m.group(), "%Y-%m-%d").strftime("%B %d, %Y"), text)
    return text

def remove_unwanted_characters(text):
    return text.replace("[REMOVE ME]", "")

def clean_text(text):
    cleaned_text = remove_extra_whitespace(text)
    cleaned_text = remove_non_alphanumeric(cleaned_text)
    cleaned_text = fix_capitalization(cleaned_text)
    cleaned_text = fix_ocr_errors(cleaned_text)
    cleaned_text = expand_abbreviations(cleaned_text)
    cleaned_text = remove_unwanted_line_breaks(cleaned_text)
    cleaned_text = format_numbers_dates(cleaned_text)
    cleaned_text = remove_unwanted_characters(cleaned_text)
    return cleaned_text

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/extract-text/")
async def extract_text(file: UploadFile = File(...)):
    try:
        # Read uploaded image using PIL
        img = Image.open(file.file)

        # Perform OCR using Tesseract
        extracted_text = pytesseract.image_to_string(img)

        # Clean the text
        cleaned_text = clean_text(extracted_text)

        # Get the current timestamp
        current_timestamp = datetime.datetime.now()

        formatted_timestamp = current_timestamp.strftime("%Y-%m-%d %H:%M:%S")

        output = [(str(formatted_timestamp), str(cleaned_text))]
        # Establish a connection to the PostgreSQL database
        conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
        # Create a cursor
        cur = conn.cursor()

        # Iterate through the output and insert into the table
        # for row in output:
        for row in output:
            cur.execute("INSERT INTO image_data (time_stamp, text_data) VALUES (%s, %s)", row)

        # Commit the changes and close the cursor and connection
        conn.commit()
        cur.close()
        conn.close()

        return {"extracted text is uploaded to the database"}, 200
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
    






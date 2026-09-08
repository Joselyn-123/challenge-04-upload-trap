# Challenge 04 - The Upload Trap

## Category
Web

## Difficulty
Intermediate

## Points
100

## Main Concept
File Upload Vulnerability

## Description
The website allows users to upload files.
The developer forgot to properly validate the uploaded content.

Can you investigate the upload functionality and find the flag?

## Learning Objectives
- Understand how file uploads work
- Learn why file validation matters
- Understand the difference between file extension and actual content
- Identify insecure upload handling

## Run Locally

pip install -r requirements.txt

python app.py

Open:
http://127.0.0.1:5000

## Intended Challenge Path

1. Open the upload page.
2. Upload a normal file.
3. Observe how the application handles the uploaded file.
4. Investigate the upload behavior.
5. Discover the intended validation weakness.
6. Access the flag.

## Deployment

This application can be deployed using Docker.
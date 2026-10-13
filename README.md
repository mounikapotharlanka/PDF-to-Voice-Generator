
# PDF to Voice Generator

## 1. Project Overview
PDF to Voice Generator is a Python-based desktop application that converts readable text from PDF documents into spoken audio. The generated speech is saved as an MP3 file, allowing users to listen to document content instead of reading it.

## 2. Objectives
- Extract readable text from PDF documents.
- Convert extracted text into speech.
- Allow users to select a speech language.
- Save generated audio as an MP3 file.
- Provide a simple graphical user interface.

## 3. Features
- Select a PDF document from the computer.
- Extract text using the pypdf library.
- Select a supported speech language.
- Convert text into speech using gTTS.
- Save the audio output as an MP3 file.
- Display conversion status and error messages.

## 4. Technologies Used
- Python
- Tkinter for the graphical user interface
- pypdf for PDF text extraction
- gTTS for text-to-speech conversion
- Visual Studio Code for development

## 5. Project Workflow
1. Open the application.
2. Select a PDF document.
3. Extract readable text from the PDF.
4. Select the speech language.
5. Convert the text into speech.
6. Save the generated MP3 file.
7. Play the audio file.

## 6. Installation
Install Python 3 and open a terminal in the project folder.

Install the required libraries:

```bash
pip install -r requirements.txt
```

## 7. How to Run
Run the following command in the project folder:

```bash
python pdf_to_voice.py
```

Select a PDF, choose a language, click the conversion button, and select where to save the MP3 file.

## 8. Requirements
- Python 3
- Internet connection for gTTS speech generation
- A PDF containing selectable, readable text
- Required Python libraries listed in requirements.txt

## 9. Limitations
- Scanned PDFs without extractable text are not supported by the current version.
- Speech generation requires an internet connection.
- Conversion time depends on the document length and internet connection.

## 10. Future Enhancements
- Add OCR support for scanned PDFs.
- Add audio playback controls inside the application.
- Improve progress reporting for large documents.
- Add more language options.

## 11. Expected Output
The application generates an MP3 audio file containing spoken text extracted from the selected PDF.

## 12. Author
Mounika Potharlanka

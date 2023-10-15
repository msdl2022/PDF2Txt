
# PDF to Text Extraction

This Python script allows you to extract text content from a PDF file and save it to a text file. It uses the PyPDF2 library for PDF processing.

## Prerequisites

- Python 3.x installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

## Installation

You need to have the `PyPDF2` library installed. If you haven't already installed it, you can do so using `pip`:

```bash
pip install PyPDF2
```

## Usage

1. Place the PDF file you want to extract text from in the same directory as the Python script.

2. Open a terminal and navigate to the directory containing the script and the PDF file.

3. Run the Python script by executing the following command, replacing `'input.pdf'` with the name of your PDF file:

```bash
python pdf_to_text.py
```

4. The extracted text will be saved to a file called `'output.txt'` in the same directory.

## Customization

- If you want to change the input PDF file, edit the `'input.pdf'` filename in the Python script to the desired filename.
- If you want to change the output text file, edit the `'output.txt'` filename in the Python script to the desired filename.

## Example

Suppose you have a PDF file named `'sample.pdf'` that you want to convert to text. You can run the script as follows:

```bash
python pdf_to_text.py
```

The extracted text will be saved to a file called `'output.txt'`.


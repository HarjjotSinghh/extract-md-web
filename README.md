# Docling Documentation Extractor

A simple Python tool that uses [Docling](https://github.com/DS4SD/docling) to extract and convert documentation from web URLs into markdown format.

## Overview

This project demonstrates how to use Docling's document conversion capabilities to extract content from web documentation and save it as structured markdown files. It's particularly useful for archiving documentation or creating local copies of online resources.

## Features

- Extract content from web URLs using Docling
- Convert extracted content to markdown format
- Save individual files for each URL
- Generate a combined markdown file with all extracted content
- Preview extracted content in the terminal

## Requirements

- Python 3.6+
- Docling library

## Installation

1. Clone or download this repository
2. Install the required dependencies:
```bash
pip install docling
```

## Usage

1. Edit the urls list in the main() function of extract_docling_docs.py to include the URLs you want to extract

2. Run the script:

```bash
python extract_docling_docs.py
```

The script will:

- Extract content from each specified URL
- Save individual markdown files in the extracted_docs/ directory
- Create a combined markdown file with all extracted content
- Display content previews in the terminal

## Output
The script generates the following files in the extracted_docs/ directory:

- Individual markdown files for each URL (named based on the URL)
- combined_docling_docs.md - A single file containing all extracted content

## Example
By default, the script extracts content from:

- https://pkg.go.dev/github.com/pdfcpu/pdfcpu/pkg/api

You can modify the urls list in the main() function to extract from different sources.

## Project Structure
```
docling-docs-extract/
├── extract_docling_docs.py    # Main extraction script
├── extracted_docs/             # Output directory
│   ├── combined_docling_docs.md
│   └── [individual_url_files].md
└── README.md   
```
## Licsense
This project is provided as-is for educational and utility purposes.

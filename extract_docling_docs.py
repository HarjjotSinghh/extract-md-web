#!/usr/bin/env python3
"""
Docling Documentation Extractor
This script uses Docling to extract content from the Docling project documentation URLs.
"""

from docling.document_converter import DocumentConverter
import os
from pathlib import Path

def extract_url_content(url, output_dir="extracted_docs"):
    """
    Extract content from a URL using Docling and save to markdown file.
    
    Args:
        url (str): The URL to extract content from
        output_dir (str): Directory to save the extracted content
    
    Returns:
        str: The extracted markdown content
    """
    print(f"Extracting content from: {url}")
    
    try:
        # Initialize the DocumentConverter
        converter = DocumentConverter()
        
        # Convert the document
        result = converter.convert(url)
        doc = result.document
        
        # Export to markdown
        markdown_content = doc.export_to_markdown()
        
        # Create output directory if it doesn't exist
        Path(output_dir).mkdir(exist_ok=True)
        
        # Create a filename from the URL
        filename = url.replace("https://", "").replace("http://", "").replace("/", "_") + ".md"
        filepath = Path(output_dir) / filename
        
        # Save the content to file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"# Extracted from: {url}\n\n")
            f.write(markdown_content)
        
        print(f"Content saved to: {filepath}")
        return markdown_content
        
    except Exception as e:
        print(f"Error extracting content from {url}: {str(e)}")
        return None

def main():
    """Main function to extract content from Docling documentation URLs."""
    
    # URLs to extract content from
    urls = [
        "https://pkg.go.dev/github.com/pdfcpu/pdfcpu/pkg/api"
    ]
    
    print("Starting Docling Documentation Extraction")
    print("=" * 50)
    
    # Create output directory
    output_dir = "extracted_docs"
    
    extracted_contents = []
    
    for url in urls:
        content = extract_url_content(url, output_dir)
        if content:
            extracted_contents.append({
                'url': url,
                'content': content
            })
    
    print("\n" + "=" * 50)
    print("Extraction Summary:")
    print(f"Successfully extracted content from {len(extracted_contents)} URLs")
    
    # Create a combined markdown file
    combined_file = Path(output_dir) / "combined_docling_docs.md"
    with open(combined_file, 'w', encoding='utf-8') as f:
        f.write("# Docling Documentation - Combined Extract\n\n")
        f.write("This file contains the combined extracted content from Docling documentation.\n\n")
        
        for item in extracted_contents:
            f.write(f"## Content from: {item['url']}\n\n")
            f.write(item['content'])
            f.write("\n\n" + "-" * 80 + "\n\n")
    
    print(f"Combined content saved to: {combined_file}")
    
    # Display first 500 characters of each extracted content as preview
    print("\nContent Previews:")
    for item in extracted_contents:
        print(f"\nURL: {item['url']}")
        print("-" * 40)
        preview = item['content'][:500] + "..." if len(item['content']) > 500 else item['content']
        print(preview)

if __name__ == "__main__":
    main()
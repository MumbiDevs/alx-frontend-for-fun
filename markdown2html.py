#!/usr/bin/python3
"""
This is a script to convert a Markdown file to HTML.

Usage:
    ./markdown2html.py [input_file] [output_file]

Arguments:
    input_file: the name of the Markdown file to be converted
    output_file: the name of the output HTML file

Example:
    ./markdown2html.py README.md README.html
"""

import argparse
import pathlib
import re
import sys

def convert_md_to_html(input_file, output_file):
    '''
    Converts markdown file to HTML file
    '''
    with open(input_file, encoding='utf-8') as f:
        md_content = f.readlines()

    html_content = ['<html>\n<head>\n<title>Converted Markdown</title>\n</head>\n<body>\n']

    for line in md_content:
        # Check for headings
        match = re.match(r'(#){1,6} (.*)', line)
        if match:
            h_level = len(match.group(1))
            h_content = match.group(2)
            html_content.append(f'<h{h_level}>{h_content}</h{h_level}>\n')

        # Check for unordered lists
        elif line.startswith('- '):
            html_content.append(f'<li>{line[2:].strip()}</li>\n')

        # Convert empty lines to <p> tags
        elif line.strip() == "":
            html_content.append('<p></p>\n')

        # Handle regular paragraphs
        else:
            html_content.append(f'<p>{line.strip()}</p>\n')

    html_content.append('</body>\n</html>')

    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(html_content)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert markdown to HTML')
    parser.add_argument('input_file', help='path to input markdown file')
    parser.add_argument('output_file', help='path to output HTML file')
    args = parser.parse_args()

    input_path = pathlib.Path(args.input_file)
    if not input_path.is_file():
        print(f'Missing {input_path}', file=sys.stderr)
        sys.exit(1)

    convert_md_to_html(args.input_file, args.output_file)

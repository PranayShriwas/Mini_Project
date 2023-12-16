from django.shortcuts import render
from bs4 import BeautifulSoup
import html2text

def html_to_python(html_data):
    soup = BeautifulSoup(html_data, 'html.parser')
    
    # Extract table data or any other relevant information from the HTML
    table_data = soup.find('table')
    
    # Convert the HTML table to plain text using html2text
    table_text = html2text.html2text(str(table_data))
    
    # Generate Python code based on the extracted data
    python_code = f"""
# This is auto-generated Python code based on the HTML table data

table_data = {repr(table_text)}

# Your further processing or code generation logic here
"""

    return python_code

# Example usage
html_data = """
<table>
  <tr>
    <th>Header 1</th>
    <th>Header 2</th>
  </tr>
  <tr>
    <td>Data 1,1</td>
    <td>Data 1,2</td>
  </tr>
  <tr>
    <td>Data 2,1</td>
    <td>Data 2,2</td>
  </tr>
</table>
"""
python_code = html_to_python(html_data)
# Save the generated Python code to a file
with open('generated_code.py', 'w') as file:
    file.write(python_code)

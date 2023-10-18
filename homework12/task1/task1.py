class TxtToHtmlAdapter:
    def __init__(self, text_data):
        self.text_data = text_data

    def convert_to_html(self):
        lines = self.text_data.split('\n')
        html = '<table>\n'
        for line in lines:
            fields = line.split(',')
            html += '  <tr>\n'
            for field in fields:
                name, value = field.split(':')
                html += f'    <{name}>{value}</{name}>\n'
            html += '  </tr>\n'
        html += '</table>'
        return html

# Sample input data
txt_data = """name:John,last_name:Malkovich,age:28,salary:1000"""

# Create the adapter and convert the text to HTML
adapter = TxtToHtmlAdapter(txt_data)
html_data = adapter.convert_to_html()

# Print the result
print(html_data)

from string import Template
from get import request_get

response = request_get("https://aves.ninjas.cl/api/birds")[:10]

img_template = Template('<img src="$url">')

nombre_template = Template('<p>$spanish</p>')
name_template = Template('<p>$english</p>')

html_template = Template('''<!DOCTYPE html>
                            <html>
                            <head>
                            <title>Aves de Chile</title>
                            </head>
                            <body>
                            <h1>Aves de Chile</h1>
                            $body
                            </body>
                            </html>
                        ''')
contenido = ""

for elemento in response:
    url = elemento["images"]["main"]
    nombre = elemento["name"]["spanish"] 
    nombre_eng = elemento["name"]["english"] 
    contenido += img_template.substitute(url = url)
    contenido += nombre_template.substitute(spanish = nombre) 
    contenido += name_template.substitute(english = nombre_eng)

html = html_template.substitute(body = contenido)

with open("output.html", "w") as f:
    f.write(html)
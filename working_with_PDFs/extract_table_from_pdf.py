import tabula

table = tabula.read_pdf('weather.pdf', pages=1)
table[0].to_csv('table.csv', index=None)
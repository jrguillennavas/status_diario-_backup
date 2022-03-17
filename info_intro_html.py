
def info_intro_html(databack):
    data_info_html = ''

    for linea in databack:
        if linea['folder']=='Mensuales' or linea['folder']=='retention':
            continue
        data_info_html += f"<tr id=\"tr\"><td>{linea['su']}</td><td>{linea['folder']}</td><td>{linea['name']}</td><td>{linea['size']}</td><td>{linea['date']}</td><td>{'✅' if linea['backup'] else '❌'}</td></tr>\n"

    css = '''
        body{margin: 0; padding: 0; box-sizing: border-box;}
        td{text-align: center; font-size: 10.9px;}
        th{text-align: center; font-size: 14px;}
    '''

    html_template = f'''
    <html>
    <head>
    <title>Tutsplus Email Newsletter</title>
    <style type="text/css">
        {css}
    </style>
    </head>
    <body>
        <table width="100%" cellpadding="5" cellspacing="0" bgcolor="e4e4e4" align="center">
            <thead>
                <tr>
                    <th>SU</th>
                    <th>Folder</th>
                    <th>Name</th>
                    <th>Size</th>
                    <th>Date</th>
                </tr>
            </thead>
            <tbody>
                {data_info_html}
            </tbody>
        </table>
    </body>
    </html>
    '''
    return html_template
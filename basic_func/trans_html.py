def create_html_table(frame):
    table_frame_result = ''
    for x in range(len(frame)):
        table_frame = ''
        for y in range(len(frame.columns)):
            table_frame = table_frame +'<td>' + str(frame.iloc[x, y]) + '</td>'
        table_frame_result = table_frame_result + '<tr>' + table_frame +'</tr>'
    return table_frame_result
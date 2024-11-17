FORMATTER_TEXT = "%(asctime)s | %(threadName)s | %(levelname)s | %(module)s | %(funcName)s | %(message)s"
FORMATTER_TEXT_HTML = """<tr class=%(levelname)s><td>%(asctime)s</td><td>%(threadName)s</td><td>%(levelname)s</td>
                       <td>%(module)s</td><td>%(funcName)s</td><td>%(message)s</td></tr>"""
HTML_PRETEXT = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        table {
            width: auto; /* Let the table take minimum width based on content */
            table-layout: auto; /* Default value, let content dictate column widths */
            border-collapse: collapse;
        }
        th, td {
            border: 1px solid #555;
            padding: 4px;
            text-align: left;
        }
        th {
            background-color: #f4f4f4;
        }
       /* CSS Classes for coloring rows */
        .DEBUG {
            background-color: #d1e7dd; /* Light green for debug */
        }
        .INFO {
            background-color: #cff4fc; /* Light blue for info */
        }
        .WARNING {
            background-color: #fff3cd; /* Light yellow for warning */
        }
        .ERROR {
            background-color: #f8d7da; /* Light red for error */
        }
    </style>
</head>
<body>
    <table>
        <thead>
            <tr>
                <th width=180>Timestamp</th>
                <th>Thread</th>
                <th>Level</th>
                <th>Module</th>
                <th>Function</th>
                <th>Message</th>
            </tr>
        </thead>
"""

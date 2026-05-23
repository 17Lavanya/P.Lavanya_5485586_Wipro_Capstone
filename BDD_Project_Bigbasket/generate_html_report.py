import json

with open("reports/report.json", "r", encoding="utf-8") as file:
    data = json.load(file)

html = """
<html>
<head>
    <title>BigBasket Automation Report</title>

    <style>

        body{
            font-family: Arial;
            background-color: #f4f4f4;
            padding: 20px;
        }

        h1{
            text-align: center;
            color: #2c3e50;
        }

        .feature{
            background: white;
            padding: 20px;
            margin-bottom: 20px;
            border-radius: 10px;
            box-shadow: 0px 0px 5px gray;
        }

        .scenario{
            margin-top: 15px;
            padding: 15px;
            border-left: 5px solid #3498db;
            background-color: #fafafa;
        }

        table{
            width: 100%;
            border-collapse: collapse;
            margin-top: 10px;
        }

        th, td{
            border: 1px solid #ccc;
            padding: 10px;
            text-align: left;
        }

        th{
            background-color: #3498db;
            color: white;
        }

        .passed{
            color: green;
            font-weight: bold;
        }

        .failed{
            color: red;
            font-weight: bold;
        }

    </style>

</head>

<body>

<h1>BigBasket BDD Automation Report</h1>

"""

for feature in data:

    html += f"""
    <div class='feature'>
        <h2>Feature: {feature['name']}</h2>
    """

    for scenario in feature["elements"]:

        html += f"""
        <div class='scenario'>
            <h3>Scenario: {scenario['name']}</h3>

            <table>
                <tr>
                    <th>Step</th>
                    <th>Status</th>
                </tr>
        """

        for step in scenario["steps"]:

            status = step["result"]["status"]

            css = "passed" if status == "passed" else "failed"

            html += f"""
            <tr>
                <td>{step['keyword']} {step['name']}</td>
                <td class='{css}'>{status.upper()}</td>
            </tr>
            """

        html += """
            </table>
        </div>
        """

    html += "</div>"

html += """
</body>
</html>
"""

with open("reports/report.html", "w", encoding="utf-8") as file:
    file.write(html)

print("HTML Report Generated Successfully")
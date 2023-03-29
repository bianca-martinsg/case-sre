import json

success_count = 0
error_count = 0
data = []

for line in open('logs.txt'):
    if 'statusCode' in line:
        statusCode = line.split("'statusCode': '")[1].split("',")[0].strip()
        if int(statusCode) < 400:
            success_count += 1
        else:
            error_count += 1

    if 'path' in line:
        path = line.split("'path': '")[1].split("',")[0].strip()
        data.append({"path": path, "errorCount": error_count, "successCount": success_count})

with open('output.json', 'w') as f:
    json.dump(data, f, indent=4)











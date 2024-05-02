import json

with open('pritomnost.json', encoding='utf-8') as inputFile:
    data = json.load(inputFile)

sourceTable = []


for user in data["data"]["userPage"]:
    row = {}
    row["user.id"] = user["id"]
    row["user.name"] = user["name"]
    row["user.surname"] = user["surname"]
    row["user.email"] = user["email"]
    for presence in user["presences"]:
        event = presence["event"]

        row["event.id"] = event["id"]
        row["event.name"] = event["name"]
        row["event.startdate"] = event["startdate"]
        row["event.enddate"] = event["enddate"]

        row["presenceType.id"] = presence["presenceType"]["id"]
        row["presenceType.name"] = presence["presenceType"]["name"]

        row["eventType.id"] = event["eventType"]["id"]
        row["eventType.name"] = event["eventType"]["name"]

    sourceTable.append(row)

        
with open('output.json',"w", encoding='utf-8') as outputFile:
    json.dump(sourceTable, outputFile, ensure_ascii=False, indent=4)
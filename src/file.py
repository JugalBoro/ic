import json

def getCompleteTemplate(schemas, temp, dir, version, template):
    template = template.replace(".json", "")
    f = open(temp + "/" + dir + "/" + version + "/" + template + ".json", "r")
    schema = json.load(f)
    f.close()

    schemas.append(schema)

    for k, v in schema["properties"].items():
        if isinstance(v, dict):
            if "$ref" in v:
                path = v["$ref"].split("/")
                print("pfad:",path)
                found = False

                for i in schemas:
                    if i["$id"] == v["$ref"]:
                        found = True
                        break
                if not found:
                    getCompleteTemplate(schemas, temp, path[0], path[1], path[2])

            if "type" in v and v["type"] == "array":
                if "items" in v and "$ref" in v["items"]:
                    path = v["items"]["$ref"].split("/")
                    print("pfad:",path)
                    found = False
                    for i in schemas:
                        if i["$id"] == v["items"]["$ref"]:
                            found = True
                            break
                    if not found:
                        getCompleteTemplate(schemas, temp, path[0], path[1], path[2])


    return schema

from flask import Flask
import json

# import pymongo
# from bson import json_util
from jsonschema import validate
import jsonschema

# from bson.objectid import ObjectId
import os
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from file import getCompleteTemplate

# Flask app configuration
app = Flask(__name__)
auth = HTTPBasicAuth()

# mongodb_url = os.environ.get('MONGODB_URL')
usernameOrig = os.environ.get("USERNAME")
passwordOrig = os.environ.get("PASSWORD")
ressource_folder = os.environ.get("RESOURCE_FOLDER")

# client = pymongo.MongoClient(mongodb_url)
# mydb = client["ics-database"]
# mycol = mydb["templates"]

# with open('../meta-schema.json') as f:
#     meta_schema = json.load(f)

users = {usernameOrig: generate_password_hash(passwordOrig)}


@auth.verify_password
def verify_password(username, password):
    if username and password:
        if username in users and check_password_hash(users.get(username), password):
            return True
        else:
            return False
    else:
        return False


# def validate_json(json_data):
#     """REF: https://json-schema.org/ """
#     # Describe what kind of json you expect.
#     for item in json_data:
#         try:
#             validate(instance=item, schema=meta_schema)
#         except jsonschema.exceptions.ValidationError as err:
#             print(err)
#             # err = "Given JSON data is InValid"
#             return False, err

#     message = "Given JSON data is Valid"
#     return True, message


# @app.route("/delete", methods=["GET"])
# @auth.login_required
# def deleteTemplates():
#     mycol.delete_many({})

#     return "Deleted all records, use import endpoint to reload"


# @app.route("/import", methods=["GET"])
# @auth.login_required
# def importTemplates():
#     with open('../resources/cutter.json') as f:
#         cutter = json.load(f)

#     with open('../resources/filter.json') as g:
#         filter = json.load(g)

#     with open('../resources/filter_catridge.json') as h:
#         filter_catridge = json.load(h)

#     with open('../resources/workpiece.json') as i:
#         workpiece = json.load(i)

#     insertList = [cutter, filter, filter_catridge, workpiece]

#     is_valid, msg = validate_json(insertList)

#     if is_valid:
#         mycol.insert_many(insertList)
#         return "Valid JSON Data"
#     else:
#         return "Invalid JSON Data"


@app.route("/asset_templates", methods=["GET"])
# @auth.login_required
def getAssetTemplates():
    res = []

    for subdirs in os.listdir(ressource_folder):
        if subdirs == "base-objects":
            continue
        for version in os.listdir(ressource_folder + "/" + subdirs):
            f = open(
                ressource_folder + "/"
                + subdirs
                + "/"
                + version
                + "/"
                + subdirs
                + ".json",
                "r",
            )
            schema = json.load(f)
            print(schema["title"])
            res.append(
                {
                    "id": schema["$id"],
                    "title": schema["title"],
                    "description": schema["description"],
                    "group": schema["group"],
                    "metadata": schema["metadata"],
                }
            )

    response = app.make_response((json.dumps(res), 200))

    return response


@app.route(
    "/asset_templates/<string:dir>/<string:version>/<string:template>",
    methods=["GET"],
)
# @auth.login_required
def getAssetTemplatesById(dir, version, template):
    f = open( ressource_folder + "/" + dir + "/" + version + "/" + template + ".json", "r")
    schema = json.load(f)

    response = app.make_response((json.dumps(schema), 200))
    return response


@app.route(
    "/asset_templates_deep/<string:dir>/<string:version>/<string:template>",
    methods=["GET"],
)
# @auth.login_required
def getAssetTemplatesByIdDeep(dir, version, template):
    schemas = []
    getCompleteTemplate(schemas, ressource_folder, dir, version, template)
    f = open( ressource_folder + "/" + dir + "/" + version + "/" + template + ".json", "r")

    response = app.make_response((json.dumps(schemas), 200))
    return response


if __name__ == "__main__":
    port = 8080
    if os.environ.get('ICSDB_PORT') is not None:
        port = int(os.environ.get('ICSDB_PORT'))
    app.run(debug="true", host="0.0.0.0", port=port)

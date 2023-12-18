# IndustryFusion Foundation (IFF) ICS service

The ICS service is a main part of IFRIC.org which serves standardized schema templates to any third party applications including "IFF - Fleet Manager" for the creation of assets/objects. The structure of the data follows JSON Schema in most parts but also includes custom parameters required for semantic modelling (E.g keys like "relationships" and "unit"). [https://json-schema.org/]

The templates define structures for industiral machines and components like cutters, air filters, power sources, sensors that deliver data in real time. These templates are not only limited to machines with real-time data servers but also assets like workpeices (Metal sheets and parts) used in different industrial processes, users, operators, manufactures, etc. All assets that can be a part of Industry 4.0 infrastructure will also be included.

There are several data sub-modules in each templates based on its type, mainly related to,
1. IFRIC Identification
2. Asset Identification
3. Measurements (Size)
4. Power Supply
5. Operating Conditions (Ambience)
6. Source Medium (Eg, Gasees) 
6. Relatime Datapoints
7. Semantic relations
8. Other standard static data (Security, Maintainance, etc)

The ICS templates are designed to accomadate ECLASS product master data for most of the static parameters [https://eclass.eu/en/eclass-standard/search-content/show?tx_eclasssearch_ecsearch%5Bdischarge%5D=0&tx_eclasssearch_ecsearch%5Blanguage%5D=1&tx_eclasssearch_ecsearch%5Bversion%5D=13.0&cHash=6fc7686eb9b7c16a23c7f8f5d588cd7d] which is popular service for standardized static product data across world. The other important data points such as realtime, IFRIC (for unique identification and certification) are provided by IFF.

## API Details

The service has three API endpoints/methods as describe below.

1. getAssetTemplates - To return the metadata of all available templates == Used to list the metadata for all templates.
2. getAssetTemplatesById - To return the data of one template based on given ID == Only return important details of one entire template.
3. getAssetTemplatesByIdDeep - To return deep details of one template based on given ID == Return all information of the template.

## Setup

The service uses Python Flask framework to implement the endpoints. Use linux machine for local development.

 - Install Python 3.8.12 in the linux machine [https://tecadmin.net/install-python-3-8-ubuntu/]

### Setup the virtual environment for installing requirements

From the root directory of this project run the below commands to install and activate venv. Second time, just use the activate command.

**To install**

`python3 -m venv .venv`


**To activate**

`source .venv/bin/activate`


**Install required modules**

`pip3 install -r requirements.txt`


**Run the project** (export environment varibales first as shown below)

`export ICSDB_PORT=5005`

The service is protected by basic auth. Export the username and password of your choice.

`export USERNAME=<any>`

`export PASSWORD=<any>`

The service must be pointed to the right folder of stored templates. This can be changed accordinlgy for testing.

`export RESOURCE_FOLDER=resources/templates`

Run the service.

`python src/main.py` 

or 

`python3 src/main.py`

The service will be available at localhost:5005. The clients must provide username and password in basic auth header while sending requests.


## Structure of folders

The templates are stored under resources/templates folder. Each type of template has its own folder (base objects are an exception and used in all templates). Each folder of the template has sub-folder for versioning. (Eg, v0.1).


## Endpoints

1. /asset_templates - Returns list of all templates (only base metadata)
2. /asset_templates/<string:dir>/<string:version>/<string:template>   - Returns shortened details of one template. (E.g., /asset_templates/filter/v0.1/filter)
3. /asset_templates_deep/<string:dir>/<string:version>/<string:template> - Returns all details of one template. (E.g /asset_templates/filter/v0.1/filter) 




from flask import Flask, make_response, request
from flask import make_response
from models.Project import Project
import conf
import json
from urllib.parse import unquote
import re

app = Flask(__name__)

@app.route('/archive', methods=['POST'])
def arhive(projectId=None):
    try:
        data = json.loads(request.data)

        output = re.search(f'{conf.rmUrlPattern}(.+)', data['url'])
        if output is not None:
            projectId = output.group(1)
            Project.setStatus(projectId, conf.rmArchiveId)

        return make_response('', 204)
    except Exception as error:
        print(error)
        return make_response('', 500)

@app.route('/unarchive', methods=['POST'])
def unarhive(projectId=None):
    try:
        data = json.loads(request.data)

        output = re.search(f'{conf.rmUrlPattern}(.+)', data['url'])
        if output is not None:
            projectId = output.group(1)
            Project.setStatus(projectId, conf.rmUnArchiveId)

        return make_response('', 204)
    except Exception as error:
        print(error)
        return make_response('', 500)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=8090)
from flask import Flask, make_response, request
from flask import make_response
from models.Project import Project
import conf

app = Flask(__name__)

@app.route('/archive/<projectId>', methods=['POST'])
def arhive(projectId=None):
    Project.setStatus(projectId, conf.rmArchiveId)
    return make_response('', 204)

@app.route('/unarchive/<projectId>', methods=['POST'])
def unarhive(projectId=None):
    Project.setStatus(projectId, conf.rmUnArchiveId)
    return make_response('', 204)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=8090)
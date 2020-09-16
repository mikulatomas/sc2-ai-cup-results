from flask import (
    current_app, Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify, send_file
)
import json
from glob import glob
import os

bp = Blueprint('api', __name__, url_prefix='/api')


@bp.route('/replays')
def api_replays():
    date = request.args.get('date')
    filename = request.args.get('filename')
    with open(os.path.join(current_app.config['RESULTS'], date, filename)) as file:
        return send_file(file, mimetype='application/octet-stream', attachment_filename=filename, as_attachment=True)


@bp.route('/results')
def api_results():
    # print(glob(os.path.join(current_app.config['RESULTS'], '*-*-*')))

    results = {}
    for path in glob(os.path.join(current_app.config['RESULTS'], '*')):
        date = os.path.basename(path)

        with open(os.path.join(path, 'Results.json')) as json_file:
            results[date] = json.load(json_file)

        for result in results[date]['Results']:
            map_name = result['Map'].replace('.SC2Map', '')

            replay_file = f"{result['Bot1']}v{result['Bot2']}-{map_name}.SC2Replay"

            # print(results[date]['Results'])
            results[date]['Results'][0]['Replay'] = url_for(
                '.api_replays', date=date, filename=replay_file, _external=True)

    return jsonify(results)

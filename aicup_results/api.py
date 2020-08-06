from flask import (
    current_app, Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
import json
from glob import glob
import os
import shutil
from zipfile import ZipFile
import subprocess

bp = Blueprint('api', __name__, url_prefix='/api')


# @bp.route('/')
# def api_index():
#     return jsonify({'a': current_app.config['BOT_DIR']})

# def generate_ladder_bots():
#     bots_dir = current_app.config['BOT_DIR']
#     print(bots_dir)

#     for zip_file in glob(os.path.join(bots_dir, '*.zip')):
#         bot_dir = zip_file.replace('.zip', '/')
#         print(bot_dir)

#         with ZipFile(zip_file, 'r') as zipObj:
#             if os.path.exists(bot_dir) and os.path.isdir(bot_dir):
#                 print("removing")
#                 shutil.rmtree(bot_dir)

#             zipObj.extractall(bots_dir)


@bp.route('/run')
def api_run():
    subprocess.Popen([current_app.config['LADDERBIN'],
                      "-e", current_app.config['SC2BIN']],
                     cwd=current_app.config['BOT_CONFIG'],
                     stdout=subprocess.PIPE,
                     stderr=subprocess.STDOUT)

    return jsonify({'Done': 'Running.'})


@bp.route('/results')
def api_results():
    try:
        with open(current_app.config['RESULTS']) as json_file:
            return jsonify(json.load(json_file))
    except (IOError, EOFError) as e:
        return jsonify({'Error': 'No results.'})

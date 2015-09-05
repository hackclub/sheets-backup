import os
import sys
import requests
import re
from contextlib import contextmanager
from flask import Flask, request
from sh import cd, git, soffice

GIT_REMOTE = os.environ['GIT_REMOTE']
GIT_AUTHOR = os.environ['GIT_AUTHOR']

app = Flask(__name__)
repo = None

def init():
    if os.path.exists('repo'):
        if not os.path.isdir('repo/.git'):
            sys.stderr.write('repo/ exists, but is not a git repo')
            sys.exit(1)
    else:
        git.clone(GIT_REMOTE, 'repo')

# From http://stackoverflow.com/a/24176022/263998
@contextmanager
def cd(newdir):
    prevdir = os.getcwd()
    os.chdir(os.path.expanduser(newdir))
    try:
        yield
    finally:
        os.chdir(prevdir)

def export_as_ods(access_token, spreadsheet_id):
    url = 'https://docs.google.com/feeds/download/spreadsheets/Export?key=' + spreadsheet_id + '&exportFormat=ods'
    headers = {
        'Authorization': 'Bearer ' + access_token
    }
    return requests.get(url, headers=headers).content

def convert_ods_to_fods(ods_path):
    ods_filename = os.path.basename(ods_path)
    dest_filename = re.sub('.ods$', '.fods', ods_filename)
    dest_dir = os.path.dirname(ods_path) or '.'

    soffice('--headless',
            '--convert-to', 'fods',
            '--outdir', dest_dir,
            ods_path)

    return os.path.join(dest_dir, dest_filename)

def write_bytes_to_file(filename, bytes):
    f = open(filename, 'wb')
    f.write(bytes)
    f.close()
    return filename

@app.route('/initiate_backup', methods=['POST'])
def backup():
    access_token = request.form['access_token']
    spreadsheet_id = request.form['spreadsheet_id']

    with cd('repo/'):
        ods = export_as_ods(access_token, spreadsheet_id)
        ods_path = write_bytes_to_file('clubs.ods', ods)
        fods_path = convert_ods_to_fods(ods_path)
        os.remove(ods_path)

        git.add(fods_path)
        git.commit('-m', 'Update spreadsheet.', '--author', GIT_AUTHOR)
        git.push()

    return 'Consider it done!'

init()

if __name__ == '__main__':
    app.run(debug=True)

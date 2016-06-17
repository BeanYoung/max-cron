#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import os
import subprocess
import time

import click
import yaml
import requests


__version__ = '0.0.1'


@click.command()
@click.argument('cmd', required=True, nargs=-1)
def main(cmd):
    config_file_path = '/etc/maxload.yml'
    uuid = ''
    if os.path.exists(config_file_path):
        with open(config_file_path, 'r') as f:
            try:
                config = yaml.load(''.join(f.readlines()))
            except yaml.parser.ParserError:
                config = None

            if config:
                uuid = config.get('uuid', '')

    cmd = ' '.join(cmd)

    cron_info = dict()
    cron_info['cmd'] = cmd
    cron_info['start_time'] = time.time()
    cron_info['exit_status'] = subprocess.call(cmd, shell=True)
    cron_info['end_time'] = time.time()
    cron_info['process_time'] = cron_info['end_time'] - cron_info['start_time']

    if uuid:
        try:
            requests.post(
                'https://maxload.io/api/crons_logs',
                params={'uuid': uuid},
                data=json.dumps(cron_info),
                headers={
                    'Content-Type': 'Application/json',
                    'User-Agent': 'MaxCron %s' % __version__},
                timeout=3
            )
        except requests.exceptions.RequestException as e:
            pass


if __name__ == '__main__':
    main()

#!/usr/bin/env bash

conda create -n export-json
conda activate export-json

pip install .

python3 export_to_json_hook/export_portfolio_to_json.py
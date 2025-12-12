#!/usr/bin/env bash

set -a
source .env
set +a
uv run python main.py

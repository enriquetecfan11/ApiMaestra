#!/bin/bash

python3 -m uvicorn main:app --reload --host 192.168.1.124 --port 8000

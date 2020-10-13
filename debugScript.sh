#!/usr/bin/env bash

cd ./ioslib
python m_to_dylib.py
cd ..
buildozer ios debug

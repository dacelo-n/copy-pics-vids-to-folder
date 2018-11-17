#!/bin/bash

find . -type f -name "*.mp4" -print0 | xargs -0 -I {} cp {} /your/folder/destination
find . -type f -name "*.mov" -print0 | xargs -0 -I {} cp {} /your/folder/destination
find . -type f -name "*.mwv" -print0 | xargs -0 -I {} cp {} /your/folder/destination
find . -type f -name "*.avi" -print0 | xargs -0 -I {} cp {} /your/folder/destination
find . -type f -name "*.flv" -print0 | xargs -0 -I {} cp {} /your/folder/destination
find . -type f -name "*.png" -print0 | xargs -0 -I {} cp {} /your/folder/destination
find . -type f -name "*.jpg" -print0 | xargs -0 -I {} cp {} /your/folder/destination
find . -type f -name "*.img" -print0 | xargs -0 -I {} cp {} /your/folder/destination

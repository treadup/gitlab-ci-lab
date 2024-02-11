#!/bin/sh
sha1sum requirements.txt | cut -d" " -f1

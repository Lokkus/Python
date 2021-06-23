#!/usr/bin/env bash

awk 'BEGIN {for (i=1; i<5; i+=.5) print i}' /dev/null


#!/bin/bash
set -e
service mysql start
mysql < /mysql/database.sql
service mysql stop
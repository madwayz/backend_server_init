#!/bin/bash

git pull

composers_args=""
for composer in $(find . -name '*.yml' -execdir basename {} ';')
do
	echo $composer
	composers_args+=" -f "$composer
done
docker-compose $composers_args up --build -d --remove-orphans

#!/bin/bash

for composer in $(find . -name 'docker-compose.*.yml' -execdir basename {} ';')
do
	docker-compose -f $composer down --remove-orphans --rmi all
	docker-compose -f $composer rm --stop --force
done
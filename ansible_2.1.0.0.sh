#!/bin/bash

pip install -U ansible==2.1.0.0
time ansible-playbook -i inventory/local playbooks/test.yml -e hosts=localhost -c local -vvvv

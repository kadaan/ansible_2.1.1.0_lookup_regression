#!/bin/bash

pip install -U ansible==2.1.1.0
time ansible-playbook -i inventory/local playbooks/test.yml -c local -vvvv

#!/bin/bash

aws ec2 run-instances --launch-template file://lt.json

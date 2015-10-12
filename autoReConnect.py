#!/usr/bin/env python
#coding=utf-8

import os
import commands
import time
import re

ping_command = "ping -c 2 www.baidu.com"
run_pst, ping_result = commands.getstatusoutput(ping_command)

ping_line = ping_result.split('\n')

if len(ping_line[1:-4])>0:
	print "nothing to do"
else:
	run_pst, connect_status = commands.getstatusoutput("bash ~/authReConnect/auth.sh")
	print connect_status

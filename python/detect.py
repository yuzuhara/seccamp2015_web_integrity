#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from slacker import Slacker
from selenium import webdriver

USERNAME = "MYNAME_BOT"

def slack_message_test(username=USERNAME):
  with open("../credentials/slack_api_key", "r") as f:
    api_key = f.read()
    slack = Slacker(api_key)
    text = "This is test!"
    # Send a message to #general channel
    slack.chat.post_message(channel='#test', username=username, text=text)

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print "Usage: "+sys.argv[0]+" TARGET_URL"
    exit()
    
  slack_message_test()
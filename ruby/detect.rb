#!/usr/bin/env ruby
require "slack"

USERNAME = 'MYNAME_BOT'

def slack_message_test(username=USERNAME)
  Slack.configure do |config|
    api_key = File.open("../credentials/slack_api_key").read
    config.token = api_key
  end
  Slack.chat_postMessage(text: 'This is test from ruby', channel: '#test', username: username)
end

# main
if ARGV.size != 2
  STDERR.print "Usage: ruby#{$0} TARGET_URL\n"
  exit
end

slack_message_test()

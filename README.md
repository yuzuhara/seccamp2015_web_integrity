# Excise Kit for Web-integrity in Security Camp 2015

## Common
### Fill-in credentials/slack_api_key
* credentials/slack_api_keyにslackのページから入手したAPIキーを入力
* phantomJSをインストールしておいて欲しいです(PATHを通しておくこと)

## for Pythonista
1. $ cd python
2. $ pip install slacker selenium beautifulsoup4 requests
3. $ python detect.py "nanndemoii"

## for Rubyist
1. $ cd ruby
2. $ bundle install
3. $ ruby detect.rb "nanndemoii"

## Sample web server on localhost(It needs python 2.x)
1. $ cd sample_webpage
2. $ bash webserver.sh

sample_webpage/index.htmlを編集することで、Webページの改ざん検知を試すことができます。
ローカルサーバで動作を確認しながら課題を進めるといいでしょう。
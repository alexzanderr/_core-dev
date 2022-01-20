

# goal
"""
{
  "version": 1,
  "width": 80,
  "height": 24,
  "duration": 1.515658,
  "command": "/bin/zsh",
  "title": "",
  "env": {
    "TERM": "xterm-256color",
    "SHELL": "/bin/zsh"
  },
  "stdout": [
    [
      0.248848,
      "\u001b[1;31mHello \u001b[32mWorld!\u001b[0m\n"
    ],
    [
      1.001376,
      "I am \rThis is on the next line."
    ]
  ]
}

"""
v1_json = {}
"""
{"version": 2, "width": 87, "height": 43, "timestamp": 1642427876, "env": {"SHELL": "/bin/zsh", "TERM": "screen.xterm-256color"}}
[0.28101, "o", "_tags:comptags:36: can only be called from completion function\r\n"]
[0.281915, "o", "_tags:comptry:55: can only be called from completion function\r\n_tags:comptags:60: can only be called from completion function\r\n"]
"""

import sys
import json
from pprint import pprint
from time import sleep

#https://github.com/asciinema/asciinema/blob/develop/doc/asciicast-v1.md

demo = "demo2.cast"
with open(demo, "r+") as file:
    lines = file.readlines()

def get_duration(lines):
    pass

v1_json.update(json.loads(lines[0]))


stdout = []
duration = None
for line in lines[1:]:
    line = line[1:-1]
    delay, _, item = line.split(",")
    duration = delay
    item = item.strip()[1:-2]
    item = item.encode('raw_unicode_escape').decode('unicode_escape')

    stdout.append([float(delay), item])

    # sys.stdout.write(item)
    # sys.stdout.flush()
    # sleep(0.05)

v1_json.pop("timestamp")
v1_json["duration"] = duration
v1_json["stdout"] = stdout
print(json.dumps(v1_json, indent=4))
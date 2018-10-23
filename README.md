# betdaqlightweight

![Build Status](https://travis-ci.org/beziasb/betdaqlightweight.svg?branch=master)

Super lightweight and fast python 3.x. wrapper for Betdaq.
Only provide json-style output for the moment.
Still in beta


For all the details about the api, please see the official documentation for the Betdaq API:
http://betdaqtraders.com/api-specification/

# Installation

```
$ pip install betdaqlightweight
```

# Examples

The complete list of examples is located in the ./examples folder

##### List of all event types

```
from betdaqlightweight.client import Client

client = Client('xxx', 'xxx')
client.readonly.list_top_level_events()
```

[![PyPI version](https://badge.fury.io/py/beets-rest-api.svg)](https://badge.fury.io/py/beets-rest-api)

# Beets REST API Plugin

This is a plugin for the music management tool [beets](https://beets.io).<br>
This plugin provides a simple REST API for your music library.<br>

The API is similar to the API provided by the official [beets web plugin](https://beets.readthedocs.io/en/stable/plugins/web.html).
In contrast to the web plugin this plugin does not provide a web interface though. With this plugin I addressed some issues in the official web plugin's api that made it unusable for me.

## API

The table below shows all interfaces currently provided by the API:

| Method | Path                | Description                                      | Parameters                                                                                  | Response Type            |
|--------|---------------------|--------------------------------------------------|---------------------------------------------------------------------------------------------|--------------------------|
| GET    | /items              | Get a list of all items matching a certain query | *query*:<br>A [beets query](https://beets.readthedocs.io/en/stable/reference/query.html)    | application/json         |
| GET    | /item/{itemId}/file | Download the audio file for an item              | -                                                                                           | application/octet-stream |
| GET    | /item/{itemId}/art  | Download the cover art for an item.              | *size* (optional):<br>If provided returns the image<br>with a resolution of size x size     | image/jpeg               |

## Setup

### Install the plugin

````bash
pip install beets-rest-api  
````

### Configure the plugin
Edit your [beets configuration file](https://beets.readthedocs.io/en/stable/reference/config.html) and add the following section:

````yaml
restapi:
    host: 0.0.0.0   # The IP address the web server should bind to
    port: 8338      # The port the web server should bind to
````

Also add *restapi* to the *plugins* section.

### Run the plugin

You can start the plugin by running:
````bash
beet restapi
````

This will start a web server and block the command execution.
If you want to run it in the background you can run it this way instead:

````bash
beet restapi &>/dev/null &    # Unix
````

If the web server should always run you can add this code to a script file and add it to the autostart (Windows), crontab (Unix) or any other way of running a script on system startup.

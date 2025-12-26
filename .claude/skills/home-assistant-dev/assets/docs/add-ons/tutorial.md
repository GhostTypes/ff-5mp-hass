# Source: https://developers.home-assistant.io/docs/add-ons/tutorial

So you've got Home Assistant going and you've been enjoying the built-in add-ons but you're missing this one application. Time to make your own add-on!

To get started with developing add-ons, we first need access to where Home Assistant looks for local add-ons. For this you can use the [Samba](https://my.home-assistant.io/redirect/supervisor_addon/?addon=core_samba) or the [SSH](https://my.home-assistant.io/redirect/supervisor_addon/?addon=core_ssh) add-ons.

For Samba, once you have enabled and started it, your Home Assistant instance will show up in your local network tab and share a folder called "addons". This is the folder to store your custom add-ons.

> **tip**
>
> If you are on macOS and the folder is not showing up automatically, go to Finder and press CMD+K then enter `smb://homeassistant.local`

For SSH, you will have to install it. Before you can start it, you will have to have a private/public key pair and store your public key in the add-on config ([see docs for more info](https://github.com/home-assistant/addons/blob/master/ssh/DOCS.md#configuration)). Once started, you can SSH to Home Assistant and store your custom add-ons in the `/addons` directory.

Once you have located your add-on directory, it's time to get started!

## Step 1: The basics

* Create a new directory called `hello_world`
* Inside that directory create three files:
  + `Dockerfile`
  + `config.yaml`
  + `run.sh`

### The `Dockerfile` file

This is the image that will be used to build your add-on.

```
ARG BUILD_FROM
FROM $BUILD_FROM

# Copy data for add-on
COPY run.sh /
RUN chmod a+x /run.sh

CMD [ "/run.sh" ]
```

### The `config.yaml` file

This is your add-on configuration, which tells the Supervisor what to do and how to present your add-on.

For an overview of all valid add-on configuration options have a look [here](/docs/add-ons/configuration#add-on-configuration)

```
name: "Hello world"
description: "My first real add-on!"
version: "1.0.0"
slug: "hello_world"
init: false
arch:
  - aarch64
  - amd64
  - armhf
  - armv7
  - i386
```

### The `run.sh` file

This is the script that will run when your add-on starts.

```
#!/usr/bin/with-contenv bashio

echo "Hello world!"
```

> **note**
>
> Make sure your editor is using UNIX-like line breaks (LF), not DOS/Windows (CRLF).

## Step 2: Installing and testing your add-on

Now comes the fun part, time to open the Home Assistant UI and install and run your add-on.

* Open the Home Assistant frontend
* Go to "Settings"
* Click on "Add-ons"
* Click "Add-on store" in the bottom right corner.

[![Open your Home Assistant instance and show the Supervisor add-on store.](https://my.home-assistant.io/badges/supervisor_store.svg)](https://my.home-assistant.io/redirect/supervisor_store/)

* On the top right three dots menu, click the "Check for updates" button
* Refresh your webpage when needed
* You should now see a new section at the top of the store called "Local add-ons" that lists your add-on!

![Screenshot of the local repository card](data:image/png;base64,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)

* Click on your add-on to go to the add-on details page.
* Install your add-on
* Start your add-on
* Click on the "Logs" tab, and refresh the logs of your add-on, you should now see "Hello world!" in your logs.

![Screenshot of the add-on logs](/assets/images/addon_hello_world_logs-456df50e0fa452d2c74b30a2496d0304.png)

### I don't see my add-on?!

Oops! You clicked "Check for updates" in the store and your add-on didn't show up. Or maybe you just updated an option, clicked refresh and saw your add-on disappear.

When this happens, try refreshing your browser's cache first by pressing `Ctrl` + `F5` (Windows/Linux) or `Cmd` + `Shift` + `R` (macOS). If that didn't help, it means that your `config.yaml` is invalid. It's either [invalid YAML](http://www.yamllint.com/) or one of the specified options is incorrect. To see what went wrong, go to ["Settings" → "System" → "Logs" and select "Supervisor" in the top-right drop-down menu](https://my.home-assistant.io/redirect/logs/?provider=supervisor). This should bring you to a page with the logs of the supervisor. Scroll to the bottom and you should be able to find the validation error.

Once you fixed the error, go to the add-on store and click "Check for updates" again.

## Step 3: Hosting a server

Until now we've been able to do some basic stuff, but it's not very useful yet. So let's take it one step further and host a server that we expose on a port. For this we're going to use the built-in HTTP server that comes with Python 3.

To do this, we will need to update our files as follows:

* `Dockerfile`: Install Python 3
* `config.yaml`: Make the port from the container available on the host
* `run.sh`: Run the Python 3 command to start the HTTP server

Update your `Dockerfile`:

```
ARG BUILD_FROM
FROM $BUILD_FROM

# Install requirements for add-on
RUN \
  apk add --no-cache \
    python3

# Python 3 HTTP Server serves the current working dir
# So let's set it to our add-on persistent data directory.
WORKDIR /data

# Copy data for add-on
COPY run.sh /
RUN chmod a+x /run.sh

CMD [ "/run.sh" ]
```

Add "ports" to `config.yaml`. This will make TCP on port 8000 inside the container available on the host on port 8000.

```
name: "Hello world"
description: "My first real add-on!"
version: "1.1.0"
slug: "hello_world"
init: false
arch:
  - aarch64
  - amd64
  - armhf
  - armv7
  - i386
startup: services
ports:
  8000/tcp: 8000
```

Update `run.sh` to start the Python 3 server:

```
#!/usr/bin/with-contenv bashio

echo "Hello world!"

python3 -m http.server 8000
```

## Step 4: Installing the update

Since we updated the version number in our `config.yaml`, Home Assistant will show an update button when looking at the add-on details. You might have to refresh your browser or click the "Check for updates" button in the add-on store for it to show up. If you did not update the version number, you can also uninstall and install the add-on again. After installing the add-on again, make sure you start it.

Now navigate to <http://homeassistant.local:8000> to see our server in action!

![Screenshot of the file index served by the add-on](/assets/images/python3-http-server-14f8fe7b93b320202d2e5d1b5eb0641e.png)

## Bonus: Working with add-on options

In the screenshot, you've probably seen that our server only served up 1 file: `options.json`. This file contains the user configuration for this add-on. Because we specified two empty objects for the `options` and `schema` keys in our `config.yaml`, the resulting file is currently empty.

Let's see if we can get some data into that file!

To do this, we need to specify the default options and a schema for the user to change the options. Change the options and schema entries in your `config.yaml` with the following:

```
...
options:
  beer: true
  wine: true
  liquor: false
  name: "world"
  year: 2017
schema:
  beer: bool
  wine: bool
  liquor: bool
  name: str
  year: int
...
```

Reload the add-on store and re-install your add-on. You will now see the options available in the add-on config screen. When you now go back to our Python 3 server and download `options.json`, you'll see the options you set. [Example of how options.json can be used inside `run.sh`](https://github.com/home-assistant/addons/blob/master/dhcp_server/data/run.sh#L10-L13)

## Bonus: Template add-on repository

We maintain a full template example repository for add-ons you can use to get started. You can find that in the [`home-assistant/addons-example` repository](https://github.com/home-assistant/addons-example).
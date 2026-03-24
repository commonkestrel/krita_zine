# Krita Zine Maker

This is a simple extension to make it easier to create zines in Krita :)

![Demonstration Image](https://raw.githubusercontent.com/commonkestrel/krita_zine/refs/heads/main/Zine.png)

## Installation

In order to install the extension in Krita,
download the zip file from the [Releases](https://github.com/commonkestrel/krita_zine/releases/tag/v0.1.1) tab,
and follow the instructions [here](https://docs.krita.org/en/user_manual/python_scripting/install_custom_python_plugin.html).

There are two functions as follows:

## `Tools > Scripts > Create New Zine`

This creates a new document
with grid lines and a nice overlay.
This will always be at 3300x2550px at 300dpi,
which is the default U.S. Letter size.

You cannot create one with a different size without altering the source code,
mostly because I'm lazy, sorry.

## `Tools > Scripts > Export Zine`

This will automatically rotate the top cells and hide the helper layer,
before exporting like you would normally.

Rhythmbox Seek Plugin
=====================

A simple plugin for [Rhythmbox](https://projects.gnome.org/rhythmbox/) (the default media player on many Debian and Ubuntu installations),
that allows you to seek forwards/backwards in the current track. Fast-forward or rewind, in other words.

Requirements
------------
This plugin has only been tested on Rhythmbox version 2.97, but any 2.9x version, or newer, should work.
For recent Gnome-based Debian and Ubuntu installs, this is the default Music media player. E.g. Debian Wheezy 7, or Ubuntu Precise Pangolin 12.04.

Installation
------------
This plugin does not have its own installer, so to install, follow these
simple steps:

* Determine your Rhythmbox local user (config) directory.
For recent Debian/Ubuntu installations, this is in `~/.local/share/rhythmbox/`
* In that directory, create a `plugins` directory if needs be.
* [Download this plugin](https://github.com/cgarvey/rhythmbox-seek/archive/master.zip).
* Extract the zip file to your `plugins` directory. Your `plugins` directory should now contain a `rhythmbox-seek-master` directory.
* Start, or restart, Rhythmbox
* Go to `Edit` > `Plugins` menu, and sroll down to `Seek`. Tick the checkbox to enable it.
* You should now be able to seek forward/backward using keyboard shortcuts or the new menu items under the `Control` menu.


Keyboard Shortcuts
------------------
Use the menu items (under `Control`), or use the arrow/cursor keys as keyboard shortcuts, as follows:

* Use `Control + Left` to skip backward by 5 seconds.
* Use `Control + Right` to skip forward by 10 seconds.

Support
-------
I don't offer any support, but if you create an Issue here on Github, or get in touch with me on Twitter [@cgarvey](https://twitter.com/cgarvey) I'll do my best to address any issues.

Credits
-------
I tried two plugins but neither worked, nor were updated any time recently.
I took the best of both of those plugins, and updated the code to work with
the latest Rhythmbox.

* [bartensud](https://github.com/bartensud/Rhythmbox-Seek-Plugin)
* [Erik Johansson](https://github.com/emj/Skip-ahead-plugin)

License
-------
**Copyright 2013 Cathal Garvey. http://cgarvey.ie/**

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

*(Free) commercial licensing available on request.*


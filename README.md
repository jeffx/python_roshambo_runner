Python RoShamBo Runner
===============================

An Engine that pits RoShamBo bots against each other

Dependencies
------------

 * prettytable

Features
--------

 * TODO

Requirements for bots
---------------------
Bots will be imported with the bots module.

It must have:

* a module level `__botname__`
* a module level `__entryfunction__`
* a function that returns:
  0 = for rock
  1 = for paper
  2 = for scissors

Bot Writing

Usage
-----

 * `pip install git+https://github.com/jeffx/python_roshambo_runner.git@master#egg=python_roshambo_runner`
 * Place bots in the bot directory
 * run `roshambo`


License
-------

GNU General Public License v3 (GPLv3)

Authors
-------

 - Jeffery Tillotson <jpt@jeffx.com>

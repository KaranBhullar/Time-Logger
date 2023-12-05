
# Time-Logger
## Description
**Time-Logger is an easy to use stopwatch CLI tool written in Python.**

## Installation

After downloading all of the files, navigate to the root directory in the terminal:

` cd timeLogger `

After this install the CLI tool via pip:

`pip install .`

And its all ready! Currently, there are three functions available: start, stop, and log, where start will begin the timer, stop will end the running timer and log will log the current time with a given string.

To start timeLogger, run the following:

`timeLogger -s` 

or

`timeLogger --start`

To stop timeLogger, run the following

`timelogger -e`
or
`timeLogger --stop`

Note to end the timer, `-s` must be invoked first to start the timer.

An example use case of the log function is as follows:

`timeLogger -l "Accomplished a task!"`
or
`timeLogger --log "Accomplished a task!"`
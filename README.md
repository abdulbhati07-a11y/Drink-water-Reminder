# Water Reminder (Python)

A lightweight Python script that sends periodic desktop notifications reminding the user to drink water. The program runs continuously and uses the **plyer** library to generate system notifications while the **time** module controls the reminder interval.

## Features

* Desktop notification reminders
* Continuous background execution
* Adjustable reminder interval
* Simple and beginner-friendly implementation

## Requirements

* Python 3.x
* plyer library

Install the dependency:

pip install plyer

## Usage

1. Clone the repository or download the script.
2. Navigate to the project directory.
3. Run the program:

python main.py

The script will start sending periodic notifications reminding you to drink water.

## Configuration

The reminder frequency can be adjusted by modifying the `time.sleep()` value in the code.

Example:

* `time.sleep(10)` → reminder every 10 seconds
* `time.sleep(1800)` → reminder every 30 minutes

## Overview

This project demonstrates a simple practical use of Python for automation and desktop notifications. It highlights the use of loops, time delays, and external libraries in a minimal and easy-to-understand implementation.

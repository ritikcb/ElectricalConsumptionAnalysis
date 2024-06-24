# ElectricalConsumptionAnalysis
This repository contains a Python project designed to analyze electrical consumption data. The project reads a CSV file containing time-series data on electrical consumption, processes it to extract relevant insights, and calculates differences in consumption over specified time ranges.

Project Overview
This project analyzes electrical consumption data from a CSV file. It reads the data, filters it for electrical consumption within a specific time range, and calculates the difference in consumption between the start and end of the specified period.

Prerequisites
Python 3.x
pandas library

Key Points:
The script reads a CSV file and converts the 'time' column to a datetime format.
It filters the data to include only the 'electrical_consumption' variable.
It defines a time range and filters the data within this range.
It calculates the closest timestamps to the start and end times and computes the difference in electrical consumption between these times.
The results are printed, showing the start and end times, their respective values, and the total electrical consumption difference.

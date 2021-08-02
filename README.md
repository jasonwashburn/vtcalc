# Valid Time Calculator

Calculates the valid time from a model run time and a given offset value.

    usage: python vtcalc.py [-h] model_run offset

    Calculate a valid time from a model run and offset.

    positional arguments:
    model_run Model Run: (Format: YYYYMMDDHH[z,Z]
    offset Number of hours to offset (Format: [+,-]HH)

    optional arguments:
    -h, --help show this help message and exit

Example Output:  
![screenshot of vtcalc](img/screenshot.png "Screenshot")

Tip: for added convienance, add an alias to your profile  
`alias vtc='python <path_to_vtcalc.py> $1 $2'`

![screenshot of vtcalc](img/screenshot_alias.png "Screenshot")

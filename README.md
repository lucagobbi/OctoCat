# OctoCat - Materialize stuff with the Cat

<img src="./assets/thumb.png" width=400>

[![awesome plugin](https://custom-icon-badges.demolab.com/static/v1?label=&message=awesome+plugin&color=F4F4F5&style=for-the-badge&logo=cheshire_cat_black)](https://)

OctoCat is a Cheshire Cat plugin that connects the Cat to your OctoPrint instance, allowing you to manage your 3D printers using natural language commands.

## Configuration

After installing the plugin via the Cheshire Cat admin panel, you must configure it to connect to your OctoPrint instance. This involves setting the OctoPrint URL (e.g., http://octopi.local:8081/) and providing an API key to authenticate requests to the OctoPrint server. For further assistance, refer to the OctoPrint <a href="http://docs.octoprint.org/en/master/api/general.html">documentation</a>.

## Usage

Congratulations! You can now control your 3D printers through the Cat by issuing commands like "What's the current print status?" or "Print the cheshire_cat.gcode".

Simple actions such as requesting information or pausing the print are directly mapped to Cheshire Cat tools. In contrast, printing commands are processed through a Cheshire Cat form that requires user confirmation, offering more precise control over the printing operations.

Current integrated actions include:

- **get_printer_info**: useful to check connectivity and printer status.

- **get_gcodes**: useful to retrieve all the gcode files in your OctoPrint server.

- **get_current_print_status**: useful to get the current print status.

- **cancel_print**: useful to cancel the current print job.

- **pause_print**: useful to pause the current print job.

- **resume_print**: useful to resume the current print job.

- **restart_print**: useful to restart the current print job.

## Potential Enhancements

Although OctoCat is currently an experimental proof of concept, future enhancements could include managing files, users, connections, printer controls, and other functionalities that OctoPrint currently supports.

## Credits

Special thanks to the <a href="https://octoprint.org/">OctoPrint</a>  project and the <a href="https://github.com/dougbrion/OctoRest">OctoRest</a> client, which greatly simplifies REST communication with the OctoPrint server.



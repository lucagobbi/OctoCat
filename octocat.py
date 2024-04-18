from cat.mad_hatter.decorators import tool
from cat.experimental.form import form, CatForm
from cat.looking_glass.cheshire_cat import CheshireCat
from pydantic import BaseModel, Field
from octorest import OctoRest

ccat = CheshireCat()

def make_client():
    try:
        settings = ccat.mad_hatter.get_plugin().load_settings()
        client = OctoRest(url=settings["octoprint_url"], apikey=settings["octoprint_api_key"])
        return client
    except Exception as e:
        print(e)

class PrintModel(BaseModel):
    gcode_filename: str = Field(description=f"Name of the gcode file to be printed")

@form
class PrintForm(CatForm):
    description = "Print a specific gcode file"
    model_class = PrintModel
    start_examples = [
        "Print the cat.gcode file",
        "Print tower.gcode file",
    ]
    stop_examples = [
        "I dont want to print anymore"
    ]
    ask_confirm = True

    def submit(self, form_data):
        client = make_client()
        gcode = form_data["gcode_filename"]
        try:
            if gcode not in [file['name'] for file in client.files()['files']]:
                return {
                    "output": f"G-code file {gcode} does not exist"
                }
            client.select(gcode)
            client.start()
            return  {
                "output": f"Started printing: {gcode}"
            }
        except Exception as e:
            return {
                "output": f"Error: {e}"
            }


@tool(return_direct=True)
def get_printer_info(tool_input, cat):
    """
    Useful to get the printer info. User may ask: "What is the printer info?" or similar.
    """
    try:
        client = make_client()
        message = ""
        message += str(client.version) + "\n"
        message += str(client.job_info()) + "\n"
        printing = client.printer()['state']['flags']['printing']
        if printing:
            message += "Currently printing!\n"
        else:
            message += "Not currently printing...\n"
        return message
    except Exception as e:
        print(e)


@tool(return_direct=True)
def get_gcodes(tool_input, cat):
    """
    Useful to retrieve all the G-code file names on OctoPrint server. User may ask: "What are the G-code files?" or similar.
    """
    client = make_client()
    message = "The GCODE files currently on the printer are:\n\n"
    for k in client.files()['files']:
        message += k['name'] + "\n"
    return message

    
@tool(return_direct=True)
def cancel_print(tool_input, cat):
    """
    Useful to cancel a print on OctoPrint server. User may ask: "Cancel the print" or similar.
    """
    client = make_client()
    try:
        client.cancel()
        return f"Printing cancelled"
    except Exception as e:
        return "Error: " + str(e)
    
@tool(return_direct=True)
def pause_print(tool_input, cat):
    """
    Useful to pause a print on OctoPrint server. User may ask: "Pause the print" or similar.
    """
    client = make_client()
    try:
        client.pause()
        return f"Printing paused"
    except Exception as e:
        return "Error: " + str(e)
    
@tool(return_direct=True)
def resume_print(tool_input, cat):  
    """
    Useful to resume a print on OctoPrint server. User may ask: "Resume the print" or similar.
    """
    client = make_client()
    try:
        client.resume()
        return f"Printing resumed"
    except Exception as e:
        return "Error: " + str(e)
    
@tool(return_direct=True)
def restart_print(tool_input, cat):
    """
    Useful to restart a print on OctoPrint server. User may ask: "Restart the print" or similar.
    """
    client = make_client()
    try:
        client.restart()
        return f"Printing restarted"
    except Exception as e:
        return "Error: " + str(e)
    

@tool()
def get_current_print_status(tool_input, cat):
    """
    Useful to get the current print status. User may ask: "What is the current print status?" similar.
    """
    client = make_client()
    try:
        return str(client.job_info())
    except Exception as e:
        return "Error: " + str(e)
    

    



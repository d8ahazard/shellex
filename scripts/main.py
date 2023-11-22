import gradio as gr
import subprocess

from modules import script_callbacks


def bash_command(command):
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
    except subprocess.CalledProcessError as e:
        output = f"Error: {e.output}"

    return output

def build_ui():
    with gr.Blocks() as auto_console:
        gr.Markdown("## Simple BASH Console Emulator")
        gr.Markdown("Enter any command to execute. **Warning**: This interface allows all commands and should be used with caution.")
        with gr.Row():
            input_text = gr.Textbox(label="Command")
            submit_input = gr.Button(label="Submit")
        output_text = gr.Textbox(label="Output", interactive=False, lines=10)
        submit_input.click(fn=bash_command, inputs=input_text, outputs=output_text)
        return ((auto_console, "Shellex", "shellex"),)

script_callbacks.on_ui_tabs(build_ui)

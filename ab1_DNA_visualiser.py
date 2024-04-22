import flet as ft
import Bio
import matplotlib.pyplot as plt
from Bio import SeqIO
from collections import defaultdict
from flet.matplotlib_chart import MatplotlibChart

def main(page: ft.Page):
    page.title = "AB1 Files Visualiser"
    page.theme_mode = "dark"
    page.vertical_alignment = ft.MainAxisAlignment.SPACE_BETWEEN
    page.window_width = 900
    page.window_height = 700
    
    # the function of changing theme mode
    def change_theme(e):
        page.theme_mode = "light" if page.theme_mode == "dark" else "dark"
        page.update()

    def pick_result(e: ft.FilePickerResultEvent):
        if not e.files:
            selected_files.value = "Nothing selected"
        else:
            # reading and visualization of the ab1 file
            selected_files.value = ""
            pisk = str(e.files)
            ab1_file_location = pisk[pisk.index("path=")+6:pisk.index(", size")-1] # getting a link to the ab1 file
            record = SeqIO.read(ab1_file_location, "abi")
            channels = ["DATA9", "DATA10", "DATA11", "DATA12"]
            trace = defaultdict(list)
            for c in channels:
                trace[c] = record.annotations["abif_raw"][c]
            fig_size_x = 150
            fig_size_y = 50
            figurs, ax = plt.subplots(figsize=(fig_size_x, fig_size_y))
            ax.plot(trace["DATA9"], c="yellow", label="G")
            ax.plot(trace["DATA10"], c="green", label="T")
            ax.plot(trace["DATA11"], c="red", label="C")
            ax.plot(trace["DATA12"], c="blue", label="A")
            ax.legend(loc="lower left", fontsize=(150 if fig_size_x > 140 else 15))
            page.add(MatplotlibChart(figurs, expand=True))   
        page.update()
    
    pick_dialog = ft.FilePicker(on_result=pick_result)
    page.overlay.append(pick_dialog)
    selected_files = ft.Text()

    # buttons
    blue_widgets = ft.Row(
            [
                ft.IconButton(ft.icons.SUNNY, on_click=change_theme)      
            ],
            vertical_alignment=ft.MainAxisAlignment.END
        )      
    upload_button =  ft.Row(
            [
                ft.ElevatedButton(
                    "Select a file", 
                    icon=ft.icons.UPLOAD_FILE, 
                    on_click=lambda _: pick_dialog.pick_files(allow_multiple=False, allowed_extensions=["ab1"]) # file selection
                    )
            ],
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER
        )
    # visualizing buttons
    page.add(
        upload_button,
        ft.Row(
            [
                selected_files
            ], 
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER
        ), 
        blue_widgets
    ) 
    page.update()
ft.app(target=main) 
#IMPORTS
import pandas
import PySimpleGUI as sg
import numpy
import os

#ENGINE

class Ticket():
    def __init__(self, issue_number, reporter, assignee, details, status, comments):
        self.issue_number = issue_number
        self.reporter = reporter
        self.assignee= assignee
        self.details = details
        self.status = status
        self.comments = comments

def ReadFile():
    global Tickets_values_to_list
    global Headings

    Tickets_data_Frame = pandas.read_excel('CRM_base.xlsx', sheet_name='Tickets')
    #print(Tickets_data_Frame)
    Tickets_values = Tickets_data_Frame.values
    #print(Tickets_values)
    Tickets_values_to_list = Tickets_values.tolist()
    print(Tickets_values_to_list)
    Headings = Tickets_data_Frame.columns.tolist()
    #print(Headings)


def Turn_data_to_tickets():
    global work_list
    global Tickets_to_display
    global Comments
    global Comments2

def Create_new_ticket():
    print("Działam!")
    CNT_layout = [[sg.Text("Działam")], sg.Input()],
    print("Działam!")
    Create_new_ticket_window = sg.Window('Create new ticket', CNT_layout, background_color="blue")
    print("Działam!")
    while True:
        event, values = Create_new_ticket_window.read()
        if event == 'Exit' or event == sg.WIN_CLOSED:
            break
    window.close()


#original window:

# Event Loop to process "events" and get the "values" of the inputs

ReadFile()
Turn_data_to_tickets()

ButtonsLayout = [[sg.Button("Create new ticket", key='-NEW-')]]

TicketsTableLayout = [[sg.Table(values=Tickets_values_to_list,headings=Headings,auto_size_columns=True,enable_events=True,enable_click_events=True,key='-TABLE-',background_color="white", text_color="black",size=(1100, 830))]]

#LinksTableLayout = [[sg.Table(values=)]]

layout = [[sg.Frame(title="Options",title_color="black",layout=ButtonsLayout,background_color="lightblue",size=(200, 600)),
           #sg.Frame(title="Click for more details",title_color="black",layout=LinksTableLayout,background_color="white",size=(1100, 600)),
            sg.Frame(title="Tickets",title_color="black",layout=TicketsTableLayout,background_color="white",size=(1100, 600))]
        ]


# Create the Window
window = sg.Window('CRM by PJO', layout, background_color="white", size=(1200, 600), auto_size_buttons=True, auto_size_text=True)


#EVENTS
while True:
    event, values = window.Read()
    print(event, values)
    if event == sg.WIN_CLOSED:
        break
    elif event == '-NEW-':
        Create_new_ticket()
    # elif event == "-TABLE-":
    #     OpenTicketWindow()
    else:
        pass
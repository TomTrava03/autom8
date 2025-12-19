import WorkflowManager from workflowmanager

from textwrap import dedent

def main_menu():
    print(""" 
            1. Add WorkFlow 
            2. Open WorkFlow
            3. Delete Workflow
            0. Exit
            """).dedent()
    check_value()
    if value == "1":
        workflow_setup_menu()
    elif value == "2":
        workflow_list_menu()
    elif value == "0":
        pass
    else:
        print("No valid character")
        main_menu()

def workflow_setup_menu():
    print("Enter WorkFlow")
    print("""
            1. 
            0. Exit
            """)
        value = input("> ")
        if value == "1":
            main_menu() 

def workflow_list_menu():
    wf_manager.list_workflows()
    value = input("> ")
    if 

def workflow_menu(wf_id):
    print(f"Workflow: {wf_id}")
    print("""
            1. Add Node
            2. Remove Node
            0. Exit 
          """)

def check_input():
    global value
    value = input("> ")
    try:
        value = int(value)
    except ValueError:
        print("") # TODO : improve

def init():
    global wf_manager
    wf_manager = WorkflowManager()
    wf_manager.load_workflows()
    main_menu()


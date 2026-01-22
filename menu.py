from workflowmanager import WorkflowManager

from textwrap import dedent

MAIN_MENU = {
        "title" : "MAIN MENU"
        "entries" : ["Add Workflow", "List Workflows", "Delete Workflow"]
        }

WORKFLOW_MENU = {
        "title" : "WORKFLOW MENU"
        "entries" : [] # filled dynamically
        }

NODE_MENU = {
        "title" : "NODE MENU"
        "entries" : []
        }

def check_input():
    global value
    try:
        value = input("> ")
        value = int(value)
    except ValueError:
        print("[!]Input not valid, try again.")
        check_input()

def workflow_setup_menu():
    wf_name = input("Workflow name? >")
    print("Adding WorkFlow...")
    wf_id = wfs_manager.add_workflow(wf_name)
    workflow_menu(wf_id)

def choose_workflow_menu():
    wfs_manager.list_workflows()
    print("0. Main Menu")
    print("Choose a Workflow to open.")
    check_input()
    if value == 0:
        main_menu()
    
def workflow_menu(wf_id):
    print(f"Workflow: {wf_id}")
    print(dedent("""\
            1. Add Node
            2. List Nodes
            3. Remove Node
            0. Main menu 
          """))
    check_input()
    if value == 2:
        wfs_manager(wf_id).list_workflows_nodes(wf)
    elif value == 0: 
        main_menu()
    else:
        print("[!]Not a valid option.")

    if value == 1:
        workflow_setup_menu()
    elif value == 2:
        choose_workflow_menu()

    
def print_menu(stdscr, menu):
    curses.curs_set(0)
    curses.start_color()

    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    SELECTED = curses.color_pair(1)

    stdscr.clear()
    stdscr.refresh()

    menu_height = len(menu["entries"])
    # selected index
    current = 0

    win = curses.newwin(
        BORDER_HEIGHT * 2 + menu_height + PADDING,
        WIN_WIDTH,
        MARGIN,
        MARGIN
    )
    win.keypad(True)

    while True: 
        win.clear()
        # WINDOW BORDERs
        win.box()
        # MENU TITLE
        win.addstr(
            0,
            (WIN_WIDTH - len(menu["title"])) // 2,
            f" {menu['title']} ",
            curses.A_BOLD
        )
        # MENU ENTRIEs
        for i, entry in enumerate(menu["entries"]):
            y = PADDING + i + 1

            if i == current:
                win.addstr(y, PADDING * 2, f"{i}.", SELECTED)
                win.addstr(y, PADDING * 6, entry, SELECTED)
            else:
                win.addstr(y, PADDING * 2, f"{i}.")
                win.addstr(y, PADDING * 6, entry)

        win.refresh()
        # Wait for a key to get pressed
        key = win.getch()
        
        if key == curses.KEY_UP:
            current = (current - 1) % menu_height

        elif key == curses.KEY_DOWN:
            current = (current + 1) % menu_height

        # ENTER
        elif key in (curses.KEY_ENTER, 10, 13):
            stdscr.clear()
            stdscr.addstr(0, 0, f"Indice selezionato: {current}")
            stdscr.refresh()
            stdscr.getch()
            break

def close(stdscr):
    curses.endwin()

def setup():
    # WORKFLOWs MANAGER SETUP
    global wfs_manager
    wfs_manager = WorkflowManager()
    wfs_manager.load_workflows()

    # CURSES SETUP
    stdscr = curses.initscr()
    curses.noecho()
    stdscr.keypad(True)
    curses.nocbreak()
    stdscr.keypad()

    print_menu(stdscr, MAIN_MENU)


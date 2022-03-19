###########################################################################################################################################
##################################################### Imports #############################################################################
###########################################################################################################################################
# Imports the pydrive wrapper, which allows for simpler usage of google's apis
from Modules.pydrive_wrapper import *



###########################################################################################################################################
##################################################### Variables ###########################################################################
###########################################################################################################################################

# The id for the google sheet which birdgate runs on
birdgate_id = "1V-a8qZ1ETO6TlET_tlkimXxYHlekjxkWQD9QnUo5uLo"



###########################################################################################################################################
##################################################### Functions ###########################################################################
###########################################################################################################################################

# Clear the Screen
def clear_screen():
  for i in range(0,100): print()



# Get the Status of the Birds
def get_status_of_birds():
  
  # Read the 'at a glance' data from the spreadsheet
  total_num_of_birds = get_sheets_range(id=birdgate_id, range="'Fleet Data'!B1", major_dimension="COLUMNS")
  num_of_broken_birds = get_sheets_range(id=birdgate_id, range="'Fleet Data'!B2", major_dimension="COLUMNS")
  num_of_charging_birds = get_sheets_range(id=birdgate_id, range="'Fleet Data'!B3", major_dimension="COLUMNS")
  number_of_deployed_birds = get_sheets_range(id=birdgate_id, range="'Fleet Data'!B4", major_dimension="COLUMNS")
  score = get_sheets_range(id=birdgate_id, range="'Fleet Data'!B5", major_dimension="COLUMNS") 

  return dict(total_num_of_birds=total_num_of_birds[0][0], number_of_deployed_birds=number_of_deployed_birds[0][0], score=score[0][0], num_of_charging_birds=num_of_charging_birds[0][0], num_of_broken_birds=num_of_broken_birds[0][0])

# Launch the Status Menu
def launch_status_menu(output):
  

  # Gather Data for Variables
  birds = get_status_of_birds()


  # Clear the Screen
  clear_screen()

  # Display the Status of all Birds, and all Options
  if output == "main":
    print(f"""
      ######################################################################################################################
      You currently have {birds['total_num_of_birds']} birds, {birds['num_of_broken_birds']} of which are broken, and {birds['num_of_charging_birds']} of which are charging. 
      This leaves {birds['number_of_deployed_birds']} birds in the market for a total score of {birds['score']}


      Please select an option using the identifying number:
      0. Alter the Status of a Bird
      1. View All Birds
      2. View Broken Birds
      3. View Charging Birds
      4. View Deployed Birds
      5. Add a Bird to the Fleet
      6. Remove a Bird from the Fleet
      7. Back

      ######################################################################################################################
      """)

    selection = input()

    # Alter the Status of a Bird
    if selection == "0":
      print("Please enter the 4 digit code of the bird's status you wish to alter.")
      bird_code = input()


    # View All Birds
    elif selection == "1":
      launch_status_menu(output="all_birds")


    # View All Broken Birds
    elif selection == "2":
      launch_status_menu(output="all_broken_birds")


    # View All Charging Birds
    elif selection == "3":
      launch_status_menu(output="all_charging_birds")


    # View All Deployed Birds
    elif selection == "4":
      launch_status_menu(output="all_deployed_birds")


    # Add a Bird to the Fleet
    elif selection == "5":
      launch_status_menu(output="main")


    # Remove a Bird from the Fleet
    elif selection == "6":
      launch_status_menu(output="main")


    # Return to the Main Menu
    elif selection == "7":
      output="exit"
      launch_main_menu()

    # Loop
    else:
      launch_status_menu(output="main")


  # Loop
  if output != "exit":
    print("\n\n\n Press Enter to Return to the Previous Menu")
    input()
    launch_status_menu(output="main")


# Launch the Main Menu
def launch_main_menu():

  # Clear the Screen
  clear_screen()


  # This menu serves as the main loop, as it hands itself off to other, non exitable loops, unless quit is chosen in this one
  while True:
    print("""\n\n\n
      ######################################################################################################################
      Welcome to Birdgate!
      Please select an option using the identifying number:

      1. Alter Status of Birds - Updates the spreadsheet with any changes
      2. Repairs - Keeps track of which birds have which issues over time, and updates parts list when a repair is completed
      3. Analytics - Take a look at a variety of statistics extrapolated from compass
      4. Quit - Close the Program
      ######################################################################################################################
      """)

    # Accept User Input
    selection = input()


    # Launch the Charging & Deploying Sub-Module
    if selection == "1":
      launch_status_menu(output="main") # Open the status menu and display it's main screen


    # Launch the Repairing Sub-Module
    elif selection == "2":
        print(f"\t{selection} is under maintenance. Please select a different number as listed in the main menu.")


    # Launch the Analytics Sub-Module
    elif selection == "3":
        print(f"\t{selection} is under maintenance. Please select a different number as listed in the main menu.")


    # Exit the Program
    elif selection == "4":
      # Ahh, classic crash to exit <3
      print(0/0)


    else:
      print(f"\t{selection} is not a supported option. Please select a number as listed in the main menu.")


###########################################################################################################################################
##################################################### Main ################################################################################
###########################################################################################################################################

launch_main_menu()
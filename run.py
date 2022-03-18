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
  pass



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
        You currently have {birds['total_num_of_birds']} birds, {birds['num_of_broken_birds']} of which are broken, and {birds['num_of_charging_birds']}
        of which are charging. This leaves {birds['number_of_deployed_birds']} birds in the market for a total score of {birds['percent_of_deployed_birds']}


        Please select an option using the identifying number:
        0. Alter the Status of a Bird
        1. View All Birds
        2. View Broken Birds
        3. View Charging Birds
        4. View Deployed Birds

        ######################################################################################################################
        """)

      selection = input()

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
      break


    else:
      print(f"\t{selection} is not a supported option. Please select a number as listed in the main menu.")


###########################################################################################################################################
##################################################### Main ################################################################################
###########################################################################################################################################

launch_main_menu()
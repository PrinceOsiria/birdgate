###########################################################################################################################################
##################################################### Imports #############################################################################
###########################################################################################################################################
# Imports the pydrive wrapper, which allows for simpler usage of google's apis
from Modules.pydrive_wrapper import *



###########################################################################################################################################
##################################################### Functions ###########################################################################
###########################################################################################################################################

# Clear the Screen
def clear_screen():
  for i in range(0,100): print()



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

      1. Charging and Deploying - Keeps track of which birds are at the shop, and which are available
      2. Repairs - Keeps track of which birds have which issues over time, and updates parts list when a repair is completed
      3. Analytics - Take a look at a variety of statistics extrapolated from compass
      4. Quit - Close the Program
      ######################################################################################################################
      """)

    # Accept User Input
    selection = input()


    # Launch the Charging & Deploying Sub-Module
    if selection == "1":
      print(f"\t{selection} is under maintenance. Please select a different number as listed in the main menu.")


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



# Check for a local SQL database, as well as records of a google sheet
def check_for_existing_data():

  # Variables
  data_verified = True

  ##### WORKSPACE
  # The id of the sheet must be stored somewhere - a text file can suffice



  # Return the Results of the Search
  return data_verified



# Initialize Birdgate
def initialize_birdgate():
  print("Give me  a Google Sheet, then we'll talk!")


###########################################################################################################################################
##################################################### Main ################################################################################
###########################################################################################################################################

# Checks for the existence of an established google sheet
if check_for_existing_data():
  launch_main_menu()
else:
  initialize_birdgate()


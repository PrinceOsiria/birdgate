###########################################################################################################################################
##################################################### Imports #############################################################################
###########################################################################################################################################


###########################################################################################################################################
##################################################### Functions ###########################################################################
###########################################################################################################################################

# Clear the Screen
def clear_screen():
  for i in range(0,100): print()



# Main Menu
def launch_main_menu():

  # This menu serves as the main loop, as it hands itself off to other, non exitable loops, unless quit is chosen in this one
  while True:
    print("""

      Please select an option using the identifying number:

      1. Charging and Deploying - Keeps track of which birds are at the shop, and which are available
      2. Repairs - Keeps track of which birds have which issues over time, and updates parts list when a repair is completed
      3. Analytics - Take a look at a variety of statistics extrapolated from compass
      4. Quit - Close the Program

      """)

    selection = input()


    # Launch the Charging & Deploying Sub-Module
    if selection == "1":
      print(f"{selection} is under maintenance. Please select a different number as listed in the main menu.")


    # Launch the Repairing Sub-Module
    elif selection == "2":
        print(f"{selection} is under maintenance. Please select a different number as listed in the main menu.")


    # Launch the Analytics Sub-Module
    elif selection == "3":
        print(f"{selection} is under maintenance. Please select a different number as listed in the main menu.")


    # Exit the Program
    elif selection == "4":
      break


    else:
      print(f"{selection} is not a supported option. Please select a number as listed in the main menu.")


###########################################################################################################################################
##################################################### Main ################################################################################
###########################################################################################################################################

# Launch the Program
print("Welcome to Birdgate! Press Enter to Begin.")
input()
  
# Clear the Screen and Launch the Main Menu
clear_screen()
launch_main_menu()


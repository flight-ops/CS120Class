#create an instance of Office class
#initialize with initial owner and user passwords


class Office:
    def __init__(self,owner_pass,user_passes,alert_state) -> None:
        self.owner_pass = owner_pass
        self.user_passes = user_passes
        self.alert_state = alert_state
        self.user_index = {"John":["activate_alarm","deactivate_alarm"], "Jane":["activate_alarm"]}


    def activate_alarm(self):
        self.alert_state = True

    def deactivate_alarm(self):
        self.alert_state = False

    def grant_permission(self, user_key, permission_allowed):
        pass

    def revoke_permission(self, user_key, permission_revoked):
        pass

    def check_permission(self, user_key):
        print(self.user_index[user_key])

def owner_actions(Network):
    owner_action_request = input("What would you like to do? \nOptions are: Activate alarm, Deactivate alarm, Grant permissions, Revoke permissions, Check permissions or quit.\n")

    if owner_action_request == "Activate alarm":
        Network.activate_alarm()
        print("Activating alarm.")
    elif owner_action_request == "Deactivate alarm":
        Network.deactivate_alarm()
        print("Deactivating alarm.")
    elif owner_action_request == "quit":
        print("Quitting.")
        return

def user_actions(Network):
    user_action_request = input("What would you like to do? \nOptions are: Activate alarm, Deactivate alarm, or quit.\n")

    if user_action_request == "Activate alarm":
        Network.activate_alarm()
        print("Activating alarm.")
    elif user_action_request == "Deactivate alarm":
        Network.deactivate_alarm()
        print("Deactivating alarm.")


def check_pass(Network,owner_pass,user_passes):

    valid_pass = False

    while valid_pass == False:
        print(f'Current alert state is: {Network.alert_state}')
        
        user_input_pass = input("Please input your password or quit.\n")

        if user_input_pass == owner_pass:
            print("Access granted. Welcome, owner.")
            valid_pass == True
            owner_actions(Network)
        elif user_input_pass in user_passes:
            print("Access granted. Welcome, user.")
            valid_pass == True
        elif user_input_pass == "quit":
            print("Quitting program.")
            break
        elif ((user_input_pass != owner_pass) or (user_input_pass not in user_passes)) and Network.alert_state == True:
            print("On alert. Quitting program.")
            break
        else:
            print("Access denied.")
            continue

def check_user_permissions():
    pass

def main():
    Office_Building_Network = Office(owner_pass="ownerpass1234",user_passes=["userpass1","userpass2"],alert_state=False)
    check_pass(Office_Building_Network,Office_Building_Network.owner_pass,Office_Building_Network.user_passes)



main()
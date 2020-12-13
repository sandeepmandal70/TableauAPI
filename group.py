import tableauserverclient as TSC #import server client

def loginToSite(email,pwd,site):
    tableau_auth = TSC.TableauAuth(email,pwd,site)
    server = TSC.Server('https://10ax.online.tableau.com') #Link of Your tableau site
    server.auth.sign_in(tableau_auth)
    return server

def createGroup(name_of_group,server):
    new_group = TSC.GroupItem(name_of_group) #Creation of Group Item
    server.groups.create(new_group) #creating group at site

def getGroupDetails(server):
    all_groups,pagination = server.groups.get() #fecthing all group name from site
    set_of_group = set(map(lambda group:group.id,all_groups))
    print(set_of_group)
    print("No. of group : ",len(set_of_group))
    return set_of_group

if __name__ == "__main__":
    print('=======================Create Group==========================')
    email = input("Enter your Tableau email : ") 
    pwd = input("Enter your Tableau Password : ") 
    site = input("Enter your Tableau site : ") 
    group = input("Enter group name : ")


    server = loginToSite(email,pwd,site)

    print("=======================Available Group==========================")
    before_creation = getGroupDetails(server)



    createGroup(group,server)

    server.auth.sign_out()
    server = loginToSite(email,pwd,site)

    after_creation = getGroupDetails(server)

    print("New Group Created : ",after_creation-before_creation)


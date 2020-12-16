import tableauserverclient as TSC 
import pandas as pd

def loginToSite(email,pwd,site):
    tableau_auth = TSC.TableauAuth(password=pwd,username=email,site=site)
    server = TSC.Server('https://10ax.online.tableau.com') #Link of Your tableau site
    server.auth.sign_in(tableau_auth)
    return server

def getUserDetails(server):
    users,pagination = server.users.get()
    # return users
    user_detail_list = list()
    temp_list = set()
    for user in users:
        
        # temp_list.append(user.id)
        # temp_list.append(user.email)
        temp_list.add(user.name)
        # temp_list.append(user.last_login)
        # temp_list.append(user.site_role)

        # user_detail_list.append(temp_list)
    return temp_list
    # return list(map(lambda user: user.site_role, users))
    


if __name__ == "__main__":
    server = loginToSite("<Email>","<Pass>","<Site>") #enter details
    allUser = getUserDetails(server) 
    # print(pd.DataFrame(allUser))
    list_to_add_user = {'a@a.com','b@b.com','y@y.com','l@l.com'}
    # set_to_add_user = set(list_to_add_user)
    new_user_list = allUser&list_to_add_user
    print(new_user_list)
    print(list_to_add_user -new_user_list )

    print(allUser)

    
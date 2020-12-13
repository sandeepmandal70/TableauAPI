import tableauserverclient as TSC 

def loginToSite(email,pwd,site):
    tableau_auth = TSC.TableauAuth(password=pwd,username=email,site=site)
    server = TSC.Server('https://10ax.online.tableau.com') #Link of Your tableau site
    server.auth.sign_in(tableau_auth)
    return server

def getUserDetails(server):
    users,pagination = server.users.get()
    user_detail_list = list()

    for user in users:
        temp_list = list()
        temp_list.append(user.id)
        temp_list.append(user.email)
        temp_list.append(user.fullname)
        temp_list.append(user.last_login)
        temp_list.append(user.site_role)

        user_detail_list.append(temp_list)
    return user_detail_list
    # return list(map(lambda user: user.site_role, users))
    


if __name__ == "__main__":
    server = loginToSite("<Your Email>","<Password>","<Site>") #enter details
    allUser = getUserDetails(server)    
    print(allUser)
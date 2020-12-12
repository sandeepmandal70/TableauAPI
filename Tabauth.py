import tableauserverclient as TSC #import server client

#Authenticating using email and password
tableau_auth = TSC.TableauAuth('<Your email>', '<password>', '<Site name>')

#Authenticating using PersonalAccessTokenAuth
tableau_auth2 = TSC.PersonalAccessTokenAuth('<Secret Token Name>', '<Token text>', site_id='<Site Id>')

server = TSC.Server('<Tableau URL>') #Link of Your tableau site

with server.auth.sign_in(tableau_auth):
    all_datasources, pagination_item = server.datasources.get()
    print("\nThere are {} datasources on site: ".format(pagination_item.total_available))
    print([datasource.name for datasource in all_datasources])

with server.auth.sign_in(tableau_auth2):
    all_datasources, pagination_item = server.datasources.get()
    print("\nThere are {} datasources on site: ".format(pagination_item.total_available))
    print([datasource.name for datasource in all_datasources])
    
    
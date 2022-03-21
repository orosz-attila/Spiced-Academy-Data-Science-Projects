# in AWS Management Console Under Services navigate to Databases section and click on RDS
# click on Databases, then Create database
# Choose Standard create, PostreSQL, Free tier
# Enter an arbitrary instance identifier (the name of the server)
# Choose ‘postgres’ as a master username
# Enter a master password (for the ‘postgres’ user)
# Leave all other settings as is, except: 
    # - Under Storage, disable storage autoscaling — because we don't want
    # Amazon to increase storage if we end up needing more =

    # - Under Connectivity, click on Yes for Public access — because we want to
    # connect our database to our dashboarding software

# it takes a few minute until the instance is ready

# edit Security Rules:
    # Databases → click on your database (e.g. unsupervised-lemon)
    # Security group rules → click on default (sg-xxxxxxxx)
    # Inbound rules → Edit inbound rules → Add rule
    # Choose:
    #     Type: All traffic
    #     Source: Anywhere (create two rules, one with IPv4, and one with IPv6)
    # Save rules
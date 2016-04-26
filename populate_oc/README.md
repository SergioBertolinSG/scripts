###ownCloud Populator

For using it, do

```
git clone git@github.com:SergioBertolinSG/scripts.git
cd scripts
git submodule update --init --recursive
```

Install dependencies

```
pip install requests
pip install docopt
pip install termcolor
```

```
Usage:
  populate_owncloud.py [--host=<host>] [--user=<user>] [--password=<password>] 
                       [--deep-structure=<deep-length>] [--assign-group-to-users] [--create-users] 
                       [--create-groups] [--check-connection]
  populate_owncloud.py -h | --help

  Options:
    -h --help                   Show this help message and exit.
    --host=<host>               OwnCloud server, include the port
    --user=<user>               OwnCloud server admin user
    --password=<password>       OwnCloud server admin password
    --check-connection          Checks the connection with the server.
    --create-users              Create users.
    --create-groups             Create groups.
    --assign-group-to-users     Assign a group to every user.
    --deep-structure=N          How deep will be the deepest folder of user0.
```



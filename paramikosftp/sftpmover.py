#!/usr/bin/env python3
## Moving files with SFTP

## import paramiko so we can talk SSH
import paramiko
import os

## iterate across the files within directory
def movethemfiles(sftp):
    for x in os.listdir("/home/student/filestocopy/"): # iterate on directory contents
          if not os.path.isdir("/home/student/filestocopy/"+x): # filter everything that is NOT a directory
              sftp.put("/home/student/filestocopy/"+x, "/tmp/"+x) # move file to target location

## Function to create the transport object
def createTranObj(host_in, port_in):
    ## where to connect to, port number casted from string to int
    t = paramiko.Transport(host_in, int(port_in)) ## IP and port

    ## how to connect (see other labs on using id_rsa private/public keypairs)
    uname = input("Username: ")
    pword = input("Password: ")
    t.connect(username=uname, password=pword)

    ## Make an sftp connection object and send it back to the main function
    sftp = paramiko.SFTPClient.from_transport(t)  
    return sftp


def main():
    """Called at runtime"""
    
    # Get user input for connection
    host = input("What host address would you like to connect to? ")
    port = input("What port would you like to try connecting to? ")

    # passing host and port information to create object
    sftp = createTranObj(host, port)
    
    # Passing the transport object into the file moving function
    movethemfiles(sftp)

    ## close the connection
    sftp.close() # close the connection

# If code is being run DIRECTLY
if __name__ == "__main__":
    main()  # Run this script now

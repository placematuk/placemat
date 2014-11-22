# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#                                                                     #
#   Utility for synchronizing the system clock with that on a         #
#   remote server.                                                    #
#                                                                     #
#   Of course, this is better done properly and regularly by NTP.     #
#   Some networks, however, block the NTP protocol. This is an        #
#   alternative method of setting the clock if you can still access   #
#   a server with synchronized time.                                  #
#                                                                     #
#   Run the script with root priveleges to set the clock:             #
#   $ sudo ./time.sh                                                  #
#                                                                     #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# Don't forget to substitute 'user' and 'host' below.
date -f "%Y%m%d %H:%M:%S" "`ssh user@host 'date "+%Y%m%d %T"'`"

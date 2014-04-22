import hashlib, os, error_reporter
from datetime import datetime
from sys import exit


## TODO : - not yet implemented, ! needs work, * feature implemented
# * validate the user input in the function, return status code indicated success or failure
# - validate our entropy pool for salt generation, wait until enough entropy is present
# - write input santization function (convert to all lowercase, ensure alphanumeric, strip whitespace)
# - add command line functionality

# author: shadoxx - date: april 21, 2014
################################################################################

################################################################################

def generate_sha1_uuid( user_common_name, current_time, salt ):
    """ Generate a UUID using a salt and the provided information. Requires 'import hashlib'. \
        Return '1' if username passed into function isn't alphanumeric after lower() and strip().
    """
    user_common_name = user_common_name.lower()
    user_common_name = user_common_name.strip()

    if user_common_name.isalnum():
        uuid = hashlib.sha1( str(current_time) + str(salt) + str(user_common_name) )
        return str( uuid.hexdigest() )
    else:
        return 1

################################################################################

print "uuid_gen - for creating cryptographically* secure unique sha1 based user ids\n"
logger = error_reporter.ErrorReporter()    # initialize our error reporting library

uuid_metadata = {
    'name' : None,
    'time' : None,
    'salt' : None,
    'uuid' : None
}

# populate the dictionary we're using to store our generator info
uuid_metadata['name'] = str( raw_input('username: ') )
uuid_metadata['time'] = datetime.strftime( datetime.now(), "%Y%m%d%H%M.%S.%f" )
uuid_metadata['salt'] = os.urandom(16).encode('base_64')
uuid_metadata['uuid'] = generate_sha1_uuid( uuid_metadata['name'], uuid_metadata['time'], uuid_metadata['salt'] )

if uuid_metadata['uuid'] == 1:
    print logger.return_formatted_status('ERROR_BAD_USER_INPUT', "usernames must be alphanumic. no symbols or special characters allowed.")
    exit()
else:
    print "    uuid: %s\n\nGenerated with the following data: \ntime: %s\nsalt: %s" % \
            ( uuid_metadata['uuid'], uuid_metadata['time'], uuid_metadata['salt'] )

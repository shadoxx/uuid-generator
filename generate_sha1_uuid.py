import hashlib, os
from datetime import datetime

################################################################################

def generate_sha1_uuid( user_common_name, current_time, salt ):
    """ Generate a UUID using a salt and the provided information. Requires 'import hashlib'. """
    uuid = hashlib.sha1( str(salt) + str(user_common_name) + str(current_time) )
    return str( uuid.hexdigest() )

################################################################################

print "uuid_gen - for creating unique sha1 based user ids\n"

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

print "    uuid: %s\n\nGenerated with the following data: \ntime: %s\nsalt: %s" % \
        ( uuid_metadata['uuid'], uuid_metadata['time'], uuid_metadata['salt'] )

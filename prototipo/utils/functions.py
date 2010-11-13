import re
import os
import settings
import gdata.docs.service
import gdata.docs.data
import gdata.docs.client
import gdata.spreadsheet.service
from urlparse import urlparse

def get_file_extension(file_name):
    match = re.search('.*\.([a-zA-Z]{3,}$)', file_name)
    if match:
        return match.group(1).upper()
    return False
    
def upload_file(description, title):
    file_path = os.path.join(settings.PROJECT_ROOT, 'media/uploaded_templates/%s.xls' % description.id)

    file_name = os.path.basename(file_path)
    ext = get_file_extension(file_name)

    if not ext or ext not in gdata.docs.service.SUPPORTED_FILETYPES:
        raise Exception
    else:
        content_type = gdata.docs.service.SUPPORTED_FILETYPES[ext]

    try:
        ms = gdata.MediaSource(file_path=file_path, content_type=content_type)
    except IOError:
        raise Exception

    gd_client = gdata.docs.service.DocsService()
    gd_client.ClientLogin(settings.ACCOUNT_EMAIL, settings.ACCOUNT_PASSWORD)
    entry = gd_client.Upload(ms, title)

    if entry:
      return entry.GetAlternateLink().href
    else:
      raise Exception
      
def get_gdoc_key(url):
    return dict([e.split('=') for e in urlparse(url).query.split('&')])['key'] 

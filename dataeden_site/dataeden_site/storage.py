import os
from django.contrib.staticfiles.storage import FileSystemStorage

class NginxStorage(FileSystemStorage):

    def save(self, name, content, **kwargs):
        # Save the static file to the Nginx server's cache.
        path = os.path.join(self.base_url, name)
        with open(path, 'wb') as f:
            f.write(content)

    def delete(self, name):
        # Delete the static file from the Nginx server's cache.
        path = os.path.join(self.base_url, name)
        os.remove(path)
        
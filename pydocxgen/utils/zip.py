from io import BytesIO
from zipfile import ZipFile
from shutil import copyfileobj


class DocxFile:
    """
    Creates a docx file in memory.
    """

    def __init__(self):
        """
        Initialises a file in memory and turns it into a zipped file
        """
        self.data = BytesIO()
        self.zipped = ZipFile(self.data, 'w')

    def write(self, path, text):
        """
        Writes string to given target within zipfile
        """
        self.zipped.writestr(path, text)

    def save(self, file_path):
        """
        Saves the zip file in path
        """
        self.zipped.close()
        self.data.seek(0)

        with open(file_path, 'wb') as file:
            copyfileobj(self.data, file)

    def get_data(self):
        """
        Returns the file for download
        """
        self.zipped.close()
        self.data.seek(0)

        return self.data

    def close(self):
        """
        Closes the zip file and deletes the file in memory
        """
        self.zipped.close()
        self.data.truncate(0)
        self.data.seek(0)

import base64

from sources.base.interface import DownloadableSource
from utils import file
from downloaders import BaseDownloader
from sources.base import BaseSource


class PictureSource(BaseSource,DownloadableSource):
    __source_name__ = "picture"

    def __init__(self, url, headers, filename,filecontent):
        self.url = url
        self.headers = headers
        self.filename = filename
        self.filecontent = filecontent

    @property
    def suffix(self):
        return self.filename.split(".")[-1]

    @classmethod
    def initFromBase64(cls,filename,src):
        data = src.split(',')
        if (len(data) == 2):
            return cls("",{},filename,base64.b64decode(data[1]))
        else:
            return cls("", {}, filename, src)

    def download(self, downloader: BaseDownloader, saveroute, **kwargs):
        if (self.url == ""):
            file.writeToFile(self.filecontent,saveroute,self.filename,binary=True)
        else:
            downloader.download(self.url, saveroute, self.filename, headers = self.headers, **kwargs)
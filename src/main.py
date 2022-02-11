import twitchdl
import os

class stream_scraper:
    def __init__(self, ClientID, streamers):
        self.streamers = streamers
        self.client_id = ClientID

        self.downloader = twitchdl.downloader(self.client_id, f"{os.curdir()}/downloaded")

if __name__ == "__main__":
    app = stream_scraper(input("ClientID -> "), [""])

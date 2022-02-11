import urllib.request
import requests
import os

class downloader:
    def __init__(self, client_ID, path=os.curdir()):
        self.clip_links = []
        self.client_ID = client_ID
        self.max_trys = 3
        self.path = path

        if not os.path.exists(self.path): os.makedirs(self.path)

    def get_info(self, clip):
        c_info = requests.get(f"https://api.twitch.tv/kraken/clips/{clip}", headers={"Client-ID": self.client_ID, "Accept":"application/vnd.twitchtv.v5+json"}).json()
        
        return {
            "thumb_nail": c_info["thumbnails"]["medium"],
            "mp4_url": c_info["thumbnails"]["medium"].split("-preview",1)[0] + ".mp4",
            "save_path": f"{self.path}/{clip}.mp4"
        }

    def download(self, clip_index):
        clip_data = self.get_info(self.clip_links[clip_index])
        trys = 0
        while trys < self.max_trys:
            try:
                urllib.request.urlretrieve(clip_data["mp4_url"], clip_data["save_path"])
                print(f"Successfully downloaded: {clip_data['mp4_url']}")

            except:
                trys += 1
                print(f"[Stream Scraper]: exception whilst downloading {clip_data['mp4_url']} \n[Stream Scraper]: {self.max_trys-trys} trys remaining")
                
    def add_clips(self, new_clip_links):
        self.clip_links += new_clip_links
        for i in range(len(self.clip_links)): self.clip_links[i] = self.clip_links[i].split("/")[-1]
        print("[Stream Scraper]: Clips Added")

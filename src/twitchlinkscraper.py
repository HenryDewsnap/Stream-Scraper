import requests_html

class listener:
    def __init__(self, streamer_names, time_period):
        self.base_link = "https://www.twitch.tv/NAME/clips?filter=clips&range=TIME_PERIODd"
        self.session = requests_html.HTMLSession()
        self.time_period = time_period

    def format_link(self, streamer_name): return self.base_link.replace("NAME", streamer_name).replace("TIME_PERIOD", self.time_period)

    def get_page(self, link):
        page = self.session.get(link)

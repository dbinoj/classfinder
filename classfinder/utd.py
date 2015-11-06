import requests

class UTD:
    status = None
    def __init__(self, id):
        s = requests.Session()

        headers = {
            'Origin': 'https://coursebook.utdallas.edu',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.8',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Accept': 'text/html, */*; q=0.01',
            'Referer': 'https://coursebook.utdallas.edu/',
            'X-Requested-With': 'XMLHttpRequest',
            'Connection': 'keep-alive',
        }

        s.get('https://coursebook.utdallas.edu/' + id.lower(), headers=headers)
        data = 'id=ce6303.501.16s&div=r-1childcontent&subaction=null'

        r = s.post('https://coursebook.utdallas.edu/clips/clip-section.zog', headers=headers, data=data)
        avail = r.text.find('<b>Section Status:')
        avail_to_end = r.text[avail:]
        end = avail_to_end.find('</td>')
        self.status = avail_to_end[:end]

    def get_availability(self):
        s = self.status
        substring1 = 'Available Seats:</b>'
        substring2 = '&nbsp;&nbsp; <b>Enrolled Total'
        return int(s[(s.index(substring1)+len(substring1)):s.index(substring2)])

    def get_status(self):
        return self.status

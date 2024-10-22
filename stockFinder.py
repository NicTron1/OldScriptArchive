from requests_html import HTML, HTMLSession
import requests
from dhooks import Webhook, Embed

session = HTMLSession()
r = session.get('https://finviz.com/screener.ashx?v=111&s=ta_topgainers')

ticker = '.screener-link-primary'
tickers = r.html.find(ticker)
tickerList = []
tickerLinks = []




for ticker in tickers:
    
    tickerSymbol = "**" + ticker.text +"**" 
    tickerLink = "https://finviz.com/" + ticker.attrs['href'] 
    tickerLinks.append('')
    tickerList.append(tickerSymbol)
   

gain = '.is-green'
gains = r.html.find(gain)
percGains = []
amntGains = []

for gain in gains:
    tickerGain = gain.text
    if "%" in tickerGain:
        percGains.append("```"+tickerGain+"```")
    
    


desc = tickerList[0]+ " " + percGains[0] + " " + tickerLinks[0] + "" + tickerList[1] +  " " + percGains[1] + " " + tickerLinks[1] + ""+tickerList[2] +  " " + percGains[2] + " " + tickerLinks[2] + ''+tickerList[3]+   " " + percGains[3] + " " + tickerLinks[3] + ''+tickerList[4]+  " " + percGains[4] + " " + tickerLinks[4] + ''+tickerList[5]+ " "   + percGains[5] + " " + tickerLinks[5] + ''+tickerList[6]+  " " + percGains[6] + " " + tickerLinks[6] + ''+tickerList[7] + " "  + percGains[7] + " " + tickerLinks[7] + ''+tickerList[8]+ " "   + percGains[8] + " " + tickerLinks[8] + ''+tickerList[9]+ " "  + percGains[9] + " " + tickerLinks[9] + ''+tickerList[10]+ " "   + percGains[10] + " " + tickerLinks[10] + ''+tickerList[11]+ " "   + percGains[11] + " " + tickerLinks[11] + ''+tickerList[12]+ " " + percGains[12] + " " + tickerLinks[12] + ''+tickerList[13] + " " + percGains[13] + " " + tickerLinks[13] + ''+tickerList[14]+ " "  + percGains[14] + " " + tickerLinks[14] + ''+tickerList[15]+ " "   + percGains[15] + " " + tickerLinks[15] + ''+tickerList[16]+ " "  + percGains[16] + " " + tickerLinks[16] + ''+tickerList[17]+ " "  + percGains[17] + " " + tickerLinks[17] + ''+tickerList[18] + " "  + percGains[18] + " " + tickerLinks[18] + ''+tickerList[19] + " "  + percGains[19] + " " + tickerLinks[19] + ''


hook = Webhook('https://discord.com/api/webhooks/783145320372240404/s4Zk3Ocu-8xqHQiKbVwUJXrrSO941v0lbSUdgzycd8AtgyoI-hEerza-IJD853nmXKpg',username="Big Boy Gains",avatar_url="https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/160/softbank/145/chart-with-upwards-trend_1f4c8.png")

embed = Embed(
    description=desc,
    color=4062976,
    
    url="https://discord.com/api/webhooks/783145320372240404/s4Zk3Ocu-8xqHQiKbVwUJXrrSO941v0lbSUdgzycd8AtgyoI-hEerza-IJD853nmXKpg",
    title="Should Have Put Your Money In These"
    )


hook.send(embed=embed)
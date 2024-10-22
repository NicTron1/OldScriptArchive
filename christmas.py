import datetime
import requests
import random 
from dhooks import Webhook, Embed

today = datetime.date.today()
someday = datetime.date(2020, 12, 25)
diff = someday - today
string = "There are " + str(diff.days) + " days until Christmas!"
print(diff.days)
imgList = []
imgList.append('https://www.history.com/.image/ar_16:9%2Cc_fill%2Ccs_srgb%2Cfl_progressive%2Cg_faces:center%2Cq_auto:good%2Cw_768/MTY5MDk1ODMyOTUwNTQ4MzYy/american-christmas-traditions-gettyimages-487756624.jpg')
imgList.append('https://static.officeholidays.com/images/935x475c/christmas.jpg')
imgList.append('https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/NativityChristmasLights2.jpg/1200px-NativityChristmasLights2.jpg')
imgList.append('https://api.time.com/wp-content/uploads/2019/06/what-is-half-christmas-workaholics.jpg')
imgList.append('https://thevideoink.com/wp-content/uploads/2019/11/5679216_110719-cc-ss-christmas-presents-generic-img.jpg')
imgList.append('https://d2rdhxfof4qmbb.cloudfront.net/wp-content/uploads/20181219152239/Christmas-Tree-Near-Fireplace-at-Home.jpg')
imgList.append('https://static.officeholidays.com/images/935x475c/christmas-eve-03.jpg')
imgList.append('https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/christmas-presents-trivia-1576852447.jpg')
imgList.append('https://cdn1.parksmedia.wdprapps.disney.com/resize/mwImage/1/900/360/75/dam/disney-world/events-tours/holidays/mainstreet-tree-5x2.jpg?1605210223702')
imgList.append('https://fortestrong.com/wp-content/uploads/christmas-frosty.jpg')
imgList.append('https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/best-christmas-quotes-1535643336.jpg')

hook = Webhook('https://discord.com/api/webhooks/777926340464607242/R65q3AwLzi7_S6jzi0-emTfyq6y_yHQ52szyH9p2Hs2AXcZ3SAiVIfFzBxqw3s3VXl2i')

embed = Embed(
    description=string,
    color=16711690,
    title="Christmas Countdown",
    
    )
embed.set_image(imgList[int(random.randrange(0, len(imgList)))])
embed.set_footer(text='Made by @NicTron')
hook.send(embed=embed)


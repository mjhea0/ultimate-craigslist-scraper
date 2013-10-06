from scrapy.item import Item, Field

class Gig(Item):
    name = Field()
    url = Field()
    skills = Field()

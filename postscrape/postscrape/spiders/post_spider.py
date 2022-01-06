import scrapy
class postsSpider(scrapy.Spider):
    name = "posts"
    start_urls=[
        'https://catalog.uncc.edu/preview_program.php?catoid=29&poid=7728',
        'https://catalog.uncc.edu/preview_program.php?catoid=29&poid=7731',
        'https://catalog.uncc.edu/preview_program.php?catoid=29&poid=7729',
        'https://catalog.uncc.edu/preview_program.php?catoid=29&poid=7532',
        'https://catalog.uncc.edu/preview_program.php?catoid=29&poid=7730',
        'https://catalog.uncc.edu/preview_program.php?catoid=29&poid=7535'
    ]

    def parse(self,response):
        for post in response.css('li.acalog-course'):
            yield{
            'title':post.css('.acalog-course a::text').get()
            }
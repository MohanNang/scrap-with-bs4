import scrapy

class glass_data(scrapy.Spider):
    name = "glassdoor"
    allowed_domains = ["www.glassdoor.co.in"]
    start_urls = ["https://www.glassdoor.co.in/Job/jobs.htm?location-redirect=true"]

    custom_settings = {
    'FEED_FORMAT': 'json',
    'FEED_URI': 'output.json'
}
    def parse(self, response):
        # job_title = response.xpath('//a[@class="jobLink css-1rd3saf eigr9kq2"]/span/text()').extract()
        # yield {'job_title_text': job_title}

        # job_data = response.xpath('//li[@data-adv-type="GENERAL"]')
        # for data in job_data:
            job_title = response.xpath('//a[@class="jobLink css-1rd3saf eigr9kq2"]/span/text()').extract()
            company_name = response.xpath('//a[@class="jobLink css-1rd3saf eigr9kq2"]/span/text()').extract()
            job_loctaion = response.xpath('//div[@class="d-flex flex-wrap css-11d3uq0 e1rrn5ka2"]/span/text()').extract()
            emp_salary = response.xpath('//div[@class="css-3g3psg pr-xxsm"]/span/text()').extract()
            yield {
                "job_title" : job_title,
                "company_name" : company_name,
                "job_location" : job_loctaion,
                "emp_salary" : emp_salary
            }
            



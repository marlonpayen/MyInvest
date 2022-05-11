'''
Created on 2 May 2022

@author: mpayen
'''

class MyClass(object):
    '''
    classdocs
    '''
    calendars = [] 
    url = 'https://api.nasdaq.com/api/calendar/dividends'
    hdrs =  {'Accept': 'application/json, text/plain, */*',
             'DNT': "1",
             'Origin': 'https://www.nasdaq.com/',
             'Sec-Fetch-Mode': 'cors',
             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0)'}


    def __init__(self, year, month):
        '''
        Parameters
        ----------
        year : year int
        month : month int
        
        Returns
        -------
        Sets instance attributes for year and month of object.
        '''
        #instance attributes
        self.year  = int(year)
        self.month = int(month)
        
    def scraper(self, date_str):
         ''' 
         Scrapes JSON object from page using requests module
         
         Parameters
         - - - - - 
         url : URL string
         hdrs : Header information
         date_str: string in yyyy-mm-dd format
             
         Returns
         - - - -
         dictionary : Returns a JSON dictionary at a given URL.
         
         
         params = {'date': date_str}     
         page=requests.get(self.url,headers=self.hdrs,params=params)
         dictionary = page.json()
         return dictionary'''
        
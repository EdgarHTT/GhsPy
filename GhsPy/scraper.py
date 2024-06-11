from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from io import open
import time


class CodeDict:

    #The default path uses backslashes which can cause issues on some systems. 
    #Using raw strings or forward slashes is a better approach.
    def __init__(self, path="dictionary/ghscode_10.txt"):
        self.code = []
        self.state = []
        self.clase = []
        self.cate = []
        self.div = []
        self.picto = []
        self.signal_p = []
        with open(path, 'r') as fichero:
            for line in fichero:
                if line.strip():
                    parts = line.split("\t")
                    self.code.append(parts[0])
                    self.state.append(parts[1])
                    self.clase.append(parts[2])
                    self.cate.append(parts[3])
                    self.div.append(parts[4])
                    self.picto.append(parts[5])
                    self.signal_p.append(parts[6])

def chemGHScode(pubchem_url=None):

    """
    The chemGHSclass func will return the GHS classification of any chemical published in Pubchem
    by scrapping the website with selenium and comparing the codes found within its html source 
    and the local dictionary database
    """
    
    chrome_options = Options()
    chrome_options.add_argument("--headless") #no GUI

    driver = webdriver.Chrome()
    driver.get(pubchem_url)
    time.sleep(0.5) #Waits for the page to load completely
    page_source = driver.page_source
    driver.quit()
    
    soup = BeautifulSoup(page_source, 'html.parser')

    HazardStat = soup.find_all(string=lambda text: any(s in text for s in code_dict.code))

    codes_found = []
    for large_string in HazardStat:
        nocommas = large_string.replace(",", " ")
        listOfstrings = nocommas.split()
        for smaller_strings in listOfstrings:
            if smaller_strings in code_dict.code:
                codes_found.append(smaller_strings)
    return codes_found

class labelBuilder():

    def __init__(self,codes_found):
        self.dict_cont = {}
        for code in codes_found:
            for index, ref_code in enumerate(code_dict.code):
                if code == ref_code:
                    self.dict_cont[code] = [
                        code_dict.state[index], 
                        code_dict.clase[index], 
                        code_dict.cate[index], 
                        code_dict.div[index],
                        code_dict.picto[index],
                        code_dict.signal_p[index],
                        ]
        """self.prod_id = []
        self.sign_w = []
        self.hazard_stat = []
        self.prec_stat = []
        self.supp_info = []
        self.picto = []"""

code_dict = CodeDict()
result = chemGHScode("https://pubchem.ncbi.nlm.nih.gov/compound/2244")
print(result)
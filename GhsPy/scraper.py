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
code_dict = CodeDict()

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
    time.sleep(5) #Waits for the page to load completely
    page_source = driver.page_source
    driver.quit()
    
    soup = BeautifulSoup(page_source, 'html.parser')
    title = soup.select("title")[0].getText()
    code_dict = CodeDict()
    HazardStat = soup.find_all(string=lambda text: any(s in text for s in code_dict.code))
    codes_found = []
    
    for large_string in HazardStat:
        nocommas = large_string.replace(",", " ")
        listOfstrings = nocommas.split()
        for smaller_strings in listOfstrings:
            if smaller_strings in code_dict.code:
                codes_found.append(smaller_strings)
    return codes_found, title

class Label_contents():

    def __init__(self,codes_found, title):
        
        self.title = title.split(" ")[0]
        
        self.hazard_cont = {}
        self.prec_cont={}
        for code in codes_found:
            for index, ref_code in enumerate(code_dict.code):
                if code == ref_code:
                    if code.startswith("H"):
                        self.hazard_cont[code] = [
                            code_dict.state[index], 
                            code_dict.clase[index], 
                            code_dict.cate[index], 
                            code_dict.div[index],
                            code_dict.picto[index],
                            code_dict.signal_p[index],
                            ]
                    else:
                        self.prec_cont[code]=[
                            code_dict.state[index]
                        ]

        
        active_pictograms = set()
        for key, value in self.hazard_cont.items():
            if value[-2] == "":
                break
            match value[-2]:
                case "GHS01":
                    active_pictograms.add("GHS01")
                case "GHS02":
                    active_pictograms.add("GHS02")
                case "GHS03":
                    active_pictograms.add("GHS03")
                case "GHS04":
                    active_pictograms.add("GHS04")
                case "GHS05":
                    active_pictograms.add("GHS05")
                case "GHS06":
                    active_pictograms.add("GHS06")
                case "GHS07":
                    active_pictograms.add("GHS07")
                case "GHS08":
                    active_pictograms.add("GHS08")
                case "GHS09":
                    active_pictograms.add("GHS09")
        self.active_pictograms = active_pictograms

        signal_word = str
        for key, value in self.hazard_cont.items():
            if key.startswith("P"):
                break
            if value[-1] == "Danger":
                signal_word = "Danger"
                break
            elif value[-1] == "Warning":
                signal_word = "Warning"
            else:
                signal_word = None
        self.signal_word = signal_word

def textLabel():
    # TODO
    return
                    
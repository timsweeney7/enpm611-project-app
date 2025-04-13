from typing import List
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from data_loader import DataLoader
from model import Issue,Event
import config



class Analysis1:
    """
    Implements an example analysis of GitHub
    issues and outputs the result of that analysis.
    """
    
    def __init__(self):
        self.DATASET:str = config.get_parameter('dataset')
        if self.DATASET == None:
            self.DATASET = 0
        
        
    def run(self):
        print("Started analysis 1")
        
        # load issues
        issues:List[Issue] = DataLoader(self.DATASET).get_issues()
        
        dates = [issue.created_date for issue in issues]
        
        # plot the sorted data on a timeline
        plt.hist(dates, bins=30)
        plt.title("Number of Issues Created by Year")
        plt.xlabel("Year")
        plt.ylabel("# of issues")
        plt.show()
        

if __name__ == "__main__":
    Analysis1().run()
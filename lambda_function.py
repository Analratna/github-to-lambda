from lib2to3.pgen2.pgen import DFAState
import pandas as pd
def lambda_handler(event, context): 
    d = {'col1': [1,2], 'col2': [3,4]} 
    df = pd.DataFrame(data=d)
print(DFAState)
print('Done x1.1')
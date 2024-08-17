# NM_Finance.py
# Steven Heinisch
# 8/17/2024

#Takes a list of returns and returns the cumulative return
def calculate_cumulative_return(returns):
    #Reference: https://www.northstarrisk.com/cumulative-return#:~:text=If%20the%20standard%20return%20over,to%20as%20the%20total%20return
    
    cumulative_return = 1
    
    for r in returns:
        cumulative_return *= (1 + r)
        
    return cumulative_return - 1
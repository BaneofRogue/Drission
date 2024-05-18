

def aggregateTransactions(inList):
        aggregated = {}

        for transaction in inList.values():
            key = (transaction['coinSpent'], transaction['coinReceived'])

            if key not in aggregated:
                aggregated[key] = {
                    'coinSpent': transaction['coinSpent'],
                    'coinReceived': transaction['coinReceived'],
                    'spentAmount': 0.0,
                    'receivedAmount': 0.0
                }
        
            # Add up the amounts
            aggregated[key]['spentAmount'] += float(transaction['spentAmount'].replace(',', ''))
            aggregated[key]['receivedAmount'] += float(transaction['receivedAmount'].replace(',', ''))
        
        return aggregated


#Please work on this.
#Should return in this format:

""" #Example

coinName1: (float) *amount of coin profited(may be negative)*
coinName2: (float) *same but for coin2*
coinName1Percent: *percentage gain/loss*
coinName2Percent: *same but for coin2*


AGGREGATED:
('meowed', 'SOL') : {'coinSpent': 'meowed', 'coinReceived': 'SOL', 'spentAmount': 15008671.202041999, 'receivedAmount': 19.444270692000003}
('SOL', 'meowed') : {'coinSpent': 'SOL', 'coinReceived': 'meowed', 'spentAmount': 8.0, 'receivedAmount': 15008671.202041999}

AFTER(2 of them become one):
0: {'meowed': 1234.0, 'SOL', 1234.0, 'meowedPercent': -100.0%, 'SOLPercent': +50.0%}

"""
def calculateProfit(inList):
    profits = {}
        
    for key, value in inList.items():
        coin_spent = value['coinSpent']
        coin_received = value['coinReceived']
        spent_amount = value['spentAmount']
        received_amount = value['receivedAmount']
            
        coin_title = coin_spent+coin_received
        
    return profits

transactionHistory = {
    0: {'coinSpent': 'meowed', 'coinReceived': 'SOL', 'spentAmount': '1,857,367.717062', 'receivedAmount': '2.666417146'},
    1: {'coinSpent': 'meowed', 'coinReceived': 'SOL', 'spentAmount': '1,857,367.717062', 'receivedAmount': '2.557739298'},
    2: {'coinSpent': 'meowed', 'coinReceived': 'SOL', 'spentAmount': '3,714,735.434124', 'receivedAmount': '4.812364341'},
    3: {'coinSpent': 'meowed', 'coinReceived': 'SOL', 'spentAmount': '3,620,267.116791', 'receivedAmount': '4.894688974'},
    4: {'coinSpent': 'meowed', 'coinReceived': 'SOL', 'spentAmount': '3,958,933.217003', 'receivedAmount': '4.513060933'},
    5: {'coinSpent': 'SOL', 'coinReceived': 'meowed', 'spentAmount': '3', 'receivedAmount': '3,620,267.116791'},
    6: {'coinSpent': 'SOL', 'coinReceived': 'meowed', 'spentAmount': '2', 'receivedAmount': '3,958,933.217003'},
    7: {'coinSpent': 'SOL', 'coinReceived': 'meowed', 'spentAmount': '3', 'receivedAmount': '7,429,470.868248'},
    8: {'coinSpent': 'SOL', 'coinReceived': 'MHGA', 'spentAmount': '5', 'receivedAmount': '9,355,826.761949'},
    9: {'coinSpent': 'rizzy', 'coinReceived': 'SOL', 'spentAmount': '938,182.845231', 'receivedAmount': '2.74654233'},
    10: {'coinSpent': 'SOL', 'coinReceived': 'rizzy', 'spentAmount': '40', 'receivedAmount': '938,182.845231'},
    11: {'coinSpent': 'bwif', 'coinReceived': 'SOL', 'spentAmount': '2,883,823.594333', 'receivedAmount': '9.994347234'},
    12: {'coinSpent': 'SOL', 'coinReceived': 'bwif', 'spentAmount': '5', 'receivedAmount': '2,883,823.594333'},
    13: {'coinSpent': 'BZONE', 'coinReceived': 'SOL', 'spentAmount': '1,216,203.126794', 'receivedAmount': '15.938252016'},
    14: {'coinSpent': 'BZONE', 'coinReceived': 'SOL', 'spentAmount': '1,216,203.126793', 'receivedAmount': '15.540299107'},
    15: {'coinSpent': 'OIIA', 'coinReceived': 'SOL', 'spentAmount': '5,154,812.141148', 'receivedAmount': '1.764311453'},
    16: {'coinSpent': 'OIIA', 'coinReceived': 'SOL', 'spentAmount': '5,504,358.545751', 'receivedAmount': '2.045177017'},
    17: {'coinSpent': 'SOL', 'coinReceived': 'OIIA', 'spentAmount': '3', 'receivedAmount': '5,504,358.545751'},
    18: {'coinSpent': 'SOL', 'coinReceived': 'OIIA', 'spentAmount': '3', 'receivedAmount': '5,154,812.141148'},
    19: {'coinSpent': 'hooray', 'coinReceived': 'SOL', 'spentAmount': '6,057,940.366724', 'receivedAmount': '2.84583994'},
    20: {'coinSpent': 'SOL', 'coinReceived': 'hooray', 'spentAmount': '5', 'receivedAmount': '6,057,940.366724'},
    21: {'coinSpent': 'coon', 'coinReceived': 'SOL', 'spentAmount': '6,309,381.308743', 'receivedAmount': '48.519909082'},
    22: {'coinSpent': 'Oops', 'coinReceived': 'SOL', 'spentAmount': '1,994,230.445652', 'receivedAmount': '1.537916444'},
    23: {'coinSpent': 'Oops', 'coinReceived': 'SOL', 'spentAmount': '2,260,427.641645', 'receivedAmount': '3.13816444'},
    24: {'coinSpent': 'SOL', 'coinReceived': 'Oops', 'spentAmount': '5', 'receivedAmount': '2,260,427.641645'},
    25: {'coinSpent': 'SOL', 'coinReceived': 'Oops', 'spentAmount': '5', 'receivedAmount': '1,994,230.445652'},
    26: {'coinSpent': 'BZONE', 'coinReceived': 'SOL', 'spentAmount': '2,432,406.253587', 'receivedAmount': '35.478785787'},
    27: {'coinSpent': 'AMC', 'coinReceived': 'SOL', 'spentAmount': '1,552,056.433004659', 'receivedAmount': '48.54553972'},
    28: {'coinSpent': 'GME', 'coinReceived': 'SOL', 'spentAmount': '1,157,674.563980911', 'receivedAmount': '45.788306633'},
    29: {'coinSpent': 'GME', 'coinReceived': 'SOL', 'spentAmount': '1,169,854.995254851', 'receivedAmount': '45.477161846'},
    30: {'coinSpent': 'SOL', 'coinReceived': 'GME', 'spentAmount': '50', 'receivedAmount': '1,169,854.995254851'},
    31: {'coinSpent': 'SOL', 'coinReceived': 'AMC', 'spentAmount': '50', 'receivedAmount': '1,552,056.433004659'},
    32: {'coinSpent': 'SOL', 'coinReceived': 'GME', 'spentAmount': '50', 'receivedAmount': '1,157,674.563980911'},
    33: {'coinSpent': '$bmichi', 'coinReceived': 'SOL', 'spentAmount': '17,454.587033112', 'receivedAmount': '6.895144874'},
    34: {'coinSpent': '$bmichi', 'coinReceived': 'SOL', 'spentAmount': '17,454.587033111', 'receivedAmount': '6.653801311'},
    35: {'coinSpent': '$bmichi', 'coinReceived': 'SOL', 'spentAmount': '33,535.182773598', 'receivedAmount': '9.630169254'},
    36: {'coinSpent': 'SOL', 'coinReceived': '$bmichi', 'spentAmount': '5', 'receivedAmount': '34,909.174066223'},
    37: {'coinSpent': 'SOL', 'coinReceived': '$bmichi', 'spentAmount': '5', 'receivedAmount': '33,535.182773598'},
    38: {'coinSpent': 'HIMMY', 'coinReceived': 'SOL', 'spentAmount': '4,282,739.643779495', 'receivedAmount': '3.709606468'},
    39: {'coinSpent': 'HIMMY', 'coinReceived': 'SOL', 'spentAmount': '6,070,009.81812075', 'receivedAmount': '5.420854843'}
    }

aggregatedHistory = aggregateTransactions(transactionHistory)
for key, value in aggregatedHistory.items():
    print(key, ":", value)

print("#"*50)
for key, value in calculateProfit(aggregatedHistory).items():
    print(key, ":", value)

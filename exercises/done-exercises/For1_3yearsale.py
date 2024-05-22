products = ['iphone', 'galaxy', 'ipad', 'tv', 'máquina de café', 'kindle', 'geladeira', 'adega', 'notebook dell', 'notebook hp', 'notebook asus', 'microsoft surface', 'webcam', 'caixa de som', 'microfone', 'câmera canon']
sales2019 = [558147,712350,573823,405252,718654,531580,973139,892292,422760,154753,887061,438508,237467,489705,328311,591120]
sales2020 = [951642,244295,26964,787604,867660,78830,710331,646016,694913,539704,324831,667179,295633,725316,644622,994303]

best_sellers = []
for i, product in enumerate(products):
    if sales2019[i] < sales2020[i]:
        growth = round(((sales2020[i] / sales2019[i] - 1) * 100), 2)    # Gets growth in % and rounds rounds in 2 decimal numbers
        best_seller = products[i], sales2019[i], sales2020[i], growth
        best_sellers.append(best_seller)

best_sellers_str = tuple(str(line) for line in best_sellers) # Converting to string the tuple list best_sellers

print('\n'.join(best_sellers_str))
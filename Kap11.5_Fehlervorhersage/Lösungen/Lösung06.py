table = X.corrwith(y).abs().sort_values(ascending=False).iloc[0:7]
table
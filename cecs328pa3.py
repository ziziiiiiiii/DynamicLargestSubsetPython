# Dynamic solution to finding the largest subset array of containers that can fit on a ship
# while adhering to constraints on the number of a given item that can be taken. 't' represents
# toasters, 'w' washing machines and 'd' dryers.
def count_items(crate):
    # Helper function to count the number of toasters, washers, and dryers in a crate.
    t = crate.count('t')
    w = crate.count('w')
    d = crate.count('d')
    return t, w, d

def cargo(crates, T, W, D):
    # Initialize a 3D DP table with zeros
    dp = [[[0 for _ in range(D + 1)] for _ in range(W + 1)] for _ in range(T + 1)]
    
    for crate in crates:
        t, w, d = count_items(crate)
        # Iterate from high to low to prevent overwriting
        for i in range(T, t - 1, -1):
            for j in range(W, w - 1, -1):
                for k in range(D, d - 1, -1):
                    if dp[i - t][j - w][k - d] + 1 > dp[i][j][k]:
                        dp[i][j][k] = dp[i - t][j - w][k - d] + 1
    
    return dp[T][W][D]

# Example calls to cargo:
# cargo(["d"],21,22,23); output: 1
# cargo(["d"],1,1,1); output: 1
# cargo(['twwddwwdtdtdddddwwwtwtttdddwwtdwt', 'td', 'wddddwwwwwttwwdwdtddwttdww', 
# 'ddtttwwwwwwwtttwwdwdwwttdwtwdwwtdwt', 'wtt', 'ttdtdtdddwtdtwtwwtwtwwwdwwwtdddtwtd', 
# 'dwwtwtdwddddt', 'twtttw', 'ddttdwwttdtwwdwtddddddwttdddwdtwwwddwddtdw', 'ddtdddttt', 
# 'wttdttdddwdttwtww', 't', 'ttwttdtwdtwwd', 'wdtwdwdttdwwdwdwtwtt', 
# 'twwwdtttttdwttdttdtdwdwdwwtwdttwwddt', 'dwtwtwwttdtdwwdwddttwtwwtwtwttdwdtwtwtddwdttt', 
# 'twtwdddttwtwtdwwwddwdttwwwtddwdtwtdddwd', 
# 'wtttwwtwwwdwddwtddwwwwdwttwwdttdtdwttw', 'twtwdddtwddttttddwtddwwtddtwdwtt', 
# 'wtdwwwddtttwtddtdwwdwwwdtddd', 'wwwt', 'ddtttwwdw', 'ttdwwwwwwwdddttttddwwd', 'd', 
# 'dwwwwddwwdddtwtwdttwtdw', 'tddddtwtttwttttt', 
# 'dtwwtdwtddddwdddwwwdwwwwwdtdddtdwwdtdddwtd', 'wdttwwwtwtwt', 
# 'tdtwwwwwwtwttdtwdddd', 'dwwwddwddddtttwdwtdwttdtdtdtd', 
# 'wwdtddtdwdtdwwtdttddwttdwwtwwtwdtwttwwwddtddt', 
# 'wtdddtttwdtdddwwtddtdwdtdwwdtwttdddwtwtwtttdtdwtd', 
# 'wdwdddtdddtddtdwtdtdtwwttwtwwwwwtdddwwdddwdtwwt', 
# 'wdwtdwttdddwwwwtwdddtdtdwdtwwddttt', 'dtddtttwdtw', 'dwwddwwdwtdwd', 
# 'twwtdwdwtwtttwddwttdwtddwtdwwttwddwwtdtttdttddt', 'ttwtwddtwdwdt', 
# 'wdwwdddddtwdwwddwdtttwwttdwdwttdwttddttwtdww', 'tddddwwtdwddd',
# 'dtwwdttdttdwwwtdtdwtwwwdwdddtdd', 'twwwddwtdtdttddtwdtwtdtd', 
# 'ttttwtdwwwtddwdwddwdwdwdwtwtdtwddttw', 'dwddtdwwwtdwwwtddtwdtdddtwtdww', 
# 'dwdwwtwwdddttdwdwtw', 'wwwtwdddwdtddwddddddwddttdwwt', 'wtttttttddwwtdwdtd', 
# 'dwwwddwttwdwtwddtdwddtdddddwddddwwddwdt', 'dwwwwwdttdtwtwwtttdddwwtwtwwwdt', 
# 'wdtwtwdwtttwddtwdwwwwwddddddtwdwttw'],20,20,20); output: 9
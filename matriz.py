def matriz(archivo):
    import numpy as np
    
    txt=str(archivo+txt)
    with open(txt) as f:
    size=sum(1 for _ in f)
    arch:open(txt,"r")
    linea=arch.readline.strip
    matris=np.zeros((size),(8))
  
    while linea != "":  
        parte=linea.split(",")
        for i in range (size):
            for j in range(8):
                matris[i][j]=parte[j-1]
        linea=arch.readline.strip








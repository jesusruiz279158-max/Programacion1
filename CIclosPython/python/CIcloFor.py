for hora in range(0,24):
    for minuto in range (0,60):
        for segundo in range (0,60):
            if hora < 10 and minuto < 10 and segundo < 10:
                print (f"0{hora}:0{minuto}:0{segundo}")
            elif hora < 10 and minuto < 10:
                print (f"0{hora}:0{minuto}:{segundo}")
            elif segundo < 10 and minuto < 10:
                print (f"{hora}:0{minuto}:0{segundo}")
            elif segundo < 10 and hora < 10:
                print (f"0{hora}:{minuto}:0{segundo}")
            elif hora < 10:
                print (f"0{hora}")
            elif minuto < 10:
                print (f"0{minuto}")
            elif segundo < 10:
                print (f"0{segundo}")
            else:        
                print (f"{hora}:{minuto}:{segundo}")
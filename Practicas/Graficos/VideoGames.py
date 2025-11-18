import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#fuente 1: Ventas internas
sales_data = {
    "GameID":["G1", "G2", "G3", "G4", "G5", "G6"],
    "Title":["Cyber-Punk 2078", "Elder Scrolls VI", "Llama Tycoon", 
             "Minecraft", "Agar.io", "Pokemon"],
    "Genre":["RPG", "RPG", "Simulation", 
             "Platform", "Sports", "RPG"],
    "Publisher":["Dev-Studious", "Bethestda", "Llama-Soft", 
                 "Nintendo", "EA", "FromSoft"],
    "Units_Sold_Millions":[15.5, 20.1, 8.0, 12.3, 18.2, 19.6]
}

sales_df = pd.DataFrame(sales_data)


#Fuente 2: Reseñas de críticos (externo)
reviews_data = {
    "GameID": ["G1", "G2", "G3", "G4", "G5", "G7"], #Nota. G6 Falta, G7 sobra
    "Critic_Score": [7.5, 9.5, 8.8, 9.7, 6.1, 8.0], #Puntucaion 0-10
    "User_Score": [5.1, 9.1, 8.5, 9.2, np.nan, 7.5] #Un NaN! Alguien olvido puntuar un juego
}

reviews_df = pd.DataFrame(reviews_data)
print("--- Datos de Ventas (Crudos) ---")
print(sales_df)
print("--- Datos de Reseñas (Crudos) ---")
print(reviews_df)

# Limpieza de datosy preparación
# Desición: Rellenaremos el User_Score que falta con el promedio ()
mean_user_score = reviews_df["User_Score"].mean() #Promedio de calicicaciones de usuarios
reviews_df["User_Score"] = reviews_df["User_Score"].fillna(mean_user_score)

print(f"\n--- Reseñas (Limpas, NaN rellenado con {mean_user_score})---")
print(reviews_df)

#Fusionar tabla (merge)
#Fusionar tabla de ventas con reseñas , GameID como llave
#INNER JOIN. Nos quedamos con los juegos existentes en ambas tablas
#G6 desaparecera, G7 desaparecera
df = pd.merge(sales_df, reviews_df, on = "GameID", how = "inner")

print("\n--- Tabla fusionada de ventas + reviews ---")
print(df)

# Crear nuevas columnas que nos den más información
# Columna Estimación de ingresos (asuminedo valen $50 cada juego)
df["Revenue_Estimate_Billions"] = (df["Units_Sold_Millions"]*50)/1000

# Columna Brecha entre reseñas de críticos y de usuarios
df["Score_Gap"] = df["Critic_Score"]-df["User_Score"]

# Columna Estandar de puntuación de los críticos (0 a 100)
df["Critic_Score_100"] = df["Critic_Score"] * 10

print("\n--- Tabla transformada (Con nuevas Columnas)")
print(df)
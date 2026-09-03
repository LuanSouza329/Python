import pandas as pd

df = pd.DataFrame({

"cliente":[
"João",
"Maria",
"João",
"Carlos",
"Maria"
],

"cidade":[
"SP",
"RJ",
"SP",
"BH",
"RJ"
]

})

total_duplicadas = df.duplicated().sum()
registros_duplicados = df[df.duplicated()]

print(total_duplicadas)
print(registros_duplicados)

print(df.shape)

df = df.duplicated()

print(df.shape)

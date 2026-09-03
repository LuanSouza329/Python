import pandas as pd

df = pd.DataFrame({

"id":[
1,
2,
3,
4
],

"cliente":[
"João",
"João",
"Maria",
"Maria"
],

"cidade":[
"SP",
"SP",
"RJ",
"RJ"
]

})

print(df)

df = df.drop_duplicates(
    subset=['cliente', 'cidade']
)

print(df)
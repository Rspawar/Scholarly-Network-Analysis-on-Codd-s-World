import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('plot.csv', delimiter=',')
df = df.reindex(index=df.index[::-1])
df = df.iloc[1:]
ax0 = df.plot(kind='bar',
                    x='Year',
                    y='CitationCount',
                    figsize=(14, 8),
                    #alpha=0.5,                  # transparency
                    color='green',
                   )

plt.title('Citation counts per year')
plt.ylabel('CitationCount')
plt.xlabel('Years')
plt.savefig('Citation counts per year.png')
plt.show()



df = pd.read_csv('plotML.csv', delimiter=',')
df = df.reindex(index=df.index[::-1])
df = df.iloc[1:]
ax0 = df.plot(kind='bar',
              x='Year',
              y='CitationCount',
              figsize=(14, 8),
              # alpha=0.5,                  # transparency
              color='blue',
              )

plt.title('Citation count for Topic Machine Learning over all the years')
plt.ylabel('CitationCount')
plt.xlabel('Years')
plt.savefig('plotML.pdf')
plt.show()
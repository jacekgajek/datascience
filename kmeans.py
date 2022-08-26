# kmeans algorithm, based on the chapter 3.1 of the book
# "Głębokie Uczenie" by Jacek Tabor, Marek Śmieja, Łukasz Struski, Przemysław Spurek, Maciej Wołczyk

import plotly.express as px
import numpy as np

# Prepare data
df = px.data.iris()

X = df.filter(items=["petal_width", "petal_length"]).to_numpy()
k = 3
N = X.shape[0]

stop = False
count = 1


# Cost function
def TE(x, v):
    return abs(x - v).sum()


def SE(x, v):
    return ((x - v) ** 2).sum()


# V – representatives (v – element, l – index, k – count)
# X – datapoints (x – element, i – index, N - count)

# The first v values are a random values taken from data points
V = X[np.random.choice(X.shape[0], size=k, replace=False), :]

while True:

    # Create indexing function j which assigns (index of) each datapoint x to index of a representative v
    # in such way that an SE error is minimal.
    j = [
        np.argmin(
            [SE(X[i], v) for v in V]
        )
        for i in range(N)
    ]

    # Create an association matrix M which length is k = |V| and M[l] is an array of data points of class l
    M = [
        [X[i] for i in range(N) if j[i] == l]
        for l in range(k)
    ]

    # Create a new array of representative values V.
    # Each new v_l value is equal to a mean of datapoints which were previously assigned to that v_l
    V1 = [
        np.mean(M[l], axis=0)
        for l in range(k)
    ]

    # If a new V array is exactly the same as previously calculated then stop the algorithm
    stop = np.all(V1 == V)

    # Assign V for the next iteration
    V = np.array(V1)
    count += 1
    if stop or count > 100:
        break

E = np.sum([np.sum([SE(X[i], v) for v in V]) for i in range(N)])
print(f'Number of steps: {count}')
print(f'Total error: {E}')

df["class"] = [str(x) for x in j]

fig = px.scatter(df,
                 x=df["petal_width"],
                 y=df["petal_length"],
                 color="class",
                 symbol="species",
                 # color_discrete_sequence=["blue", "red", "white"]
                 )

fig.show()

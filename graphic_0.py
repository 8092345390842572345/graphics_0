import matplotlib.pyplot as plt

fig, ax = plt.subplots()

plt.scatter(1, 3, c = "green", s = 250)
plt.annotate(s = "гусеницы", xy = (1.05, 2.98))
plt.scatter(3, 1, c = "blue", s = 250)
plt.annotate(s = "жуки", xy = (2.82, 0.975))
plt.xlabel("ширина")
plt.ylabel("длина")

ax.set_facecolor("whitesmoke")
ax.set_title("график")


fig.set_figwidth(8)
fig.set_figheight(8)

plt.show()

# show the diagrams

fig, ax = plt.subplots(1,5, figsize=(30,3))

ax[0] = a[my_ind].plot(kind='box', ax=ax[0])
ax[0].set_title(my_ind + ' boxplot')

sns.set_theme()
try:
    ax[1] = a[my_ind + '_no_outlier'].plot(kind='kde', ax=ax[1])
    ax[1].set_title('no outlier histogram')
except:
    ax[1] = a[my_ind + '_no_outlier'].plot(kind='box', ax=ax[1])
    ax[1].set_title('no outlier histogram')

ax[2] = sns.histplot(x=a[my_ind + '_score'], kde=True, ax=ax[2])
ax[2].set_title('score histogram')

u, c = np.unique(np.c_[a[my_ind],a[my_ind + '_score']], return_counts=True, axis=0)
ax[3] = sns.scatterplot(x=u[:,0], y=u[:,1], size=c, ax=ax[3]);
ax[3].set_title('score to indicator')

u, c = np.unique(np.c_[a[my_ind + '_no_outlier'],a[my_ind + '_score']], return_counts=True, axis=0)
ax[4] = sns.scatterplot(x=u[:,0], y=u[:,1], size=c, ax=ax[4]);
ax[4].set_title('score to no_outlier')
plt.show()

a.index.name='id'
a;

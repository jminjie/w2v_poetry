import gensim.downloader
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from adjustText import adjust_text

def download_and_save_model():
    w2v = gensim.downloader.load('glove-twitter-200')
    with open('saved_model') as f:
        w2v.save(f.name)


# On first run, download and save the model by uncommenting this line
#download_and_save_model()

# load the model
w2v = gensim.models.KeyedVectors.load('saved_model')

BG_WHITE = "#fbf9f4"
GREY50 = "#7F7F7F"
GREY30 = "#4d4d4d"
BOYGIRL = w2v['girl'] - w2v['boy']

def plot_data_1d(orig_data, labels):
    pca = PCA(n_components=1)
    data = pca.fit_transform(orig_data)

    data0 = np.append(data, np.zeros([len(data), 1]), 1)

    fig, ax = plt.subplots(figsize= (9, 9))
    fig.patch.set_facecolor(BG_WHITE)
    ax.set_facecolor(BG_WHITE)

    ax.scatter(x=data0[:,0], y=data0[:,1])
    TEXTS = []
    for i in range(len(data0)):
        #plt.annotate(labels[i], xy = data0[i])
        x = data0[i, 0]
        y = data0[i, 1]
        text = labels[i]
        TEXTS.append(ax.text(x, y, text, color=GREY30, fontsize=13, fontname="Poppins"))

    plt.grid('on')

    adjust_text(
            TEXTS,
            expand_points=(1.3, 1.3),
            arrowprops=dict(
                arrowstyle="-",
                color=GREY50,
                lw=0
                ),
            ax=fig.axes[0]
            )
    ax.set_ylabel("")
    ax.set_yticklabels([])
    ax.set_xticklabels([])
    ax.spines["right"].set_color("none")
    ax.spines["left"].set_color("none")
    ax.spines["top"].set_color("none")
    ax.spines["bottom"].set_color("none")

    plt.show()

def plot_data_2d(orig_data, labels):
    pca = PCA(n_components=2)
    data = pca.fit_transform(orig_data)

    plt.figure(figsize=(7, 5), dpi=100)
    fig, ax = plt.subplots()
    fig.patch.set_facecolor(BG_WHITE)
    ax.set_facecolor(BG_WHITE)
    plt.plot(data[:,0], data[:,1], '.')
    for i in range(len(data)):
        plt.annotate(labels[i], xy = data[i])

    plt.grid('on')
    plt.show()

def plot_data_2d_2(orig_data, labels):
    pca = PCA(n_components=2)
    data = pca.fit_transform(orig_data)

    fig, ax = plt.subplots(figsize= (9, 9))
    fig.patch.set_facecolor(BG_WHITE)
    ax.set_facecolor(BG_WHITE)

    ax.scatter(x=data[:,0], y=data[:,1])
    TEXTS = []
    for i in range(len(data)):
        #plt.annotate(labels[i], xy = data[i])
        x = data[i, 0]
        y = data[i, 1]
        text = labels[i]
        TEXTS.append(ax.text(x, y, text, color=GREY30, fontsize=11, fontname="Poppins"))

    plt.grid('on')

    adjust_text(
            TEXTS, 
            expand_points=(1.5, 1.5),
            arrowprops=dict(
                arrowstyle="-", 
                color=GREY50, 
                lw=0
                ),
            ax=fig.axes[0]
            )
    ax.set_ylabel("")
    ax.set_yticklabels([])
    ax.set_xticklabels([])
    ax.spines["right"].set_color("none")
    ax.spines["left"].set_color("none")
    ax.spines["top"].set_color("none")
    ax.spines["bottom"].set_color("none")

    plt.show()

def plot_analogies(words):
    labels = words
    data = [w2v[w] for w in labels]
    plot_data_2d_2(data, labels)

def projection(base, vec):
    return base * np.dot(vec, base) / np.dot(base, base)

# project CD onto AB, then plot A, B, C, C+projection
def plot_projected(worda, wordb, wordc, wordd):
    base_vec = w2v[wordb] - w2v[worda]
    vec = w2v[wordd] - w2v[wordc]

    proj = projection(base_vec, vec)
    plot_data_1d(labels=[worda, wordb, wordc, wordd], orig_data=[w2v[worda], w2v[wordb], w2v[wordc], w2v[wordc] + proj])

def do_analogy(worda, wordb, wordc):
    return w2v.most_similar(negative=[worda], positive=[wordb, wordc])

def sort_list_by_gender(things):
    first_thing = things[0]
    other_things = things[1:]

    data = [w2v[first_thing]]
    labels = [first_thing]

    data.append(w2v['boy'])
    data.append(w2v['girl'])
    labels.append('boy')
    labels.append('girl')

    for thing in other_things:
        p = projection(BOYGIRL, w2v[thing] - w2v[first_thing])
        data.append(w2v[first_thing] + p)
        labels.append(thing)

    plot_data_2d_2(data, labels)

VOWELS=['a', 'e', 'i', 'o', 'u', 'y']
FRUITS = ['pear', 'cranberry', 'pomegranate', 'raspberry', 'blueberry', 'strawberry', 'peach']
BEATLES = ['paul', 'george', 'ringo', 'john']
CARDINAL_DIRECTIONS = ['north', 'east', 'south', 'west']
STUDIOS = ['disney', 'pixar', 'dreamworks']
SLANG = ['haha', 'huh', 'wtf', 'lolol']
NUMBERS = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
COMPOSERS=['mozart', 'bach', 'beethoven', 'debussy', 'schoenberg']
NEWS = ['foxnews', 'cnn', 'nbcnews', 'cbsnews', 'abcnews']

#plot_analogies(['boy', 'girl', 'huh', 'lolol', 'orgasm', 'orgasms'])
#plot_projected('boy', 'girl', 'huh', 'lolol')
#do_analogy('boy', 'girl', 'huh')

sort_list_by_gender(NEWS)

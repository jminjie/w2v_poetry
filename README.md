# Newly Gendered THings

This demo uses the pretrained Gensim Twitter Word2Vec model.
See [here](https://radimrehurek.com/gensim/auto_examples/tutorials/run_word2vec.html) for more info.

## Instructions
To run:
`python3 main.py`
Or run interactively:
```
python3 -i main.py
>>> sort_list_by_gender(['my', 'new', 'words'])
```

## Other graphs
To plot word embeddings in 2D
`>>> plot_analogies(['boy', 'girl', 'pants', 'leggings'])`

To plot projected/flattened word embeddings in 2D
`>>> plot_projected(['boy', 'girl', 'pants', 'leggings'])`

To do W2V analogies
`>>> do_analogy('boy', 'girl', 'pants')`

Note that certain claims regarding gendered analogies may not be completely
true. See [here](https://blog.esciencecenter.nl/king-man-woman-king-9a7fd2935a85?gi=65626e818925)
for more info

## GPU 0
## Lib Load
import os
import numpy as np
import heapq
from sentence_transformers import SentenceTransformer,util

# Select GPU
os.environ["CUDA_VISIBLE_DEVICES"] = "1"

# Load Model
m = SentenceTransformer("./text2vec/")

## Lib Embeddings
from Doclib.load_Filelist import filelist
fl,fnl = filelist()

# Embeddings Extraction
embed_list = []
for _fl in fnl:
    _embeddings = m.encode(_fl)
    embed_list.append(_embeddings)
    
# calculate similarity
def simlist(question):
    # input embedding
    input_embeddings = m.encode(question)
    
    # Simlarity Calculate
    cos_list = []
    for _embeddings in embed_list:
        _score = util.pytorch_cos_sim(input_embeddings, _embeddings)
        cos_list.append(float(_score))
        
    return(cos_list)

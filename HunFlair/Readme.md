## Bio-medical NER: HunFlair

This repo contains templates and documentation on using HunFlair for bio-medical and clinical ner

*HunFlair* is a state-of-the-art NER tagger for biomedical texts. This was trained over 24 biomedical NER data sets and can recognize 5 different entity types, i.e. cell lines, chemicals, disease, gene / proteins and species.

## Installation:
```
pip install flair

# ScispaCy is used for better pre-processing and tokenization
pip install scispacy==0.2.5

# For downloading models
# pip install <model_link_given_in_next_section>
pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.2.5/en_core_sci_sm-0.2.5.tar.gz
```

## Comparison to other biomedical NER tools
Tools for biomedical NER are typically trained and evaluated on rather small gold standard data sets. 
However, they are applied "in the wild" to a much larger collection of texts, often varying in 
topic, entity distribution, genre (e.g. patents vs. scientific articles) and text type (e.g. abstract 
vs. full text), which can lead to severe drops in performance.

*HunFlair* outperforms other biomedical NER tools on corpora not used for training of neither *HunFlair*
or any of the competitor tools.

| Corpus         | Entity Type  | Misc<sup><sub>[1](#f1)</sub></sup>   | SciSpaCy | HUNER | HunFlair | 
| ---            | ---          | ---    | ---   | ---  | ---         |
| [CRAFT v4.0](https://github.com/UCDenver-ccp/CRAFT)     | Chemical     | 42.88 | 35.73 | 42.99 | *__59.83__* |
|                | Gene/Protein | 64.93 | 47.76 | 50.77 | *__73.51__* |
|                | Species      | 81.15 | 54.21 | 84.45 | *__85.04__* |
| [BioNLP 2013 CG](https://www.aclweb.org/anthology/W13-2008/) | Chemical     | 72.15 | 58.43 | 67.37 | *__81.82__* |
|                | Disease      | 55.64 | 56.48 | 55.32 | *__65.07__* |
|                | Gene/Protein | 68.97 | 66.18 | 71.22 | *__87.71__* |
|                | Species      | *__80.53__* | 57.11 | 67.84 | 76.41 |
| [Plant-Disease](http://gcancer.org/pdr/)  | Species      | 80.63 | 75.90 | 73.64 | *__83.44__*  |

<sub>All results are F1 scores using partial matching of predicted text offsets with the original char offsets 
of the gold standard data. We allow a shift by max one character.</sub>

<sub><a name="f1">1</a>:  Misc displays the results of multiple taggers: 
[tmChem](https://www.ncbi.nlm.nih.gov/research/bionlp/Tools/tmchem/) for Chemical, 
[GNormPus](https://www.ncbi.nlm.nih.gov/research/bionlp/Tools/gnormplus/) for Gene and Species, and 
[DNorm](https://www.ncbi.nlm.nih.gov/CBBresearch/Lu/Demo/tmTools/DNorm.html) for Disease
</sub>

Here's how to [reproduce these numbers](https://github.com/MageshDominator/bio-medical-clinical-ner/tree/master/HunFlair/hunflair_from_scratch.py) using Flair. 
You can find detailed evaluations and discussions in [paper](https://arxiv.org/abs/2008.07347).

## Usage:
### [Tagger Usage](https://github.com/MageshDominator/bio-medical-clinical-ner/tree/master/HunFlair/flair_ner_usage.py)
* Template for using hunflair for BioMedical NER
* Extracting only required spans (diseases, cell-lines etc..)
* Extracting all types of spans at once (diseases, cell-lines, genes, species, and chemical entites)

### [Fine Tuning](https://github.com/MageshDominator/bio-medical-clinical-ner/tree/master/HunFlair/flair_ner_finetuning.py)
* Fine-tuning HunFlair on specific NER datasets
* Loads NCBI Disease datset from flair dataset then fine-tune HunFlair models
* Using this fine-tuning approach on other biomedical datasets will yield better results

### [Train HunFlair from Scratch](https://github.com/MageshDominator/bio-medical-clinical-ner/tree/master/HunFlair/flair_train_ner_single_corpus.py): On Single Corpus
* Template for Training HunFlair NER model on Single corpus

### [Train HunFlair from Scratch](https://github.com/MageshDominator/bio-medical-clinical-ner/tree/master/HunFlair/flair_train_ner_single_entity.py): Multiple Corpura for Single Entity
* Template for Training HunFlair NER model on Single Entity type(Ex: Cell line) with multiple corpura(HUNER_CELL_LINE).
* Distinct models can be trained for chemicals, diseases, genes/proteins and species using HUNER_CHEMICALS, HUNER_DISEASE, HUNER_GENE, HUNER_SPECIES respectively.

### [HunFlair Experimentation](https://github.com/MageshDominator/bio-medical-clinical-ner/tree/master/HunFlair/hunflair_from_scratch.py)
* Code used to reproduce results of [paper](https://arxiv.org/abs/2008.07347)

## References
* [Docs from Flair Repo](https://github.com/flairNLP/flair/blob/master/resources/docs/HUNFLAIR.md)
* [Hunflair Experiments repo](https://github.com/hu-ner/hunflair-experiments)

## Citation
~~~
@article{weber2020hunflair,
    title={HunFlair: An Easy-to-Use Tool for State-of-the-Art Biomedical Named Entity Recognition},
    author={Weber, Leon and S{\"a}nger, Mario and M{\"u}nchmeyer, Jannes  and Habibi, Maryam and Leser, Ulf and Akbik, Alan},
    journal={arXiv preprint arXiv:2008.07347},
    year={2020}
}
~~~
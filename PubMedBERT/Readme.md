## PubMedBERT
[PubMedBERT](https://arxiv.org/pdf/2007.15779.pdf) creates a new paradigm for building neural language models in biomedicine and specialized domains.

### Pre-training:
As in mainstream NLP, prior work on pretraining is largely concerned about newswires and the Web. For specialized domains like biomedicine, which has abundant text that is drastically different from general-domain corpora, this rationale no longer applies. PubMed contains over 30 million abstracts, and PubMed Central (PMC) contains millions of full-text articles. Still, the prevailing assumption is that out-domain text, in this case text not related to biomedicine, can be helpful, so prior work typically adopts a mixed-domain approach by starting from a general-domain language model.
Here is a comparison of mixed-domain pretraining and PubMedBERT pretraining:
![](https://github.com/MageshDominator/bio-medical-clinical-ner/blob/master/PubMedBERT/assets/pretraining.png)

One downside of the usual mixed-domain pretraining is that some bio medical terms will not be present in vocabulary. For example, lymphoma is represented as l, ##ym, ##ph, or ##oma. Acetyltransferase is reduced to ace, ##ty, ##lt, ##ran, ##sf, ##eras, or ##e. This will hurt the performance. 

**As you can see here in the below comparison where most of bio-medical terms are missing from previous SOTA models,**
![](https://github.com/MageshDominator/bio-medical-clinical-ner/blob/master/PubMedBERT/assets/vocab.png)

**Corpus Comparison:**
![](https://github.com/MageshDominator/bio-medical-clinical-ner/blob/master/PubMedBERT/assets/corpus_comparison.png)

### Biomedical Language Understanding and Reasoning Benchmark(BLURB):
Comprehensive benchmarks and leaderboards, such as GLUE, have greatly accelerated progress in general NLP. For biomedicine, however, such benchmarks and leaderboards are ostensibly absent. Prior work tends to use different tasks and datasets for downstream evaluation, which makes it hard to assess the true impact of biomedical pretraining strategies.

To address this problem, we have created the Biomedical Language Understanding and Reasoning Benchmark (BLURB) for PubMed-based biomedical NLP applications. BLURB consists of 13 publicly available datasets in six diverse tasks including: named entity recognition, evidence-based medical information extraction, relation extraction, sentence similarity, document classification, and question answering. To avoid placing undue emphasis on tasks with many available datasets, such as named entity recognition (NER), BLURB reports the macro average across all tasks as the main score.

**Benchmark datasets comparison:**
![](https://github.com/MageshDominator/bio-medical-clinical-ner/blob/master/PubMedBERT/assets/biomedical_dataset_comparison.png)

### Benchmarks:
PubMedBERT consistently outperforms all prior language models across biomedical NLP applications, often by a significant margin. The gains are most substantial against general-domain models. Most notably, while RoBERTa uses the largest pretraining corpus, its performance on biomedical NLP tasks is among the worst, similar to the original BERT model. Models using biomedical text in pretraining generally perform better. However, mixing out-domain text in pretraining generally leads to worse performance. In particular, even though clinical notes are more relevant to the biomedical domain than general-domain text, adding them does not confer any advantage, as evident by the results of ClinicalBERT and BlueBERT. Not surprisingly, BioBERT is the closest to PubMedBERT, as it also uses PubMed text for pretraining. However, by conducting domain-specific pretraining from scratch, PubMedBERT is able to obtain consistent gains over BioBERT in most tasks.
![](https://github.com/MageshDominator/bio-medical-clinical-ner/blob/master/PubMedBERT/assets/benchmark_comparison.png)
[Link](https://microsoft.github.io/BLURB/leaderboard.html) to leaderboard

### Models:
BLURB team has open-sourced 2 models:
* PubMedBERT(abstracts only)
* PubMedBERT (abstracts + full text)
[Link](https://microsoft.github.io/BLURB/models.html) to models page.

### Models Usage:
As the models are readily available in [transformers](https://huggingface.co/transformers/) library, You easily load them as shown below:
```
from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext")

model = AutoModel.from_pretrained("microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext")
```

### Reference
@misc{pubmedbert,
  author = {Yu Gu and Robert Tinn and Hao Cheng and Michael Lucas and Naoto Usuyama and Xiaodong Liu and Tristan Naumann and Jianfeng Gao and Hoifung Poon},
  title = {Domain-Specific Language Model Pretraining for Biomedical Natural Language Processing},
  year = {2020},
  eprint = {arXiv:2007.15779},
}
## Bio-medical and Clinical NER: sciSpacy

This repo contains templates and documentation on using sciSpacy for bio-medical and clinical ner

## Installation
```
pip install scispacy

# For downloading models
# pip install <model_link_given_in_next_section>
pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.2.5/en_core_sci_sm-0.2.5.tar.gz
```
## Available Models
| Model          | Description       | Install URL
|:---------------|:------------------|:----------|
| en_core_sci_sm | A full spaCy pipeline for biomedical data with a ~100k vocabulary. |[Download](https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.2.5/en_core_sci_sm-0.2.5.tar.gz)|
| en_core_sci_md |  A full spaCy pipeline for biomedical data with a ~360k vocabulary and 50k word vectors. |[Download](https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.2.5/en_core_sci_md-0.2.5.tar.gz)|
| en_core_sci_lg |  A full spaCy pipeline for biomedical data with a ~785k vocabulary and 600k word vectors. |[Download](https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.2.5/en_core_sci_lg-0.2.5.tar.gz)|
| en_ner_craft_md|  A spaCy NER model trained on the CRAFT corpus.|[Download](https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.2.5/en_ner_craft_md-0.2.5.tar.gz)|
| en_ner_jnlpba_md | A spaCy NER model trained on the JNLPBA corpus.| [Download](https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.2.5/en_ner_jnlpba_md-0.2.5.tar.gz)|
| en_ner_bc5cdr_md |  A spaCy NER model trained on the BC5CDR corpus. | [Download](https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.2.5/en_ner_bc5cdr_md-0.2.5.tar.gz)|
| en_ner_bionlp13cg_md |  A spaCy NER model trained on the BIONLP13CG corpus. |[Download](https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.2.5/en_ner_bionlp13cg_md-0.2.5.tar.gz)|

## Usage:
### [NER](https://github.com/MageshDominator/bio-medical-clinical-ner/tree/master/sciSpacy/run_ner.py)
* Template for loading scispacy models and perform inference

### [Abbrevation Detector](https://github.com/MageshDominator/bio-medical-clinical-ner/tree/master/sciSpacy/abbrevationDetector.py)
The AbbreviationDetector is a Spacy component which implements the abbreviation detection algorithm in "A simple algorithm for identifying abbreviation definitions in biomedical text.", (Schwartz & Hearst, 2003).
* Template for adding Abbrevation detector pipe and accessing abbrevation ouptut

### [Entity Linker](https://github.com/MageshDominator/bio-medical-clinical-ner/tree/master/sciSpacy/bioMedicalEntityLinker.py)
The EntityLinker is a SpaCy component which performs linking to a knowledge base. The linker simply performs a string overlap - based search (char-3grams) on named entities, comparing them with the concepts in a knowledge base using an approximate nearest neighbours search.

Currently (v2.5.0), there are 5 supported linkers:

- `umls`: Links to the [Unified Medical Language System](https://www.nlm.nih.gov/research/umls/index.html), levels 0,1,2 and 9. This has ~3M concepts.
- `mesh`: Links to the [Medical Subject Headings](https://www.nlm.nih.gov/mesh/meshhome.html). This contains a smaller set of higher quality entities, which are used for indexing in Pubmed. MeSH contains ~30k entities. NOTE: The MeSH KB is derrived directly from MeSH itself, and as such uses different unique identifiers than the other KBs.
- `rxnorm`: Links to the [RxNorm](https://www.nlm.nih.gov/research/umls/rxnorm/index.html) ontology. RxNorm contains ~100k concepts focused on normalized names for clinical drugs. It is comprised of several other drug vocabularies commonly used in pharmacy management and drug interaction, including First Databank, Micromedex, and the Gold Standard Drug Database.
- `go`: Links to the [Gene Ontology](http://geneontology.org/). The Gene Ontology contains ~67k concepts focused on the functions of genes.
- `hpo`: Links to the [Human Phenotype Ontology](https://hpo.jax.org/app/). The Human Phenotype Ontology contains 16k concepts focused on phenotypic abnormalities encountered in human disease.

You may want to play around with some of the parameters
below to adapt to your use case (higher precision, higher recall etc).

- `resolve_abbreviations : bool = True, optional (default = False)`
    Whether to resolve abbreviations identified in the Doc before performing linking.
    This parameter has no effect if there is no `AbbreviationDetector` in the spacy
    pipeline.
- `k : int, optional, (default = 30)`
    The number of nearest neighbours to look up from the candidate generator per mention.
- `threshold : float, optional, (default = 0.7)`
    The threshold that a mention candidate must reach to be added to the mention in the Doc
    as a mention candidate.
-   `no_definition_threshold : float, optional, (default = 0.95)`
        The threshold that a entity candidate must reach to be added to the mention in the Doc
        as a mention candidate if the entity candidate does not have a definition.
- `filter_for_definitions: bool, default = True`
    Whether to filter entities that can be returned to only include those with definitions
    in the knowledge base.
- `max_entities_per_mention : int, optional, default = 5`
    The maximum number of entities which will be returned for a given mention, regardless of
    how many are nearest neighbours are found.

This class sets the `._.kb_ents` attribute on spacy Spans, which consists of a
List[Tuple[str, float]] corresponding to the KB concept_id and the associated score
for a list of `max_entities_per_mention` number of entities.

You can look up more information for a given id using the kb attribute of this class:
```
print(linker.kb.cui_to_entity[concept_id])
```

## Citation
@inproceedings{neumann-etal-2019-scispacy,
    title = "{S}cispa{C}y: {F}ast and {R}obust {M}odels for {B}iomedical {N}atural {L}anguage {P}rocessing",
    author = "Neumann, Mark  and
      King, Daniel  and
      Beltagy, Iz  and
      Ammar, Waleed",
    booktitle = "Proceedings of the 18th BioNLP Workshop and Shared Task",
    month = aug,
    year = "2019",
    address = "Florence, Italy",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/W19-5034",
    doi = "10.18653/v1/W19-5034",
    pages = "319--327",
    eprint = {arXiv:1902.07669},
    abstract = "Despite recent advances in natural language processing, many statistical models for processing text perform extremely poorly under domain shift. Processing biomedical and clinical text is a critically important application area of natural language processing, for which there are few robust, practical, publicly available models. This paper describes scispaCy, a new Python library and models for practical biomedical/scientific text processing, which heavily leverages the spaCy library. We detail the performance of two packages of models released in scispaCy and demonstrate their robustness on several tasks and datasets. Models and code are available at https://allenai.github.io/scispacy/.",
}

ScispaCy is an open-source project developed by the Allen Institute for Artificial Intelligence (AI2). AI2 is a non-profit institute with the mission to contribute to humanity through high-impact AI research and engineering.

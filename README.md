# 19-20MetaPNC
***Metadata-enriched Polish Novel Corpus from the 19th and 20th centuries***

The corpus consists of 1,000 novels originally written in Polish and initially published as books between 1864 and 1939, with the plot timeframe set after 1815. The current version is v1.0.1. 

Following Linked Open Data (LOD) standards, we do not publish the corpus texts in .txt format. Instead, the entire corpus is accessible through a knowledge graph in .ttl format, with each text being linked separately. The following sections include a tutorial and code explanation to assist in downloading all the corpus texts independently.

## Contributors

- Marek Kubis, Adam Mickiewicz University in Poznan
- Cezary Rosiński, Patryk Hubar, Institute of Literary Research of the Polish Academy of Sciences
- Agnieszka Karlińska, NASK National Research Institute
- Jan Wieczorek, Wroclaw University of Science and Technology

## Corpus design

The collected texts come from different sources. 
The initial set consisted of 100 novels from the [Polish ELTeC subcorpus](https://distantreading.github.io/ELTeC/pol/index.html), encoded in TEI format. 
Subsequently, an additional 193 texts from the [Wolne Lektury](https://wolnelektury.pl/) library were added. The Wolne Lektury data is accessible in a custom XML format that preserves paragraph boundary information. 
Next, 225 novels from the Polish edition of the [Wikisource](https://pl.wikisource.org/wiki/Wiki%C5%BAr%C3%B3d%C5%82a:Strona_g%C5%82%C3%B3wna) project were included, encoded in MediaWiki format and proofread by Wikisource editors. 
The [Polona](https://polona.pl) digital library, maintained by the National Library of Poland, served as the final source of texts. It provides scans of printed books along with the OCR-derived textual layer. Approx. 6,000 digitized volumes were retrieved from Polona, which, after merging multi-volume editions of novels, resulted in a total of 4,808 texts.

Exactly one edition of each novel was selected from the 5,326 pieces of literary fiction that made up the original dataset. Texts that were not novels, that were written before or after the selected period, and that were set before 1815 were rejected. Duplicates were also identified and removed, resulting in a database of 1,707 unique novels. 

### Balancing criteria:

As it was not possible to maintain equal proportions between classes, we determined the minimum and maximum share of a particular text class in the corpus. 
1. Date: three literary eras distinguished in Polish literary studies determined by the date of first publication (>= 20% each)
   - Positivism (1864–1890)
   - Young Poland (1890–1918)
   - the Interwar Period (1918–1939)
2. Gender: female author 10%–50%
3. Place of publication (three partitions): >=15% each
4. Level of reception:
   - no more than 2 reprints >= 30%
   - more than 2 reprints >= 30%

We obtained the following proportions of titles for each balance criterion:

<p align="center">
  <img src="balancing_criteria.jpg" alt="Balancing criteria" width="65%">
</p>

### Metadata (PH)
#### Classes

- Corpus
- Text
- Place
- Partition
- Epoch
#### Classes attributes
#### Classes relations
#### Examples
```turtle
tco:metapnc_e_1572 a dcterms:PeriodOfTime ;
    rdfs:label "Interwar period" ;
    tco:isEpoch true ;
    owl:sameAs <https://www.wikidata.org/wiki/Q11761904> .

tco:metapnc_p_1100 a foaf:Person ;
    rdfs:label "Jezierski, Edmund" ;
    schema:birthPlace tco:metapnc_g_1418 ;
    owl:sameAs <http://www.wikidata.org/entity/Q21288157> ;
    foaf:gender "male" .

tco:metapnc_g_1418 a dcterms:Location ;
    rdfs:label "Warsaw" ;
    tco:inPartition tco:metapnc_z_1571 ;
    owl:sameAs <http://www.wikidata.org/entity/Q270>,
        <https://www.geonames.org/756135> ;
    geo:lat "52.22977"^^xsd:float ;
    geo:long "21.01178"^^xsd:float .

tco:metapnc_z_1571 a dcterms:Location ;
    rdfs:label "Russian Partition" ;
    tco:isPartition true ;
    owl:sameAs <https://www.wikidata.org/wiki/Q129797> .

tco:metapnc_b_246 a tco:Text,
        dcterms:BibliographicResource ;
    tco:inEpoch tco:metapnc_e_1572 ;
    tco:numberOfReissues 1 ;
    tco:numberOfTokens 76607 ;
    dcterms:creator tco:metapnc_p_1100 ;
    dcterms:date "1925"^^xsd:year ;
    dcterms:subject "Plot after the Congress of Vienna" ;
    dcterms:title "Wyspa Lenina" ;
    fabio:hasPlaceOfPublication tco:metapnc_g_1418 ;
    schema:contentUrl <https://polona2.pl/archive?uid=84911046&cid=87260474> ;
    schema:genre "Novel" ;
    owl:sameAs <http://polona.pl/item/84911046> .
```
  
#### Ontology (PH)
- ontology description
- ontology visualization
![](TCO_ontology.jpg)

## Corpus manual (MK)
- code explanation

## Licence

The knowledge graph and code in the repository are made available under a Creative Commons Attribution International 4.0 licence [(CC BY)](https://creativecommons.org/licenses/by/4.0/).
The texts in the corpus are in the public domain. Detailed information about the licences can be found at the following links:

- [Polona](https://polona.pl/static/polona/22d8f8e5-078f-41f1-93ed-daceb2ef98c7)
- [Wolne Lektury](https://wolnelektury.pl/info/zasady-wykorzystania/)
- [Wikisource](https://foundation.wikimedia.org/wiki/Policy:Terms_of_Use/pl)

## Citation

Agnieszka Karlińska, Cezary Rosiński, Jan Wieczorek, Patryk Hubar, Jan Kocoń, Marek Kubis, Stanisław Woźniak, Arkadiusz Margraf, and Wiktor Walentynowicz. 2022. [Towards a contextualised spatial-diachronic history of literature: mapping emotional representations of the city and the country in Polish fiction from 1864 to 1939](https://aclanthology.org/2022.latechclfl-1.14). In *Proceedings of the 6th Joint SIGHUM Workshop on Computational Linguistics for Cultural Heritage, Social Sciences, Humanities and Literature*, pages 115–125, Gyeongju, Republic of Korea. International Conference on Computational Linguistics.

```
@inproceedings{karlinska-etal-2022-towards,
    title = "Towards a contextualised spatial-diachronic history of literature: mapping emotional representations of the city and the country in {P}olish fiction from 1864 to 1939",
    author = "Karli{\'n}ska, Agnieszka  and
      Rosi{\'n}ski, Cezary  and
      Wieczorek, Jan  and
      Hubar, Patryk  and
      Koco{\'n}, Jan  and
      Kubis, Marek  and
      Wo{\'z}niak, Stanis{\l}aw  and
      Margraf, Arkadiusz  and
      Walentynowicz, Wiktor",
    booktitle = "Proceedings of the 6th Joint SIGHUM Workshop on Computational Linguistics for Cultural Heritage, Social Sciences, Humanities and Literature",
    month = oct,
    year = "2022",
    address = "Gyeongju, Republic of Korea",
    publisher = "International Conference on Computational Linguistics",
    url = "https://aclanthology.org/2022.latechclfl-1.14",
    pages = "115--125",
    }
```
---
![](authors_institutions.jpg)

# 19-20MetaPNC
***Metadata-enriched Polish Novel Corpus from the 19th and 20th centuries***

The corpus consists of 1,000 novels originally written in Polish and initially published as books between 1864 and 1939, featuring a plot timeframe set after 1815. The current version is v1.0.1.

## Contributors

- Marek Kubis, Adam Mickiewicz University in Poznan
- Cezary Rosiński, Patryk Hubar, Institute of Literary Research of the Polish Academy of Sciences
- Agnieszka Karlińska, NASK National Research Institute
- Jan Wieczorek, Wroclaw University of Science and Technology

## Corpus design

The collected texts come from different sources. The initial set consisted of 100 novels from the [Polish ELTeC subcorpus]([https://zenodo.org/record/4662725](https://distantreading.github.io/ELTeC/pol/index.html), encoded in TEI format. Subsequently, an additional 193 texts from the Wolne Lektury library were added. The Wolne Lektury data is accessible in a custom XML format that preserves paragraph boundary information. Next, 225 novels from the Polish edition of the Wikisource project were included, encoded in MediaWiki format and proofread by Wikisource editors. The Polona digital library, maintained by the National Library of Poland, served as the final source of texts. It provides scans of printed books along with the OCR-derived textual layer. Approx. 6,000 digitized volumes were retrieved from Polona, which, after merging multi-volume editions of novels, resulted in a total of 4,808 texts.

![](meta_belka.jpg)

Exactly one edition of each novel was selected from the 5,326 pieces of literary fiction that made up the original dataset. Texts that were not novels, that were written before or after the selected period, and that were set before 1815 were rejected. Duplicates were also identified and removed, resulting in a database of 1,707 unique novels. Measures were then taken to balance the corpus. 

### Balancing criteria:
1. Date: three literary eras distinguished in Polish literary studies determined by the date of first publication (>= 20% each)
   - Positivism (1864–1890)
   - Young Poland (1890–1918)
   - the Interwar Period (1918–1939)
2. Gender: female author 10%–50%
3. Place of publication (three partitions): >=15% each
4. Level of reception:
   - no more than 2 reprints >= 30%
   - more than 2 reprints >= 30%

The balanced corpus consists of 1,000 novels. 

### Metadata
xxxxxxx

## Licence
All texts in this collection are in the public domain.
xxxxxxx

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

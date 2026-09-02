# TNBC Chemoresistance Gene Analysis

Sequence-level GC content and nucleotide composition analysis of five TNBC chemoresistance genes, compared against a 15-gene baseline.

## Motivation

BCL2, EGFR, TP53, MYC, and ABCB1 recur throughout TNBC chemoresistance literature as key drivers of chemoresistance, but always at the protein or pathway level. This project set out to test a narrower, sequence-level question: do these five genes show unusually high GC content compared to typical human genes?

The initial assumption was that high GC content indicates a CpG island especially near gene's promoter region. While CpG islands matter because they're prone to methylation, a known mechanism of gene silencing in cancer. If these five genes showed unusually high GC content, that seemed like it could point toward CpG-island-driven regulation as part of why they're prone to dysregulation in TNBC.

This assumption was imprecise. GC content and CpG islands are not equivalent. A CpG island is a short, localized region, typically 200 bp to a few kb with GC content above 50% and a high CpG observed/expected ratio, usually located at or near a gene's promoter region (Deaton & Bird, 2011). It is a property of a small region within a gene, not of the gene's overall sequence. A gene can have entirely unremarkable whole-sequence GC content while still carrying a CpG island in its promoter.

Whole-gene GC% was still measured because it is the simplest, cheapest compositional feature to extract from a sequence and a legitimate first step before attempting a more targeted, computationally heavier test. An unusual result at this coarse level would have been a signal worth following up with a direct CpG island test. Its absence doesn't confirm or rule out CpG islands in these genes; it simply means the answer isn't visible at this resolution.

## Genes Analysed

**TNBC chemoresistance genes (5):** BCL2, EGFR, TP53, MYC, ABCB1

**Baseline set (15):** PGK1, TPI1, ATP5A1, TUBB, PFN1, RPL8, RPS6, HSPA8, HSPA5, SOD1, YWHAE, YWHAB, RAN, PSMA1, VCP

Baseline genes are sourced from Eisenberg & Levanon (2013), the standard reference for human housekeeping genes, chosen to span functionally diverse categories across metabolism, ribosomal machinery, cytoskeleton, chaperones, signaling, protein degradation, oxidative stress, nuclear transport. So the baseline isn't biased toward one cellular process, since the five target genes themselves span different biological roles.

## Methods

1. Downloaded RefSeq mRNA FASTA sequences for all 20 genes from NCBI
2. Parsed sequences with Biopython (`SeqIO`)
3. Computed GC content and nucleotide composition (A/T/G/C counts) using my custom functions (`GC_content()`, `count_nucleotide()`)
4. Combined both gene sets into a single DataFrame with a `group` column
5. Compared each TNBC gene individually against the baseline distribution (mean, standard deviation, range), rather than relying on group averages alone, since averaging can obscure individual variation in a sample this small
6. Visualised the comparison as a color-coded bar chart with a ±1 SD reference band marking the baseline's normal range

**Pipeline:** NCBI → Biopython (SeqIO) → custom functions → Pandas → Matplotlib

## Results

- Baseline GC% - mean: 47.26%, std: 6.31%, range: 40.18%–60.47%
- All five TNBC genes fell within ±1 SD of the baseline mean (z-scores: -0.95 to +0.97)
- No unusual whole-sequence GC bias detected in any of the five genes

![GC content comparison](gc_content_comparison.png)

## Interpretation

Whole-gene GC% cannot confirm or rule out CpG island presence, since a CpG island is a localized promoter-region feature that whole-gene averaging cannot resolve. The result shows that these five genes are not compositionally unusual at the whole-sequence level but it does not show whether their promoters carry CpG islands.

Testing that directly would require computing the CpG observed/expected ratio within a defined window across each gene's promoter region specifically, following the Gardiner-Garden & Frommer criteria (length ≥200 bp, GC% >50%, CpG obs/exp ratio ≥0.6)
not attempted in this analysis.

## Limitations

- Whole-gene GC% is a coarse compositional screen, not a CpG island test
- Sample size (5 target genes, 15 baseline genes) supports descriptive, individual-gene comparison but not formal statistical significance testing

## References

- Eisenberg, E., & Levanon, E. Y. (2013). Human housekeeping genes, revisited. *Trends in Genetics*, 29(10), 569–574.
- Deaton, A. M., & Bird, A. (2011). CpG islands and the regulation of transcription. *Genes & Development*, 25(10), 1010–1022.
- Esteller, M. (2007). Epigenetic gene silencing in cancer: the DNA hypermethylome. *Human Molecular Genetics*, 16(R1), R50–R59.

## Files

- `Project2.py` - main analysis script
- `gc_content_comparison.png` - final visualisation
- `*.fasta` - downloaded gene sequences (20 files)
- `dna_function.py` - custom functions (from Project 1)
- `requirements.txt` - dependencies

## How to Run

```bash
pip install biopython pandas matplotlib
python Project2.py
```

## Author

Chhavi Chandra - B.Sc. Biochemistry Honours, Adamas University
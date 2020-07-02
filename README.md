# VBS-customNanoAODProduction

### Recipe for SM EWK and QCD production

```bash
cmsrel CMSSW_10_2_18
git cms-init
git cms-merge-topic singh-ramanpreet:patch-lheHeader-10_2_18
git clone git@github.com:singh-ramanpreet/VBS-customNanoAODProduction.git VBSAnalysis
scram b
cd VBSAnalysis/NanoAODProduction/test
./make_config.sh
```

#### Submitting to condor
Edit the file `submit.py`, mainly few starting variables. Then,
```
python submit.py
```

## Stored Weight Indices

### 2016 SM EWK and QCD


1. LHEScaleWeight

central variation: `LHEScaleWeight[20]`

6 variations (muf, mur): 
```
{(0.5, 0.5), (0.5, 1), (1, 0.5), (1, 2), (2, 1), (2, 2)}
{0, 5, 15, 25, 35, 40}
```

Full table for more info:

| Index |  ID in header  |  mur  |  muf  |  dyn                    |
| ----- | -------------- | ----- | ----- | ----------------------- |
|  0    | 1041           |  0.50 | 0.50  |                         |
|  1-4  | 1042 - 1045    |  0.50 | 0.50  | sum pt, HT, HT/2, sqrts |
|  5    | 1011           |  0.50 | 1.00  |                         |
|  6-9  | 1012 - 1015    |  0.50 | 1.00  | sum pt, HT, HT/2, sqrts |
| 10    | 1026           |  0.50 | 2.00  |                         |
| 11-14 | 1027 - 1030    |  0.50 | 2.00  | sum pt, HT, HT/2, sqrts |
| 15    | 1031           |  1.00 | 0.50  |                         |
| 16-19 | 1032 - 1035    |  1.00 | 0.50  | sum pt, HT, HT/2, sqrts |
| 20    | 1001           |  1.00 | 1.00  |                         |
| 21-24 | 1002 - 1005    |  1.00 | 1.00  | sum pt, HT, HT/2, sqrts |
| 25    | 1016           |  1.00 | 2.00  |                         |
| 26-29 | 1017 - 1020    |  1.00 | 2.00  | sum pt, HT, HT/2, sqrts |
| 30    | 1036           |  2.00 | 0.50  |                         |
| 31-34 | 1037 - 1040    |  2.00 | 0.50  | sum pt, HT, HT/2, sqrts |
| 35    | 1006           |  2.00 | 1.00  |                         |
| 36-39 | 1007 - 1010    |  2.00 | 1.00  | sum pt, HT, HT/2, sqrts |
| 40    | 1021           |  2.00 | 2.00  |                         |
| 41-44 | 1022 - 1025    |  2.00 | 2.00  | sum pt, HT, HT/2, sqrts |

2. LHEPdfWeight

[More Info on PDF sets](https://lhapdf.hepforge.org/pdfsets.html)

Pdf name: `NNPDF31_nnlo_as_0118_mc_hessian_pdfas`

central variation: `LHEPdfWeight[0]`

variations: `LHEPdfWeight[1]` to `LHEPdfWeight[100]`

$\alpha_s$ variations: `LHEPdfWeight[101]` (0.116) and `LHEPdfWeight[102]` (0.120)


### 2017/2018 SM EWK and QCD

1. LHEScaleWeight

central variation: `LHEScaleWeight[4]`

6 variations (muf, mur): 
```
{(0.5, 0.5), (0.5, 1), (1, 0.5), (1, 2), (2, 1), (2, 2)}
{0, 1, 3, 5, 7, 8}
```

Full table for more info:

| Index |  ID in header  |  mur  |  muf  |
| ----- | -------------- | ----- | ----- |
|  0    | 9              | 0.50  | 0.50  |
|  1    | 7              | 0.50  | 1.00  |
|  2    | 8              | 0.50  | 2.00  |
|  3    | 3              | 1.00  | 0.50  |
|  4    | 1              | 1.00  | 1.00  |
|  5    | 2              | 1.00  | 2.00  |
|  6    | 6              | 2.00  | 0.50  |
|  7    | 4              | 2.00  | 1.00  |
|  8    | 5              | 2.00  | 2.00  |

2. LHEPdfWeight

Pdf name: `NNPDF31_nnlo_hessian_pdfas`

->everything else same as 2016


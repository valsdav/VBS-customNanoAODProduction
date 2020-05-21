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

#!/bin/bash

#cmsDriver.py nano_production_mc_2016_old -s NANO --mc --eventcontent NANOAODSIM --datatier NANOAODSIM --no_exec --conditions 102X_mcRun2_asymptotic_v7 --era Run2_2016,run2_miniAOD_80XLegacy \
#-n 10 \
#--filein  \
#--fileout nano.root \
#--customise_commands="process.add_(cms.Service('InitRootHandlers', EnableIMT = cms.untracked.bool(False)))\n\
#process.genWeightsTable.debug = cms.untracked.bool(True)\n\
#process.genWeightsTable.missingLHEHeaderFile = cms.FileInPath('VBSAnalysis/NanoAODProduction/data/')\n\
#process.genWeightsTable.preferredPDFs = cms.VPSet(cms.PSet( name = cms.string(''), lhaid = cms.uint32()))"

cmsDriver.py nano_production_mc_aqgc_2016 -s NANO --mc --eventcontent NANOAODSIM --datatier NANOAODSIM --no_exec --conditions 102X_mcRun2_asymptotic_v7 --era  Run2_2016,run2_nanoAOD_94X2016 \
-n 10 \
--filein /store/mc/RunIISummer16MiniAODv3/WplusTo2LZTo2JJJ_EWK_LO_aQGC_MJJ100PTJ10_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/280000/F6C40845-7F18-EA11-AB34-248A07C6D770.root \
--fileout nano.root \
--customise_commands="process.add_(cms.Service('InitRootHandlers', EnableIMT = cms.untracked.bool(False)))\n\
process.genWeightsTable.debug = cms.untracked.bool(True)\n\
process.genWeightsTable.missingLHEHeaderFile = cms.FileInPath('VBSAnalysis/NanoAODProduction/data/initrwgt_aQGC16.header')\n\
process.genWeightsTable.preferredPDFs = cms.VPSet(cms.PSet( name = cms.string('NNPDF30_nlo_nf_4_pdfas'), lhaid = cms.uint32(292000)))"


cmsDriver.py nano_production_mc_aqgc_2017 -s NANO --mc --eventcontent NANOAODSIM --datatier NANOAODSIM --no_exec --conditions 102X_mc2017_realistic_v7 --era Run2_2017,run2_nanoAOD_94XMiniAODv2 \
-n 10 \
--filein /store/mc/RunIIFall17MiniAODv2/WplusTo2LZTo2JJJ_EWK_LO_aQGC_MJJ100PTJ10_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/130000/FAD814B3-63CA-E911-B0D2-0025902D1212.root \
--fileout nano.root \
--customise_commands="process.add_(cms.Service('InitRootHandlers', EnableIMT = cms.untracked.bool(False)))\n\
process.genWeightsTable.debug = cms.untracked.bool(True)\n\
process.genWeightsTable.missingLHEHeaderFile = cms.FileInPath('VBSAnalysis/NanoAODProduction/data/initrwgt_aQGC17.header')\n\
process.genWeightsTable.preferredPDFs = cms.VPSet(cms.PSet( name = cms.string('NNPDF31_nnlo_as_0118_nf_4'), lhaid = cms.uint32(320900)))" 


cmsDriver.py nano_production_mc_aqgc_2018 -s NANO --mc --eventcontent NANOAODSIM --datatier NANOAODSIM --no_exec --conditions 102X_upgrade2018_realistic_v20 --era Run2_2018,run2_nanoAOD_102Xv1 \
-n 10 \
--filein root://cmsxrootd.fnal.gov//store/mc/RunIIAutumn18MiniAOD/WplusTo2LZTo2JJJ_EWK_LO_aQGC_MJJ100PTJ10_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/FD135E01-1001-8046-9F39-A7CBF3757E57.root \
--fileout nano.root \
--customise_commands="process.add_(cms.Service('InitRootHandlers', EnableIMT = cms.untracked.bool(False)))\n\
process.genWeightsTable.debug = cms.untracked.bool(True)\n\
process.genWeightsTable.missingLHEHeaderFile = cms.FileInPath('VBSAnalysis/NanoAODProduction/data/initrwgt_aQGC17.header')\n\
process.genWeightsTable.preferredPDFs = cms.VPSet(cms.PSet( name = cms.string('NNPDF31_nnlo_as_0118_nf_4'), lhaid = cms.uint32(320900)))" 

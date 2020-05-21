#!/bin/bash

cmsDriver.py nano_production_mc_2017 -s NANO --mc --eventcontent NANOAODSIM --datatier NANOAODSIM --no_exec --conditions 102X_mc2017_realistic_v7 --era Run2_2017,run2_nanoAOD_94XMiniAODv2 \
-n -1 \
--filein /store/mc/RunIIFall17MiniAODv2/WplusToLNuWminusTo2JJJ_QCD_LO_SM_MJJ100PTJ10_TuneCP5_13TeV/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/E89EAA26-B138-E911-A09A-0CC47A0093EC.root \
--fileout nano.root \
--customise_commands="process.add_(cms.Service('InitRootHandlers', EnableIMT = cms.untracked.bool(False)))\n\
process.genWeightsTable.debug = cms.untracked.bool(True)\n\
process.genWeightsTable.missingLHEHeaderFile = cms.FileInPath('VBSAnalysis/NanoAODProduction/data/initrwgt17.header')\n\
process.genWeightsTable.preferredPDFs = cms.VPSet(cms.PSet( name = cms.string('NNPDF31_nnlo_hessian_pdfas'), lhaid = cms.uint32(306000)))" 


cmsDriver.py nano_production_mc_2018 -s NANO --mc --eventcontent NANOAODSIM --datatier NANOAODSIM --no_exec --conditions 102X_upgrade2018_realistic_v20 --era Run2_2018,run2_nanoAOD_102Xv1 \
-n -1 \
--filein /store/mc/RunIIAutumn18MiniAOD/WplusToLNuZTo2JJJ_QCD_LO_SM_MJJ100PTJ10_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/F0048AF8-C693-B844-8EEE-46426918C7DE.root \
--fileout nano.root \
--customise_commands="process.add_(cms.Service('InitRootHandlers', EnableIMT = cms.untracked.bool(False)))\n\
process.genWeightsTable.debug = cms.untracked.bool(True)\n\
process.genWeightsTable.missingLHEHeaderFile = cms.FileInPath('VBSAnalysis/NanoAODProduction/data/initrwgt17.header')\n\
process.genWeightsTable.preferredPDFs = cms.VPSet(cms.PSet( name = cms.string('NNPDF31_nnlo_hessian_pdfas'), lhaid = cms.uint32(306000)))" 

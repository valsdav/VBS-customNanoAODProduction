#!/bin/bash
# NanoV7 config: https://gitlab.cern.ch/cms-nanoAOD/nanoaod-doc/-/wikis/Releases/NanoAODv7

cmsDriver.py nano_production_mc_2016 -s NANO --mc --eventcontent NANOAODSIM --datatier NANOAODSIM --no_exec --conditions 102X_mcRun2_asymptotic_v8 --era  Run2_2016,run2_nanoAOD_94X2016 \
-n 10 \
--filein /store/mc/RunIISummer16MiniAODv3/ZTo2LZTo2JJJ_EWK_LO_SM_MJJ100PTJ10_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/100000/F683D5FF-FAAA-EA11-AB2D-0CC47A7C347E.root \
--fileout nano.root \
--customise_commands="process.add_(cms.Service('InitRootHandlers', EnableIMT = cms.untracked.bool(False)))\n\
process.genWeightsTable.debug = cms.untracked.bool(True)\n\
process.genWeightsTable.missingLHEHeaderFile = cms.FileInPath('VBSAnalysis/NanoAODProduction/data/initrwgt16.header')\n\
process.genWeightsTable.preferredPDFs = cms.VPSet(cms.PSet( name = cms.string('NNPDF31_nnlo_as_0118_mc_hessian_pdfas'), lhaid = cms.uint32(325300)))"


cmsDriver.py nano_production_mc_2017 -s NANO --mc --eventcontent NANOAODSIM --datatier NANOAODSIM --no_exec --conditions 102X_mc2017_realistic_v8 --era Run2_2017,run2_nanoAOD_94XMiniAODv2 \
-n -1 \
--filein /store/mc/RunIIFall17MiniAODv2/WplusToLNuWminusTo2JJJ_QCD_LO_SM_MJJ100PTJ10_TuneCP5_13TeV/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/E89EAA26-B138-E911-A09A-0CC47A0093EC.root \
--fileout nano.root \
--customise_commands="process.add_(cms.Service('InitRootHandlers', EnableIMT = cms.untracked.bool(False)))\n\
process.genWeightsTable.debug = cms.untracked.bool(True)\n\
process.genWeightsTable.missingLHEHeaderFile = cms.FileInPath('VBSAnalysis/NanoAODProduction/data/initrwgt17.header')\n\
process.genWeightsTable.preferredPDFs = cms.VPSet(cms.PSet( name = cms.string('NNPDF31_nnlo_hessian_pdfas'), lhaid = cms.uint32(306000)))" 


cmsDriver.py nano_production_mc_2018 -s NANO --mc --eventcontent NANOAODSIM --datatier NANOAODSIM --no_exec --conditions 102X_upgrade2018_realistic_v21 --era Run2_2018,run2_nanoAOD_102Xv1 \
-n -1 \
--filein /store/mc/RunIIAutumn18MiniAOD/WplusToLNuZTo2JJJ_QCD_LO_SM_MJJ100PTJ10_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/F0048AF8-C693-B844-8EEE-46426918C7DE.root \
--fileout nano.root \
--customise_commands="process.add_(cms.Service('InitRootHandlers', EnableIMT = cms.untracked.bool(False)))\n\
process.genWeightsTable.debug = cms.untracked.bool(True)\n\
process.genWeightsTable.missingLHEHeaderFile = cms.FileInPath('VBSAnalysis/NanoAODProduction/data/initrwgt17.header')\n\
process.genWeightsTable.preferredPDFs = cms.VPSet(cms.PSet( name = cms.string('NNPDF31_nnlo_hessian_pdfas'), lhaid = cms.uint32(306000)))" 

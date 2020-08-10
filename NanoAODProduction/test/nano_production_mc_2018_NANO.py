# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: nano_production_mc_2018 -s NANO --mc --eventcontent NANOAODSIM --datatier NANOAODSIM --no_exec --conditions 102X_upgrade2018_realistic_v21 --era Run2_2018,run2_nanoAOD_102Xv1 -n -1 --filein /store/mc/RunIIAutumn18MiniAOD/WplusToLNuZTo2JJJ_QCD_LO_SM_MJJ100PTJ10_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/F0048AF8-C693-B844-8EEE-46426918C7DE.root --fileout nano.root --customise_commands=process.add_(cms.Service('InitRootHandlers', EnableIMT = cms.untracked.bool(False)))\nprocess.genWeightsTable.debug = cms.untracked.bool(True)\nprocess.genWeightsTable.missingLHEHeaderFile = cms.FileInPath('VBSAnalysis/NanoAODProduction/data/initrwgt17.header')\nprocess.genWeightsTable.preferredPDFs = cms.VPSet(cms.PSet( name = cms.string('NNPDF31_nnlo_hessian_pdfas'), lhaid = cms.uint32(306000)))
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('NANO',eras.Run2_2018,eras.run2_nanoAOD_102Xv1)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('PhysicsTools.NanoAOD.nano_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('/store/mc/RunIIAutumn18MiniAOD/WplusToLNuZTo2JJJ_QCD_LO_SM_MJJ100PTJ10_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/90000/F0048AF8-C693-B844-8EEE-46426918C7DE.root'),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('nano_production_mc_2018 nevts:-1'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.NANOAODSIMoutput = cms.OutputModule("NanoAODOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(9),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('NANOAODSIM'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('nano.root'),
    outputCommands = process.NANOAODSIMEventContent.outputCommands
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '102X_upgrade2018_realistic_v21', '')

# Path and EndPath definitions
process.nanoAOD_step = cms.Path(process.nanoSequenceMC)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.NANOAODSIMoutput_step = cms.EndPath(process.NANOAODSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.nanoAOD_step,process.endjob_step,process.NANOAODSIMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.

# Automatic addition of the customisation function from PhysicsTools.NanoAOD.nano_cff
from PhysicsTools.NanoAOD.nano_cff import nanoAOD_customizeMC 

#call to customisation function nanoAOD_customizeMC imported from PhysicsTools.NanoAOD.nano_cff
process = nanoAOD_customizeMC(process)

# End of customisation functions

# Customisation from command line

process.add_(cms.Service('InitRootHandlers', EnableIMT = cms.untracked.bool(False)))
process.genWeightsTable.debug = cms.untracked.bool(True)
process.genWeightsTable.missingLHEHeaderFile = cms.FileInPath('VBSAnalysis/NanoAODProduction/data/initrwgt17.header')
process.genWeightsTable.preferredPDFs = cms.VPSet(cms.PSet( name = cms.string('NNPDF31_nnlo_hessian_pdfas'), lhaid = cms.uint32(306000)))
# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion

from CRABClient.UserUtilities import config, getUsernameFromCRIC

samples_list = 'samples2016.txt'
#samples_list = 'samples2017.txt'
#samples_list = 'samples2018.txt'
pset_file = 'nano_production_mc_2016_NANO.py'
#pset_file = 'nano_production_mc_2017_NANO.py'
#pset_file = 'nano_production_mc_2018_NANO.py'
out_dataset_tag = 'VVjj_2016v6'
#out_dataset_tag = 'VVjj_2017v6'
#out_dataset_tag = 'VVjj_2018v6'
storage_location = '/store/group/lnujj/VVjj_aQGC/custom_nanoAOD/'

config = config()

config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = pset_file
config.JobType.outputFiles = ['nano.root']

config.JobType.allowUndistributedCMSSW = True

config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1

config.Data.publication = True
config.Data.outputDatasetTag = out_dataset_tag

config.Data.outLFNDirBase = storage_location
config.Site.storageSite = 'T3_US_FNALLPC'


from CRABAPI.RawCommand import crabCommand

inputDatasets = open(samples_list, "r")

for dataset in inputDatasets:
    if dataset[0] == "#":
        continue
    dataset = dataset.strip()
    print(dataset)

    config.General.requestName = (dataset.split("/")[1] + "_" + dataset.split("/")[2].split("-")[0])[:100]
    print(config.General.requestName)

    config.Data.inputDataset = dataset
    
    #print(config)
    crabCommand('submit', config=config)
    #crabCommand('submit', '--dryrun', config=config)
    #break

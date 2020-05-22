from CRABClient.UserUtilities import config, getUsernameFromCRIC

year = '2018'
#which_mc = 'sm'
which_mc = 'aqgc'
dryrun = True
print_config = True
just_print_config = True
just_first_sample = False

if which_mc == 'sm':
    samples_list = 'samples%s.txt' % year
    pset_file = 'nano_production_mc_%s_NANO.py' % year
    out_dataset_tag = 'VVjj_%sv6' % year

elif which_mc == 'aqgc':
    samples_list = 'samples%s_aQGC.txt' % year
    pset_file = 'nano_production_mc_aqgc_%s_NANO.py' % year
    out_dataset_tag = 'VVjj_%sv6' % year
else:
    exit("incorrect mc choice ... exiting")

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

    if print_config: print(config)
    if just_print_config: continue

    if dryrun:
        crabCommand('submit', '--dryrun', config=config)
    else:
        crabCommand('submit', config=config)

    if just_first_sample: break

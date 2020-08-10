from CRABClient.UserUtilities import config, getUsernameFromCRIC
import os 

year = '2018'
#which_mc = 'sm'
which_mc = 'sm'
dryrun = False
resubmit=True
print_config = True
just_print_config = False
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

storage_location = '/store/group/phys_smp/VJets_NLO_VBSanalyses/Samples/NanoAOD'

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
config.Site.storageSite = 'T2_CH_CERN'


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

    if not resubmit:
        if dryrun:
            crabCommand('submit', '--dryrun', config=config)
        else:
            crabCommand('submit', config=config)
    else:
        try:
            os.chdir('crab_'+(config.General.requestName))
            crabCommand('resubmit')
            os.chdir("..")
        except:
            print("nothing to resubmit")
            os.chdir("..")

    if just_first_sample: break

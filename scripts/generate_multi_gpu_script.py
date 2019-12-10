import os
BASE_DIR = 'run_superglue'
TASKS = ['commit', 'copa', 'multirc', 'record', 'rte', 'wic', 'wsc',
         'boolq++', 'commit++', 'copa++', 'rte++',
         'boolq-bow', 'commit-bow', 'copa-bow', 'multirc-bow', 'record-bow',
         'rte-bow', 'wic-bow', 'wsc-bow']
NGPUS = 4
of_l = []
for i in range(NGPUS):
    of = open(os.path.join(BASE_DIR, 'run_gpu{}.sh'.format(i)), 'w')
    of.write('source ../user_config.sh\n')
    of_l.append(of)
for i, task in enumerate(TASKS):
    gpu_id = i % NGPUS
    of_l[gpu_id].write('bash ../superglue-baselines.sh {} {}\n'.format(task, gpu_id))
for i in range(NGPUS):
    of_l[i].close()

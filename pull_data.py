import openneuro as on
import os
import pandas as pd


if __name__ == "__main__":
    # download 100 rats from StandardRat dataset on OpenNeuro
    # specify ds number and version #
    ds_num = 'ds004116'
    tag_num = '1.0.0'

    os.makedirs('data', exist_ok=True)


    # get subject list
    participants = pd.read_csv('participants.tsv', delimiter='\t')
    participant_id = participants.participant_id

    # only download 100 participant directories
    include_dirs = [f'{p_id}/*' for p_id in participant_id]
    # download with openneuro-py
    on.download(dataset=ds_num, tag=tag_num, target_dir='data', 
                include=include_dirs)

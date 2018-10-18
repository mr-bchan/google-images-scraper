import os
import json
import pandas


def build_metadata(logs_folder, output_folder):
    files = os.listdir(logs_folder)

    output_filename = 'metadata.csv'
    output_file = os.path.join(output_folder, output_filename)
    output = []

    print('Reading metadata files stored in {} folder'.format(logs_folder))

    for file in files:
        source = file.split()[0].replace('site:','').strip()
        keyword = ' '.join(file.split()[1:]).replace('.json','').replace('"','')

        with open(os.path.join(logs_folder, file), 'r') as infile:
            json_data = json.load(infile)

            for data in json_data:
                data['source'] = source
                data['keyword'] = keyword

            output.extend(json_data)

    output_csv = pandas.DataFrame(output)
    output_csv = output_csv.sort_values(by=['keyword', 'source'])
    output_csv = output_csv.drop_duplicates(subset=['image_link'])

    print('Saved resulting csv file to folder: {}\n'.format(output_file))
    output_csv.to_csv(output_file, index=False)

if __name__  == '__main__':

    LOG_FOLDER = 'logs'
    OUT_CSV = 'downloads'

    build_metadata(logs_folder=LOG_FOLDER, output_folder=OUT_CSV)


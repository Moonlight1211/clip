from getopt import GetoptError, gnu_getopt
import json
import os
import sys
import requests


# Fetch API response
def get_api_data(args):
    ip = args['ip']
    fields = args['fields']
    url = f'http://ip-api.com/json/{ip}?fields={fields}'

    response = requests.get(url).json()
    if response['status'] == 'fail':
        print(f'Failed to fetch IP data: {response['message']}')
        sys.exit(1)

    response.pop('status')

    return response


def main(args):
    field_names_pretty = {
        'continent': 'Continent',
        'continentCode': 'Continent Code',
        'country': 'Country',
        'countryCode': 'Country Code',
        'region': 'Province Code',
        'regionName': 'Province',
        'city': 'City',
        'district': 'District',
        'zip': 'Zip Code',
        'lat': 'Latitude',
        'lon': 'Longitude',
        'timezone': 'Timezone',
        'offset': 'Timezone Offset (seconds)',
        'currency': 'Local Currency',
        'isp': 'Interner Service Provider',
        'org': 'Organization Name',
        'as': 'AS Number and Organization',
        'asname': 'AS name (RIR)',
        'reverse': 'Reverse DNS',
        'mobile': 'Mobile Connection',
        'proxy': 'Proxy Connection',
        'hosting': 'Hosting/Colocated/Data Center',
    }
    response = get_api_data(args)
    if len(args['output']) > 0:
        output_path = args['output']
        response_json = json.dumps(response, indent=4)
        with open(output_path, 'w') as file:
            file.write(response_json)

        sys.exit(0)

    ip = response['query']
    response.pop('query')
    print(f'    IP Geolocation data for {ip}')

    for field_name in response:
        field_value = response[field_name]
        if len(str(field_value)) > 0:
            field_text = field_names_pretty[field_name]
            print(f'\t{field_text}: {field_value}')
        else:
            continue

    return


# Function to print help text
def print_help_text():
    print('CLIp - Internet Protocol Address Tracer\n')
    print('Usage: clip [OPTIONS] <ip> \n')
    print('Options:')
    print('  -h                           Prints this help message')
    print('  -o, --output <Filename>      Output IP information to text file')
    print('  -A                           Display all fields.')
    print('  -F, --field-file             CSV file to read fields from. Defaults to lib/fields.csv')
    print('  -f, --fields <fields>        Comma-separated list of fields to include. Takes precedence over -F and -A.')


# Generate a numeric fields value to pass to the API
def generate_csv_numeric(fields='', filepath=''):
    # Please see https://ip-api.com/docs/api:json for more information on the API used for this program
    field_values = {
        'status': [16384, True],
        'message': [32768, True],
        'continent': [1048576, False],
        'continentCode': [2097152, False],
        'country': [1, False],
        'countryCode': [2, False],
        'region': [4, False],
        'regionName': [8, False],
        'city': [16, False],
        'district': [524288, False],
        'zip': [32, False],
        'lat': [64, False],
        'lon': [128, False],
        'timezone': [256, False],
        'offset': [33554432, False],
        'currency': [8388608, False],
        'isp': [512, False],
        'org': [1024, False],
        'as': [2048, False],
        'asname': [4194304, False],
        'reverse': [4096, False],
        'mobile': [65536, False],
        'proxy': [131072, False],
        'hosting': [16777216, False],
        'query': [8192, True],
    }
    field_list = []
    if len(fields) > 0:
        field_list = fields.split(',')

    elif len(filepath) > 0:
        file = os.path.abspath(filepath)
        with open(file, 'r') as f:
            field_list = f.readline().split(',')

    for field_name in field_list:
        if field_name in field_values:
            try:
                field_values[field_name][1] = True
            except KeyError:
                continue

    numeric = 0
    for field_name in field_values:
        if field_values[field_name][1]:
            numeric += field_values[field_name][0]

    return numeric


# Parse the user's arguments'
def parse_args(argv):
    args = {
        # IP address to trace
        'ip': '',
        # Output file location
        'output': '',
        # Fields to request
        'fields': 1632249,
    }

    try:
        opts, _args = gnu_getopt(argv, 'o:hAf:F:', ['output=', 'fields=', 'field-file='])
    except GetoptError:
        print_help_text()
        sys.exit(1)

    try:
        args['ip'] = _args[0]
    except IndexError:
        pass

    for opt, arg in opts:

        if opt == '-h':
            print_help_text()
            sys.exit(0)

        elif opt in ('-o', '--output'):
            if os.path.isdir(os.path.dirname(os.path.abspath(arg))):
                if arg[-5:] != ".json":
                    args['output'] = f"{os.path.abspath(arg)}.json"
                else:
                    args['output'] = os.path.abspath(arg)
            else:
                print(f'"{arg}" is not a valid file location. Please try again.')
                sys.exit(1)

            # -f --fields handling
        elif opt in ('-f', '--fields'):
            args['fields'] = generate_csv_numeric(arg)

        # -A handling
        elif opt == '-A':
            args['fields'] = 66846719

        # -F --field-file handling
        elif opt in ('-F', '--field-file'):
            if os.path.isfile(arg):
                args['fields'] = generate_csv_numeric('', arg)
            else:
                print(f'"{arg}" is not a valid file. Please try again.')
                sys.exit(1)

    return args


if __name__ == '__main__':
    main(parse_args(sys.argv[1:]))

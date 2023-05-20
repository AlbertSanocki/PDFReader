"""PDF Reader CLI"""
import argparse

def pdf_file(value: str):
    """Validate PDF file"""

    if value.endswith('.pdf'):
        return value
    raise argparse.ArgumentError(
        None,
        f'Invalid file: "{value}". Only PDF files are allowed'
    )

def main(args):
    files_to_process = args.file
    print(files_to_process)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='PDF Reader',
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument(
        '-o',
        '--output',
        choices=['csv', 'dict', 'json'],
        required=True,
        help="""csv -> output file format CSV\
            \ndict -> output file format Python Dictionary\
            \njson -> output file format JSON"""
    )

    parser.add_argument(
        '-n',
        '--name',
        required=True,
        help='Name of the output file'
    )

    parser.add_argument(
        '-v',
        '--verbose',
        action='count',
        default=0
    )

    parser.add_argument(
        '-f',
        '--file',
        action='append',
        type=pdf_file,
        help='list of files to process'
    )

    parser.add_argument(
        '-d',
        '--directory',
        help='directory for saving output file'
    )

    args = parser.parse_args()
    main(args)
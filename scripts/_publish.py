#!/usr/bin/env python3
import sys
import os
from os import path


def find_ext(folder, ext):
    return [path.join(folder, f)
            for f
            in os.listdir(folder)
            if (path.isfile(path.join(folder, f))
                and
                (ext == '' or f.lower().endswith("." + ext.lower()))
                )]


def seperate_pdf(folder):
    # Find felix_xxxx.pdf
    print()
    print('Doing nothing atm, should be identifying pdfs now...')
    print(folder)
    pdfs = find_ext(folder, "pdf")
    # Scrape to find xxxx
    for f in pdfs:
        issue_num = f[f.find("/felix_")+7:-4]
        issue_confirmation = input(
            "I have detected " + issue_num + " to be the issue number. Please confirm this is correct (y/n): ")
        if issue_confirmation == 'n':
            issue_num = input(
                "Please input your correct issue number, but be warned that it is not the issue number I detected. Please check that the Book is named felix_xxxx.pdf. : ")
        elif issue_confirmation == 'y':
            # TODO: now that issue_number is confirmed, create a folder in .. that contains the split up pages
            # parent_dir = f[0:f.find("/felix_")]
            # print(parent_dir)
            continue
        else:
            print("Error message, try to reroute this upwards...")
            # TODO while loop here? while issue_conf != 'y'
    print('Done')

    # use pdfReader and pdf Writer to seperate the pdf
    # Rename the pdfs

# Create new folder in Desktop with issue number as the name

    ###############################
if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Usage: _publish.py /full/path/to/current/issue.directory")
        print("Missing arguments.")
        sys.exit(1)

    # working_dir for testing should be pwd/../tests/files
    working_dir = sys.argv[1]

    while True:
        print()
        print('What would you like to do?')
        print('1. Confirm issue number')
        print('2. Separate felix_xxxx.pdf into separate pages')
        print('q. Quit')

        try:
            command = input("> ").lower()
            print('********')
        except KeyboardInterrupt:
            print("\nBye!")
            sys.exit(0)

        if command == 'q':
            print("\nBye!")
            sys.exit(0)

        elif command == "1":
            seperate_pdf(working_dir)

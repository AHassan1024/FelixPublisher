#!/usr/bin/env python3
import sys
import os
from os import path
# Requires PyPDF2 through pip install PyPDF2 in main directory
# > Successfully installed PyPDF2-1.26.0
from PyPDF2 import PdfFileReader, PdfFileWriter


def find_ext(folder, ext):
    return [path.join(folder, f)
            for f
            in os.listdir(folder)
            if (path.isfile(path.join(folder, f))
                and
                (ext == '' or f.lower().endswith("." + ext.lower()))
                )]


def create_directory(file, issue_number):
    print("Creating empty folder called %s!" % issue_number)
    parent_dir = file[0:file[0:file.rfind("/")].rfind("/")]
    print(parent_dir)
    try:
        os.mkdir(os.path.join(parent_dir, issue_number))
        print("Directory '%s' created" % issue_number)
    except OSError as error:
        print(error)


def split_and_save(file_path, issue_number):
    print("Now splitting felix_%s.pdf" % issue_number)
    full_pdf = PdfFileReader(file_path)
    for page in range(full_pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(full_pdf.getPage(page))
        if page < 8:
            output_filename = 'PDFE-E01-S2-00{}.pdf'.format(page + 1)
        else:
            output_filename = 'PDFE-E01-S2-0{}.pdf'.format(page + 1)
        with open(working_dir.join(output_filename), 'wb') as out:
            pdf_writer.write(out)
        print('Created: {}'.format(output_filename))


def find_pdf(folder):
    # Find felix_xxxx.pdf
    print()
    print('Doing nothing atm, should be identifying pdfs now...')
    print(folder)
    pdfs = find_ext(folder, "pdf")
    # Scrape to find xxxx
    for f in pdfs:
        f = pdfs[-1]
        issue_num = f[f.find("/felix_")+7:-4]
        issue_confirmation = input(
            "I have detected " + issue_num + " to be the issue number. Please confirm this is correct (y/n): ").lower() in ['y', "yup", "yes"]
        if not issue_confirmation:
            print("I was unable to detect the correct issue number. Please check the Final Book pdf is named 'felix_xxxx.pdf'")
            sys.exit(1)

            # Go back to the menu now
        else:
            print("Issue %s confirmed!" % issue_num)

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
    issue_num = 0

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
            success = False
            f = find_pdf(working_dir)
            if (issue_num != 0):
                create_directory(working_dir, issue_num)
                split_and_save(f, issue_num)
            # success = True
            print(success)
        else:
            print("Apologies, this option is not yet supported.")

#!/usr/bin/env python
"""
Example command-line app

This is a simple command-line app that accepts arguments and options,
performs some action, and outputs the results.

Usage:
  main.py [options] -m <mode> -c <client-id> [-g <gap>]

Arguments:
  <client-id> 
  <mode>
  <gap>

Options:
  -c --client   to specify the client address to send mail to 
  -g --gap      to specify the time (in sec) for sucessive motion capture
  -m --mode     image : captures 4 images and sends them to mail\nvideo : send video to mail
  -h --help     Show this screen.
  -v --verbose  Enable verbose mode.
"""
from email_validator import validate_email, EmailNotValidError
from docopt import docopt


def main(verbose, mode, mode_id):
    if verbose:
        print("Verbose mode enabled")
    if mode:
        if mode_id == 'image':
            print('CaptureImg_main()')
        elif mode_id == 'video':
            print('CaptureVid_main()')
    if verbose:
        print("Verbose mode enabled")


GAP_TIME = 90

def email_validate_with_err(mail_id):
    try:
        # Validate the email address
        valid = validate_email(mail_id)
        # Print the result
        if valid:
            print("The email address is valid")
            return True
        else:
            print("The email address is not valid")
            return False

    except EmailNotValidError as e:
        # The email address is not valid
        print("The email address is not valid: {}".format(str(e)))
        return False


if __name__ == '__main__':
    args = docopt(__doc__)
    verbose = args['--verbose']
    mode = args['--mode']
    mode_id = args['<mode>']
    client = args['--client']
    CLIENT_EMAIL_ID = args['<client-id>']
    gap = args['--gap']
    if gap:
        GAP_TIME = int(float(args['<gap>']))
    print(args)
    # Call the main function
    if mode and mode_id in ('image', 'video') and email_validate_with_err(CLIENT_EMAIL_ID):
        print(type(GAP_TIME))
        main(verbose, mode, mode_id)

# -*- coding: UTF-8 -*-

import logging
import sys

def main():
    ''' assuming loglevel is bound to string value obtained from the
    command line argument. convert to upper case to aollow the user to
    specify --log=DEBUG or --log=debug
    '''
    if sys.argv[1] not in ['DEBUG', 'debug', 'INFO', 'info', 'WARNING',
                           'warning','ERROR', 'error', 'CRITICAL', 'critical']:
        print('invalid argument')
        log_level = 'WARNING'
        return
    else:
        log_level = sys.argv[1]
    numeric_level = getattr(logging, log_level.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError('Invalid log level:%s' %log_level)
    logging.basicConfig(level=numeric_level)
    logging.debug('this message should go to the log file')
    logging.info('so should this')
    logging.warning('and this ,too,{}'.format('wanghong'))

if __name__ == '__main__':
    main()
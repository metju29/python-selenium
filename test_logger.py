'''
From https://stackoverflow.com/questions/4673373/logging-within-pytest-tests
'''

import logging

logger = logging.getLogger(__name__)


def test_eggs():
    logger.info('eggs info')
    logger.warning('eggs warning')
    logger.error('eggs error')
    logger.critical('eggs critical')
    assert True



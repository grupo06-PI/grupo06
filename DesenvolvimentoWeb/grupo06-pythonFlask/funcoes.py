import logging
import hashlib


class Funcoes(object):

    def encrypt(self, senha):
        return hashlib.sha3_256(senha.encode('utf-8')).hexdigest()

    def logInfo(self, parametro_log):
        logging.info(parametro_log)
        return parametro_log

    def logWarning(self, parametro_log):
        logging.warning(parametro_log)
        return parametro_log

    def logError(self, parametro_log):
        logging.error(parametro_log)
        return parametro_log
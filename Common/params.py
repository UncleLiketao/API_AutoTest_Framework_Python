import json

from Common import aes_crypt


class Params(object):
    def __init__(self):
        self.commn_params = {
            'gimiPid': 'EHFAJEF79TAU', 'gimiDevice': 'aosp_synsepalum_YN', 'xgimiDeviceName': 'synsepalum_Y',
            'deviceMac': '80-0B-52-02-44-26', 'systemVersion': 'v1.6.23', 'launcherVersionCode': 1510,
        }

    def add_param(self, key, value):
        self.commn_params[key] = value
        return self.commn_params

    def encrypt_data(self):
        before_encrypt_data = json.dumps(self.commn_params)
        params = aes_crypt.AesCrypt().aes_encode(before_encrypt_data)
        requests_data = {"params": "%s" % params}
        return requests_data


if __name__=='__main__':
    Params().add_param("sourceId", "10001")
    data = Params().encrypt_data()
    print(data)

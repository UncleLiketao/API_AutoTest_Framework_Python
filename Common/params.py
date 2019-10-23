import json

from Common import aes_crypt


class Params(object):
    def __init__(self):
        self.commn_params = {
            'gimiPid': 'EHFAJEF79TAU', 'gimiDevice': 'aosp_synsepalum_YN', 'xgimiDeviceName': 'synsepalum_Y',
            'deviceMac': '80-0B-52-02-44-26', 'systemVersion': 'v1.6.23', 'launcherVersionCode': 1510,
        }

    def encrypt_data(self, data=None):
        if data is None:
            data = {}
        for key in data.keys():
            self.commn_params[key] = data[key]
        before_encrypt_data = json.dumps(self.commn_params)
        params = aes_crypt.AesCrypt().aes_encode(before_encrypt_data)
        requests_data = {"params": "%s" % params}
        return requests_data

    def non_encrypted_data(self, data: dict):
        requests_data = {"params": "%s" % json.dumps(data)}
        return requests_data


if __name__=='__main__':
    req_data = Params().encrypt_data({"source": "iqiyi", "dockId": "1", "gender": "1", "ageDuration": "1"})
    print(req_data)
    # data = Params().encrypt_data()
    # print(data)

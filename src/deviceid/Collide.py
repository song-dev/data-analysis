import json
import unittest
import pandas as pd

'''
指纹碰撞分析
'''


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_print_json(self):
        # 程序
        # parse_json('../files/fp_2IS7D53X4SB7DQYDDIPJCNUXB7BTX4WN.json') # todo mac_address 碰撞，且值为 00:90:4c:11:22:33 非常可疑，需要重点排查
        # parse_json('../files/fp_WRWBJZH7HDDA3XDX6RDUNKSQTDWTA5HY.json')  # todo imei和android被篡改
        # parse_json('../files/fp_DNFK6M2IZ32TVWNIP45MSBWMIBSMIHHZ.json')  # todo 未篡改数据，只是 uuid 和 boot 改变
        # parse_json('../files/fp_U3ERSYVYOZJPIVJLDQA53XF2LRQCVVQM.json')  # todo 未篡改数据，ip_de 碰撞
        # parse_json('../files/fp_AZ72N5M2IOPDO34QMBRO7Q4HKVD6AJ54.json')  # todo 未篡改数据，mac 碰撞, 无效 Mac 地址 00:00:00:80:00:00
        # parse_json('../files/fp_U3ERSYVYOZJPIVJLDQA53XF2LRQCVVQM.json')  # todo 未篡改数据，ip_de 碰撞
        # parse_json('../files/fp_W37HJQ5ZKKD6UEXOIC7CHAIGIVQHXOG6.json')  # todo 未篡改数据，mac 碰撞, 64:cc:2e:6a:f3:a3
        # parse_json('../files/fp_PPDSEX2YVCOVDXIZLWCLIUQVXFGXDWMV.json')  # todo 未篡改数据，ip_de 碰撞
        # parse_json('../files/androidid_mult_fp_0keys.json')  # todo
        # parse_json('../files/0226_80mac.json')  # todo mac 异常
        # parse_json('../files/la_XFFId.json')  # todo la 异常
        # parse_json('../files/la_VtzgXR.json')  # todo  la 异常
        # parse_json('../files/db_cbd_51FCE98.json')  # todo  篡改 android imei 异常
        # parse_json('../files/db_cbd_9CB08B6973.json')  # todo  恶意篡改数据 异常
        # parse_json('../files/db_cbd_99FBBB80.json')  # todo ip 异常
        # parse_json('../files/db_cbd_F92D6CF.json')  # todo  androidid imei 异常
        # parse_json('../files/db_cbd_81FA75BB2.json')  # todo  恶意篡改数据 异常
        # parse_json('../files/la_VoVSmWb.json')  # todo la 异常
        # parse_json('../files/la_VoVRICEO.json')  # todo la 异常
        # parse_json('../files/mac_00-00-00-00-00-00.json')  # todo mac碰撞 异常
        # parse_json('../files/mac_00-08-22-52-fd-fb.json')  # todo mac碰撞 异常
        # parse_json('../files/mac_7c-a1-77-aa-17-a9.json')  # todo mac碰撞 相同机型
        # parse_json('../files/mac_10-00-92-88-61-01.json')  # todo mac碰撞 相同机型异常 OPPO A59s
        # parse_json('../files/mac_20-82-c0-cc-de-19.json')  # todo mac碰撞 异常 ？？？ 2014813
        # parse_json('../files/mac_34-80-b3-3c-40-17.json')  # todo mac碰撞 异常 ？？？ MI 4LTE
        # parse_json('../files/mac_48-13-f3-01-07-b5.json')  # todo mac碰撞 异常 ？？？ vivo Y35\vivo X9
        # parse_json('../files/mac_48-13-f3-01-17-bc.json')  # todo mac碰撞 异常 ？？？ vivo X6S A\vivo Xplay5A
        # parse_json('../files/mac_64-cc-2e-6a-f3-a3.json')  # todo mac碰撞 异常 ？？？ MI 5
        # parse_json('../files/mac_d4-50-3f-d7-07-11.json')  # todo mac碰撞 异常 ？？？ OPPO R11/OPPO R11 Plusk
        # parse_json('../files/mac_dc-90-88-39-d4-e5.json')  # todo mac碰撞 异常 ？？？ VCE-AL00/MHA-AL00
        # parse_json('../files/mac_ec-01-ee-59-9b-2c.json')  # todo mac碰撞 异常 ？？？ OPPO A59s
        # parse_json('../files/sys_8a6f8f82.json')  # todo androidid、bdid、la被篡改
        # parse_json('../files/sys_23c62bdb.json')  # todo androidid、bdid、la 被篡改
        parse_json('../files/key_new_pengzhuang.json')  # todo mac碰撞 异常 ？？？ OPPO A59s
        self.assertEqual(True, True)


mainKey = 'androidId'

def parse_json(name):
    '''
    解析 json
    :return:
    '''

    with open(name, 'r') as f:
        origin = json.load(f)
        print('len', len(origin))
        # 输出
        num = 0
        a = []
        for item in origin:
            time = json.loads(item['unique_t'])
            a.append(item[mainKey])
            if item['ip'] == '117.136.87.162':
                num = num + 1
                print(item['uuid'], item['boot'], item['systemFile'], item['androidId'])
                # print(item['db_cbd'], item['la_dx'], item['idv'], item['mac_address'], item['csdf_sys'], item['csdf_ali'], item['csdf_ten'])
                # print(item['fonts'], item['skt_list'], item['model'], item['ip'], time['app'], time['cust'] if ('cust' in time) else '$unknown')
                # print(item['fonts'], item['skt_list'], item['model'], item['ip'])
                # print(item['androidId'],time['cust'] if ('cust' in time) else '$unknown')
                # print(item['idv'],item['mac_address'], item['ip_de'] if ('ip_de' in item) else '$unknown')
        # print(origin[-1])
        print('num', num)
        result = pd.value_counts(a)
        print(result)
        check_item(name, list(pd.unique(a)))
    return


def check_item(name, a):
    '''
    给出列表循环校验异常值
    :param name:
    :return:
    '''

    for value in a:
        with open(name, 'r') as f:
            origin = json.load(f)
            for item in origin:
                time = json.loads(item['unique_t'])
                if item[mainKey] == value:
                    print(item['mac_address'], item['fonts'], item['db_cbd'], item['la_dx'], item['androidId'],
                          item['idv'],
                          item['systemFile'], time['app'],
                          item['ip'])
                # if item['model'] == 'OPPO R9s Plus':
                #     print(item)
            print(origin[1])
        print()


if __name__ == '__main__':
    unittest.main()

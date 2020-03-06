import json
import unittest

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
        parse_json('../files/fp_PPDSEX2YVCOVDXIZLWCLIUQVXFGXDWMV.json')  # todo 未篡改数据，ip_de 碰撞
        self.assertEqual(True, True)


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
        for item in origin:
            time = json.loads(item['unique_t'])
            if item['model'] != 'MI 5' and item['ip_de'] != '9915e6a809a3d31c68d53d0e35db194f8b02abeaaffd6df2a75acbafa7907c754bad145a8084b6fcd2341e6268afe9f8':
                num = num + 1
                # print(item['uuid'], item['boot'], item['systemFile'], item['androidId'])
                print(item['db_cbd'], item['la_dx'], item['idv'], item['mac_address'], item['csdf_sys'])
                # print(item['fonts'], item['skt_list'], item['model'], item['ip'], time['app'], time['cust'] if ('cust' in time) else '$unknown')
                # print(item['androidId'],time['cust'] if ('cust' in time) else '$unknown')
                # print(item['idv'],item['mac_address'], item['ip_de'] if ('ip_de' in item) else '$unknown')
        print(origin[-1])
        print('num', num)

    return


if __name__ == '__main__':
    unittest.main()

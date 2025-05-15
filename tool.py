
    with open(file, 'rb') as f:


def saveFile(path, content):
    file = open(path, mode='w', encoding='utf-8')

    '🇭🇰': re.compile(
        r'香港|沪港|呼港|中港|HKT|HKBN|HGC|WTT|CMI|穗港|广港|京港|🇭🇰|HK|Hongkong|Hong Kong|HongKong|HONG KONG'),
    '🇺🇸': re.compile(
        r'美国|美國|京美|硅谷|凤凰城|洛杉矶|西雅图|圣何塞|芝加哥|哥伦布|纽约|广美|(\s|-)?(?<![AR])US\d*|USA|America|United States'),
    '🇨🇳': re.compile(
        r'中国|中國|江苏|北京|上海|广州|深圳|杭州|徐州|青岛|宁波|镇江|沈阳|济南|回国|back|(\s|-)?CN(?!2GIA)\d*|China'),



    file = open(path, 'rb')

        if len(t) > 0:
            if index + 1 < len(lines):


        name += random.choice(string.ascii_letters + string.digits)

    return re.search(r'^\d+\.\d+\.\d+\.\d+$', str)


def checkKeywords(keywords, str):
        if str.find(keyword) > -1:

def filterNodes(nodelist, keywords):
        if not checkKeywords(keywords, node['name']):
            print('过滤节点名称 ' + node['name'])

def replaceStr(nodelist, keywords):
            node['name'] = node['name'].replace(k, '').strip()


    temp_list = []
    i = 0
        _node = {'server': node['server'], 'port': node['port']}
            i += 1
    print('去除了 ' + str(i) + ' 个重复节点')
    print('Đã xóa các proxy trùng lặp ' + str(i))
    print('实际获取 ' + str(len(newlist)) + ' 个节点')
    print('Thực tế nhận được ' + str(len(newlist)) + ' proxy')

def prefixStr(nodelist, prestr):
        node['name'] = prestr + node['name'].strip()

        # 'User-Agent': 'clash.meta'
        response = requests.get(url, headers=headers, timeout=5000)
        if response.status_code == 200:


    server = {'ip': None, 'port': 22, 'user': None, 'password': ''}

    def __init__(self, server: dict) -> None:

        ssh.connect(hostname=self.server['ip'], port=22, username=self.server['user'], password=self.server['password'])
    def execCMD(self, command: str):
        stdin, stdout, stderr = self.ssh.exec_command(command)
        print(stdout.read().decode('utf-8'))
    def uploadFile(self, source: str, target: str):
    def getFile(self, remote: str, local: str):
        scp.get(remote, local)


'''
根据 domain 查询服务器节点的区域
'''


def get_node_region_by_domain(domain):
    try:
        domain = domain.split("//")[-1].split("/")[0]
        '''
         {
          "domain_name": "FC-SMARTGLOBAL.XYZ",
          "registrar": "NAMECHEAP INC",
          "registrar_url": [
            "https://namecheap.com",
            "http://www.namecheap.com"
          ],
          "reseller": "NAMECHEAP INC",
          "whois_server": "whois.namecheap.com",
          "referral_url": null,
          "updated_date": [
            "2025-03-03 12:14:19",
            "2025-02-03 07:08:48.790000"
          ],
          "creation_date": "2024-03-05 03:46:26",
          "expiration_date": "2026-03-05 23:59:59",
          "name_servers": [
            "NS1.HUAWEICLOUD-DNS.ORG",
            "NS1.HUAWEICLOUD-DNS.NET",
            "NS1.HUAWEICLOUD-DNS.CN",
            "NS1.HUAWEICLOUD-DNS.COM"
          ],
          "status": "clientTransferProhibited https://icann.org/epp#clientTransferProhibited",
          "emails": [
            "abuse@namecheap.com",
            "b3ee1aa185ef4ab6b3320f9cc6166e1b.protect@withheldforprivacy.com"
          ],
          "dnssec": "unsigned",
          "name": "Redacted for Privacy",
          "org": "Privacy service provided by Withheld for Privacy ehf",
          "address": "Kalkofnsvegur 2",
          "city": "Reykjavik",
          "state": "Capital Region",
          "registrant_postal_code": "101",
          "country": "IS"
        }        
    '''
        w = whois.whois(domain)
        if w and hasattr(w, 'country'):
            return w
        else:
            return "国家信息未找到"
    except whois.parser.PywhoisError:
        return "域名未注册或 WHOIS 查询失败"
    except Exception as e:
        return f"发生错误: {e}"

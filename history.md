 1/1: import pyodbc
 1/2: conn = pyodbc.connect('MSDB-DV-1-SQL2\SQL2;')
 1/3: conn = pyodbc.connect('DSN=MSDB-DV-1-SQL2\SQL2;')
 1/4: conn = pyodbc.connect('DSN=MSDB-DV-1-SQL2;')
 1/5: conn = pyodbc.connect('DSN=MSDB-DV-1-SQL2;PORT=1435;')
 1/6: conn = pyodbc.connect('DSN=MSDB-DV-1-SQL2')
 1/7: conn = pyodbc.connect('DSN=MSDB-DV-1-SQL2vfgfss')
 1/8: conn = pyodbc.connect('DSN=MSDB-DV-1-SQL2')
 1/9: conn = pyodbc.connect('DSN=MSDB-DV-1-SQL2;')
1/10: conn = pyodbc.connect('DSN=MSDB-DV-1-SQL2;')
1/11: conn = pyodbc.connect('DSN=MSDB-DV-1-SQL2;')
1/12: conn = pyodbc.connect('DSN=MSDB-DV-1-SQL2\MILLEBASESR2;')
1/13: cursor = conn.cursor()
1/14: cursor.execute("SELECT auth_scheme FROM sys.dm_exec_connections WHERE session_id = @@spid;")
1/15: cursor.execute("SELECT auth_scheme FROM dbo.Visite WHERE id_Navigateur = 1;")
1/16: cursor.execute("SELECT dVisite FROM dbo.Visite WHERE id_Navigateur = 1;")
1/17: cursor.execute("SELECT NB FROM dbo.Stickiness;")
1/18: cursor.execute("SELECT auth_scheme FROM sys.dm_exec_connections WHERE session_id = @@spid;")
1/19: cursor.fetchone()
1/20: cursor.execute("SELECT auth_scheme FROM sys.dm_exec_connections WHERE session_id = @@spid;")
1/21: import os
1/22: os.environ['KRB5_CONFIG']
1/23: clear
1/24: :ls
1/25: !ls
1/26: !ls -a
1/27: !klisr
1/28: !klist
1/29: !kdestroy
1/30: !klist
1/31: import subprocess
1/32: clear
1/33: subprocess.check_call(['kinit', '-kt', '/home/nodar/nka.keytab', 'nka@MILLEMERCIS.COM'])
1/34: !klist
1/35: cursor.execute("SELECT auth_scheme FROM sys.dm_exec_connections WHERE session_id = @@spid;")
1/36: conn = pyodbc.connect('DSN=MSDB-DV-1-SQL2\MILLEBASESR2;')
1/37: cursor = conn.cursor()
1/38: cursor.execute("SELECT auth_scheme FROM sys.dm_exec_connections WHERE session_id = @@spid;")
1/39: !klist
 2/1: import pyodbc
 2/2: conn = pyodbc.connect('DSN=MSDB-DV-1-SQL2\MILLEBASESR2;')
 2/3: import os
 2/4: import subprocess
 2/5: os.environ['KRB5_CONFIG']='/etc/krb5.conf'
 2/6: osd.environ['KRB5CCNAME'] = 'DIR:/tmp/Dior_BundleME2018'
 2/7: os.environ['KRB5CCNAME'] = 'DIR:/tmp/Dior_BundleME2018'
 2/8: !echo $KRB5CCNAME
 2/9: !kinit nka -kt nka.keytab
2/10: !ls
2/11: !ls /etc/krb5.winad.conf
2/12: os.environ['KRB5_CONFIG']='/etc/krb5.winad.conf'
2/13: !kinit nka -kt nka.keytab
2/14: conn = pyodbc.connect('DSN=MSDB-DV-1-SQL2\MILLEBASESR2;')
2/15: cursor = conn.cursor()
2/16: cursor.execute("SELECT auth_scheme FROM sys.dm_exec_connections WHERE session_id = @@spid;")
 3/1: import ldap
 3/2: ad = ldap.initialize('ldap://millemercis.com')
 3/3: ad
 3/4: ad.protocol_version = 3
 3/5: ad.set_option(ldap.OPT_TIMEOUT, 2)
 3/6: ad.set_option(ldap.OPT_NETWORK_TIMEOUT, 2)ad.set_option(ldap.OPT_REFERRALS, ldap.OPT_OFF)
 3/7: ad.set_option(ldap.OPT_NETWORK_TIMEOUT, 2)ad.set_option(ldap.OPT_REFERRALS, ldap.OPT_OFF)
 3/8: ad.set_option(ldap.OPT_NETWORK_TIMEOUT, 2) ad.set_option(ldap.OPT_REFERRALS, ldap.OPT_OFF)
 3/9:
ad.set_option(ldap.OPT_NETWORK_TIMEOUT, 2)
ad.set_option(ldap.OPT_REFERRALS, ldap.OPT_OFF)
3/10: ad.set_option(ldap.OPT_NETWORK_TIMEOUT, 2);ad.set_option(ldap.OPT_REFERRALS, ldap.OPT_OFF)
3/11: username = "nka"
3/12: password = "BlaBla"
3/13: ad.simple_bind_s('nka@millemercis.com', password)
3/14: ad.simple_bind_s('nka@millemercis.com', 'Halamadrid7!!')
3/15: clear
3/16:
base_dn = 'dc=millemercis, dc=com'
            search_scope = ldap.SCOPE_SUBTREE
            search_filter = 'mailNickname=%s' % username
            attributes = ['displayName', 'mail', 'mailNickname', 'distinguishedName', 'memberOf']
3/17:
base_dn = 'dc=millemercis, dc=com'
search_scope = ldap.SCOPE_SUBTREE
search_filter = 'mailNickname=%s' % username
attributes = ['displayName', 'mail', 'mailNickname', 'distinguishedName', 'memberOf']
3/18: ad.search_s(base=base_dn, scope=search_scope, filterstr=search_filter, attrlist=attributes)
3/19: ad.search_s(base=base_dn, scope=search_scope, attrlist=attributes)
3/20: ad.search_s(base=base_dn, scope=search_scope, filterstr=search_filter, attrlist=attributes)
3/21: search_filter
3/22: ad.search_s(base=base_dn, scope=search_scope, filterstr='mailNickname=te', attrlist=attributes)
3/23: ad.search_s(base=base_dn, scope=search_scope, filterstr='mailNickname=dade', attrlist=attributes)
3/24: ad.search_s(base=base_dn, scope=search_scope, filterstr='mailNickname=dsfdsf', attrlist=attributes)
3/25: ad.search_s(base=base_dn, scope=search_scope, filterstr='mailNickname=pacu', attrlist=attributes)
3/26: ad.search_s(base=base_dn, scope=search_scope, filterstr='mailNickname=thh', attrlist=attributes)
3/27: ad.search_s(base=base_dn, scope=search_scope, filterstr='mailNickname=dade', attrlist=attributes)
3/28: ad.search_s(base=base_dn, scope=search_scope, filterstr='mailNickname=dsfdsfdfsdfsfdfdsfdfsdds', attrlist=attributes)
3/29: ad.search_s(base=base_dn, scope=search_scope, filterstr='mailNickname=dsfdsfdfsdfsfdfdsfdfsdds', attrlist=attributes)
3/30: ad.search_s(base=base_dn, scope=search_scope, filterstr='mailNickname=nka', attrlist=attributes)
3/31: ad.search_s(base=base_dn, scope=search_scope, filterstr='mailNickname=pacu', attrlist=attributes)
3/32: base_dn
3/33: search_scope
3/34: base_dn
3/35: ad.search_s(base='dc=1000mercis', scope=search_scope, filterstr='mailNickname=pacu', attrlist=attributes)
3/36: ad.search_s(base='dc=1000mercis, dc=com', scope=search_scope, filterstr='mailNickname=pacu', attrlist=attributes)
3/37: base_dn
3/38: ad.search_s(base='dc=millemercis, dc=com', scope=search_scope, filterstr='mailNickname=pacu', attrlist=attributes)
3/39: ad.search_s(base='dc=millemercis, dc=com', scope=search_scope, filterstr='mailNickname=nka', attrlist=attributes)
3/40: ad.search_s(base='dc=com', scope=search_scope, filterstr='mailNickname=nka', attrlist=attributes)
3/41: ad.search_s(base='dc=fdsfd, dc=com', scope=search_scope, filterstr='mailNickname=nka', attrlist=attributes)
3/42: ad.search_s(base='dc=millemercis, dc=com', scope=search_scope, filterstr='mailNickname=nka', attrlist=attributes)
3/43: clear
3/44: ldqp
3/45: ldap
3/46: ldap.SCOPE_BASE
3/47: ldap.SCOPE_
3/48: ldap.SCOPE_
3/49: ldap.SCOPE_BASE
3/50: ad.search_s(base='dc=millemercis, dc=com', scope=0, filterstr='mailNickname=nka', attrlist=attributes)
3/51: ad.search_s(base='dc=millemercis, dc=com', scope=1, filterstr='mailNickname=nka', attrlist=attributes)
3/52: ad.search_s(base='dc=millemercis, dc=com', scope=2, filterstr='mailNickname=nka', attrlist=attributes)
3/53: ad.search_s(base='dc=millemercis, dc=com', scope=3, filterstr='mailNickname=nka', attrlist=attributes)
3/54: clear
3/55: ldap.SCOPE_SUBORDINATE
3/56: ldap.SCOPE_SUBTREE
3/57: ldap.SCOPE_ONELEVEL
3/58: ldap.SCOPE_
3/59: ad.search_s(base='dc=millemercis, dc=com', scope=search_scope, filterstr='mailNickname=nka', attrlist=attributes)
3/60: ad.search_s(base='dc=millemercis, dc=com', scope=search_scope, filterstr='mailNickname=te', attrlist=attributes)
3/61: ad.search_s(base='dc=millemercis, dc=com', scope=search_scope, filterstr='mailNickname=jhd', attrlist=attributes)
3/62: ad.search_s(base='dc=millemercis, dc=com', scope=search_scope, filterstr='mailNickname=nka', attrlist=attributes)
3/63: ldap$
3/64: ldap
3/65: ad.search_s(base='dc=millemercis, dc=com', scope=search_scope, filterstr='mailNickname=nka', attrlist=attributes)
3/66: ad = ldap.initialize('ldap://millemercis.com')
3/67: ad.search_s(base='dc=millemercis, dc=com', scope=search_scope, filterstr='mailNickname=nka', attrlist=attributes)
3/68: clear
3/69:
        ad.protocol_version = 3
        ad.set_option(ldap.OPT_TIMEOUT, 2)
        ad.set_option(ldap.OPT_NETWORK_TIMEOUT, 2)
        ad.set_option(ldap.OPT_REFERRALS, ldap.OPT_OFF)
3/70:
ad.simple_bind_s('%s@millemercis.com' % username, password)
base_dn = 'dc=millemercis, dc=com'
search_scope = ldap.SCOPE_SUBTREE
search_filter = 'mailNickname=%s' % username
attributes = ['displayName', 'mail', 'mailNickname', 'distinguishedName', 'memberOf']  # All attributes
3/71:
ad.simple_bind_s('%s@millemercis.com' % username, password)
base_dn = 'dc=millemercis, dc=com'
search_scope = ldap.SCOPE_SUBTREE
search_filter = 'mailNickname=%s' % username
attributes = ['displayName', 'mail', 'mailNickname', 'distinguishedName', 'memberOf']
3/72: username
3/73: password
3/74: clear
3/75: password='Halamadrid7!!'
3/76: clear
3/77:
ad.simple_bind_s('%s@millemercis.com' % username, password)
base_dn = 'dc=millemercis, dc=com'
search_scope = ldap.SCOPE_SUBTREE
search_filter = 'mailNickname=%s' % username
attributes = ['displayName', 'mail', 'mailNickname', 'distinguishedName', 'memberOf']
3/78: clear
3/79: ad.search_s(base='dc=millemercis, dc=com', scope=search_scope, filterstr='mailNickname=nka', attrlist=attributes)
3/80: ad.search_s(base='dc=millemercis, dc=com', scope=search_scope, filterstr='mailNickname=jhd', attrlist=attributes)
3/81: ad.search_s(base='dc=millemercis, dc=com', scope=search_scope, filterstr='mailNickname=jd', attrlist=attributes)
 5/1: import ldap
 5/2: clear
 5/3:
ad = ldap.initialize('ldap://millemercis.com')
        ad.protocol_version = 3
        ad.set_option(ldap.OPT_TIMEOUT, 2)
        ad.set_option(ldap.OPT_NETWORK_TIMEOUT, 2)
        ad.set_option(ldap.OPT_REFERRALS, ldap.OPT_OFF)
 5/4:
        ad = ldap.initialize('ldap://millemercis.com')
        ad.protocol_version = 3
        ad.set_option(ldap.OPT_TIMEOUT, 2)
        ad.set_option(ldap.OPT_NETWORK_TIMEOUT, 2)
        ad.set_option(ldap.OPT_REFERRALS, ldap.OPT_OFF)
 5/5: username = 'nka'
 5/6: clear
 5/7: password = 'Halamadrid7!!'
 5/8: clear
 5/9:
            ad.simple_bind_s('%s@millemercis.com' % username, password)
            base_dn = 'dc=millemercis, dc=com'
            search_scope = ldap.SCOPE_SUBTREE
            search_filter = 'mailNickname=%s' % username
            attributes = ['displayName', 'mail', 'mailNickname', 'distinguishedName', 'memberOf']  # All attributes
5/10: ad.search_s(base=base_dn, scope=search_scope, filterstr=search_filter, attrlist=attributes)
5/11: ad.search_s(base=base_dn, scope=search_scope, filterstr='mailNickname=nka', attrlist=attributes)
5/12: ad.search_s(base=base_dn, scope=search_scope, filterstr='mailNickname=pacu', attrlist=attributes)
5/13: ad.search_s(base=base_dn, scope=search_scope, filterstr='mailNickname=nka', attrlist=attributes)
5/14: ad.search_s(base=base_dn, scope=search_scope, filterstr='mailNickname=the', attrlist=attributes)
5/15: ad.search_s(base=base_dn, scope=search_scope, filterstr='mailNickname=th', attrlist=attributes)
5/16: ad.search_s(base=base_dn, scope=search_scope, filterstr='mailNickname=te', attrlist=attributes)
5/17: clear
5/18: ad.search_s(base=base_dn, scope=search_scope, filterstr='mailNickname=', attrlist=attributes)
5/19: ad.search_s(base=base_dn, scope=search_scope, filterstr='', attrlist=attributes)
5/20: clear
5/21: ad.search_s(base=base_dn, scope=search_scope, filterstr='mailNickname=jua', attrlist=attributes)
5/22: ad.search_s(base=base_dn, scope=search_scope, filterstr='mailNickname=nka', attrlist=attributes)
5/23: clear
5/24: username = 'nka'
5/25:
        ad = ldap.initialize('ldap://millemercis.com')
        ad.protocol_version = 3
        ad.set_option(ldap.OPT_TIMEOUT, 2)
        ad.set_option(ldap.OPT_NETWORK_TIMEOUT, 2)
        ad.set_option(ldap.OPT_REFERRALS, ldap.OPT_OFF)
5/26:
            ad.simple_bind_s('%s@millemercis.com' % username, password)
            base_dn = 'dc=millemercis, dc=com'
            search_scope = ldap.SCOPE_SUBTREE
            search_filter = 'mailNickname=%s' % username
            attributes = ['displayName', 'mail', 'mailNickname', 'distinguishedName', 'memberOf']  # All attributes
5/27: ad.search_s(base=base_dn, scope=search_scope, filterstr='mailNickname=nka', attrlist=attributes)
5/28: ad.search_s(base=base_dn, scope=search_scope, filterstr='mailNickname=jua', attrlist=attributes)
5/29: ad.search_s(base=base_dn, scope=ldap.SCOPE_BASE, filterstr='mailNickname=', attrlist=attributes)
5/30: ad.search_s(base=base_dn, scope=ldap.SCOPE_BASE, filterstr='mailNickname=nka', attrlist=attributes)
5/31: ad.search_s(base=base_dn, scope=ldap.SCOPE_BASE, filterstr='mailNickname=pacu', attrlist=attributes)
5/32: ad.search_s(base=base_dn, scope=ldap.SCOPE_ONELEVEL, filterstr='mailNickname=pacu', attrlist=attributes)
5/33: ad.search_s(base=base_dn, scope=ldap.SCOPE_ONELEVEL, filterstr='mailNickname=nka', attrlist=attributes)
5/34: clear
5/35: ad.search_s(base=base_dn, scope=ldap.SCOPE_SUBORDINATE, filterstr='mailNickname=pacu', attrlist=attributes)
5/36: ad.search_s(base=base_dn, scope=ldap.SCOPE_SUBORDINATE, filterstr='mailNickname=nka', attrlist=attributes)
5/37: ad.search_s(base=base_dn, scope=ldap.SCOPE_SUBTREE, filterstr='mailNickname=nka', attrlist=attributes)
5/38: ad.search_s(base=base_dn, scope=ldap.SCOPE_SUBORDINATE, filterstr='mailNickname=pacu', attrlist=attributes)
5/39: clear
5/40: ad.search_s(base=base_dn, scope=ldap.SCOPE_SUBORDINATE, filterstr='sAMAccountName=pacu', attrlist=attributes)
5/41: clear
5/42: ad.search_s(base=base_dn, scope=ldap.SCOPE_SUBTREE, filterstr='sAMAccountName=nka', attrlist=attributes)
5/43: ad.search_s(base=base_dn, scope=ldap.SCOPE_SUBTREE, filterstr='sAMAccountName=pacu', attrlist=attributes)
5/44: ad.search_s(base=base_dn, scope=ldap.SCOPE_SUBTREE, filterstr='sAMAccountName=dade', attrlist=attributes)
5/45: ad.search_s(base=base_dn, scope=ldap.SCOPE_SUBTREE, filterstr='sAMAccountName=jhd', attrlist=attributes)
5/46: ad.search_s(base=base_dn, scope=ldap.SCOPE_SUBTREE, filterstr='sAMAccountName=jd', attrlist=attributes)
5/47: ad.search_s(base=base_dn, scope=ldap.SCOPE_SUBTREE, filterstr='sAMAccountName=nka', attrlist=attributes)
5/48:
            ad.simple_bind_s('%s@millemercis.com' % username, password)
            base_dn = 'dc=millemercis, dc=com'
            search_scope = ldap.SCOPE_SUBTREE
            search_filter = 'mailNickname=%s' % username
            attributes = ['displayName', 'mail', 'sAMAccountName', 'distinguishedName', 'memberOf']  # All attributes
5/49: clear
5/50: ad.search_s(base=base_dn, scope=ldap.SCOPE_SUBTREE, filterstr='sAMAccountName=nka', attrlist=attributes)
5/51: attributes
 7/1: from millemercis.op.services.coupon import CouponService
 7/2: CouponService
 7/3: help(CouponService)
 8/1: import requests
 8/2: help(requests.get)
 8/3: requests.get(url='127.0.0.1:8080/api/v0/ysl_tatouagelipstick/v1/session/token')
 8/4: requests.get(url='http://127.0.0.1:8080/api/v0/ysl_tatouagelipstick/v1/session/token')
 8/5: resp = requests.get(url='http://127.0.0.1:8080/api/v0/ysl_tatouagelipstick/v1/session/token')
 8/6: resp
 8/7: resp.text
 9/1: import requests
 9/2: resp = requests.get(url='http://127.0.0.1:8080/api/v0/ysl_tatouagelipstick/v1/session/token')
 9/3: res.json()
 9/4: resp.json()
 9/5: d = resp.json()
 9/6: d.get("dara")
 9/7: d.get("data", 400)
 9/8: d.get("dataj", 400)
10/1: import requests
10/2: resp = requests.post(url='http://127.0.0.1:8080/api/v0/ysl_tatouagelipstick/v1/sessio/token')
10/3: resp.data()
10/4: resp.json()
10/5: resp = requests.post(url='http://127.0.0.1:8080/api/v0/ysl_tatouagelipstick/v1/sessio/token', data={})
10/6: resp.json()
11/1: import requests
11/2: data = json.dumps({})
11/3: import json
11/4: data = json.dumps({})
11/5: data
11/6: resp = requests.post(url='http://127.0.0.1:8080/api/v0/ysl_tatouagelipstick/v1/sessio/token', data='{}')
11/7: resp.json()
11/8: resp = requests.post(url='http://127.0.0.1:8080/api/v0/ysl_tatouagelipstick/v1/sessio/token', json='{}')
11/9: resp.json()
11/10: resp = requests.post(url='http://127.0.0.1:8080/api/v0/ysl_tatouagelipstick/v1/session/token', json='{}')
11/11: resp.json()
11/12: resp = requests.post(url='http://127.0.0.1:8080/api/v0/ysl_tatouagelipstick/v1/session/token', json={})
11/13: resp.json()
13/1: int(5.5)
13/2: round(5.5)
13/3: int(5.9)
14/1: from pygrok import Grok
14/2: text = "2018-03-26 11:21:54 :: pierrevacances_paradis2018 :: http://monparadis-pierreetvacances.com/api/v0/pierrevacances_paradis2018/v1/track/page_view?token=e4f810f56a8448a6889c662ea26a823e :: INFO :: token :: get_token_by_id [l.80] :: e4f810f56a8448a6889c662ea26a823e :: api.core :: :: token_id=e4f810f56a8448a6889c662ea26a823e token={u'uid': None, u'idU': None, u'expiredAt': datetime.datetime(2018, 3, 26, 9, 41, 53, 944000), u'ueId': None, u'fromId': 8, u'_id': u'e4f810f56a8448a6889c662ea26a823e', u'parrainId': None, u'visitId': 90095}"
14/3: pattern = "%{TIMESTAMP_ISO8601:datetime} :: %{WORD:op_name} :: {URI:url} :: %{LOGLEVEL:level} :: %{GREEDYDATA:message}"
14/4: grok = Grok(pattern)
14/5: grok.match(text)
14/6: grok
14/7: grok.match(text)
14/8: pattern = "%{DATA:datetime} :: %{WORD:op_name} :: {URI:url} :: %{LOGLEVEL:level} :: %{GREEDYDATA:message}"
14/9: grok = Grok(pattern)
14/10: grok.match(text)
14/11:
text = 'gary is male, 25 years old and weighs 68.5 kilograms'
pattern = '%{WORD:name} is %{WORD:gender}, %{NUMBER:age} years old and weighs %{NUMBER:weight} kilograms'
grok = Grok(pattern)
print grok.match(text)
14/12: print(grok.match(text))
14/13: text = "2018-03-26 11:21:54 :: pierrevacances_paradis2018 :: http://monparadis-pierreetvacances.com/api/v0/pierrevacances_paradis2018/v1/track/page_view?token=e4f810f56a8448a6889c662ea26a823e :: INFO :: token :: get_token_by_id [l.80] :: e4f810f56a8448a6889c662ea26a823e :: api.core :: :: token_id=e4f810f56a8448a6889c662ea26a823e token={u'uid': None, u'idU': None, u'expiredAt': datetime.datetime(2018, 3, 26, 9, 41, 53, 944000), u'ueId': None, u'fromId': 8, u'_id': u'e4f810f56a8448a6889c662ea26a823e', u'parrainId': None, u'visitId': 90095}"
14/14: pattern = "%{TIMESTAMP_ISO8601:datetime} :: %{WORD:op_name} :: {URI:url} :: %{LOGLEVEL:level} :: %{GREEDYDATA:message}"
14/15: grok = Grok(pattern)
14/16: grok.match(text)
14/17: grok(grok.match(text))
14/18: print(grok.match(text))
14/19: pattern = "%{DATA:datetime} :: %{WORD:op_name} :: {URI:url} :: %{LOGLEVEL:level} :: %{GREEDYDATA:message}"
14/20: grok = Grok(pattern)
14/21: grok.match(text)
15/1: from pygrok import Grok
15/2:
text2 = "2018-03-26 11:21:54 :: pierrevacances_paradis2018 :: "\
    "http://monparadis-pierreetvacances.com/api/v0/pierrevacances_paradis2018/v1/track/page_view?token=e4f810f56a8448a6889c662ea26a823e"\
    " :: INFO :: token :: get_token_by_id [l.80] :: e4f810f56a8448a6889c662ea26a823e"\
    " :: api.core ::  :: token_id=e4f810f56a8448a6889c662ea26a823e token={u'uid': None, u'idU': None, u'expiredAt': datetime.datetime(2018, 3, 26, 9, 41, 53, 944000), u'ueId': None, u'fromId': 8, u'_id': u'e4f810f56a8448a6889c662ea26a823e', u'parrainId': None, u'visitId': 90095}"
    pattern2 = "%{DATESTAMP:datetime} :: %{WORD:op_name} :: %{URI:url} :: %{LOGLEVEL:level}"\
    " :: %{WORD:module} :: %{WORD:funcName} \[l.%{INT:linuNum}\] :: %{WORD:token}"\
    " :: %{USERNAME:logger} :: %{DATA:email} :: %{GREEDYDATA:message}"
15/3:
text2 = "2018-03-26 11:21:54 :: pierrevacances_paradis2018 :: "\
    "http://monparadis-pierreetvacances.com/api/v0/pierrevacances_paradis2018/v1/track/page_view?token=e4f810f56a8448a6889c662ea26a823e"\
    " :: INFO :: token :: get_token_by_id [l.80] :: e4f810f56a8448a6889c662ea26a823e"\
    " :: api.core ::  :: token_id=e4f810f56a8448a6889c662ea26a823e token={u'uid': None, u'idU': None, u'expiredAt': datetime.datetime(2018, 3, 26, 9, 41, 53, 944000), u'ueId': None, u'fromId': 8, u'_id': u'e4f810f56a8448a6889c662ea26a823e', u'parrainId': None, u'visitId': 90095}"

pattern2 = "%{DATESTAMP:datetime} :: %{WORD:op_name} :: %{URI:url} :: %{LOGLEVEL:level}"\
    " :: %{WORD:module} :: %{WORD:funcName} \[l.%{INT:linuNum}\] :: %{WORD:token}"\
    " :: %{USERNAME:logger} :: %{DATA:email} :: %{GREEDYDATA:message}"
15/4: grok = Grok(pattern2)
15/5: %timeit grok.match(text2)
15/6: text = " fsdfddfdsfsfdf sf sdf  :: s dfssf"
15/7: %timeit grok.match(text2)
15/8: text = "[spooler /var/spool/uwsgi/op/error_emails pid: 11428] managing request uwsgi_spoolfile_on_http-pr-3-p2_27510_2_1338606540_1494025812_408885 ..."
15/9: %timeit grok.match(text2)
15/10: %timeit grok.match(text)
15/11: text3 = "INFO:api.core.db:ws_insert_result - took 0.00491809844971 s."
15/12: %timeit grok.match(text)
15/13: %timeit grok.match(text3)
15/14: %timeit grok.match(text3)
15/15: %timeit grok.match(text2)
15/16: %timeit grok.match(text2)
15/17: %timeit grok.match(text)
15/18: %timeit grok.match(text3)
15/19: text4 = 'DEBUG:requests.packages.urllib3.connectionpool:"POST /front/getprofiles/pv HTTP/1.1" 200 63'
15/20: %timeit grok.match(text4)
15/21: %timeit grok.match(text4)
15/22: %timeit grok.match(text4)
15/23: %timeit grok.match(text3)
15/24: grok.match(text3)
15/25: grok.match(text2)
16/1: import requests
16/2: requests.get(url='example.com').json()
16/3: requests.get(url='http://example.com').json()
16/4: requests.get(url='http://example.com')
16/5: requests.get(url='http://example.com').text()
16/6: requests.get(url='http://example.com').text
16/7: requests.get(url='http://example.com', payload={}).text
16/8: requests.post(url='http://example.com', payload={}).text
16/9: requests.get(url='http://example.com', json={}).text
16/10: requests.get(url='http://example.com').text
16/11: requests.get(url='http://example.com', json={}).text
16/12: requests.post(url='http://example.com', json={}).text
16/13: type(requests)
16/14: type(requests.get)
16/15: getattr(requests, 'get')
17/1: from pygments import lexers
17/2: lexers.JsonLexer()
17/3: lexers.HTMLLexer()
17/4: help(lexers)
17/5: lexers.HtmlLexer()
18/1: import datetime
18/2: datetime.strptime("2018-04-09 12:23:21")
18/3: strptime("2018-04-09 12:23:21")
18/4: datetime.datetime.strptime("2018-04-09 12:23:21")
18/5: help(datetime.datetime.strptime)
18/6: datetime.datetime.strptime("2018-04-09 12:23:21", "%Y-%m-%d %H:%M:S")
18/7: datetime.datetime.strptime("2018-04-09 12:23:21", "%Y-%m-%d %H:%M:%S")
18/8: datetime.datetime.strptime("2018-04-09 12:23:21", "%Y-%m-%d %H:%M:%S").isoformat()
18/9: type(datetime.datetime.strptime("2018-04-09 12:23:21", "%Y-%m-%d %H:%M:%S").isoformat())
19/1: import requests
19/2:
payload = {
    "idCampaign": "44b517df15",
    "dateLeadCollected": "2017-01-19T13:34:20+01:00",
    "acceptEndUserAgreement": true,
    "mode":"dryrun",
    "contact": {
        "salutation": "m",
        "lastname": "jean",
        "firstname": "guyberret",
        "phone1": "+33677264435",
        "email": "jean.guyberret@gmail.com",
        "type": "part"
    },
    "project": {
        "description": "peinture de mes volets",
        "address": {
            "postalCode": "78220",
            "city": "viroflay"
        },
        "categoryId": 9999
    }
}
19/3: payload = "{\n\t\"idCampaign\": \"44b517df15\",\n\t\"dateLeadCollected\": \"2017-01-19T13:34:20+01:00\",\n\t\"acceptEndUserAgreement\": true,\n\t\"mode\":\"dryrun\",\n\t\"contact\": {\n\t\t\"salutation\": \"m\",\n\t\t\"lastname\": \"jean\",\n\t\t\"firstname\": \"guyberret\",\n\t\t\"phone1\": \"+33677264435\",\n\t\t\"email\": \"jean.guyberret@gmail.com\",\n\t\t\"type\": \"part\"\n\t},\n\t\"project\": {\n\t\t\"description\": \"peinture de mes volets\",\n\t\t\"address\": {\n\t\t\t\"postalCode\": \"78220\",\n\t\t\t\"city\": \"viroflay\"\n\t\t},\n\t\t\"categoryId\": 9999\n\t}\n}"
19/4: requests.post(data=payload, auth=('partner_1000mercis', 'ne5<y=!_~QDhS_jF_X4|B$U0ocR2Y3'))
19/5: requests.post(url='https://partnership.homly-you.com/rest/v2/lead/create', data=payload, auth=('partner_1000mercis', 'ne5<y=!_~QDhS_jF_X4|B$U0ocR2Y3'))
19/6: res = requests.post(url='https://partnership.homly-you.com/rest/v2/lead/create', data=payload, auth=('partner_1000mercis', 'ne5<y=!_~QDhS_jF_X4|B$U0ocR2Y3'))
19/7: res.text
19/8:
pld = payload = {
            "idCampaign": "44b517df15",
            "dateLeadCollected": user["dCrea"].isoformat(),
            "acceptEndUserAgreement": True,
            "idLeadPartner": "string",
            "formName": "string",
            "refererType": "string",
            "mode": "dryrun",
            "contact": {
                "salutation": user["civilite"],
                "firstname": user["Nom"],
                "lastname": user["Prenom"],
                "phone1": user["telmobile"],
                "email": user["Email"],
                "type": "part"
            },
            "project": {
                "description": "string",
                "address": {
                    "city": user["Ville"],
                    "insee": "string",
                    "postalCode": user["CP"]
                },
                "categoryId": 9999,
            },
            "customData": "string",
            # "callbackUrl": "string",
        }
19/9:
pld = {
"idCampaign": "cf5bb03e2f",
"dateLeadCollected": "2017-01-19T13:34:20+01:00",
"acceptEndUserAgreement": true,
"mode":"dryrun",
"contact": {
"salutation": "m",
"lastname": "jean",
"firstname": "guyberret",
"phone1": "+33677264435",
"email": "jean.guyberret@gmail.com",
"type": "part"
},
"project": {
"description": "peinture de mes volets",
"address": {
"postalCode": "78220",
"city": "viroflay"
},
"categoryId":1027
}
}
19/10:
pld = {
"idCampaign": "cf5bb03e2f",
"dateLeadCollected": "2017-01-19T13:34:20+01:00",
"acceptEndUserAgreement": True,
"mode":"dryrun",
"contact": {
"salutation": "m",
"lastname": "jean",
"firstname": "guyberret",
"phone1": "+33677264435",
"email": "jean.guyberret@gmail.com",
"type": "part"
},
"project": {
"description": "peinture de mes volets",
"address": {
"postalCode": "78220",
"city": "viroflay"
},
"categoryId":9999
}
}
19/11: res = requests.post(url='https://partnership.homly-you.com/rest/v2/lead/create', data=pld, auth=('partner_1000mercis', 'ne5<y=!_~QDhS_jF_X4|B$U0ocR2Y3'))
19/12: res.text
19/13: res = requests.post(url='https://partnership.homly-you.com/rest/v2/lead/create', json=pld, auth=('partner_1000mercis', 'ne5<y=!_~QDhS_jF_X4|B$U0ocR2Y3'))
19/14: res.text
19/15: user={u'Etape': 0, u'Nom': u'user', u'idu_email': 27, u'Prenom': u'random', u'JeuOK': 1, u'idU': 55, u'dCrea': datetime.datetime(2018, 4, 10, 9, 39, 38, 457000), u'Ville': u'Paris', u'iduParrain': None, u'telmobile': None, u'civilite': u'M.', u'id_From': 0, u'CP': u'75006', u'Email': u'udc5bsbs6lr0bb2@example.com', u'id_Declinaison_Culture': None, u'uid': UUID('4e5bd049-b5da-48f2-81f9-8417a0b8ab7a')}
19/16: from datetime import datetime
19/17: user={u'Etape': 0, u'Nom': u'user', u'idu_email': 27, u'Prenom': u'random', u'JeuOK': 1, u'idU': 55, u'dCrea': datetime.datetime(2018, 4, 10, 9, 39, 38, 457000), u'Ville': u'Paris', u'iduParrain': None, u'telmobile': None, u'civilite': u'M.', u'id_From': 0, u'CP': u'75006', u'Email': u'udc5bsbs6lr0bb2@example.com', u'id_Declinaison_Culture': None, u'uid': UUID('4e5bd049-b5da-48f2-81f9-8417a0b8ab7a')}
19/18: import datetime
19/19: user={u'Etape': 0, u'Nom': u'user', u'idu_email': 27, u'Prenom': u'random', u'JeuOK': 1, u'idU': 55, u'dCrea': datetime.datetime(2018, 4, 10, 9, 39, 38, 457000), u'Ville': u'Paris', u'iduParrain': None, u'telmobile': None, u'civilite': u'M.', u'id_From': 0, u'CP': u'75006', u'Email': u'udc5bsbs6lr0bb2@example.com', u'id_Declinaison_Culture': None, u'uid': UUID('4e5bd049-b5da-48f2-81f9-8417a0b8ab7a')}
19/20: user={u'Etape': 0, u'Nom': u'user', u'idu_email': 27, u'Prenom': u'random', u'JeuOK': 1, u'idU': 55, u'dCrea': datetime.datetime(2018, 4, 10, 9, 39, 38, 457000), u'Ville': u'Paris', u'iduParrain': None, u'telmobile': None, u'civilite': u'M.', u'id_From': 0, u'CP': u'75006', u'Email': u'udc5bsbs6lr0bb2@example.com', u'id_Declinaison_Culture': None}
19/21:
pld = payload = {
            "idCampaign": "44b517df15",
            "dateLeadCollected": user["dCrea"].isoformat(),
            "acceptEndUserAgreement": True,
            "idLeadPartner": "string",
            "formName": "string",
            "refererType": "string",
            "mode": "dryrun",
            "contact": {
                "salutation": user["civilite"],
                "firstname": user["Nom"],
                "lastname": user["Prenom"],
                "phone1": user["telmobile"],
                "email": user["Email"],
                "type": "part"
            },
            "project": {
                "description": "string",
                "address": {
                    "city": user["Ville"],
                    "insee": "string",
                    "postalCode": user["CP"]
                },
                "categoryId": 9999,
            },
            "customData": "string",
            # "callbackUrl": "string",
        }
19/22: pld
19/23: payload
19/24: res = requests.post(url='https://partnership.homly-you.com/rest/v2/lead/create', json=pld, auth=('partner_1000mercis', 'ne5<y=!_~QDhS_jF_X4|B$U0ocR2Y3'))
19/25: res.text
19/26: requests.post(url='https://partnership.homly-you.com/rest/v2/lead/create', json=pld, auth=('partner_1000mercis', 'ne5<y=!_~QDhS_jF_X4|B$U0ocR2Y3')).text
19/27:
payload = {
            "idCampaign": "44b517df15",
            "dateLeadCollected": user["dCrea"].isoformat(),
            "acceptEndUserAgreement": True,
            "idLeadPartner": "string",
            "formName": "string",
            "refererType": "string",
            "mode": "dryrun",
            "contact": {
                "salutation": "m",
                "firstname": user["Nom"],
                "lastname": user["Prenom"],
                "phone1": user["telmobile"],
                "email": user["Email"],
                "type": "part"
            },
            "project": {
                "description": "string",
                "address": {
                    "city": user["Ville"],
                    "insee": "string",
                    "postalCode": user["CP"]
                },
                "categoryId": 9999,
            },
            "customData": "string",
            # "callbackUrl": "string",
        }
19/28: requests.post(url='https://partnership.homly-you.com/rest/v2/lead/create', json=pld, auth=('partner_1000mercis', 'ne5<y=!_~QDhS_jF_X4|B$U0ocR2Y3')).text
19/29: requests.post(url='https://partnership.homly-you.com/rest/v2/lead/create', json=payload, auth=('partner_1000mercis', 'ne5<y=!_~QDhS_jF_X4|B$U0ocR2Y3')).text
19/30: requests.post(url='https://partnership.homly-you.com/rest/v2/lead/create', json=payload, auth=('partner_1000mercis', 'ne5<y=!_~QDhS_jF_X4|B$U0ocR2Y3')).json
19/31: requests.post(url='https://partnership.homly-you.com/rest/v2/lead/create', json=payload, auth=('partner_1000mercis', 'ne5<y=!_~QDhS_jF_X4|B$U0ocR2Y3')).json()
19/32: user["dCrea"]
19/33: user["dCrea"].isoformat()
19/34:
payload = {
            "idCampaign": "44b517df15",
            "dateLeadCollected": user["dCrea"].isoformat(),
            "acceptEndUserAgreement": True,
            # "formName": "string"
            # "refererType": "string",
            "mode": "dryrun",
            "contact": {
                "salutation": "m",
                "firstname": user["Nom"],
                "lastname": user["Prenom"],
                "phone1": user["telmobile"],
                "email": user["Email"],
                "type": "part"
            },
            "project": {
                "description": "string",
                "address": {
                    "city": user["Ville"],
                    "insee": "string",
                    "postalCode": user["CP"]
                },
                "categoryId": 9999,
            },
            "customData": "string",
            # "callbackUrl": "string",
        }
19/35: requests.post(url='https://partnership.homly-you.com/rest/v2/lead/create', json=payload, auth=('partner_1000mercis', 'ne5<y=!_~QDhS_jF_X4|B$U0ocR2Y3')).json()
19/36:
payload = {
            "idCampaign": "44b517df15",
            "dateLeadCollected": user["dCrea"].isoformat(),
            "acceptEndUserAgreement": True,
            # "formName": "string"
            # "refererType": "string",
            "mode": "dryrun",
            "contact": {
                "salutation": "m",
                "firstname": user["Nom"],
                "lastname": user["Prenom"],
                "phone1": user["telmobile"],
                "email": user["Email"],
                "type": "part"
            },
            "project": {
                "description": "string",
                "address": {
                    "city": user["Ville"],
                    # "insee": "string",
                    "postalCode": user["CP"]
                },
                "categoryId": 9999,
            },
            "customData": "string",
            # "callbackUrl": "string",
        }
19/37: requests.post(url='https://partnership.homly-you.com/rest/v2/lead/create', json=payload, auth=('partner_1000mercis', 'ne5<y=!_~QDhS_jF_X4|B$U0ocR2Y3')).json()
19/38: payload
19/39:
pld = {
    "project": {
        "categoryId": 9999,
        "description": "string",
        "address": {
            "postalCode": "75006",
            "city": "Paris"
        }
    },
    "idCampaign": "44b517df15",
    "mode": "dryrun",
    "dateLeadCollected": "2018-04-10T09:57+00:00",
    "contact": {
        "firstname": "user",
        "lastname": "random
19/40:
pld = {
"project": {
"categoryId": 9999,
"description": "string",
"address": {
"postalCode": "75006",
"city": "Paris"
}
},
"idCampaign": "44b517df15",
"mode": "dryrun",
"dateLeadCollected": "2018-04-10T09:57+00:00",
"contact": {
"firstname": "user",
"lastname": "random",
"salutation": "m",
"type": "part",
"email": "6kgb852myirx0e3@example.com",
"phone1": "0033677264435"

},
"customData": "string",
"acceptEndUserAgreement": true,
"formName": "string"
}
19/41:
pld = {
"project": {
"categoryId": 9999,
"description": "string",
"address": {
"postalCode": "75006",
"city": "Paris"
}
},
"idCampaign": "44b517df15",
"mode": "dryrun",
"dateLeadCollected": "2018-04-10T09:57+00:00",
"contact": {
"firstname": "user",
"lastname": "random",
"salutation": "m",
"type": "part",
"email": "6kgb852myirx0e3@example.com",
"phone1": "0033677264435"

},
"customData": "string",
"acceptEndUserAgreement": True,
"formName": "string"
}
19/42: requests.post(url='https://partnership.homly-you.com/rest/v2/lead/create', json=payload, auth=('partner_1000mercis', 'ne5<y=!_~QDhS_jF_X4|B$U0ocR2Y3')).json()
19/43: requests.post(url='https://partnership.homly-you.com/rest/v2/lead/create', data=payload, auth=('partner_1000mercis', 'ne5<y=!_~QDhS_jF_X4|B$U0ocR2Y3')).json()
19/44: requests.post(url='https://partnership.homly-you.com/rest/v2/lead/create', json=payload, auth=('partner_1000mercis', 'ne5<y=!_~QDhS_jF_X4|B$U0ocR2Y3')).json()
19/45:
pld = {
"project": {
"categoryId": 9999,
"description": "string",
"address": {
"postalCode": "75006",
"city": "Paris"
}
},
"idCampaign": "44b517df15",
"mode": "dryrun",
"dateLeadCollected": "2018-04-10T09:57+00:00",
"contact": {
"firstname": "user",
"lastname": "random",
"salutation": "m",
"type": "part",
"email": "6kgb852myirx0e3@example.com",
"phone1": "0033677264435"

},
"customData": "string",
"acceptEndUserAgreement": True,
"formName": "string"
}
19/46:
url = "https://partnership.homly-you.com/rest/v2/lead/create"

payload = "{\n\"project\": {\n\"categoryId\": 9999,\n\"description\": \"string\",\n\"address\": {\n\"postalCode\": \"75006\",\n\"city\": \"Paris\"\n}\n},\n\"idCampaign\": \"44b517df15\",\n\"mode\": \"dryrun\",\n\"dateLeadCollected\": \"2018-04-10T09:57+00:00\",\n\"contact\": {\n\"firstname\": \"user\",\n\"lastname\": \"random\",\n\"salutation\": \"m\",\n\"type\": \"part\",\n\"email\": \"6kgb852myirx0e3@example.com\",\n\"phone1\": \"0033677264435\"\n},\n\"customData\": \"string\",\n\"acceptEndUserAgreement\": true,\n\"formName\": \"string\"\n}\n"
headers = {
    'Content-Type': "application/json",
    'Authorization': "Basic cGFydG5lcl8xMDAwbWVyY2lzOm5lNTx5PSFfflFEaFNfakZfWDR8QiRVMG9jUjJZMw==",
    'Cache-Control': "no-cache",
    'Postman-Token': "4d7f3892-a354-4b30-ad6d-c58be9209036"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
19/47: response = requests.request("POST", url, data=payload, headers=headers, auth=('partner_1000mercis', 'ne5<y=!_~QDhS_jF_X4|B$U0ocR2Y3'))
19/48: response.text
19/49:
pld = {
"project": {
"categoryId": 9999,
"description": "string",
"address": {
"postalCode": "75006",
"city": "Paris"
}
},
"idCampaign": "44b517df15",
"mode": "dryrun",
"dateLeadCollected": "2018-04-10T09:57+00:00",
"contact": {
"firstname": "user",
"lastname": "random",
"salutation": "m",
"type": "part",
"email": "6kgb852myirx0e3@example.com",
"phone1": "0033677264435"

},
"customData": "string",
"acceptEndUserAgreement": True,
"formName": "string"
}
19/50: requests.post(url='https://partnership.homly-you.com/rest/v2/lead/create', json=pld, auth=('partner_1000mercis', 'ne5<y=!_~QDhS_jF_X4|B$U0ocR2Y3')).json()
19/51:
payload = {
            "idCampaign": "44b517df15",
            "dateLeadCollected": user["dCrea"].isoformat(),
            "acceptEndUserAgreement": True,
            # "formName": "string"
            # "refererType": "string",
            "mode": "dryrun",
            "contact": {
                "salutation": "m",
                "firstname": user["Nom"],
                "lastname": user["Prenom"],
                "phone1": user["telmobile"],
                "email": user["Email"],
                "type": "part"
            },
            "project": {
                "description": "string",
                "address": {
                    "city": user["Ville"],
                    # "insee": "string",
                    "postalCode": user["CP"]
                },
                "categoryId": 9999,
            },
            "customData": "string",
            # "callbackUrl": "string",
        }
19/52: payload
19/53: pld
19/54:
payload = {
            "idCampaign": "44b517df15",
            "dateLeadCollected": user["dCrea"].isoformat(),
            "acceptEndUserAgreement": True,
            # "formName": "string"
            # "refererType": "string",
            "mode": "dryrun",
            "contact": {
                "salutation": "m",
                "firstname": user["Nom"],
                "lastname": user["Prenom"],
                "phone1": "0033677264435",
                "email": user["Email"],
                "type": "part"
            },
            "project": {
                "description": "string",
                "address": {
                    "city": user["Ville"],
                    # "insee": "string",
                    "postalCode": user["CP"]
                },
                "categoryId": 9999,
            },
            "customData": "string",
            # "callbackUrl": "string",
        }
19/55: requests.post(url='https://partnership.homly-you.com/rest/v2/lead/create', json=payload, auth=('partner_1000mercis', 'ne5<y=!_~QDhS_jF_X4|B$U0ocR2Y3')).json()
19/56: user["dCrea"]
19/57: user["dCrea"].isoformat()
19/58: help(user["dCrea"].isoformat)
19/59: user["dCrea"].isoformat()
19/60: import pytz
19/61: local_tz = pytz.timezone('Europe/Paris')
19/62: ud = user["dCrea"]
19/63: ud
19/64: ud.replace(tzinfo=pytz.utc)
19/65: ud.isoformat()
19/66: ud.replace(tzinfo=pytz.timezone('Europe/Paris'))
19/67: ud.isoformat()
19/68: ud
19/69: ud.replace(tzinfo=pytz.timezone('Europe/Paris')).isoformat()
19/70: ud.replace(tzinfo=pytz.utc).isoformat()
19/71: ud.replace(tzinfo=pytz.utc).astimezone(local_tz).isoformat()
19/72: ud.astimezone(local_tz).isoformat()
19/73: ud.replace(tzinfo=pytz.utc).astimezone(local_tz)
19/74: ud.replace(tzinfo=local_tz).isoformat()
19/75: ud.replace(tzinfo=pytz.utc).astimezone(local_tz).isoformat()
19/76:
payload = {
            "idCampaign": "44b517df15",
            "dateLeadCollected": user["dCrea"].replace(tzinfo=pytz.utc).astimezone(pytz.timezone(Europe/Paris)).isoformat(),
            "acceptEndUserAgreement": True,
            # "formName": "string"
            # "refererType": "string",
            "mode": "dryrun",
            "contact": {
                "salutation": "m",
                "firstname": user["Nom"],
                "lastname": user["Prenom"],
                "phone1": "0033677264435",
                "email": user["Email"],
                "type": "part"
            },
            "project": {
                "description": "string",
                "address": {
                    "city": user["Ville"],
                    # "insee": "string",
                    "postalCode": user["CP"]
                },
                "categoryId": 9999,
            },
            "customData": "string",
            # "callbackUrl": "string",
        }
19/77:
payload = {
            "idCampaign": "44b517df15",
            "dateLeadCollected": user["dCrea"].replace(tzinfo=pytz.utc).astimezone(pytz.timezone('Europe/Paris')).isoformat(),
            "acceptEndUserAgreement": True,
            # "formName": "string"
            # "refererType": "string",
            "mode": "dryrun",
            "contact": {
                "salutation": "m",
                "firstname": user["Nom"],
                "lastname": user["Prenom"],
                "phone1": "0033677264435",
                "email": user["Email"],
                "type": "part"
            },
            "project": {
                "description": "string",
                "address": {
                    "city": user["Ville"],
                    # "insee": "string",
                    "postalCode": user["CP"]
                },
                "categoryId": 9999,
            },
            "customData": "string",
            # "callbackUrl": "string",
        }
19/78: requests.post(url='https://partnership.homly-you.com/rest/v2/lead/create', json=payload, auth=('partner_1000mercis', 'ne5<y=!_~QDhS_jF_X4|B$U0ocR2Y3')).json()
19/79: import json
19/80: json.decode({"payload": {"idCampaign": "44b517df15", "acceptEndUserAgreement": true, "project": {"categoryId": 9999, "description": "non compl\u00e9t\u00e9", "address": {"postalCode": "75006", "city": "Paris", "insee": "75106"}}, "contact": {"firstname": "random", "lastname": "user", "phone1": "+33612345678", "salutation": "mr", "type": "part", "email": "ikx8nktzz0jwi@example.com"}, "mode": "dryrun", "dateLeadCollected": "2018-04-12T18:37:34.590000+02:00"}, "ws_url": "https://partnership.homly-you.com/rest/v2/lead/create"})
19/81: json.dumps({"payload": {"idCampaign": "44b517df15", "acceptEndUserAgreement": true, "project": {"categoryId": 9999, "description": "non compl\u00e9t\u00e9", "address": {"postalCode": "75006", "city": "Paris", "insee": "75106"}}, "contact": {"firstname": "random", "lastname": "user", "phone1": "+33612345678", "salutation": "mr", "type": "part", "email": "ikx8nktzz0jwi@example.com"}, "mode": "dryrun", "dateLeadCollected": "2018-04-12T18:37:34.590000+02:00"}, "ws_url": "https://partnership.homly-you.com/rest/v2/lead/create"})
19/82: json.loads({"payload": {"idCampaign": "44b517df15", "acceptEndUserAgreement": true, "project": {"categoryId": 9999, "description": "non compl\u00e9t\u00e9", "address": {"postalCode": "75006", "city": "Paris", "insee": "75106"}}, "contact": {"firstname": "random", "lastname": "user", "phone1": "+33612345678", "salutation": "mr", "type": "part", "email": "ikx8nktzz0jwi@example.com"}, "mode": "dryrun", "dateLeadCollected": "2018-04-12T18:37:34.590000+02:00"}, "ws_url": "https://partnership.homly-you.com/rest/v2/lead/create"})
19/83: json.loads('{"payload": {"idCampaign": "44b517df15", "acceptEndUserAgreement": true, "project": {"categoryId": 9999, "description": "non compl\u00e9t\u00e9", "address": {"postalCode": "75006", "city": "Paris", "insee": "75106"}}, "contact": {"firstname": "random", "lastname": "user", "phone1": "+33612345678", "salutation": "mr", "type": "part", "email": "ikx8nktzz0jwi@example.com"}, "mode": "dryrun", "dateLeadCollected": "2018-04-12T18:37:34.590000+02:00"}, "ws_url": "https://partnership.homly-you.com/rest/v2/lead/create"}')
19/84:
pl = {u'payload': {u'acceptEndUserAgreement': True,
  u'contact': {u'email': u'ikx8nktzz0jwi@example.com',
   u'firstname': u'random',
   u'lastname': u'user',
   u'phone1': u'+33612345678',
   u'salutation': u'mr',
   u'type': u'part'},
  u'dateLeadCollected': u'2018-04-12T18:37:34.590000+02:00',
  u'idCampaign': u'44b517df15',
  u'mode': u'dryrun',
  u'project': {u'address': {u'city': u'Paris',
    u'insee': u'75106',
    u'postalCode': u'75006'},
   u'categoryId': 9999,
   u'description': u'non complété'}},
 u'ws_url': u'https://partnership.homly-you.com/rest/v2/lead/create'}
19/85: pl
19/86: json.dumps(pl, ensure_ASCII=False)
19/87: json.dumps(pl, ensure_ascii=False)
19/88: bla =
19/89: bla = json.dumps(pl, ensure_ascii=False)
19/90: bla
19/91: json.loads(bla)
19/92: json.loads(bla, ensure_ascii=False)
19/93:
pl = {u'payload': {u'acceptEndUserAgreement': True,
  u'contact': {u'email': u'ikx8nktzz0jwi@example.com',
   u'firstname': u'random',
   u'lastname': u'user',
   u'phone1': u'+33612345678',
   u'salutation': u'mr',
   u'type': u'part'},
  u'dateLeadCollected': u'2018-04-12T18:37:34.590000+02:00',
  u'idCampaign': u'44b517df15',
  u'mode': u'dryrun',
  u'project': {u'address': {u'city': u'Paris',
    u'insee': u'75106',
    u'postalCode': u'75006'},
   u'categoryId': 9999,
   u'description': 'non complété'.encode('utf-8')}},
 u'ws_url': u'https://partnership.homly-you.com/rest/v2/lead/create'}
19/94:
pl = {u'payload': {u'acceptEndUserAgreement': True,
  u'contact': {u'email': u'ikx8nktzz0jwi@example.com',
   u'firstname': u'random',
   u'lastname': u'user',
   u'phone1': u'+33612345678',
   u'salutation': u'mr',
   u'type': u'part'},
  u'dateLeadCollected': u'2018-04-12T18:37:34.590000+02:00',
  u'idCampaign': u'44b517df15',
  u'mode': u'dryrun',
  u'project': {u'address': {u'city': u'Paris',
    u'insee': u'75106',
    u'postalCode': u'75006'},
   u'categoryId': 9999,
   u'description': 'non complété'.decode('latint-1').encode('utf-8')}},
 u'ws_url': u'https://partnership.homly-you.com/rest/v2/lead/create'}
19/95:
pl = {u'payload': {u'acceptEndUserAgreement': True,
  u'contact': {u'email': u'ikx8nktzz0jwi@example.com',
   u'firstname': u'random',
   u'lastname': u'user',
   u'phone1': u'+33612345678',
   u'salutation': u'mr',
   u'type': u'part'},
  u'dateLeadCollected': u'2018-04-12T18:37:34.590000+02:00',
  u'idCampaign': u'44b517df15',
  u'mode': u'dryrun',
  u'project': {u'address': {u'city': u'Paris',
    u'insee': u'75106',
    u'postalCode': u'75006'},
   u'categoryId': 9999,
   u'description': 'non complété'.decode('latin-1').encode('utf-8')}},
 u'ws_url': u'https://partnership.homly-you.com/rest/v2/lead/create'}
19/96: pl
19/97: bla = json.dumps(pl, ensure_ascii=False)
19/98: pl
19/99: bla = json.dumps(pl, ensure_ascii=False)
19/100: bla = json.dumps(pl, ensure_ascii=False).encode('utf-8')
19/101: bla = json.dumps(pl, ensure_ascii=False).encode('utf-8')
19/102: bla = json.dumps(pl, ensure_ascii=False).decode('utf-8')
19/103: json.dumps(pl, ensure_ascii=False)
19/104:
pl = {u'payload': {u'acceptEndUserAgreement': True,
  u'contact': {u'email': u'ikx8nktzz0jwi@example.com',
   u'firstname': u'random',
   u'lastname': u'user',
   u'phone1': u'+33612345678',
   u'salutation': u'mr',
   u'type': u'part'},
  u'dateLeadCollected': u'2018-04-12T18:37:34.590000+02:00',
  u'idCampaign': u'44b517df15',
  u'mode': u'dryrun',
  u'project': {u'address': {u'city': u'Paris',
    u'insee': u'75106',
    u'postalCode': u'75006'},
   u'categoryId': 9999,
   u'description': json.dumps('non complété', ensure_ascii=False).encode('utf-8')}},
 u'ws_url': u'https://partnership.homly-you.com/rest/v2/lead/create'}
19/105:
pl = {u'payload': {u'acceptEndUserAgreement': True,
  u'contact': {u'email': u'ikx8nktzz0jwi@example.com',
   u'firstname': u'random',
   u'lastname': u'user',
   u'phone1': u'+33612345678',
   u'salutation': u'mr',
   u'type': u'part'},
  u'dateLeadCollected': u'2018-04-12T18:37:34.590000+02:00',
  u'idCampaign': u'44b517df15',
  u'mode': u'dryrun',
  u'project': {u'address': {u'city': u'Paris',
    u'insee': u'75106',
    u'postalCode': u'75006'},
   u'categoryId': 9999,
   u'description': json.dumps('non complété', ensure_ascii=False, encoding='utf-8').encode('utf-8')}},
 u'ws_url': u'https://partnership.homly-you.com/rest/v2/lead/create'}
19/106:
pl = {u'payload': {u'acceptEndUserAgreement': True,
  u'contact': {u'email': u'ikx8nktzz0jwi@example.com',
   u'firstname': u'random',
   u'lastname': u'user',
   u'phone1': u'+33612345678',
   u'salutation': u'mr',
   u'type': u'part'},
  u'dateLeadCollected': u'2018-04-12T18:37:34.590000+02:00',
  u'idCampaign': u'44b517df15',
  u'mode': u'dryrun',
  u'project': {u'address': {u'city': u'Paris',
    u'insee': u'75106',
    u'postalCode': u'75006'},
   u'categoryId': 9999,
   u'description': json.dumps('non complété', ensure_ascii=False, encoding='utf8').encode('utf8')}},
 u'ws_url': u'https://partnership.homly-you.com/rest/v2/lead/create'}
19/107: pl
19/108: json.dumps(pl, ensure_ascii=False, encoding='utf8')
19/109: json.dumps(pl, ensure_ascii=False, encoding='utf8').decode('utf8')
19/110: "dsfdfds".decode('utf8')
19/111: s = '{"payload": {"idCampaign": "44b517df15", "acceptEndUserAgreement": true, "project": {"categoryId": 9999, "description": "non compl\u00e9t\u00e9", "address": {"postalCode": "75006", "city": "Paris", "insee": "75106"}}, "contact": {"firstname": "random", "lastname": "user", "phone1": "+33612345678", "salutation": "mr", "type": "part", "email": "74jeqhmg8y1oah@example.com"}, "mode": "dryrun", "dateLeadCollected": "2018-04-12T19:15:55.190000+02:00"}, "ws_url": "https://partnership.homly-you.com/rest/v2/lead/create"}'
19/112: json.loads(s)
19/113: print(json.loads(s))
19/114: print(json.loads(s)['payload']['project']['description'])
19/115: None == 1
19/116: None == None
19/117: None is None
19/118: 1 is None
19/119: 1 is 1
20/1: from datetime import datetime
20/2: datetime(2018, 4, 24, 18, 0)
20/3: datetime(2018, 4, 24, 18, 0).strptime()
20/4: datetime(2018, 4, 24, 18, 0)
20/5: dt = datetime(2018, 4, 24, 18, 0)
20/6: dt.year
20/7: dt.day
20/8: dt.month
20/9: dt.hour
20/10: dt.minute
20/11: datetime.now()
21/1: d={}
21/2: dd = { "bla": "value" }
21/3: d.keys()
21/4: dd.keys()
21/5: d.get("bla", {})
23/1: import v1.services.inscription
23/2: ls ..
24/1: [] == True
24/2: [] == False
24/3:
if []:
    print ("True")
    else:
24/4:
if []:
    print ("True")
else:
    print ("False")
25/1:
if not []:
    print ("True")
else:
    print ("False")
25/2: eexit
26/1: import hashlib
26/2: hashlib.algorithms
26/3: hashlib.sha256("fdsfdsff")
26/4: hashlib.sha256("fdsfdsff").
26/5: clear
26/6: hashlib.sha256("fdsfdsff").digest()
26/7: import base64
26/8: base64.b64encode( hashlib.sha256("fdsfdsff").digest()  )
27/1: import models.guest
28/1: import common.models.guest
28/2: guest
28/3: from common.models.guest import GuestModel
28/4: GuestModel
28/5: GuestModel()
28/6: help(GuestModel)
28/7: from common.services.guest import GuestService
28/8: from common.services.guest import GuestService
29/1: from common.services.guest import GuestService
29/2: pwd
29/3: from accorhotels_onboarding.commmon.models.guest import GuestModel
29/4: from common.models.guest import GuestModel
29/5: from common.services.guest import Model
29/6: from common.services.guest import GuestService
29/7: from common.services.guest import GuestService
30/1: from common.services.guest import GuestService
30/2: GuestService().get_guest()
30/3: GuestService().get_guest("sdfsdf")
31/1: from apitester import apitester
31/2: apitester.ApiTester
31/3: from apitester.apitester import ApiTest
31/4: from apitester.apitester import ApiTester
31/5: help(ApiTester)
32/1: import hasjhlib
32/2: import hashlib
33/1: import urlparse
33/2: urlparse.urlparse('http://127.0.0.1:8080/api/v0/total_gdpr2018/v1/inscription/register?token=5c9ab8672c064615936a115299904c79')
33/3: parsed = urlparse.urlparse('http://127.0.0.1:8080/api/v0/total_gdpr2018/v1/inscription/register?token=5c9ab8672c064615936a115299904c79')
33/4: parsed
33/5: domain = None
34/1: import urlparse
34/2: urlparse.urlparse('http://127.0.0.1:8080/api/v0/total_gdpr2018/v1/inscription/register?token=e8a8114b64bf49b7814b535fe1e5a53e')
35/1: from models.ref import RefModel
35/2: from opticalcenter_formulairenl.v1.models.ref import RefModel
35/3: from v1.models.ref import RefModel
38/1: ls
38/2: from labanquepostaleprospectspatrimoniaux.v1.models.prospect import ProspectModel
38/3: from v1.models.prospect import ProspectModel
38/4: import flask
39/1: import flask
39/2: from v1.models.prospect import ProspectModel
39/3: from v1.services import prospect
39/4: cd ..
39/5: from labanquepostaleprospectspatrimoniaux.v1.services import prospect
39/6: prospect
39/7: prospect.ReportService
39/8: prospect.ReportService()
39/9: rs = prospect.ReportService()
39/10: rs.get_csv()
40/1: import pdfkit
40/2: pdfkit.from_url('https://pypi.org/project/pdfkit/', 'out.pdf')
41/1: import json
41/2: json.dumps()
41/3: json.dumps(None)
41/4: json.loads('null')
41/5: a = json.loads('null')
41/6: a
41/7: print a()
41/8: print (a)
43/1: import requests
44/1: import requests
45/1: i;port gitlab
45/2: import gitlab
45/3: gitlab.Gitlab('https://gitlab.1000mercis.com', 'iwY6CkNxyRiamYsngFQ7')
45/4: git_account = gitlab.Gitlab('https://gitlab.1000mercis.com', 'iwY6CkNxyRiamYsngFQ7')
45/5: git_account.getgroups()
45/6: git_account.getgroups(181)
45/7: git_account.projects.list()
45/8: git_account.groups.list()
45/9: git_account.groups.get(181)
45/10: gr = git_account.groups.get(181)
45/11: gr.get('projects')
45/12: gr
45/13: gr.projects
45/14: hasattr(gr, projects)
45/15: hasattr(gr, 'projects')
45/16: hasattr(gr, 'projectsdsfdfs')
45/17: gr.projects
45/18: gr.projects.archived
45/19: gr.projects.id
45/20: gr.id
45/21: gr.name
45/22: gr.http_url_to_rep
45/23: gr.__dict__
45/24: gr.http_url_to_repo
45/25: gr
45/26: gr.projects.list()
45/27: projects = gr.projects.list()
45/28: projects_nar = filter(lambda x: not hasattr(x, 'archived'), group.projects)
45/29: projects_nar = filter(lambda x: not hasattr(x, 'archived'), groups.projects)
45/30: projects_nar = filter(lambda x: not hasattr(x, 'archived'), gr.projects)
45/31: projects_nar = filter(lambda x: not hasattr(x, 'archived'), projects)
45/32: projects_nar = filter(lambda x: not hasattr(x, 'archived'), gr.projects.list())
45/33: projects_nar
45/34: projects[0]
45/35: projects[0].archived
45/36: projects[0].['archived']
45/37: projects[0]['archived']
45/38: projects[0].name
45/39: projects[0].__dict__
45/40: projects[0].archived
45/41: projects_nar = filter(lambda x: not x.archived, group.projects.list())
45/42: projects_nar = filter(lambda x: not x.archived, gr.projects.list())
45/43: projects_nar
45/44: pr = projects_nar
45/45: pr[0].http_url_to_repo
45/46: pr = list(map(lambda x: {'id': x.id, 'name': x.name, 'url': x.http_url_to_repo}, op_projects))
45/47: pr = list(map(lambda x: {'id': x.id, 'name': x.name, 'url': x.http_url_to_repo}, projects_nar))
45/48: pr
46/1: import gitlab
46/2: gitlab.Gitlab('https://gitlab.1000mercis.com', 'iwY6CkNxyRiamYsngFQ7')
46/3: git_account = gitlab.Gitlab('https://gitlab.1000mercis.com', 'iwY6CkNxyRiamYsngFQ7')
46/4: git_account.projects.list()
46/5: git_account.projects.list()[0].ID
46/6: git_account.projects.list()[0].id
46/7: git_account.projects.get(8521)
46/8: pr = git_account.projects.get(8521)
46/9: pr.files.list90
46/10: pr.files.list()
46/11: pr.files
46/12: pr.files()
46/13: pr.files.get()
46/14: pr.files.get('Q')
46/15: pr.branches.get('master')
46/16: pr.branches.get('master')
46/17: pr.name
46/18: pr.branches.list()
46/19: git_account.projects.list()[100].id
46/20: git_account.projects.list()[10].id
46/21: git_account.projects.get(8506)
46/22: git_account.projects.get(8506).branches.list()
46/23: git_account.projects.get(8506).branches.get('master')
46/24: git_account.projects.get(8506).branches.get('master')
46/25: br = git_account.projects.get(8506).branches.get('master')
46/26: br
46/27: br.attributes
46/28: br = git_account.projects.get(8506).name
46/29: br
46/30: git_account.projects.list()
46/31: git_account.gruops.get(181)
46/32: git_account.groups.get(181)
46/33: gr = git_account.groups.get(181)
46/34: gr.projects.list()
46/35: gr.projects.get(8519).name
46/36: gr.projects.get(8519)
46/37: gr.projects.list()[0]
46/38: gr.projects.list()[0].name
46/39: pr = gr.projects.list()[0]
46/40: pr.repo
46/41: pr
46/42: pr.__dict__
46/43: pr.files
46/44: pr.files.list()
46/45: pr
46/46: git_account.projects.list()
46/47: git_account.groups.get(181)
46/48: gr
46/49: gr.projects.list()
46/50: gr.projects.get()
46/51: pr
46/52: git_account.projects.list()
46/53: git_account.projects.get(8521)
46/54: git_account.projects.get(8521).name
46/55: git_account.projects.get(8517).name
46/56: git_account.projects.get(8516).name
46/57: git_account.projects.get(8507).name
46/58: git_account.projects.get(8483).name
46/59: git_account.projects.get(8483).
46/60: git_account.projects.get(8483).repository_tree()
46/61: git_account.projects.get(8483).repository_tree(path='')
46/62: git_account.projects.get(8483).repository_tree(path='/koufar.yaml')
46/63: git_account.projects.get(8483).repository_tree(path='/')
46/64: ''.endswith()
46/65: ''.endsWith()
46/66: ''.ends_with()
46/67: ''.endswith()
46/68: ''.endswith('')
46/69: ''.endswith()
46/70: git_account.projects.get(8483).name
46/71: import re
46/72: re.search('[a-zA-Z0-9]*\s*[(](\d*)[)]', 'clarins_us')
46/73: re.search('[a-zA-Z0-9]*\s*[(](\d*)[)]', 'clarins_us').groups()
46/74: re.search('[a-zA-Z0-9]*\s*[(](\d*)[)]', 'clarins_angel').groups()
46/75: re.search('[a-zA-Z0-9]*\s*[(](\d*)[)]', 'clarins_us (15)').groups()
46/76: git_account.projects.get(8047).
46/77: git_account.projects.get(8047)
46/78: git_account.projects.get(8047).ref
46/79: git_account.projects.get(8047).__dict__
46/80: git_account.projects.get(8047).tags
46/81: git_account.projects.get(8047).tags.list()
46/82: git_account.projects.get(8047).branches.list()
46/83: git_account.projects.get(8047).branches.list()[0]
46/84: git_account.projects.get(8047).branches.list()[0].files
46/85: br git_account.projects.get(8047).branches.list()[0].
46/86: br = git_account.projects.get(8047).branches.list()[0]
46/87: pr = git_account.projects.get(8047)
46/88: pr
46/89: pr.files
46/90: pr.files.list()
46/91: pr.files.get()
46/92: herlp(pr.files.get())
46/93: help(pr.files.get())
46/94: help(pr.files.get)
46/95: pr.files.get(file_path='v1/emails/1.html', ref='master')
46/96: pf = pr.files.get(file_path='v1/emails/1.html', ref='master')
46/97: pf.attributes
46/98: pf.content
46/99: pf.content.decode('base64')
46/100: pf.attributes
46/101: type(pf.attributes)
46/102: pr = git_account.projects.get(8047).commits.list()
46/103: pr
46/104: pr = git_account.projects.get(8047)
46/105: git_account.projects.get(8047).commits.list()
46/106:
data = {
                'branch': 'master',
                'commit_message': 'testing gitlab API',
                'actions': [
                    {
                        'action': 'update',
                        'file_path': 'v1/emails/1.html',
                        'content': '<!DOCTYPE html> <html> <head lang="en"> <meta charset="UTF-8"> <title>{{op_title}}</title> </head> <body> <!--Pixel de visu--> <table border="0" cellpadding="0" cellspacing="0"> <tr> <td width="0" height="0" align="left" style="font-size:0px;"><img src="{{op_base_url}}/track/mail_visu?idue={{idue}}&idto={{idto}}&e={{e}}" width="1" height="1" border="0"></td> </tr> </table> Hello, <br/> <br/> Here is your link to <a href="{{op_base_url}}/track/page_click?iIdU={{user_id}}&iVisitId={{visit_id}}&sUid={{uid}}&iPageId=0&iLinkNumber=1" target="_blank">Clarins Kickoff to Summer Sweepstakes</a> as requested. <br/> <br/> Thanks, <br/> Clarins </body> </html>'
                    }
                ]
            }
46/107: commit = git_account.projects.get(8047).commits.create(data)
46/108: commit
46/109: commit.attributes
46/110:
data = {
                'branch': 'master',
                'commit_message': 'testing gitlab API',
                'actions': [
                    {
                        'action': 'create',
                        'file_path': 'v1/emails/9999.html',
                        'content': '<!DOCTYPE html> <html> <head lang="en"> <meta charset="UTF-8"> <title>{{op_title}}</title> </head> <body> <!--Pixel de visu--> <table border="0" cellpadding="0" cellspacing="0"> <tr> <td width="0" height="0" align="left" style="font-size:0px;"><img src="{{op_base_url}}/track/mail_visu?idue={{idue}}&idto={{idto}}&e={{e}}" width="1" height="1" border="0"></td> </tr> </table> Hello, <br/> <br/> Here is your link to <a href="{{op_base_url}}/track/page_click?iIdU={{user_id}}&iVisitId={{visit_id}}&sUid={{uid}}&iPageId=0&iLinkNumber=1" target="_blank">Clarins Kickoff to Summer Sweepstakes</a> as requested. <br/> <br/> Thanks, <br/> Clarins </body> </html>'
                    }
                ]
            }
46/111: commit2 = git_account.projects.get(8047).commits.create(data)
46/112:
data2 = {
                'branch': 'master',
                'commit_message': 'testing gitlab API',
                'actions': [
                    {
                        'action': 'delete',
                        'file_path': 'v1/emails/9999.html',
                        'content': '<!DOCTYPE html> <html> <head lang="en"> <meta charset="UTF-8"> <title>{{op_title}}</title> </head> <body> <!--Pixel de visu--> <table border="0" cellpadding="0" cellspacing="0"> <tr> <td width="0" height="0" align="left" style="font-size:0px;"><img src="{{op_base_url}}/track/mail_visu?idue={{idue}}&idto={{idto}}&e={{e}}" width="1" height="1" border="0"></td> </tr> </table> Hello, <br/> <br/> Here is your link to <a href="{{op_base_url}}/track/page_click?iIdU={{user_id}}&iVisitId={{visit_id}}&sUid={{uid}}&iPageId=0&iLinkNumber=1" target="_blank">Clarins Kickoff to Summer Sweepstakes</a> as requested. <br/> <br/> Thanks, <br/> Clarins </body> </html>'
                    }
                ]
            }
46/113: commit3 = git_account.projects.get(8047).commits.create(data2)
46/114: print(commit3.attributes)
46/115: pr.files.get(file_path='v1/config_dv.py', ref='master')
46/116:
try:
    pr.files.get(file_path='v1/config_dv.py', ref='master')
except Exception as e:
    print(repr(e))
46/117: from gitlab.exceptions import GitlabGetError
46/118:
try:
    pr.files.get(file_path='v1/config_dv.py', ref='master')
except GitlabGetError:
    print('pass')
47/1: import gitlab
47/2: gitlab.Gitlab('https://gitlab.1000mercis.com', 'iwY6CkNxyRiamYsngFQ7')
47/3: ga = gitlab.Gitlab('https://gitlab.1000mercis.com', 'iwY6CkNxyRiamYsngFQ7')
47/4: group = ga.groups.get(181)
47/5: group
47/6: group.projects
47/7: group.projects.list()
47/8: len(group.projects.list())
47/9: group.subgroups
47/10: group.subgroups.list()
47/11: group.search()
47/12: help(group.search)
47/13: group.search('', 'total')
47/14: group.search('group', 'total')
47/15: group.projects.list(archived=1)
47/16: len(group.projects.list(archived=1))
47/17: len(group.projects.list())
47/18: help(group.projects.list)
47/19: group.projects.list(archived=1, all=True)
47/20: projects = group.projects.list(archived=1, all=True)
47/21: len(projects)
47/22: projects_na = group.projects.list(archived=0, all=True)
47/23: len(projects_na)
47/24: projects_all = group.projects.list(all=True)
47/25: len(projects_all)
47/26: help(group.projects.list)
47/27: projects_all = group.projects.list(all=True)
47/28: op_projects = filter(lambda x: not x.archived, group.projects.list(all=True))
47/29: op_projects
47/30: len(op_projects)
47/31: op_projects[200]
47/32: op_projects[200].archived
47/33:
for p in op_projects:
    if p.archived:
        print(p)
        print('Is archived')
48/1: 1<<2
48/2: 1<<1
48/3: 1<<3
48/4: 1<<1+1
48/5: 1<<1
48/6: (1<<1)+1
48/7: bit3()
48/8: bit(3)
48/9: bin(3)
48/10: bin(2)
48/11: (1<<1)+1
48/12: ((1<<1)+1<<1)+1
48/13: bin(4)
48/14: ((1<<1)|1<<1)|1
48/15: 1<<1|1<<1|1
48/16: 1<<1
48/17: 1<<1|1
48/18: (1<<1|1)<<1
48/19: (1<<1|1)<<1|1
48/20: a = 0
48/21: a|1
48/22: a|2
48/23: a|4
48/24: (a|4)|1
48/25: (a|4)|2
48/26: a |= 1
48/27: a
48/28: a |= 2
48/29: a
48/30: a |= 4
48/31: a
48/32: a&7
48/33: a&4
48/34: bin(7)
48/35: bin(4)
48/36: bin(2)
48/37: bin(1)
48/38: 3&4
48/39: 3&2
48/40: bin(3)
48/41: 3&1
49/1: from leon_common.validator import validate
51/1: a = []
51/2: a.get('a')
51/3: isinstance(a, dict)
51/4: isinstance(b, dict)
51/5: b = None
51/6: isinstance(b, dict)
51/7: isinstance(b, list)
51/8: isinstance(q, list)
51/9: isinstance(a, list)
52/1: ''
52/2:
if '':
    print 'a'
53/1:
if "123":
    print "q"
54/1: ''.join([1, 2, 3])
54/2: ','.join([1, 2, 3])
54/3: ','.join(['1', '2', '3'])
54/4: ','.join(['.', '+', '-'])
54/5: ''.join(['.', '+', '-'])
54/6: import regex
54/7: regex.sub('[.,]', '', '1,2.3')
54/8: regex.sub('[.,+,-]', '', '1,2.3')
54/9: '123'.split('')
54/10: '123'.split(None)
54/11: '1 2 3'.split(None)
55/1: import requests
55/2: pwd
55/3: ls v1/models/ws_templates/
55/4: ls v1/models/ws_templates/search_card.xml
55/5:
with open('v1/models/ws_templates/search_card.xml', 'r') as fd:
    xml_template = fd.read()
55/6: from jinja2 import Template
55/7: xml_template = Template(xml_template)
55/8: xml = xml_template.render(params)
55/9: xml = xml_template.render({'card_number': '1324564657987897'})
55/10: headers = {'Content-Type': 'application/xml'}
55/11: ws_url = 'https://maxxing-ppr-intersportv2.ate.info/mpcm/web/api/ws/5.4/CustomerInformationServer.php'
55/12: login = 'ws_1000mercis'
55/13: pwd = 'Ppd_1000mcisM@xxinG18'
55/14: response = resquests.post(ws_url, data=xml, headers=headers, auth=(login, pwd), timeout=3)
55/15: response = requests.post(ws_url, data=xml, headers=headers, auth=(login, pwd), timeout=3)
55/16: response
55/17: response.txt
55/18: response.json
55/19: response.json()
55/20: response.raw
55/21: response.text
55/22: response.url
55/23: response.status_code
55/24: response.request
55/25: ws_url_prod = 'https://maxxingnonhermes.intersport.fr/mpcm/web/api/ws/5.4/CustomerInformationServer.php'
55/26: pwd_prod = 'liw{94D/J$D4'
55/27: response_prod = requests.post(ws_url_prod, data=xml, headers=headers, auth=(login, pwd_prod), timeout=3)
55/28: response_prod
55/29: response_prod.text
55/30: Template(response.text).rendre()
55/31: Template(response.text).render()
55/32: pwd
55/33: ls
56/1: from pprint import pprint
56/2: pprint('<!--\tBEGIN mapAuthentificationDisplay.html -->\n\t\t\t<table align=\"center\" width=\"75%\" border=\"0\">\n\t\t\t\t\t<tr>\n\t\t\t\t\t\t<td align=\"center\"><font size=\"+2\" color=\"#FF0000\"><b>Error: Access denied.</b></font></td>\n\t\t\t\t\t</tr>\n\t\t\t\t\t<tr>\n\t\t\t\t\t\t<td align=\"center\"><font size=\"+1\"><b>You do not have sufficient permissions to access this page.</b></font></td>\n\t\t\t\t\t</tr>\n\t\t\t\t\t<tr>\n\t\t\t\t\t\t<td align=\"center\"><font size=\"+1\"><b>Contact your system administrator.</b></font></td>\n\t\t\t\t\t</tr>\n\t\t\t</table>\n<!--\tEND mapAuthentificationDisplay.html -->')
57/1: pprint('<!--\tBEGIN mapAuthentificationDisplay.html -->\n\t\t\t<table align=\"center\" width=\"75%\" border=\"0\">\n\t\t\t\t\t<tr>\n\t\t\t\t\t\t<td align=\"center\"><font size=\"+2\" color=\"#FF0000\"><b>Error: Access denied.</b></font></td>\n\t\t\t\t\t</tr>\n\t\t\t\t\t<tr>\n\t\t\t\t\t\t<td align=\"center\"><font size=\"+1\"><b>You do not have sufficient permissions to access this page.</b></font></td>\n\t\t\t\t\t</tr>\n\t\t\t\t\t<tr>\n\t\t\t\t\t\t<td align=\"center\"><font size=\"+1\"><b>Contact your system administrator.</b></font></td>\n\t\t\t\t\t</tr>\n\t\t\t</table>\n<!--\tEND mapAuthentificationDisplay.html -->')
57/2: from jinja2 import Environment, BaseLoader
57/3: Environment(loader=BaseLoader()).from_string()
57/4: s = '<!--\tBEGIN mapAuthentificationDisplay.html -->\n\t\t\t<table align=\"center\" width=\"75%\" border=\"0\">\n\t\t\t\t\t<tr>\n\t\t\t\t\t\t<td align=\"center\"><font size=\"+2\" color=\"#FF0000\"><b>Error: Access denied.</b></font></td>\n\t\t\t\t\t</tr>\n\t\t\t\t\t<tr>\n\t\t\t\t\t\t<td align=\"center\"><font size=\"+1\"><b>You do not have sufficient permissions to access this page.</b></font></td>\n\t\t\t\t\t</tr>\n\t\t\t\t\t<tr>\n\t\t\t\t\t\t<td align=\"center\"><font size=\"+1\"><b>Contact your system administrator.</b></font></td>\n\t\t\t\t\t</tr>\n\t\t\t</table>\n<!--\tEND mapAuthentificationDisplay.html -->'
57/5: Environment(loader=BaseLoader()).from_string(s)
57/6: t =Environment(loader=BaseLoader()).from_string(s)
57/7: t.render()
57/8: t.render() > template.html
57/9:
with open('response.html', 'w') as fd:
    xml_template = fd.write(s)
58/1: ls
58/2: import v1.models.tas
59/1: from v1.models.tas import TASModel
59/2: import v1.models.tas
59/3: from v1.models.tas import TasModel
59/4: from v1.services.tas import TAsService
60/1: from v1.services.tas import TAsService
61/1: import pandas
61/2: import pandas as pd
61/3: pd.read_excel('exratesyearsgeo.xlsx', index_col=0)
62/1: import pandas as pd
62/2: pd.read_excel('exratesyearsgeo.xlsx', index_col=0)
62/3: pd.read_excel('exratesyearsgeo.xlsx', index_col=0, skiprows=5)
62/4: pd.read_excel('exratesyearsgeo.xlsx', index_col=0, skiprows=5, nrows=10)
62/5: pd.read_excel('exratesyearsgeo.xlsx', index_col=0, skiprows=5, nrows=10, na_values=0)
62/6: pd.read_excel('exratesyearsgeo.xlsx', index_col=0, skiprows=5, nrows=10, na_values=0, usecols='D,P')
62/7: pd.read_excel('exratesyearsgeo.xlsx', index_col=0, skiprows=6, nrows=10, na_values=0, usecols='D,P')
62/8: pd.read_excel('exratesyearsgeo.xlsx', index_col=0, skiprows=6, nrows=10, na_values=0, usecols='A,D,P')
62/9: pd.read_excel('exratesyearsgeo.xlsx', skiprows=6, nrows=10, na_values=0, usecols='A,D,P')
62/10: pd.read_excel('exratesyearsgeo.xlsx', index_col=0, skiprows=6, nrows=10, na_values=0, usecols='A,D,P')
62/11: pd.read_excel('exratesyearsgeo.xlsx', index_col=0, skiprows=7, nrows=10, na_values=0, usecols='A,D,P')
62/12: pd.read_excel('exratesyearsgeo.xlsx', index_col=0, skiprows=5, nrows=10, na_values=0, usecols='A,D,P')
62/13: data = pd.read_excel('exratesyearsgeo.xlsx', index_col=0, skiprows=5, nrows=10, na_values=0, usecols='A,D,P')
62/14: data
62/15: data[0]
62/16: data.columns
62/17: data.index
62/18: data.columns[0]
62/19: data.dtypes
62/20: data.values
62/21: data.values[0]
62/22: data = pd.read_excel('exratesyearsgeo.xlsx', index_col=0, skiprows=5, na_values=0, usecols='A,D,P')
62/23: data.axes
62/24: data = pd.read_excel('exratesyearsgeo.xlsx', skiprows=5, na_values=0, usecols='A,D,P')
62/25: data.axes
62/26: data[0]
62/27: data.plot.line
62/28: data['0']
62/29: data.columns
62/30: data['Unnamed: 0']
62/31: data.plot.line
62/32: data.plot.line(('Unnamed: 0', 'EUR'))
62/33: data.plot.line(['Unnamed: 0', 'EUR'])
62/34: data.plot.line()
63/1: import pandas as pd
63/2: data = pd.read_excel('exratesyearsgeo.xlsx', index_col=0, skiprows=5, na_values=0, usecols='A,D,P')
63/3: data.plot.line()
64/1: import pandas as pd
64/2: data = pd.read_excel('exratesyearsgeo.xlsx', index_col=0, skiprows=5, na_values=0, usecols='A,D,P')
64/3: pl = data.plot.line()
64/4: pl = data.plot()
64/5: export MPLBACKEND=agg
64/6: $export MPLBACKEND=agg
64/7: ls
65/1: echot $MPLBACKEND
65/2: echo $MPLBACKEND
65/3: import pandas as pd
65/4: data = pd.read_excel('exratesyearsgeo.xlsx', index_col=0, skiprows=5, na_values=0, usecols='A,D,P')
65/5: pl = data.plot.line()
65/6: pl
65/7: data.plot.line()
65/8: pl.get_figure()
65/9: fig = pl.get_figure()
65/10: fig.savefig('plot.png')
65/11: pl = data[].plot.line()
65/12: data = pd.read_excel('exratesyearsgeo.xlsx', index_col=0, skiprows=5, na_values=0, usecols='A,D,P', names=['day'])
65/13: data = pd.read_excel('exratesyearsgeo.xlsx', index_col=0, skiprows=5, na_values=0, usecols='A,D,P', names=['day', 'EUR', ''USD])
65/14: data = pd.read_excel('exratesyearsgeo.xlsx', index_col=0, skiprows=5, na_values=0, usecols='A,D,P', names=['day', 'EUR', 'USD'])
65/15: pl = data[data.day > '2018'].plot.line()
65/16: data.day
65/17: data['day']
65/18: data['EUR']
65/19: data['2018']
65/20: data['2018-12-01']
65/21: data2018 = data['2018']
65/22: pl = data2018.plot.line()
65/23: data2018.plot.line().get_figure()
65/24: data2018.plot.line().get_figure().save_figure('plot2.png')
65/25: data2018.plot.line().get_figure().savefig('plot2.png')
65/26: data2018.plot.line().get_figure(figsize=(780, 1024)).save_figure('plot2.png')
65/27: data2018.plot.line().get_figure().set_size_inches(780, 1024).save_figure('plot2.png')
65/28: fig = data2018.plot.line().get_figure()
65/29: fig.set_size_inches(780, 1024)
65/30: fig.save_figure('plot2.png')
65/31: fig.savefig('plot2.png')
65/32: fig.set_size_inches(7, 10)
65/33: fig.savefig('plot2.png')
65/34: fig.set_size_inches(10, 7)
65/35: fig.savefig('plot2.png')
65/36: fig.set_size_inches(15, 7)
65/37: fig.savefig('plot2.png')
65/38: fig.set_size_inches(20, 7)
65/39: fig.savefig('plot2.png')
65/40: data['day']
66/1: from utils import db_provisioning
66/2: from utils import db_provisioning as dbp
66/3: dbp.read_meta()
67/1: import pandas as pd
67/2:
names = pd.read_excel(
        'exratesyearsgeo.xlsx',
        skiprows=_xlsx_conf['rows']['names'],
        usecols='D,P',
        names=currencies,
        nrows=1
    )
67/3:
_xlsx_conf = {
    'rows': {
        'names': 4,
        'quantity': 5,
        'code': 6,
    },
    'columns':  {
        'Index': 'A',
        'EUR': 'D',
        'USD': 'P',
    }
}
67/4:
names = pd.read_excel(
        'exratesyearsgeo.xlsx',
        skiprows=_xlsx_conf['rows']['names'],
        usecols='D,P',
        names=currencies,
        nrows=1
    )
67/5: currencies = ['EUR', 'USD']
67/6:
names = pd.read_excel(
        'exratesyearsgeo.xlsx',
        skiprows=_xlsx_conf['rows']['names'],
        usecols='D,P',
        names=currencies,
        nrows=1
    )
67/7: names
67/8:
_xlsx_conf = {
    'rows': {
        'names': 3,
        'quantity': 4,
        'code': 5,
    },
    'columns':  {
        'Index': 'A',
        'EUR': 'D',
        'USD': 'P',
    }
}
67/9:
names = pd.read_excel(
        'exratesyearsgeo.xlsx',
        skiprows=_xlsx_conf['rows']['names'],
        usecols='D,P',
        names=currencies,
        nrows=1
    )
67/10: names
67/11:
names = pd.read_excel(
        'exratesyearsgeo.xlsx',
        skiprows=_xlsx_conf['rows']['names'],
        usecols='D,P',
        names=currencies,
        nrows=1,
        header=None
    )
67/12: names
68/1: import pandas as pd
68/2: data = pd.read_excel('exratesyearsgeo.xlsx', index_col=0, skiprows=5, na_values=0, usecols='A,D,P', nrows=10)
68/3: data
68/4: columns = ['date', 'EUR', 'USD']
68/5: data = pd.read_excel('exratesyearsgeo.xlsx', index_col=0, skiprows=5, usecols='A,D,P', nrows=10, names=vcolumns)
68/6: data = pd.read_excel('exratesyearsgeo.xlsx', index_col=0, skiprows=5, usecols='A,D,P', nrows=10, names=columns)
68/7: data
68/8:
for i,s in data.iterrows():
    print(i, s)
    print(s['date'])
68/9:
for row in data:
    print(i, row)
    print(row['date'])
68/10:
for row in data:
    print(row)
    print(row['date'])
68/11:
for row in data:
    print(row)
68/12:
for row in data.iterrows():
    print(row)
68/13:
for row in data.iteritems():
    print(row)
68/14:
for row in data.iteritems():
    print(row)
    print(row['date'])
68/15: data
68/16: data['date']
68/17: columns = ['date', 'EUR', 'USD']
68/18: columns
68/19: data['USD']
68/20:
names = pd.read_excel(
        'exratesyearsgeo.xlsx',
        skiprows=_xlsx_conf['rows']['names']+1,
        usecols='D,P',
        names=currencies,
        nrows=1,
        header=None
    )
68/21: data = pd.read_excel('exratesyearsgeo.xlsx', index_col=0, skiprows=6, usecols='A,D,P', nrows=10, names=columns)
68/22: data
68/23: data = pd.read_excel('exratesyearsgeo.xlsx', index_col=0, skiprows=6, usecols='A,D,P', nrows=10, names=columns, headers=None)
68/24: data
68/25: data['date']
68/26: data = pd.read_excel('exratesyearsgeo.xlsx', skiprows=5, usecols='A,D,P', nrows=10, names=columns)
68/27: data['date']
68/28:
for row in data.iteritems():
    print(row)
    print(row['date'])
68/29:
for row in data.iterrows():
    print(row)
    print(row['date'])
68/30:
for row in data.iterrows():
    print(row)
68/31:
for i, row in data.iterrows():
    print(row)
68/32:
for i, row in data.iterrows():
    print(row)
    print(row['date'])
68/33:
for i, row in data.iterrows():
    # print(row)
    print(row['date'])
70/1: import pandas as pd
70/2: data = pd.read_excel('exratesyearsgeo.xlsx', skiprows=5, usecols='A,D,P', nrows=10, names=columns)
70/3: columns = ['date', 'EUR', 'USD']
70/4: data = pd.read_excel('exratesyearsgeo.xlsx', skiprows=5, usecols='A,D,P', nrows=10, names=columns)
70/5: data
70/6:
for i, row in data.iterrows():
    # print(row)
    print(row['date'], row['EUR', row['USD']])
70/7:
for i, row in data.iterrows():
    # print(row)
    print(row['date'], row['EUR'], row['USD'])
70/8: data['EUR'][à]
70/9: data['EUR'][9]
70/10: data['EUR'][9].isnull()
70/11: pd.isna(data['EUR'][9])
71/1: import pandas as pd
71/2: columns = ['date', 'EUR', 'USD']
71/3: data = pd.read_excel('exratesyearsgeo.xlsx', skiprows=5, usecols='A,D,P', nrows=10, names=columns)
71/4:
for i, row in data.iterrows():
    # print(row)
    print(row['date'], row['EUR'], row['USD'])
71/5: data['date'][0]
71/6: d = data['date'][0]
71/7: d.date
71/8: d.date()
71/9: d.datetime()
71/10: d.to_pydatetime
71/11: d.to_pydatetime()
72/1: from utils.models import initialize_db, Rate, RefCurrency
72/2: db_session = initialize_db()
72/3: db_session.query(Rate).join(RefCurrency).filter().all()
72/4: rates = db_session.query(Rate).join(RefCurrency).filter().all()
72/5: rates[0]
72/6: rates[0].rate
72/7: rates = db_session.query(Rate).join(RefCurrency).all()
72/8: rates[0].rate
72/9: rates = db_session.query(Rate).join(RefCurrency).filter(RefCurrency.code == 'EUR').all()
72/10: rates_eur = db_session.query(Rate).join(RefCurrency).filter(RefCurrency.code == 'EUR').all()
72/11: rates_usd = db_session.query(Rate).join(RefCurrency).filter(RefCurrency.code == 'USD').all()
72/12: rs = [r.rate for r in rates_eur]
72/13: rs
72/14: len(rs)
72/15: rs = {'rate': [r.rate for r in rates_eur], 'date': [r.date for r in rates_eur], 'qty': [r.quantity for r in rates_eur], 'code': [r.code for r in rates_eur]}
72/16: rates_all = db_session.query(Rate).join(RefCurrency).all()
72/17: rates_all
72/18: rates_all[0]
72/19: rates_all[0].quantity
72/20: rates_all = db_session.query(Rate, RefCurrency).join(RefCurrency).all()
72/21: rates_all[0].quantity
72/22: rates_all[0]
72/23: rates_all[0][1]
72/24: rates_all[0][1].quantity
72/25: rates_eur = db_session.query(Rate, RefCurrency).join(RefCurrency).filter(RefCurrency.code == 'EUR').all()
72/26: rs = {'rate': [r.rate for r,rc in rates_eur], 'date': [r.date for r,rc in rates_eur], 'qty': [rc.quantity for r,rc in rates_eur], 'code': [r.code for r, rc in rates_eur]}
72/27: rs = {'rate': [r.rate for r,rc in rates_eur], 'date': [r.date for r,rc in rates_eur], 'qty': [rc.quantity for r,rc in rates_eur], 'code': [rc.code for r,rc in rates_eur]}
72/28: rs
72/29: import pandas as pd
72/30: pd.DataFrame(data=d)
72/31: pd.DataFrame(data=rs)
72/32: pd.DataFrame(data=rs, index='date')
72/33: pd.DataFrame(data=rs, index=index('date'))
72/34: pd.DataFrame(data=rs)
72/35: df = pd.DataFrame(data=rs)
72/36: df.set_index('date', inplace=True)
72/37: df
72/38: rs = {'rate': [r.rate/rc.quantity for r,rc in rates_eur], 'date': [r.date for r,rc in rates_eur]}
72/39: rs.keys()
72/40: rs.values()
73/1: ls
   1: %hist -o -g -f history.md
